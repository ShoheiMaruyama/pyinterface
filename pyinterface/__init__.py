
import os
import ctypes

LIB_DIR = 'library'
LIB_PATH = os.path.join(__path__[0], LIB_DIR)

so_available = []

# ==============
# Common Classes
# ==============

# Error
# =====
class InterfaceError(Exception):
    pass

# Identifer
# =========

# identifer container
# -------------------
class Identifer(object):
    @classmethod
    def verify(cls, to_be_verified):
        for key, value in cls.__dict__.iteritems():
            if value == to_be_verified: return value
            continue
        raise ValueError, '%s is not supported in %s.%s'%(to_be_verified, cls.__module__, cls.__name__)
        pass
    
    @classmethod
    def get_id(cls, to_be_verified):
        for key, value in cls.__dict__.iteritems():
            if value == to_be_verified: return key
            continue
        return 'NO ID'
    
    @classmethod
    def get_element(cls, to_be_verified):
        for key, value in cls.__dict__.iteritems():
            if value == to_be_verified: return value
            continue
        return None
    
    @classmethod
    def print_members(cls):
        dic = dict(cls.__dict__)
        for key, value in dic.items():
            if not key.isupper(): dic.pop(key)
            continue
        
        maxlen = max([len(d) for d in dic.keys()])
        fmt = '%%-%ds'%(maxlen)
        for key, value in sorted(dic.items(), key=lambda x: x[1]):
            print(fmt%(key) + ' :  %d'%(value))
            continue
        return
        
    @classmethod
    def get_members(cls):
        dic = dict(cls.__dict__)
        for key, value in dic.items():
            if not key.isupper(): dic.pop(key)
            continue
        return dic


# identifer element
# -----------------
class IdentiferElement(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        pass
    
    def __repr__(self):
        t = type(self)
        return "%s.%s(id=%d, name='%s')"%(t.__module__, t.__name__, self.id, self.name)

    def __str__(self):
        return self.name
    
    def __int__(self):
        return self.id
    
    def __eq__(self, x):
        if self.id == x: return True
        if self.name == x: return True
        return False
    
    def __and__(self, x):
        if self.id & x: return 1
        return 0

class BitIdentifer(object):
    size = 0
    bits = []
    
    def __init__(self, value=None):
        if value is not None:
            if type(value)==int: self.set(value)
            if type(value)==str: self.set_by_str(value)
            pass
        pass
    
    def __int__(self):
        return sum([int(b) for b in self.bits])
    
    def __repr__(self):
        msg = '%s\n'%(object.__repr__(self))
        for b in self.bits:
            if b.is_set():
                msg += '%3d : %s = %d (%s)\n'%(b.bit, b.name, b, b)
            else:
                msg += '%3d :   (%s)\n'%(b.bit, b.name)
                pass
        return msg
        
    def __len__(self):
        return self.size
        
    def __getitem__(self, i):
        return self.bits[i]
        
    def set(self, value):
        [b.set(value) for b in self.bits]
        return
        
    def set_by_str(self, string):
        [b.set_by_str(string) for b in self.bits]
        return
    
    def _get(self, on_off='ON'):
        if on_off=='ON': return [b.bit for b in self.bits if b&b.is_set()]
        return [b.bit for b in self.bits if (not b)&b.is_set()]
        
    def get_on(self):
        return ', '.join(['%d:%s'%(b.bit, b.name) for b in self._get('ON')])

    def get_off(self):
        return ', '.join(['%d:%s'%(b.bit, b.name) for b in self._get('OFF')])
    
    def get_ind_on(self):
        return [b.bit for b in self._get('ON')]

    def get_ind_off(self):
        return [b.bit for b in self._get('OFF')]

    def count_on(self):
        return sum([1 for b in self._get('ON')])

    def count_off(self):
        return sum([1 for b in self._get('OFF')])


class BitIdentiferElement(object):
    name = 'N/A'
    val0 = ''
    val1 = ''
    value = 0
    bit = 0
    
    def __init__(self, bit):
        self.bit = bit
        pass
    
    def __int__(self):
        if self.value==1: return 2**self.bit
        return 0
    
    def __bool__(self):
        if not self.is_set(): return False
        return bool(self.value)
    # for python 2.x
    __nonzero__ = __bool__
        
    def __repr__(self):
        msg = '%s\n'%(object.__repr__(self))
        if self.is_set():
            msg += '%d, (%d:%s=%s)'%(self, self.bit, self.name, self)
        else:
            msg += '%d, (%d:%s)'%(self, self.bit, self.name)
            pass
        return msg
        
    def __str__(self):
        if self.name=='N/A': return ''
        if self: return self.val1
        return self.val0
    
    def is_set(self):
        if self.name =='N/A': return False
        return True
        
    def set(self, value):
        if value & 2**self.bit: return self.set_on()
        return self.set_off()
    
    def set_by_str(self, string):
        if self.name in string: return self.set_on()
        return self.set_off()
        
    def set_on(self):
        self.value = 1
        return
        
    def set_off(self):
        self.value = 0
        return
        
    def set_params(self, name, v0, v1):
        self.name = name
        self.val0 = v0
        self.val1 = v1
        return
    

# error code
# ----------
class ErrorCode(object):
    @classmethod
    def check(cls, to_be_checked):
        if to_be_checked == cls._success: return
        for key, value in cls.__dict__.iteritems():
            if key[0]=='_': continue
            if value == to_be_checked: 
                raise InterfaceError, '%s (0x%X)'%(key, to_be_checked)
            continue
        raise InterfaceError, 'UnknownError (0x%X)'%(to_be_checked)
        pass

# ctypes.Structure wrapper
# ========================
class Structure(ctypes.Structure):
    def __str__(self):
        keys = [key for key, dtype in self._fields_]
        maxlen = max([len(k) for k in keys])
        fmt = '%%-%ds'%(maxlen)
        msg = ''
        for key in keys:
            msg += fmt%(key) + ' :  %s\n'%(self.__getattribute__(key))
            continue
        return msg
    

# 
# ======================


# ---

import gpg3100
import gpg3300
#import gpg7400

from gpg3100 import gpg3100 as create_gpg3100
from gpg3300 import gpg3300 as create_gpg3300
#from gpg7400 import gpg7400 as create_gpg7400





