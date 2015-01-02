
import types
import socket
import pickle
import threading

transunit = 65536

class server_wrapper(object):
    flag_shutdown = False
    
    def __init__(self, instance, host, port, monitor_port=None):
        self.load_instance(instance)
        self.server_host = host
        self.set_control_port(port)
        self.set_monitor_port(monitor_port)
        pass
    
    def load_instance(self, instance):
        method_list = []
        monitor_method_list = []
        names = dir(instance)
        for name in names:
            if name[0]=='_': continue
            if isinstance(instance.__getattribute__(name), types.MethodType):
                method_list.append(name)
                if name[:5]=='read_':
                    monitor_method_list.append(name)
                    pass
                pass
            continue
        self.instance = instance
        self.name = instance.__class__.__name__.upper()
        self.available_methods = method_list
        self.available_monitor_methods = monitor_method_list
        return
    
    def set_control_port(self, port):
        self.control_port = port
        return
        
    def set_monitor_port(self, port):
        self.monitor_port = port
        return
    
    def start(self):
        threading.Thread(target=self._start_control_server).start()
        if self.monitor_port is not None:
            threading.Thread(target=self._start_monitor_server).start()
            pass
        return
        
    def _start_control_server(self):
        print(self.name+'::ControlServer ---- START ----')
        print(self.name+'::ControlServer INFO: port=%d'%(self.control_port))
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.server_host, self.control_port))
        server.listen(1)
        
        while True:
            client, client_address = server.accept()
            print(self.name+'::ControlServer ACCEPT %s:%d'%(client_address[0],
                                                              client_address[1]))
            
            while True:
                recv = client.recv(transunit)
                if len(recv)==0: 
                    print(self.name+'::ControlServer INFO: Connection is broken.')
                    break
                
                command = recv[:20].strip()                
                params = pickle.loads(recv[20:])
                kwparams = params[-1]
                params = params[:-1]
                print(self.name+'::ControlServer RECV %s %s %s'%(command, params, kwparams))
                
                if command=='server_stop':
                    print(self.name+'::ControlServer INFO: Start shutdown.')
                    self.shutdown()
                    rets = pickle.dumps('Server Shutdown')
                    sends = '%-10d%s'%(len(rets), rets)
                    client.send(sends)
                    client.close()
                    server.close()
                    return
                
                if command=='bye':
                    rets = pickle.dumps('Bye')
                    sends = '%-10d%s'%(len(rets), rets)
                    client.send(sends)
                    break
                
                if not command in self.available_methods:
                    print(self.name+'::ControlServer INFO: Received command is not available.')
                    rets = pickle.dumps('MethodError')
                    sends = '%-10d%s'%(len(rets), rets)
                    client.send(sends)
                    continue
                
                try:
                    ret = self.instance.__getattribute__(command)(*params, **kwparams)
                except TypeError:
                    print(self.name+'::ControlServer INFO: argument error.')
                    ret = 'ArgumentError'
                    pass
                    
                rets = pickle.dumps(ret)
                sends = '%-10d%s'%(len(rets), rets)
                client.send(sends)
                continue
            
            print(self.name+'::ControlServer CLOSE %s:%d'%(client_address[0],
                                                           client_address[1]))
            client.close()
            continue
        pass            

    def _start_monitor_server(self):
        print(self.name+'::MonitorServer ---- START ----')
        print(self.name+'::MonitorServer INFO: port=%d'%(self.monitor_port))
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.settimeout(1)
        server.bind((self.server_host, self.monitor_port))
        server.listen(5)
        
        while True:
            try:
                client, client_address = server.accept()
                print(self.name+'::MonitorServer ACCEPT %s:%d'%(client_address[0],
                                                                client_address[1]))
                
                threading.Thread(target=self._monitor_client_handler,
                                 args=(client, client_address)).start()
                
            except socket.timeout:
                if self.flag_shutdown: break
                pass
                
            continue
        
        server.close()
        print(self.name+'::MonitorServer INFO: shutdown')
        return            
        
    def _monitor_client_handler(self, client, client_address):
        print(client, client_address)
        
        client.settimeout(1)
        
        while True:
            try:
                recv = client.recv(transunit)
            except socket.timeout:
                if self.flag_shutdown: break
                continue
            
            if len(recv)==0: 
                print(self.name+'::MonitorServer INFO: Connection is broken.')
                break
                
            command = recv[:20].strip()                
            params = pickle.loads(recv[20:])
            print(self.name+'::MonitorServer RECV %s %s'%(command, params))
            
            if command=='bye':
                break
                
            if not command in self.available_monitor_methods:
                print(self.name+'::MonitorServer INFO: Received command is not available.')
                continue
                
            ret = self.instance.__getattribute__(command)(*params)
            rets = pickle.dumps(ret)
            sends = '%-10d%s'%(len(rets), rets)
            client.send(sends)
            continue
            
        print(self.name+'::MonitorServer CLOSE %s:%d'%(client_address[0],
                                                       client_address[1]))
        client.close()
        return
    
    def shutdown(self):
        self.flag_shutdown = True
        return


# ===========

# ===========


class control_client_wrapper(object):
    def __init__(self, cls, host, port):
        self.load_class(cls)
        self.connect(host, port)
        pass
    
    def __getattr__(self, name):
        if name in self.available_methods:
            send_func = lambda *p, **kw: self._send(name, *p, **kw)
            return send_func
        raise AttributeError
        return
        
    def load_class(self, cls):
        method_list = []
        monitor_method_list = []
        names = dir(cls)
        for name in names:
            if name[0]=='_': continue
            if isinstance(object.__getattribute__(cls, name), types.FunctionType):
                method_list.append(name)
                if name[:5]=='read_':
                    monitor_method_list.append(name)
                    pass
                pass
            continue
        method_list.append('server_stop')
        method_list.append('bye')
        self.cls = cls
        self.name = cls.__name__.upper()
        self.available_methods = method_list
        self.available_monitor_methods = monitor_method_list
        return
        
    def connect(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket()
        self.client.connect((host, port))
        return
    
    def _send(self, command, *params, **kwparams):
        params.append(kwparams)
        sends = '%-20s%s'%(command, pickle.dumps(params))
        self.client.send(sends)
        
        datalen = int(self.client.recv(10, socket.MSG_WAITALL))
        rets = self.client.recv(datalen, socket.MSG_WAITALL)
        ret = pickle.loads(rets)
        return ret
        

class monitor_client_wrapper(control_client_wrapper):
    def __getattr__(self, name):
        if name in self.available_monitor_methods:
            send_func = lambda *p: self._send(name, *p)
            return send_func
        if name in self.available_methods:
            print('%s() is not supported in the monitor_client'%(name))
            return lambda *p: None
        raise AttributeError
        return
        
    
