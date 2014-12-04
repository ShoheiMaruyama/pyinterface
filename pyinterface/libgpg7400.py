
import os
import ctypes
import pyinterface

#
# based on fbimtn.h (Version 1.01-02)
#

# ==========
# Structures
# ==========

# function pointer
# ----------------
PLPMTNDVCALLBACK = ctypes.CFUNCTYPE(ctypes.c_ulong, ctypes.c_ulong)
PLPMTNCALLBACK = ctypes.CFUNCTYPE(ctypes.c_ulong, ctypes.c_ulong)

# Return code 
# -----------
class MTNRETCODE(pyinterface.Structure):
    _fields_ = [('ulResultCode', ctypes.c_ulong*4)]

# Buffer 
# ------
class MTNBUFDATA(pyinterface.Structure):
    _fields_ = [('wBufData', ctypes.c_ubyte*4)]

# Interupt 
# --------
class MTNINTRDATA(pyinterface.Structure):
    _fields_ = [('lpCallBackProc', PLPMTNDVCALLBACK),
                ('ulUser', ctypes.c_ulong),
                ('uReserved', ctypes.c_uint)]

# Factor 
# ------
class MTNEVENTFACTOR(pyinterface.Structure):
    _fields_ = [('ulREST', ctypes.c_ulong*4),
                ('ulRIST', ctypes.c_ulong*4)]

# Motion 
# ------
class MTNMOTION(pyinterface.Structure):
    _fields_ = [('wClock', ctypes.c_ushort),
                ('wAccMode', ctypes.c_ushort),
                ('fLowSpeed', ctypes.c_float),
                ('fSpeed', ctypes.c_float),
                ('ulAcc', ctypes.c_ulong),
                ('ulDec', ctypes.c_ulong),
                ('fSAccSpeed', ctypes.c_float),
                ('fSDecSpeed', ctypes.c_float),
                ('lStep', ctypes.c_long)]

# MotionLine 
# ----------
class MTNLINE(pyinterface.Structure):
    _fields_ = [('wAxis', ctypes.c_ushort),
                ('wClock', ctypes.c_ushort),
                ('wMode', ctypes.c_ushort),
                ('wAccMode', ctypes.c_ushort),
                ('fLowSpeed', ctypes.c_float),
                ('fSpeed', ctypes.c_float),
                ('ulAcc', ctypes.c_ulong),
                ('ulDec', ctypes.c_ulong),
                ('fSAccSpeed', ctypes.c_float),
                ('fSDecSpeed', ctypes.c_float),
                ('lStep', ctypes.c_long*4)]

# MotionArc 
# ---------
class MTNARC(pyinterface.Structure):
    _fields_ = [('wAxis', ctypes.c_ushort),
                ('wClock', ctypes.c_ushort),
                ('wMode', ctypes.c_ushort),
                ('fSpeed', ctypes.c_float),
                ('lCenterX', ctypes.c_long),
                ('lCenterY', ctypes.c_long),
                ('lEndX', ctypes.c_long),
                ('lEndY', ctypes.c_long)]

# Comparator 
# ----------
class MTNCOMP(pyinterface.Structure):
    _fields_ = [('wConfig', ctypes.c_ushort),
                ('wMotion', ctypes.c_ushort),
                ('lCounter', ctypes.c_long),
                ('wCntType', ctypes.c_ushort)]

# Event Mask 
# ----------
class MTNEVENTTABLE(pyinterface.Structure):
    _fields_ = [('wPulseOut', ctypes.c_ushort),
                ('wCounter', ctypes.c_ushort),
                ('wComparator', ctypes.c_ushort),
                ('wSignal', ctypes.c_ushort),
                ('wReserved', ctypes.c_ushort)]

# Interrupt 
# ---------
class MTNEVENTREQ(pyinterface.Structure):
    _fields_ = [('lpCallBackProc', PLPMTNCALLBACK),
                ('ulUser', ctypes.c_ulong)]

# Sampling 
# --------
class MTNSAMPLEREQ(pyinterface.Structure):
    _fields_ = [('wAxis', ctypes.c_ushort),
                ('wMode', ctypes.c_ushort),
                ('ulSampleRate', ctypes.c_ulong),
                ('ulBufferSize', ctypes.c_ulong),
                ('ulSampleCounter', ctypes.c_ulong)]

# Sampling Data 
# -------------
class MTNSAMPDATA(pyinterface.Structure):
    _fields_ = [('lPosX', ctypes.c_long),
                ('lPosY', ctypes.c_long),
                ('lPosZ', ctypes.c_long),
                ('lPosU', ctypes.c_long)]

# Structure of MtnDeviceFind Data
# -------------------------------
class MTN_FIND_DEV(pyinterface.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('rsw', ctypes.c_int),
                ('subsys', ctypes.c_int)]


# ==========
# Identifers
# ==========

MTR_CLOCK_1M = 0
MTR_CLOCK_1_4M = 1
MTR_CLOCK_1_16M = 2

# --

MTR_0P5PULSE = 1
MTR_1P5PULSE = 3

# --

MTR_1MICRO = 0x10
MTR_10MICRO = 0x11
MTR_100MICRO = 0x12
MTR_DI = 0x000

# --

MTR_NOT_COUNT = 0

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

# --

MTR_NORMAL = 0x00000

# --

MTR_ACC_EXP = 2
MTR_ACC_ORIGINAL = 3

# --

MTR_STOP_ORG = 0x0000
MTR_STOP_ORG_EZ = 0x0100

# --

MTR_SQUEAR_ROOT2 = 0x0200
MTR_MARK = 0x0400
MTR_MARK_ACC = 0x0800

# --

MTR_STOP_ALL = 2

# --

MTR_RESET_SYNC_START = 0
MTR_SET_SYNC_START = 1

# --

MTR_RELEASE_DEC = 5
MTR_HOLD_NOW_SPEED = 6
MTR_RELEASE_HOLD = 7

# --

MTR_ERROR_CODE = 5
MTR_CONFIRM_END = 6

# --

MTR_COMPLETE = 0
MTR_NOT_COMPLETE = 1
MTR_COMPARATOR = 7

# --

MTR_NORMAL_SAMP = 0x0000
MTR_ONETIME = 0x0000

# --

MTR_COUNTER_CLEAR = 2

# --

MTR_ORG_PLS = 0x03

# --

MTR_NONE = 0xffffffff

# Open Flag
# --------- **
MTR_FLAG_NORMAL = 0x00
MTR_FLAG_OVERLAPPED = 0x01
MTR_ILOCK_RESET_OFF = 0x10
MTR_EXT_RESET_OFF = 0x100
MTR_FLAG_SHARE = 0x10000

# Reset Mode
# ---------- **
MTR_RESET_CTL = 0x00
MTR_RESET_MOTION = 0x01

# Pulse Out Config Section
# ======================== **
MTR_METHOD = 0x00
MTR_IDLING = 0x01
MTR_FINISH_FLAG = 0x03
MTR_SYNC_OUT = 0x04

# Pulse Out Config : Finish Flag
# ------------------------------ **
MTR_PULSE_OUT = 0x00
MTR_INP = 0x01
MTR_PULSE_OFF = 0x02

# Pulse Out Config : Sync Out Mode
# -------------------------------- **
MTR_SYNC_OFF = 0x00
# MTR_COMP1 = 0x01
# MTR_COMP2 = 0x02
# MTR_COMP3 = 0x03
# MTR_COMP4 = 0x04
# MTR_COMP5 = 0x05
MTR_ACC_START = 0x08
MTR_ACC_FINISH = 0x09
MTR_DEC_START = 0x0a
MTR_DEC_FINISH = 0x0b

# Limit Config Section
# ==================== **
MTR_MASK = 0x00
MTR_LOGIC = 0x01
MTR_SD_FUNC = 0x02
MTR_SD_ACTIVE = 0x03
MTR_ORG_FUNC = 0x04
MTR_ORG_ACTIVE = 0x05
MTR_ORG_EZ_COUNT = 0x06
MTR_ALM_FUNC = 0x07
MTR_SIGNAL_FILTER = 0x08
MTR_EL_FUNC = 0x09
MTR_EZ_ACTIVE = 0x10
MTR_LTC_FUNC = 0x11
MTR_CLR_FUNC = 0x12
MTR_PCS_FUNC = 0x13
MTR_PCS_ACTIVE = 0x14

# Limit Config : SD Func
# ---------------------- **
MTR_CHANGE_SD_SPEED = 0x00
MTR_DEC_STOP_SIGNAL = 0x01
MTR_SD_OFF = 0x02

# Limit Config : SD Active
# ------------------------ **
MTR_SIGNAL_LEVEL = 0x00
MTR_SIGNAL_LATCH = 0x02

# Limit Config : ORG Func
# ----------------------- **
MTR_ORG_STOP = 0x00
MTR_ORG_DEC_EZ_STOP = 0x01
MTR_ORG_EZ_STOP = 0x02
MTR_ORG_REVERSAL = 0x03
MTR_ORG_REV_EZ_STOP = 0x04
MTR_ORG_STOP_ZERO = 0x05
MTR_ORG_EZ_STOP_ZERO = 0x06
MTR_ORG_REV_EZ_ZERO = 0x07

# Limit Config : ALM Func
# ----------------------- **
MTR_ALM_STOP = 0x00
MTR_ALM_DEC_STOP = 0x01

# Limit Config : Signal Filter
# ---------------------------- **
MTR_OFF = 0x00
MTR_ON = 0x01

# Limit Config : EL Func
# ---------------------- **
MTR_EL_STOP = 0x00
MTR_EL_DEC_STOP = 0x01

# Limit Config : EZ Active
# ------------------------ **
MTR_DOWN_EDGE = 0x00
MTR_UP_EDGE = 0x01

# Limit Config : LTC Func
# ----------------------- **
# MTR_DOWN_EDGE = 0x00
# MTR_UP_EDGE = 0x01

# Limit Config : CLR Func
# ----------------------- **
# MTR_DOWN_EDGE = 0x00
# MTR_UP_EDGE = 0x01
MTR_LOW_LEVEL = 0x02
MTR_HIGH_LEVEL = 0x03

# Limit Config : PCS Func
# ----------------------- **
# MTR_OFF = 0x00
# MTR_ON = 0x01
# MTR_EXT_START = 0x02

# Counter Config Section
# ====================== **
MTR_ENCODER_MODE = 0x00
MTR_ENCODER_CLEAR = 0x01
MTR_COUNTER_CLEAR_ORG = 0x02
MTR_COUNTER_CLEAR_CLR = 0x03
MTR_LATCH_MODE = 0x04
MTR_DECLINO_MODE = 0x05
MTR_SOFT_LATCH = 0x06

# Counter Config : Encoder Mode
# ----------------------------- **
MTR_SINGLE = 0x01
MTR_DOUBLE = 0x02
MTR_QUAD = 0x03
MTR_UP_DOWN = 0x04

# Counter Config : Latch Mode
# --------------------------- **
# MTR_OFF = 0x00
# MTR_ORG = 0x01
MTR_LTC = 0x02
# MTR_COMP4 = 0x04
# MTR_COMP5 = 0x05

# Counter Config : Declino Mode
# ----------------------------- **
# MTR_DECLINO = 0x100
MTR_SPEED = 0x00

# Comparator
# ========== **
MTR_COMP1 = 0x01
MTR_COMP2 = 0x02
MTR_COMP3 = 0x03
MTR_COMP4 = 0x04
MTR_COMP5 = 0x05

# Sync Section
# ============ **
MTR_START_MODE = 0x00
MTR_EXT_START = 0x02
MTR_EXT_STOP = 0x03
MTR_START_LINE = 0x04
MTR_STOP_LINE = 0x05

# Sync : Start Mode
# ----------------- **
# MTR_NO = 0x00
MTR_X = 0x01
MTR_Y = 0x02
MTR_Z = 0x04
MTR_U = 0x08
MTR_SYNC_X = 0x10
MTR_SYNC_Y = 0x11
MTR_SYNC_Z = 0x12
MTR_SYNC_U = 0x13
MTR_SYNC_EXT = 0x20

# Sync : Ext Stop
# --------------- **
# MTR_OFF = 0x00
MTR_CSTP_STOP = 0x01
MTR_CSTP_DEC_STOP = 0x02

# --

MTR_SIGNAL_EDGE = 0x01

# --

# Set/GetCLR
# ----------
MTR_ONESHOT = 0
MTR_CLR_OUT = 2

# Motion Section
# ============== **
MTR_JOG = 0x00
MTR_ORG = 0x01
MTR_PTP = 0x02
MTR_TIMER = 0x04
MTR_SINGLE_STEP = 0x05
MTR_ORG_SEARCH = 0x10
MTR_ORG_EXIT = 0x11
MTR_ORG_ZERO = 0x12
MTR_PTP_REPEAT = 0x10000
MTR_REPEAT_CLEAR = 0x20000
MTR_START_MODE_OFF = 0x40000

MTR_DRAW_IN = 0x08
MTR_RESTART = 0x09
MTR_LIMIT = 0x100

# Motion Line Section
# =================== **
MTR_LINE_NORMAL = 0x00
MTR_LINE_REPEAT = 0x10000
# MTR_REPEAT_CLEAR = 0x20000
# MTR_START_MODE_OFF = 0x40000

# Motion Arc Section
# ================== **
MTR_ARC_NORMAL = 0x00
MTR_ARC_REPEAT = 0x10000
# MTR_REPEAT_CLEAR = 0x20000
# MTR_START_MODE_OFF = 0x40000

# Start Motion
# ============ **
MTR_ACC = 0x00
MTR_CONST = 0x01
MTR_CONST_DEC = 0x02

# Motion Mode
# ----------- **
# MTR_JOG = 0x00
# MTR_ORG = 0x01
# MTR_PTP = 0x02
# MTR_TIMER = 0x04
# MTR_SINGLE_STEP = 0x05
# MTR_ORG_SEARCH = 0x10
# MTR_ORG_EXIT = 0x11
# MTR_ORG_ZERO = 0x12
MTR_LINE = 0x06
MTR_SYNC_LINE = 0x07
MTR_ARC = 0x08
MTR_CP = 0x20
# MTR_LIMIT = 0x100
# MTR_ABSOLUTE = 0x200

# Stop Motion
# =========== **
MTR_DEC_STOP = 0x00
MTR_IMMEDIATE_STOP = 0x01

# Output Sync
# =========== **
# MTR_EXT_START = 0x02
# MTR_EXT_STOP = 0x03
MTR_SYNC_NORMAL = 0x05
MTR_SYNC_SLAVE = 0x06
MTR_SYNC_MASTER = 0x07

# Change Speed
# ============ **
MTR_IMMEDIATE_CHANGE = 0x00
MTR_ACCDEC_CHANGE = 0x01
MTR_LOW_SPEED = 0x03
MTR_DEC_LOW_SPEED = 0x04

# ChangeStep
# ==========
MTR_RELATIVE = 0x00

# Status Section
# ============== **
MTR_BUSY = 0x00
MTR_FINISH_STATUS = 0x01
MTR_LIMIT_STATUS = 0x02
MTR_INTERLOCK_STATUS = 0x04
MTR_PRIREG_STATUS = 0x08
MTR_SYNC_STATUS = 0x09
MTR_PTP_REPEAT_NUM = 0x10
MTR_IP_REPEAT_NUM = 0x11

# Status : Interlock Status
# ------------------------- **
MTR_ILOCK_OFF = 0x00
MTR_ILOCK_ON = 0x01

# Counter Type
# ============ **
MTR_ENCODER = 0x00
MTR_COUNTER = 0x01
MTR_REMAINS = 0x02
MTR_DECLINO = 0x100
MTR_ABSOLUTE = 0x200
MTR_LATCH = 0x1000

# Start Repeat
# ============

# Start Repeat : Repat Move Mode
# ------------------------------ **
# MTR_PTP = 0x02
MTR_IP = 0x10
MTR_IP_SPEED = 0x100

# Sample Status
# ============= **
MTR_REPEAT = 0x1000
MTR_SAMPLE_FINISHED = 0x00
MTR_NOW_SAMPLING = 0x01
MTR_WAITING_BUSY = 0x02
MTR_FULL_BUFFER = 0x03
MTR_EMPTY_DATA = 0x04

# Revise Section
# ============== **
MTR_PULSE = 0x00
MTR_REVISE_MODE = 0x01
MTR_COUNTER_MODE = 0x02
MTR_REST_RT = 0x03
MTR_REST_FT = 0x04

# Revise : Revise Mose
# -------------------- **
MTR_BACK = 0x01
MTR_SLIP = 0x02

# ERC Config Section
# ================== **
MTR_AUTO = 0x00
# MTR_LOGIC = 0x01
MTR_WIDTH = 0x02
MTR_OFF_TIMER = 0x03
MTR_SIGNAL_ON = 0x04
MTR_SIGNAL_OFF = 0x05

# ERC Config : ERC Logic
# ---------------------- **
MTR_ACTIVE_LOW = 0x00
MTR_ACTIVE_HIGH = 0x01

# ERC Config : ERC Width
# ---------------------- **
MTR_12MICRO = 0x01
MTR_102MICRO = 0x02
MTR_409MICRO = 0x03
MTR_1600MICRO = 0x04
MTR_13M = 0x05
MTR_52M = 0x06
MTR_104M = 0x07
MTR_LEVEL = 0x08

# ERC Config : ERC Off Timer
# -------------------------- **
MTR_ZERO = 0x00
# MTR_12MICRO = 0x01
# MTR_1600MICRO = 0x04
# MTR_104M = 0x07

# MTNCOMP Structure
# ================= **

# MTNCOMP : Config
# ---------------- **
MTR_NO = 0x00
MTR_EQ = 0x01
MTR_EQ_UP = 0x02
MTR_EQ_DOWN = 0x03
MTR_LT = 0x04
MTR_GT = 0x05
MTR_SOFT_LIMIT = 0x06

# MTNCOMP : Motion
# ---------------- **
# MTR_NO = 0x00
MTR_STOP = 0x01
MTR_DEC = 0x02
MTR_CHG_REG = 0x03

# MTNCOMP : CntType
# ----------------- **
MTR_CMP_COUNTER = 0x00
MTR_CMP_ENCODER = 0x01
MTR_CMP_DECLINO = 0x02
MTR_CMP_SPEED = 0x05

# MTNMOTION struct
# ================ **

# MTNMOTION : AccMode
# ------------------- **
MTR_ACC_NORMAL = 0x00
MTR_ACC_SIN = 0x01
MTR_FH = 0x100

MTR_CW = 1
MTR_CCW = 1

# MTNLINE struct
# ============== **

# MTNLINE : Mode
# -------------- **
# MTR_LINE = 0x06
MTR_LINE_JOG = 0x16

# MTNLINE : AccMode
# ----------------- **
# MTR_ACC_NORMAL = 0x00
# MTR_ACC_SIN = 0x01
MTR_SP_COMPOSE = 0x1000

# MTNARC struct
# ============= **

# MTNARC : Mode
# ------------- **
MTR_ARC_CW = 0x00
MTR_ARC_CCW = 0x01
# MTR_SP_COMPOSE = 0x1000

# MTNSAMPEFREQ struct
# =================== **

# MTNSAMPEFREQ : Mode
# ------------------- **
# MTR_ENCODER = 0x00
# MTR_COUNTER = 0x01
# MTR_DECLINO = 0x100
MTR_BUSY_SAMP = 0x400
# MTR_REPEAT = 0x1000

# Command Buffer Section
# ====================== **
MTR_CMD_MOVE = 0x87
MTR_CMD_CLOCK = 0x85
MTR_CMD_LOW_SPEED = 0x81
MTR_CMD_SPEED = 0x82
MTR_CMD_ACC = 0x83
MTR_CMD_DEC = 0x84
MTR_CMD_ACC_SPEED = 0x89
MTR_CMD_DEC_SPEED = 0x8a
MTR_CMD_STEP = 0x80
MTR_CMD_CENTER = 0x88
MTR_CMD_START_MODE = 0x50

# Command Buffer : Mode
# --------------------- **
MTR_CMD_JOG_P = 0x00
MTR_CMD_JOG_M = 0x08
MTR_CMD_ORG_P = 0x10
MTR_CMD_ORG_M = 0x18
MTR_CMD_ORG_EXIT_P = 0x12
MTR_CMD_ORG_EXIT_M = 0x1a
MTR_CMD_ORG_SEARCH_P = 0x15
MTR_CMD_ORG_SEARCH_M = 0x1d
MTR_CMD_PTP = 0x41
MTR_CMD_ORG_ZERO = 0x44
MTR_CMD_SINGLE_STEP_P = 0x46
MTR_CMD_SINGLE_STEP_M = 0x4e
MTR_CMD_TIMER = 0x47
MTR_CMD_LINE = 0x61
MTR_CMD_ARC_CW = 0x64
MTR_CMD_ARC_CCW = 0x65
MTR_CMD_ACC_SIN = 0x400
MTR_CMD_FH_OFF = 0x4000000
MTR_CMD_SP_COMPOSE = 0x8000

# Command Buffer : Start Mode
# --------------------------- **
MTR_CMD_CONST = 0x51
MTR_CMD_ACC_DEC = 0x53
MTR_CMD_CONST_DEC = 0x52

# Start Command Buffer
# ==================== **
MTR_CMD_AUTO_START = 0x00
MTR_CMD_STEP_START = 0x01

# RETURN VALUE
# ============ **
MTR_ERROR_SUCCESS = 0
MTR_ERROR_NOT_DEVICE = 0xc0000001
MTR_ERROR_NOT_OPEN = 0xc0000002
MTR_ERROR_INVALID_DEVICE_NUMBER = 0xc0000003
MTR_ERROR_ALREADY_OPEN = 0xc0000004
MTR_ERROR_NOT_SUPPORTED = 0xc0000009
MTR_ERROR_NOW_MOVING = 0xc0001000
MTR_ERROR_NOW_STOPPED = 0xc0001001
MTR_ERROR_NOW_SAMPLING = 0xc0001002
MTR_ERROR_NOW_STOP_SAMPLING = 0xc0001003
MTR_ERROR_NOW_BUSY_CMD_BUFF = 0xc0001004
MTR_ERROR_NOW_STOP_CMD_BUFF = 0xc0001005
MTR_ERROR_EEPROM_BUSY = 0xc0001006
MTR_ERROR_WRITE_FAILED = 0xc0001010
MTR_ERROR_READ_FAILED = 0xc0001011
MTR_ERROR_INVALID_DEVICE = 0xc0001012
MTR_ERROR_INVALID_AXIS = 0xc0001013
MTR_ERROR_INVALID_SPEED = 0xc0001014
MTR_ERROR_INVALID_ACCDEC = 0xc0001015
MTR_ERROR_INVALID_PULSE = 0xc0001016
MTR_ERROR_INVALID_PARAMETER = 0xc0001017
MTR_ERROR_INVALID_INDEX = 0xc0001018
MTR_ERROR_REPEAT_LINE_ARC = 0xc0001019
MTR_ERROR_NOW_INTERLOCKED = 0xc0001020
MTR_ERROR_IMPOSSIBLE = 0xc0001021
MTR_ERROR_WRITE_FAILED_EEPROM = 0xc0001022
MTR_ERROR_READ_FAILED_EEPROM = 0xc0001023
MTR_ERROR_NOT_ALLOCATE_MEMORY = 0xc0001024
MTR_ERROR_NOW_WAIT_STA = 0xc0001025
MTR_ERROR_EMPTY_DATA = 0xc0001026
MTR_ERROR_FULL_PRIREG = 0xc0001030
MTR_ERROR_FAILED_CREATE_THREAD = 0xc0001031
MTN_ERROR_NOT_ALLOCATE_MEMORY = 0xc0001081


# =========
# Functions
# =========

SO_DIR = '/usr/lib'
SO_NAME = 'libgpg7400.so'
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
    
    # int MtnOpen( int, unsigned long);
    # ----------------------------------------------------------------------------------
    MtnOpen = lib.MtnOpen
    MtnOpen.restype = _uint
    MtnOpen.argtypes = (_int, _ulong)

    # int MtnClose( int );
    # --------------------
    MtnClose = lib.MtnClose
    MtnClose.restype = _uint 
    MtnClose.argtypes = (_int,)

    # int MtnReset( int, unsigned short, unsigned short );
    # ----------------------------------------------------
    MtnReset = lib.MtnReset
    MtnReset.restype = _uint 
    MtnReset.argtypes = (_int, _ushort, _ushort)

    # int MtnSetPulseOut( int, unsigned short, unsigned short, unsigned short );
    # --------------------------------------------------------------------------
    MtnSetPulseOut = lib.MtnSetPulseOut
    MtnSetPulseOut.restype = _uint 
    MtnSetPulseOut.argtypes = (_int, _ushort, _ushort, _ushort)

    # int MtnGetPulseOut( int, unsigned short, unsigned short, unsigned short* );
    # ---------------------------------------------------------------------------
    MtnGetPulseOut = lib.MtnGetPulseOut
    MtnGetPulseOut.restype = _uint 
    MtnGetPulseOut.argtypes = (_int, _ushort, _ushort, _ushort_p)

    # int MtnSetLimitConfig( int, unsigned short, unsigned short, unsigned short );
    # -----------------------------------------------------------------------------
    MtnSetLimitConfig = lib.MtnSetLimitConfig
    MtnSetLimitConfig.restype = _uint 
    MtnSetLimitConfig.argtypes = (_int, _ushort, _ushort, _ushort)

    # int MtnGetLimitConfig( int, unsigned short, unsigned short, unsigned short* );
    # ------------------------------------------------------------------------------
    MtnGetLimitConfig = lib.MtnGetLimitConfig
    MtnGetLimitConfig.restype = _uint 
    MtnGetLimitConfig.argtypes = (_int, _ushort, _ushort, _ushort_p)

    # int MtnSetCounterConfig( int, unsigned short, unsigned short, unsigned short );
    # -------------------------------------------------------------------------------
    MtnSetCounterConfig = lib.MtnSetCounterConfig
    MtnSetCounterConfig.restype = _uint 
    MtnSetCounterConfig.argtypes = (_int, _ushort, _ushort, _ushort)
    
    # int MtnGetCounterConfig( int, unsigned short, unsigned short, unsigned short* );
    # --------------------------------------------------------------------------------
    MtnGetCounterConfig = lib.MtnGetCounterConfig
    MtnGetCounterConfig.restype = _uint 
    MtnGetCounterConfig.argtypes = (_int, _ushort, _ushort, _ushort_p)

    # int MtnSetComparator( int, unsigned short, unsigned short, PMTNCOMP );
    # ----------------------------------------------------------------------
    MtnSetComparator = lib.MtnSetComparator
    MtnSetComparator.restype = _uint 
    MtnSetComparator.argtypes = (_int, _ushort, _ushort, _P(MTNCOMP))

    # int MtnGetComparator( int, unsigned short, unsigned short, PMTNCOMP );
    # ----------------------------------------------------------------------
    MtnGetComparator = lib.MtnGetComparator
    MtnGetComparator.restype = _uint
    MtnGetComparator.argtypes = (_int, _ushort, _ushort, _P(MTNCOMP))

    # int MtnSetSync( int, unsigned short, unsigned short, unsigned short* );
    # -----------------------------------------------------------------------
    MtnSetSync = lib.MtnSetSync
    MtnSetSync.restype = _uint 
    MtnSetSync.argtypes = (_int, _ushort, _ushort, _ushort_p)

    # int MtnGetSync( int, unsigned short, unsigned short, unsigned short* );
    # -----------------------------------------------------------------------
    MtnGetSync = lib.MtnGetSync
    MtnGetSync.restype = _uint 
    MtnGetSync.argtypes = (_int, _ushort, _ushort, _ushort_p)

    # int MtnSetRevise( int, unsigned short, unsigned short, unsigned long );
    # -----------------------------------------------------------------------
    MtnSetRevise = lib.MtnSetRevise
    MtnSetRevise.restype = _uint 
    MtnSetRevise.argtypes = (_int, _ushort, _ushort, _ulong)

    # int MtnGetRevise( int, unsigned short, unsigned short, unsigned long* );
    # ------------------------------------------------------------------------
    MtnGetRevise = lib.MtnGetRevise
    MtnGetRevise.restype = _uint 
    MtnGetRevise.argtypes = (_int, _ushort, _ushort, _ulong_p)

    # int MtnSetERCConfig( int, unsigned short, unsigned short, unsigned short );
    # ---------------------------------------------------------------------------
    MtnSetERCConfig = lib.MtnSetERCConfig
    MtnSetERCConfig.restype = _uint 
    MtnSetERCConfig.argtypes = (_int, _ushort, _ushort, _ushort)

    # int MtnGetERCConfig( int, unsigned short, unsigned short, unsigned short* );
    # ----------------------------------------------------------------------------
    MtnGetERCConfig = lib.MtnGetERCConfig
    MtnGetERCConfig.restype = _uint 
    MtnGetERCConfig.argtypes = (_int, _ushort, _ushort, _ushort_p)
    
    # --
    
    # int MtnSetMotion( int, unsigned short, unsigned long, PMTNMOTION );
    # -------------------------------------------------------------------
    MtnSetMotion = lib.MtnSetMotion
    MtnSetMotion.restype = _uint 
    MtnSetMotion.argtypes = (_int, _ushort, _ulong, _P(MTNMOTION))
    
    # int MtnSetMotionCp( int, unsigned short, unsigned long, PMTNMOTION );
    # ---------------------------------------------------------------------
    MtnSetMotionCp = lib.MtnSetMotionCp
    MtnSetMotionCp.restype = _uint 
    MtnSetMotionCp.argtypes = (_int, _ushort, _ulong, _P(MTNMOTION))
    
    # int MtnSetMotionLine( int, unsigned long, PMTNLINE );
    # -----------------------------------------------------
    MtnSetMotionLine = lib.MtnSetMotionLine
    MtnSetMotionLine.restype = _uint 
    MtnSetMotionLine.argtypes = (_int, _ulong, _P(MTNLINE))
    
    # int MtnSetSyncLine( int, long, PMTNLINE );
    # ------------------------------------------
    MtnSetSyncLine = lib.MtnSetSyncLine
    MtnSetSyncLine.restype = _uint 
    MtnSetSyncLine.argtypes = (_int, _long, _P(MTNLINE))
    
    # int MtnSetMotionArc( int, unsigned long, PMTNARC );
    # ---------------------------------------------------
    MtnSetMotionArc = lib.MtnSetMotionArc
    MtnSetMotionArc.restype = _uint 
    MtnSetMotionArc.argtypes = (_int, _ulong, _P(MTNARC))
    
    # --
    
    # int MtnGetMotion( int, unsigned short, unsigned long, PMTNMOTION );
    # -------------------------------------------------------------------
    MtnGetMotion = lib.MtnGetMotion
    MtnGetMotion.restype = _uint 
    MtnGetMotion.argtypes = (_int, _ushort, _ulong, _P(MTNMOTION))
    
    # int MtnGetMotionCp( int, unsigned short, unsigned long*, PMTNMOTION );
    # ----------------------------------------------------------------------
    MtnGetMotionCp = lib.MtnGetMotionCp
    MtnGetMotionCp.restype = _uint 
    MtnGetMotionCp.argtypes = (_int, _ushort, _ulong_p, _P(MTNMOTION))
    
    # int MtnGetMotionLine( int, unsigned long, PMTNLINE );
    # -----------------------------------------------------
    MtnGetMotionLine = lib.MtnGetMotionLine
    MtnGetMotionLine.restype = _uint 
    MtnGetMotionLine.argtypes = (_int, _ulong, _P(MTNLINE))
    
    # int MtnGetSyncLine( int, long*, PMTNLINE );
    # -------------------------------------------
    MtnGetSyncLine = lib.MtnGetSyncLine
    MtnGetSyncLine.restype = _uint 
    MtnGetSyncLine.argtypes = (_int, _long_p, _P(MTNLINE))
    
    # int MtnGetMotionArc( int, unsigned long, PMTNARC );
    # ---------------------------------------------------
    MtnGetMotionArc = lib.MtnGetMotionArc
    MtnGetMotionArc.restype = _uint 
    MtnGetMotionArc.argtypes = (_int, _ulong, _P(MTNARC))
    
    # --
    
    # int MtnStartMotion( int, unsigned short, unsigned short, unsigned short );
    # --------------------------------------------------------------------------
    MtnStartMotion = lib.MtnStartMotion
    MtnStartMotion.restype = _uint
    MtnStartMotion.argtypes = (_int, _ushort, _ushort, _ushort)
    
    # int MtnStartRepeat( int, unsigned short, unsigned short, unsigned short,
    #                     unsigned long, unsigned long );
    # ------------------------------------------------------------------------
    MtnStartRepeat = lib.MtnStartRepeat
    MtnStartRepeat.restype = _uint 
    MtnStartRepeat.argtypes = (_int, _ushort, _ushort, _ushort, _ulong, _ulong)
    
    # int MtnStopMotion( int, unsigned short, unsigned short );
    # ---------------------------------------------------------
    MtnStopMotion = lib.MtnStopMotion
    MtnStopMotion.restype = _uint 
    MtnStopMotion.argtypes = (_int, _ushort, _ushort)
    
    # int MtnRestart( int, unsigned short, unsigned short );
    # ------------------------------------------------------
    MtnRestart = lib.MtnRestart
    MtnRestart.restype = _uint 
    MtnRestart.argtypes = (_int, _ushort, _ushort)
    
    # int MtnOutputSync( int, unsigned short );
    # -----------------------------------------
    MtnOutputSync = lib.MtnOutputSync
    MtnOutputSync.restype = _uint 
    MtnOutputSync.argtypes = (_int, _ushort)
    
    # --
    
    # int MtnChangeSpeed( int, unsigned short, unsigned short, float* );
    # ------------------------------------------------------------------
    MtnChangeSpeed = lib.MtnChangeSpeed
    MtnChangeSpeed.restype = _uint 
    MtnChangeSpeed.argtypes = (_int, _ushort, _ushort, _float_p)
    
    # int MtnChangeStep( int, unsigned short, long* );
    # ------------------------------------------------
    MtnChangeStep = lib.MtnChangeStep
    MtnChangeStep.restype = _uint 
    MtnChangeStep.argtypes = (_int, _ushort, _long_p)
    
    # --
    
    # int MtnGetStatus( int, unsigned short, unsigned short, unsigned long* );
    # ------------------------------------------------------------------------
    MtnGetStatus = lib.MtnGetStatus
    MtnGetStatus.restype = _uint 
    MtnGetStatus.argtypes = (_int, _ushort, _ushort, _ulong_p)
    
    # int MtnGetEventFactor(int, unsigned short, PMTNEVENTTABLE);
    # -----------------------------------------------------------
    MtnGetEventFactor = lib.MtnGetEventFactor
    MtnGetEventFactor.restype = _uint
    MtnGetEventFactor.argtypes = (_int, _ushort, _P(MTNEVENTTABLE))
    
    # int MtnReadSpeed( int, unsigned short, float* );
    # ------------------------------------------------
    MtnReadSpeed = lib.MtnReadSpeed
    MtnReadSpeed.restype = _uint 
    MtnReadSpeed.argtypes = (_int, _ushort, _float_p)
    
    # int MtnReadCounter( int, unsigned short, unsigned short, long* );
    # -----------------------------------------------------------------
    MtnReadCounter = lib.MtnReadCounter
    MtnReadCounter.restype = _uint 
    MtnReadCounter.argtypes = (_int, _ushort, _ushort, _long_p)
    
    # int MtnWriteCounter( int, unsigned short, unsigned short, long* );
    # ------------------------------------------------------------------
    MtnWriteCounter = lib.MtnWriteCounter
    MtnWriteCounter.restype = _uint 
    MtnWriteCounter.argtypes = (_int, _ushort, _ushort, _long_p)
    
    # int MtnOutputDO( int, unsigned short );
    # ---------------------------------------
    MtnOutputDO = lib.MtnOutputDO
    MtnOutputDO.restype = _uint 
    MtnOutputDO.argtypes = (_int, _ushort)
    
    # int MtnInputDI( int, unsigned short* );
    # ---------------------------------------
    MtnInputDI = lib.MtnInputDI
    MtnInputDI.restype = _uint 
    MtnInputDI.argtypes = (_int, _ushort_p)
    
    # --
    
    # int MtnSetSampleCounter( int, PMTNSAMPLEREQ );
    # ----------------------------------------------
    MtnSetSampleCounter = lib.MtnSetSampleCounter
    MtnSetSampleCounter.restype = _uint 
    MtnSetSampleCounter.argtypes = (_int, _P(MTNSAMPLEREQ))
    
    # int MtnGetSampleCounter( int, PMTNSAMPLEREQ );
    # ----------------------------------------------
    MtnGetSampleCounter = lib.MtnGetSampleCounter
    MtnGetSampleCounter.restype = _uint 
    MtnGetSampleCounter.argtypes = (_int, _P(MTNSAMPLEREQ))
    
    # int MtnGetSampleStatus( int, unsigned short*, unsigned long* );
    # ---------------------------------------------------------------
    MtnGetSampleStatus = lib.MtnGetSampleStatus
    MtnGetSampleStatus.restype = _uint 
    MtnGetSampleStatus.argtypes = (_int, _ushort_p, _ulong_p)
    
    # int MtnStartSampleCounter( int );
    # ---------------------------------
    MtnStartSampleCounter = lib.MtnStartSampleCounter
    MtnStartSampleCounter.restype = _uint 
    MtnStartSampleCounter.argtypes = (_int,)
    
    # int MtnStopSampleCounter( int );
    # --------------------------------
    MtnStopSampleCounter = lib.MtnStopSampleCounter
    MtnStopSampleCounter.restype = _uint 
    MtnStopSampleCounter.argtypes = (_int,)
    
    # int MtnGetSampleData( int, unsigned long*, PMTNSAMPDATA);
    # ---------------------------------------------------------
    MtnGetSampleData = lib.MtnGetSampleData
    MtnGetSampleData.restype = _uint 
    MtnGetSampleData.argtypes = (_int, _ulong_p, _P(MTNSAMPDATA))
    
    # --
    
    # int MtnSetEvent( int, unsigned short, PMTNEVENTTABLE, PLPMTNCALLBACK,
    #                  unsigned long );
    # ---------------------------------------------------------------------
    MtnSetEvent = lib.MtnSetEvent
    MtnSetEvent.restype = _uint 
    MtnSetEvent.argtypes = (_int, _ushort, _P(MTNEVENTTABLE), PLPMTNCALLBACK, _ulong)

    # int MtnGetEvent( int, unsigned short, PMTNEVENTTABLE, PLPMTNCALLBACK,
    #                  unsigned long* );
    # ---------------------------------------------------------------------
    MtnGetEvent = lib.MtnGetEvent
    MtnGetEvent.restype = _uint 
    MtnGetEvent.argtypes = (_int, _ushort, _P(MTNEVENTTABLE), PLPMTNCALLBACK, _ulong_p)
    
    # --
    
    # int MtnSetCmdBufferData( int, unsigned long, unsigned short,
    #                          unsigned short, unsigned long );
    # ------------------------------------------------------------
    MtnSetCmdBufferData = lib.MtnSetCmdBufferData
    MtnSetCmdBufferData.restype = _uint 
    MtnSetCmdBufferData.argtypes = (_int, _ulong, _ushort, _ushort, _ulong)
    
    # int MtnGetCmdBufferData( int, unsigned long, unsigned short*, unsigned short* );
    # --------------------------------------------------------------------------------
    MtnGetCmdBufferData = lib.MtnGetCmdBufferData
    MtnGetCmdBufferData.restype = _uint 
    MtnGetCmdBufferData.argtypes = (_int, _ulong, _ushort_p, _ushort_p)
    
    # int MtnStartCmdBuffer( int, unsigned short, unsigned long, unsigned long );
    # ---------------------------------------------------------------------------
    MtnStartCmdBuffer = lib.MtnStartCmdBuffer
    MtnStartCmdBuffer.restype = _uint 
    MtnStartCmdBuffer.argtypes = (_int, _ushort, _ulong, _ulong)
    
    # int MtnStopCmdBuffer( int );
    # ----------------------------
    MtnStopCmdBuffer = lib.MtnStopCmdBuffer
    MtnStopCmdBuffer.restype = _uint 
    MtnStopCmdBuffer.argtypes = (_int,)



