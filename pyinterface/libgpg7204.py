
import os
import ctypes
import pyinterface

#
# based on fbimtr.h (Version 1.01-01)
#


# ==========
# Structures
# ==========

# function pointer
# ----------------
LPMTRCALLBACK = ctypes.CFUNCTYPE(ctypes.c_ulong, ctypes.c_ulong)

# Original ACC 
# ------------
class MTRORIGINALACC(pyinterface.Structure):
    _fields_ = [('dwSpeed', ctypes.c_ulong),
                ('dwAcc', ctypes.c_ulong)]

# Motion 
# ------
class MTRMOTION(pyinterface.Structure):
    _fields_ = [('dwMode', ctypes.c_ulong),
                ('dwLowSpeed', ctypes.c_long),
                ('dwSpeed', ctypes.c_ulong),
                ('dwAcc', ctypes.c_ulong),
                ('dwDec', ctypes.c_ulong),
                ('dwSSpeed', ctypes.c_ulong),
                ('nStep', ctypes.c_long),
                ('nReserved', ctypes.c_long)]


# ==========
# Identifers
# ==========

MTR_FLAG_NORMAL = 0
MTR_FLAG_OVERLAPPED = 1


# 5: Base Clock
# =============

# Base Clock : Clock
# ------------------
MTR_CLOCK_1M = 0
MTR_CLOCK_1_4M = 1
MTR_CLOCK_1_16M = 2


# 6: Pulse Out
# ============

# Pulse Out : Mode
# ----------------
# MTR_METHOD = 0
# MTR_FINISH_FLAG = 3

# Pulse Out : Finish Flag
# -----------------------
# MTR_PULSE_OUT = 0
# MTR_INP = 1


# --

MTR_METHOD = 0
MTR_IDLING = 1
MTR_0P5PULSE = 1
MTR_1P5PULSE = 3
MTR_WIDTH = 2
MTR_FINISH_FLAG = 3
MTR_PULSE_OUT = 0
MTR_INP = 1
MTR_PULSE_OFF = 2

# --

# 7: Limit Config
# ===============

# Limit Config : Mode
# -------------------
# MTR_MASK = 0
# MTR_LOGIC = 1
# MTR_SIGNAL_FILTER = 8
# MTR_DI = 0x000
# MTR_LIMIT = 0x100
# MTR_SYNC_EXT = 0x200

# Limit Config : Signal Filter
# ----------------------------
# MTR_1MICRO = 0x10
# MTR_10MICRO = 0x11
# MTR_100MICRO = 0x12

MTR_MASK = 0
MTR_LOGIC = 1
MTR_SD_FUNC = 2
MTR_SD_ACTIVE = 3
MTR_ORG_FUNC = 4
MTR_ORG_ACTIVE = 5
MTR_ORG_EZ_COUNT = 6
MTR_ALM_FUNC = 7
MTR_SIGNAL_FILTER = 8
MTR_1MICRO = 0x10
MTR_10MICRO = 0x11
MTR_100MICRO = 0x12
MTR_DI = 0x000
MTR_LIMIT = 0x100
MTR_SYNC_EXT = 0x200

# --

MTR_CHANGE_SD_SPEED = 0

# --

MTR_DEC_STOP_SIGNAL = 1
MTR_SD_OFF = 2

# --

MTR_SIGNAL_LEVEL = 0
MTR_SIGNAL_EDGE = 1
MTR_SIGNAL_LATCH = 2

# --

MTR_ORG_STOP = 0
MTR_ORG_DEC_EZ_STOP = 1

# --

MTR_ORG_EZ_STOP = 2

# --

MTR_ALM_STOP = 0
MTR_ALM_DEC_STOP = 1

# --

MTR_OFF = 0
MTR_ON = 1

# --

MTR_ENCODER_MODE = 0
MTR_ENCODER_CLEAR = 1
MTR_COUNTER_CLEAR = 2

# --

MTR_NOT_COUNT = 0
MTR_SINGLE = 1
MTR_DOUBLE = 2
MTR_QUAD = 3
MTR_UP_DOWN = 4

# --

MTR_NOT_CLEAR = 0x0000
MTR_STOPPED_BY_ORG = 0x0001
MTR_STOPPED_BY_ORG_Z = 0x0002
MTR_NORMAL_STOPPED = 0x0004
MTR_STOPPED_BY_LIMIT = 0x0008

# --

MTR_COMP_CONFIG1 = 0
MTR_COMP_CONFIG2 = 1
MTR_COMP_CONFIG3 = 2
MTR_NO_COMP = 0
MTR_GT_COMP = 1
MTR_EQ_COMP = 2
MTR_PRESET1 = 3
MTR_PRESET2 = 4
MTR_PRESET3 = 5
MTR_COMP_OBJECT = 6
MTR_COMP_OBJECT1 = 6
MTR_COMP_OBJECT2 = 7
MTR_COMP_OUT = 9

# Set/GetCLR
# ----------
MTR_ONESHOT = 0
MTR_LEVEL = 1
MTR_CLR_OUT = 2

# 10: Motion
# ==========

# Motion : Mode
# -------------
# MTR_JOG = 0
# MTR_ORG = 1
# MTR_PTP = 2

MTR_JOG = 0
MTR_ORG = 1
MTR_PTP = 2
MTR_ORG_PLS = 3
MTR_TIMER = 4
MTR_LINE = 6
MTR_ARC = 7
MTR_DRAW_IN = 8
MTR_RESTART = 9

# 17: Start Motion
# ================

# Start Motion : Mode
# -------------------
# MTR_JOG = 0
# MTR_ORG = 1
# MTR_PTP = 2
# MTR_CONST = 0x10000

MTR_NORMAL = 0x00000
MTR_CONST = 0x10000

# MTRMOTION
# =========

# MTRMOTION.dwMode
# ----------------
# MTR_ACC_NORMAL = 0
# MTR_ACC_SIN = 1
# MTR_ACC_ORIGINAL = 3

MTR_ACC_NORMAL = 0
MTR_ACC_SIN = 1
MTR_ACC_EXP = 2
MTR_ACC_ORIGINAL = 3
MTR_FH = 0x100

# --

MTR_STOP_ORG = 0x0000
MTR_STOP_ORG_EZ = 0x0100

# --

MTR_SQUEAR_ROOT2 = 0x0200
MTR_MARK = 0x0400
MARK_ACC = 0x0800

# 18: Single Step
# ===============

# Single Step : Dir
# -----------------
MTR_CW = 1
MTR_CCW = -1

# 19: Stop Motion
# ===============

# Stop Motion : Mode
# ------------------
# MTR_DEC_STOP = 0
# MTR_IMMEDIATE_STOP = 1

MTR_DEC_STOP = 0
MTR_IMMEDIATE_STOP = 1
MTR_STOP_ALL = 2


# 9: Sync
# =======

# Sync : Synchronize
# ------------------
MTR_RESET_SYNC_START = 0
MTR_SET_SYNC_START = 1

# 21: Change Speed
# ================

# Change Speed : Mode
# -------------------
# MTR_IMMEDIATE_CHANGE = 0
# MTR_ACCDEC_CHANGE = 1

MTR_IMMEDIATE_CHANGE = 0
MTR_ACCDEC_CHANGE = 1
MTR_LOW_SPEED = 3
MTR_DEC_LOW_SPEED = 4
MTR_RELEASE_DEC = 5
MTR_HOLD_NOW_SPEED = 6
MTR_RELEASE_HOLD = 7

# --

MTR_ENCODER = 0
MTR_COUNTER = 1
MTR_REMAINS = 2

# 22: Status
# ==========

# Status : Mode
# -------------
MTR_BUSY = 0
MTR_FINISH_STATUS = 1
MTR_LIMIT_STATUS = 2
MTR_INTERLOCK_STATUS = 4
# MTR_ERROR_CODE = 5

# Status : Interlock
# ------------------
MTR_ILOCK_OFF = 0
MTR_ILOCK_ON = 1

# --

MTR_ERROR_CODE = 5
MTR_CONFIRM_END = 6

# --

MTR_COMPLETE = 0
MTR_NOT_COMPLETE = 1
MTR_COMPARATOR = 7

# --

MTR_NORMAL_SAMP = 0x0000
MTR_BUSY_SAMP = 0x0100
MTR_ONETIME = 0x0000
MTR_REPEAT = 0x1000

# --

MTR_SAMPLE_FINISHED = 0
MTR_NOW_SAMPLING = 1
MTR_WAITING_BUSY = 2
MTR_FULL_BUFFER = 3

# RETURN VALUE
# ============ 
MTR_ERROR_SUCCESS = 0
MTR_ERROR_NOT_DEVICE = 0xc0000001
MTR_ERROR_NOT_OPEN = 0xc0000002
MTR_ERROR_INVALID_DEVICE_NUMBER = 0xc0000003
MTR_ERROR_ALREADY_OPEN = 0xc0000004
MTR_ERROR_NOT_SUPPORTED = 0xc0000009
MTR_ERROR_NOW_MOVING = 0xc0001000
MTR_ERROR_NOW_STOPPED = 0xc0001001
MTR_ERROR_WRITE_FAILED = 0xc0001010
MTR_ERROR_READ_FAILED = 0xc0001011
MTR_ERROR_INVALID_AXIS = 0xc0001013
MTR_ERROR_INVALID_SPEED = 0xc0001014
MTR_ERROR_INVALID_ACCDEC = 0xc0001015
MTR_ERROR_INVALID_PULSE = 0xc0001016
MTR_ERROR_INVALID_PARAMETER = 0xc0001017
MTR_ERROR_NOW_INTERLOCKED = 0xc0001020
MTR_ERROR_IMPOSSIBLE = 0xc0001021
MTR_ERROR_NOT_ALLOCATE_MEMORY = 0xc0001024


# =========
# Functions
# =========

SO_DIR = '/usr/lib'
SO_NAME = 'libgpg7204.so'
SO_PATH = os.path.join(SO_DIR, SO_NAME)

try:
    lib = ctypes.cdll.LoadLibrary(SO_PATH)
except OSError:
    pass
else:
    pyinterface.so_available.append(SO_PATH)
    
    _P = ctypes.POINTER
    _char_p = ctypes.c_char_p
    _ubyte = ctypes.c_ubyte
    _ushort = ctypes.c_ushort
    _ushort_p = _P(ctypes.c_ushort)
    _int = ctypes.c_int
    _int_p = _P(ctypes.c_int)
    _uint = ctypes.c_uint
    _long = ctypes.c_long
    _long_p = _P(ctypes.c_long)
    _ulong = ctypes.c_ulong
    _ulong_p = _P(ctypes.c_ulong)
    _float = ctypes.c_float
    _float_p = _P(ctypes.c_float)
    _void_p = ctypes.c_void_p

    # int MtrOpen( int );
    # -------------------
    MtrOpen = lib.MtrOpen
    MtrOpen.restype = _uint
    MtrOpen.argtypes = (_int,)

    # int MtrClose(int);
    # ------------------
    MtrClose = lib.MtrClose
    MtrClose.restype = _uint
    MtrClose.argtypes = (_int,)

    # int MtrReset(int);
    # ------------------
    MtrReset = lib.MtrReset
    MtrReset.restype = _uint
    MtrReset.argtypes = (_int,)

    # int MtrOffInterLock(int);
    # -------------------------
    MtrOffInterLock = lib.MtrOffInterLock
    MtrOffInterLock.restype = _uint
    MtrOffInterLock.argtypes = (_int,)

    
    # int MtrSetBaseClock(int,  unsigned long);
    # -----------------------------------------
    MtrSetBaseClock = lib.MtrSetBaseClock
    MtrSetBaseClock.restype = _uint
    MtrSetBaseClock.argtypes = (_int, _ulong)

    # int MtrSetPulseOut(int, unsigned long, unsigned long);
    # ------------------------------------------------------
    MtrSetPulseOut = lib.MtrSetPulseOut
    MtrSetPulseOut.restype = _uint
    MtrSetPulseOut.argtypes = (_int, _ulong, _ulong)

    # int MtrSetLimitConfig(int, unsigned long, unsigned long);
    # ---------------------------------------------------------
    MtrSetLimitConfig = lib.MtrSetLimitConfig
    MtrSetLimitConfig.restype = _uint
    MtrSetLimitConfig.argtypes = (_int, _ulong, _ulong)

    # int MtrSetAccCurve(int, unsigned long, PMTRORIGINALACC);
    # --------------------------------------------------------
    MtrSetAccCurve = lib.MtrSetAccCurve
    MtrSetAccCurve.restype = _uint
    MtrSetAccCurve.argtypes = (_int, _ulong, _P(MTRORIGINALACC))

    # int MtrSetSync(int, unsigned long);
    # -----------------------------------
    MtrSetSync = lib.MtrSetSync
    MtrSetSync.restype = _uint
    MtrSetSync.argtypes = (_int, _ulong)

    # int MtrSetMotion(int, unsigned long, PMTRMOTION);
    # -------------------------------------------------
    MtrSetMotion = lib.MtrSetMotion
    MtrSetMotion.restype = _uint
    MtrSetMotion.argtypes = (_int, _ulong, _P(MTRMOTION))

    
    # int MtrGetBaseClock(int,  unsigned long*);
    # ------------------------------------------
    MtrGetBaseClock = lib.MtrGetBaseClock
    MtrGetBaseClock.restype = _uint
    MtrGetBaseClock.argtypes = (_int, _ulong_p)

    # int MtrGetPulseOut(int, unsigned long, unsigned long*);
    # -------------------------------------------------------
    MtrGetPulseOut = lib.MtrGetPulseOut
    MtrGetPulseOut.restype = _uint
    MtrGetPulseOut.argtypes = (_int, _ulong, _ulong_p)

    # int MtrGetLimitConfig(int, unsigned long, unsigned long*);
    # ----------------------------------------------------------
    MtrGetLimitConfig = lib.MtrGetLimitConfig
    MtrGetLimitConfig.restype = _uint
    MtrGetLimitConfig.argtypes = (_int, _ulong, _ulong_p)

    # int MtrGetAccCurve(int, unsigned long*, PMTRORIGINALACC);
    # ---------------------------------------------------------
    MtrGetAccCurve = lib.MtrGetAccCurve
    MtrGetAccCurve.restype = _uint
    MtrGetAccCurve.argtypes = (_int, _ulong_p, _P(MTRORIGINALACC))

    # int MtrGetSync(int, unsigned long*);
    # ------------------------------------
    MtrGetSync = lib.MtrGetSync
    MtrGetSync.restype = _uint
    MtrGetSync.argtypes = (_int, _ulong_p)

    # int MtrGetMotion(int, unsigned long, PMTRMOTION);
    # -------------------------------------------------
    MtrGetMotion = lib.MtrGetMotion
    MtrGetMotion.restype = _uint
    MtrGetMotion.argtypes = (_int, _ulong, _P(MTRMOTION))

    
    # int MtrStartMotion(int, unsigned long);
    # ---------------------------------------
    MtrStartMotion = lib.MtrStartMotion
    MtrStartMotion.restype = _uint
    MtrStartMotion.argtypes = (_int, _ulong)

    # int MtrSingleStep(int, int);
    # ----------------------------
    MtrSingleStep = lib.MtrSingleStep
    MtrSingleStep.restype = _uint
    MtrSingleStep.argtypes = (_int, _int)

    # int MtrStartSync(int);
    # ----------------------
    MtrStartSync = lib.MtrStartSync
    MtrStartSync.restype = _uint
    MtrStartSync.argtypes = (_int,)

    # int MtrStopMotion(int, unsigned long);
    # --------------------------------------
    MtrStopMotion = lib.MtrStopMotion
    MtrStopMotion.restype = _uint
    MtrStopMotion.argtypes = (_int, _ulong)

    # int MtrChangeSpeed(int, unsigned long, unsigned long);
    # ------------------------------------------------------
    MtrChangeSpeed = lib.MtrChangeSpeed
    MtrChangeSpeed.restype = _uint
    MtrChangeSpeed.argtypes = (_int, _ulong, _ulong)

    
    # int MtrGetStatus(int, unsigned long, unsigned long*);
    # -----------------------------------------------------
    MtrGetStatus = lib.MtrGetStatus
    MtrGetStatus.restype = _uint
    MtrGetStatus.argtypes = (_int, _ulong, _ulong_p)

    # int MtrReadSpeed(int, unsigned long*);
    # --------------------------------------
    MtrReadSpeed = lib.MtrReadSpeed
    MtrReadSpeed.restype = _uint
    MtrReadSpeed.argtypes = (_int, _ulong_p)

    # int MtrReadCounter(int, unsigned long, long*);
    # ----------------------------------------------
    MtrReadCounter = lib.MtrReadCounter
    MtrReadCounter.restype = _uint
    MtrReadCounter.argtypes = (_int, _ulong, _long_p)

    # int MtrWriteCounter(int, unsigned long, long);
    # ----------------------------------------------
    MtrWriteCounter = lib.MtrWriteCounter
    MtrWriteCounter.restype = _uint
    MtrWriteCounter.argtypes = (_int, _ulong, _long)

    # int MtrClearCounter(int, unsigned long);
    # ----------------------------------------
    MtrClearCounter = lib.MtrClearCounter
    MtrClearCounter.restype = _uint
    MtrClearCounter.argtypes = (_int, _ulong)

    
    # int MtrOutputDO(int, unsigned long);
    # ------------------------------------
    MtrOutputDO = lib.MtrOutputDO
    MtrOutputDO.restype = _uint
    MtrOutputDO.argtypes = (_int, _ulong)

    # int MtrInputDI(int, unsigned long*);
    # ------------------------------------
    MtrInputDI = lib.MtrInputDI
    MtrInputDI.restype = _uint
    MtrInputDI.argtypes = (_int, _ulong_p)

    
    # int MtrSetEvent(int, unsigned long, PLPMTRCALLBACK, unsigned long);
    # -------------------------------------------------------------------
    MtrSetEvent = lib.MtrSetEvent
    MtrSetEvent.restype = _uint
    MtrSetEvent.argtypes = (_int, _ulong, _P(LPMTRCALLBACK), _ulong)
    
    # int MtrGetEvent(int, unsigned long*, PLPMTRCALLBACK, unsigned long*);
    # ---------------------------------------------------------------------
    MtrGetEvent = lib.MtrGetEvent
    MtrGetEvent.restype = _uint
    MtrGetEvent.argtypes = (_int, _ulong_p, _P(LPMTRCALLBACK), _ulong_p)





