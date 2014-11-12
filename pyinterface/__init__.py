
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

from gpg3100 import gpg3100
import gpg3300
from gpg3300 import gpg3300 as create_gpg3300





