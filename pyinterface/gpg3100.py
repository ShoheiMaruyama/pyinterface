
import os
import time
import ctypes
import socket
import threading
try:
    import cPickle as pickle
except:
    import pickle
    pass

import pyinterface

SO_NAME = 'lib_gpg3100.so'
SO_PATH = os.path.join(pyinterface.LIB_PATH, SO_NAME)


# Identifers
# ----------

AD_INPUT_SINGLE = 1
AD_INPUT_DIFF = 2

AD_0_1V      = 0x00000001
AD_0_2P5V    = 0x00000002
AD_0_5V      = 0x00000004
AD_0_10V     = 0x00000008
AD_1_5V      = 0x00000010
AD_0_2V      = 0x00000020
AD_0_0P125V  = 0x00000040
AD_0_1P25V   = 0x00000080
AD_0_0P625V  = 0x00000100
AD_0_0P156V  = 0x00000200
AD_0_20mA    = 0x00001000
AD_4_20mA    = 0x00002000
AD_20mA      = 0x00004000
AD_1V        = 0x00010000
AD_2P5V      = 0x00020000
AD_5V        = 0x00040000
AD_10V       = 0x00080000
AD_20V       = 0x00100000
AD_50V       = 0x00200000
AD_0P125V    = 0x00400000
AD_1P25V     = 0x00800000
AD_0P625V    = 0x01000000
AD_0P156V    = 0x02000000
AD_1P25V_AC  = 0x04000000
AD_0P625V_AC = 0x08000000
AD_0P156V_AC = 0x10000000
AD_GND       = 0x80000000


# Structures
# ----------

class ADBoardSpec(ctypes.Structure):
    _fields_ = [('BoardType', ctypes.c_ulong),
                ('BoardID', ctypes.c_ulong),
                ('SamplingMode', ctypes.c_ulong),
                ('Resolution', ctypes.c_ulong),
                ('ChCountS', ctypes.c_ulong),
                ('ChCountD', ctypes.c_ulong),
                ('Range', ctypes.c_ulong),
                ('Isolation', ctypes.c_ulong),
                ('DI', ctypes.c_ulong),
                ('DO', ctypes.c_ulong)]
    
    def __init__(self):
        self.BoardType = 0
        self.BoardID = 0
        self.SamplingMode = 0
        self.Resolution = 0
        self.ChCountS = 0
        self.ChCountD = 0
        self.Range = 0
        self.Isolation = 0
        self.DI = 0
        self.DO = 0
        pass
    
    def __str__(self):
        s = 'BoardType: %d\n'%(self.BoardType)
        s += 'BoardID: %d\n'%(self.BoardID)
        s += 'SamplingMode: %d\n'%(self.SamplingMode)
        s += 'Resolution: %d\n'%(self.Resolution)
        s += 'ChCountS: %d\n'%(self.ChCountS)
        s += 'ChCountD: %d\n'%(self.ChCountD)
        s += 'Range: %d\n'%(self.Range)
        s += 'Isolation: %d\n'%(self.Isolation)
        s += 'DI: %d\n'%(self.DI)
        s += 'DO: %d\n'%(self.DO)
        return s


# ==========================
# GPG-3100 Python Controller
# ==========================
class gpg3100(object):
    com = None
    info = None
    mode = AD_INPUT_SINGLE
    ch_count = 0
    range = AD_10V
    
    def __init__(self, *args):
        if len(args)>1:
            if (type(args[0])==str)&(type(args[1])==int):
                self._remote_init(*args)
            else:
                self._local_init(*args)
                pass
        else:
            self._local_init(*args)
            pass
        
        self._init()
        return
    
    def _local_init(self, ndev=1, lib=SO_PATH):
        #print(ndev, lib)
        self.com = gpg3100_local_communicator(ndev, lib)
        return
    
    def _remote_init(self, host, port, timeout=5):
        #print(host, port, timeout)
        self.com = gpg3100_remote_communicator(host, port, timeout)
        pass
    
    def _init(self):
        self.get_device_info()
        self.use_singleend()
        self.set_range(AD_10V)
        return
    
    def server_stop(self):
        return self.com.server_stop()
    
    def use_singleend(self):
        self.mode = AD_INPUT_SINGLE
        self.ch_count = self.info.ChCountS
        return
    
    def use_differential(self):
        self.mode = AD_INPUT_DIFF
        self.ch_count = self.info.ChCountD
        return
    
    def set_range(self, range):
        self.range = range
        return
    
    def show_device_info(self):
        print(self.info)
        return
    
    def get_device_info(self):
        self.info = self.com.get_device_info()
        return self.info
    
    def get_oneshot_ad(self):
        return self.com.get_oneshot_ad(self.ch_count, self.mode, self.range)
    
    def get_ad(self, num, freq, start=0):
        return self.com.get_ad(num, freq, start, self.ch_count, self.mode, self.range)

# 
# Communicator
# ============

# Communicator Interface
# ----------------------
class gpg3100_communicator(object):
    def server_stop(self):
        return None
    
    def get_device_info(self):
        return ADBoardSpec()
    
    def get_oneshot_ad(self):
        return [float(),]
    
    def get_ad(self):
        return [[float(),],]

# Local Communicator
# ------------------
class gpg3100_local_communicator(gpg3100_communicator):
    lib = None
    
    def __init__(self, ndev, libpath):
        self.ndev = ndev
        self.c_ndev = ctypes.c_long(ndev)
        self.lib = ctypes.cdll.LoadLibrary(libpath)
        pass
    
    def get_device_info(self):
        info = ADBoardSpec()
        self.lib.get_device_info(self.c_ndev, ctypes.byref(info))
        if info.ChCountS < info.ChCountD:
            tmp = info.ChCountS
            info.ChCountS = info.ChCountD
            info.ChCountD = tmp
            pass
        return info
    
    def get_oneshot_ad(self, ch_count, mode, adrange):
        ch_count = int(ch_count)
        mode = int(mode)
        adrange = int(adrange)
        c_mode = ctypes.c_ulong(mode)
        c_range = ctypes.c_ulong(adrange)
        d = (ctypes.c_ushort * ch_count)(0)
        self.lib.get_oneshot_ad(self.c_ndev, c_mode, c_range,
                                ctypes.byref(d))
        return list(d)
    
    def get_ad(self, num, freq, start, ch_count, mode, adrange):
        num = int(num)
        freq = float(freq)
        start = float(start)
        ch_count = int(ch_count)
        mode = int(mode)
        adrange = int(adrange)
        c_num = ctypes.c_ulong(num)
        c_freq = ctypes.c_float(freq)
        c_start = ctypes.c_double(start)
        c_mode = ctypes.c_ulong(mode)
        c_range = ctypes.c_ulong(adrange)
        d = (ctypes.c_ushort * (ch_count * num))(0)
        self.lib.get_ad(self.c_ndev, c_mode, c_range, c_num,
                        c_freq, c_start, ctypes.byref(d))
        dd = list(d)
        ddd = [d[i:i+ch_count] for i in range(0, len(dd), ch_count)]
        
        return ddd

# Remote Communicator
# -------------------
class gpg3100_remote_communicator(gpg3100_communicator):
    sock = None
    sockfp = None
    
    def __init__(self, host, port, timeout):
        self.host = host
        self.port = port
        self.timeout = timeout
        pass
    
    def _open(self):
        sock = socket.socket()
        sock.settimeout(self.timeout)
        sock.connect((self.host, self.port))
        self.sock = sock
        self.sockfp = sock.makefile()
        return
    
    def _receive_data(self):
        datasize = int(self.sock.recv(8))
        recv = ''
        while len(recv)<datasize:
            recv += self.sock.recv(8192)
            #print(len(recv))
            continue
        data = pickle.loads(recv)
        return data
    
    def _close(self):
        self.sock.send('close\n')
        self.sock.close()
        self.sock = None
        self.sockfp = None
        return
    
    def server_stop(self):
        self._open()
        self.sock.send('server_stop\n')
        self.sock.close()
        self.sock = None
        self.sockfp = None
        return
            
    def get_device_info(self):
        self._open()
        self.sock.send('GPG-3100:get_device_info\n')
        ret = self._receive_data()
        self._close()
        return ret
    
    def get_oneshot_ad(self, ch_count, mode, range):
        self._open()
        self.sock.send('GPG-3100:get_oneshot_ad %d %d %d\n'%(ch_count, mode, range))
        ret = self._receive_data()
        self._close()
        return ret
    
    def get_ad(self, num, freq, start, ch_count, mode, range):
        self._open()
        self.sock.send('GPG-3100:get_ad %d %f %f %d %d %d\n'%(num, freq, start,
                                                              ch_count, mode, range))
        ret = self._receive_data()
        self._close()
        return ret

# 
# Server
# ======
class gpg3100_server(object):
    shutdown_signal = False
    _data = []
    _freq = 1
    _num = 0
    
    def __init__(self, control_port, monitor_port=None, ndev=1, lib=SO_PATH):
        self.gpg3100 = gpg3100(ndev, lib)
        if monitor_port is None: monitor_port = control_port + 1
        self.control_port = control_port
        self.monitor_port = monitor_port
        self.start_control_server()
        self.start_monitor_server()
        pass
    
    def start_control_server(self):
        threading.Thread(target=self._start_control_server).start()
        return
    
    def _start_control_server(self):
        print('GPG3100::ControlServer, --START-- (%d)'%(self.control_port))
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('127.0.0.1', self.control_port))
        server.listen(1)
        
        while True:
            client, client_address = server.accept()
            print('GPG3100::ControlServer, Accepted %s:%d'%(client_address[0],
                                                            client_address[1]))
            
            while True:
                recv = client.recv(8192)
                if len(recv)==0: break
                
                recv = recv.strip()
                print('GPG3100::ControlServer, Received [%s]'%(recv))
                command_params = recv.split()
                command = command_params[0]
                params = command_params[1:]
                if command=='server_stop':
                    self.shutdown_signal = True
                    client.close()
                    server.close()
                    print('GPG3100::ControlServer, --STOP--')
                    return
                if command=='close':
                    break
                
                self._control_handler(client, command, params)
                continue
            
            client.close()
            print('GPG3100::ControlServer, Close %s:%d'%(client_address[0],
                                                         client_address[1]))
            continue
        
        # never come here
        pass
    
    def _control_handler(self, client, command, params):
        if command=='GPG-3100:get_device_info':
            ret = self.gpg3100.com.get_device_info()
        elif command=='GPG-3100:get_oneshot_ad':
            ret = self.gpg3100.com.get_oneshot_ad(*params)
        elif command=='GPG-3100:get_ad':
            ret = self.gpg3100.com.get_ad(*params)
            self._data = pickle.dumps(ret)
            self._num = int(params[0])
            self._freq = float(params[1])
        else:
            ret = 'Bad Command %s\n'%(command)
            pass
        
        rets = pickle.dumps(ret)
        
        print('GPG3100::ControlServer, SendData, %d'%(len(rets)))
        client.send('%08d'%(len(rets)))
        client.setblocking(0)
        for i in range(0, len(rets), 8192):
            time.sleep(0.001)
            client.send('%s'%(rets[i:i+8192]))
            continue
        client.setblocking(1)
        return
    
    def start_monitor_server(self):
        threading.Thread(target=self._start_monitor_server).start()
        return
    
    def _start_monitor_server(self):
        print('GPG3100::MonitorServer, --START-- (%d)'%(self.monitor_port))
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('127.0.0.1', self.monitor_port))
        server.listen(5)
        server.settimeout(1)
        
        while True:
            try:
                client, client_address = server.accept()
            except socket.timeout:
                if self.shutdown_signal: break
                continue
            
            client.settimeout(1)
            thread = threading.Thread(target=self._monitor_client_manager,
                             args=(client, client_address))
            thread.start()
            continue
        
        server.close()
        print('GPG3100::MonitorServer, --STOP--')
        return
    
    def _monitor_client_manager(self, client, client_address):
        host = client_address[0]
        port = client_address[1]
        while True:
            try:
                if self.shutdown_signal: break
                
                print('GPG3100::MonitorServer, SendData, %s:%d'%(host, port))
                data = self._data
                freq = self._freq
                num = self._num
                client.send('%08d %016.2f %08d'%(len(data), freq, num))
                client.setblocking(0)
                for i in range(0, len(data), 8192):
                    time.sleep(0.001)
                    client.send('%s'%(data[i:i+8192]))
                    continue
                client.setblocking(1)
                
            except socket.error:
                break
            
            time.sleep(1)
            continue
        
        client.close()
        return
    


class gpg3100_monitor_client(object):
    def __init__(self, host, port, timeout=5):
        self.host = host
        self.port = port
        self.timeout = timeout
        pass
    
    def start(self):
        import matplotlib.animation
        import pylab
        import numpy
        
        def refresh(num):
            head = self.sock.recv(34)
            datasize = int(head.split()[0])
            freq = float(head.split()[1])
            num = int(head.split()[2])
            recv = ''
            while len(recv)<datasize:
                recv += self.sock.recv(8192)
                continue
            data = pickle.loads(recv)
            
            x = numpy.arange(0, num/freq, 1/freq)
            y = numpy.array(data).T
            for i in range(self.num_lines):
                self.lines.set_data(x, y[i])
                continue
            return
        
        self.sock = socket.socket()
        self.sock.connect((self.host, self.port))
        self.sock.settimeout(self.timeout)
        
        head = self.sock.recv(34)
        datasize = int(head.split()[0])
        freq = float(head.split()[1])
        num = float(head.split()[2])
        recv = ''
        while len(recv)<datasize:
            recv += self.sock.recv(8192)
            continue
        data = pickle.loads(recv)
        
        d = numpy.array(data)
        self.num_lines = d.shape[1]
        
        
        fig = pylab.figure()
        ax = fig.add_subplot(111)
        
        self.lines = []
        for i in range(self.num_lines):
            line, = ax.plot([], [])
            self.lines.append(line)
            continue
        
        anime = matplotlib.animation.FuncAnimation(fig, refresh, frames=1000,
                                                   interval=10, blit=False)
        pylab.show()
        
        print('stop')
        return
        
        


