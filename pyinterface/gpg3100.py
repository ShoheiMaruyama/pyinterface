
import os
import time
import ctypes
import socket
import threading
try: import cPickle as pickle
except: import pickle
import numpy

import pyinterface

# configurations
# ==============

# shared object
# -------------

SO_NAME = 'lib_gpg3100.so'
SO_PATH = os.path.join(pyinterface.LIB_PATH, SO_NAME)


# Identifers
# ----------

class identifer(object):
    @classmethod
    def verify(cls, to_be_verified):
        for key, value in cls.__dict__.iteritems():
            if value == to_be_verified: return value
            continue
        raise ValueError, '%s is not supported in %s.%s'%(to_be_verified, __name__, cls.__name__)
        pass
    
    @classmethod
    def print_members(cls):
        dic = dict(cls.__dict__)
        for key, value in dic.items():
            if not key.isupper(): dic.pop(key)
            continue
        
        maxlen = max([len(d) for d in dic.keys()])
        fmt = '%%-%ds'%(maxlen)
        for key, value in sorted(dic.items(), key=lambda x: x[1]):
            print(fmt%(key) + ' :  %s'%(value))
            continue
        return
        
    @classmethod
    def get_members(cls):
        dic = dict(cls.__dict__)
        for key, value in dic.items():
            if not key.isupper(): dic.pop(key)
            continue
        return dic
        

class ADMODE(identifer):
    SINGLE = 1
    DIFF = 2
    pass

class ADRANGE(identifer):
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
    pass


# Structures
# ----------

class ADBoardSpec(ctypes.Structure):
    _fields_ = [('BoardType', ctypes.c_ulong),
                ('BoardID', ctypes.c_ulong),
                ('SamplingMode', ctypes.c_ulong),
                ('ChCountS', ctypes.c_ulong),
                ('ChCountD', ctypes.c_ulong),
                ('Resolution', ctypes.c_ulong),
                ('Range', ctypes.c_ulong),
                ('Isolation', ctypes.c_ulong),
                ('DI', ctypes.c_ulong),
                ('DO', ctypes.c_ulong)]
    # COMMENT: The definition in the manual (help.pdf) is wrong.
    #          Must check the source code "include/fbiad.h".
    
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

class lib_gpg3100(object):
    libpath = str
    lib = ctypes.CDLL
    
    def __init__(self, libpath):
        self.libpath = libpath
        self.lib = ctypes.cdll.LoadLibrary(libpath)
        pass
    
    def get_device_info(self, ndev):
        c_ndev = ctypes.c_long(int(ndev))
        info = ADBoardSpec()
        self.lib.get_device_info(c_ndev, ctypes.byref(info))
        return info
    
    def get_oneshot_ad(self, ndev, ch_count, mode, adrange):
        c_ndev = ctypes.c_long(int(ndev))
        c_mode = ctypes.c_ulong(ADMODE.verify(mode))
        c_range = ctypes.c_ulong(ADRANGE.verify(adrange))
        d = (ctypes.c_ushort * int(ch_count))(0)
        self.lib.get_oneshot_ad(c_ndev, c_mode, c_range,
                                ctypes.byref(d))
        return numpy.array(list(d))
    
    def get_ad(self, ndev, num, freq, start, ch_count, mode, adrange):
        c_ndev = ctypes.c_long(int(ndev))
        c_num = ctypes.c_ulong(int(num))
        c_freq = ctypes.c_float(float(freq))
        c_start = ctypes.c_double(float(start))
        c_mode = ctypes.c_ulong(ADMODE.verify(mode))
        c_range = ctypes.c_ulong(ADRANGE.verify(adrange))
        d = (ctypes.c_ushort * (int(ch_count) * int(num)))(0)
        self.lib.get_ad(c_ndev, c_mode, c_range, c_num,
                        c_freq, c_start, ctypes.byref(d))
        return numpy.array(list(d)).reshape([num, ch_count])


class gpg3100(object):
    ndev = int()
    nchannel = int()
    info = ADBoardSpec()
    
    mode = ADMODE
    range = ADRANGE
    
    datalog = []
    
    def __init__(self, ndev=1, libpath=SO_PATH):
        self.ndev = ndev
        self.lib = lib_gpg3100(libpath)
        self.initialize()
        return
    
    def initialize(self):
        self.get_device_info()
        self.use_singleend()
        default_range = max(self.read_available_range().values())
        self.set_range(default_range)
        return
        
    def read_inputmode(self):
        return self.mode
    
    def read_channels(self):
        return self.nchannel
    
    def use_singleend(self):
        self.mode = ADMODE.SINGLE
        self.nchannel = self.info.ChCountS
        return
    
    def use_differential(self):
        self.mode = ADMODE.DIFF
        self.nchannel = self.info.ChCountD
        return
    
    def _verify_available_range(self, to_be_verified):
        to_be_verified = ADRANGE.verify(to_be_verified)
        if (self.info.Range & to_be_verified)!=0:
            return to_be_verified
        raise ValueError, 'ADRANGE=%s is not supported in BoardType=%s'%(to_be_verified, self.info.BoardType)
        pass
        
    def read_available_range(self):
        dic = ADRANGE.get_members()
        for key, value in dic.items():
            if (value & self.info.Range)==0: dic.pop(key)
            continue
        return dic
    
    def print_available_range(self):
        dic = self.read_available_range()
        maxlen = max([len(d) for d in dic.keys()])
        fmt = '%%-%ds'%(maxlen)
        for key, value in sorted(dic.items(), key=lambda x: x[1]):
            print(fmt%(key) + ' :  %s'%(value))
            continue
        return
    
    def read_range(self):
        return self.range
    
    def set_range(self, adrange):
        self.range = self._verify_available_range(adrange)
        return
    
    def print_device_info(self):
        print(self.info)
        return
    
    def get_device_info(self):
        self.info = self.lib.get_device_info(self.ndev)
        return self.info
    
    def read_device_info(self):
        return self.info
    
    def get_oneshot_ad(self):
        ret = self.lib.get_oneshot_ad(self.ndev, self.nchannel, self.mode, self.range)
        self.datalog = ret
        return ret
    
    def get_ad(self, num, freq, start=0):
        ret = self.lib.get_ad(self.ndev, num, freq, start, self.nchannel, self.mode, self.range)
        self.datalog = ret
        return ret
    
    def read_latestdata(self):
        return self.datalog
        


