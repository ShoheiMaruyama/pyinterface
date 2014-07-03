
import ctypes

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


# Wrapper Class
# -------------
class gpg3100(object):
    ndev = 1
    lib = None
    info = None
    mode = AD_INPUT_SINGLE
    ch_count = 0
    range = AD_10V
    
    def __init__(self, ndev=1, lib='library/lib_gpg3100.so'):
        self.set_device_number(ndev)
        if lib is None: pass
        else: self.load_library(lib)
        self.use_singleend()
        pass
    
    def load_library(self, lib):
        self.lib = ctypes.cdll.LoadLibrary(lib)
        self.get_device_info()
        return
    
    def set_device_number(self, ndev):
        self.ndev = ndev
        return
    
    def use_singleend(self):
        self.mode = AD_INPUT_SINGLE
        self.ch_count = self.info.ChCountS
        return
    
    def use_differential(self):
        self.mode = AD_INPUT_DIFF
        self.ch_count = self.info.ChCountD
        return
    
    def get_device_info(self):
        info = ADBoardSpec()
        self.lib.get_device_info(self.ndev, ctypes.byref(info))
        if info.ChCountS < info.ChCountD:
            tmp = info.ChCountS
            info.ChCountS = info.ChCountD
            info.ChCountD = tmp
            pass
        self.info = info
        return info
    
    def get_oneshot_ad(self):
        d = (ctypes.c_ushort * self.ch_count)(0, 0)
        self.lib.get_oneshot_ad(self.ndev, self.mode, self.range,
                                ctypes.byref(d), self.ch_count)
        return list(d)
