
import os
import ctypes
import pyinterface

# ==========
# Structures
# ==========

# Structure of AD board specification 
# -----------------------------------
class ADBOARDSPEC(pyinterface.Structure):
    _fields_ = [('ulBoardType', ctypes.c_ulong),
                ('ulBoardID', ctypes.c_ulong),
                ('ulSamplingMode', ctypes.c_ulong),
                ('ulChCountS', ctypes.c_ulong),
                ('ulChCountD', ctypes.c_ulong),
                ('ulResolution', ctypes.c_ulong),
                ('ulRange', ctypes.c_ulong),
                ('ulIsolation', ctypes.c_ulong),
                ('ulDI', ctypes.c_ulong),
                ('ulDO', ctypes.c_ulong)]

# Structure of ch Sampling Configuration 
# --------------------------------------
class ADSMPLCHREQ(pyinterface.Structure):
    _fields_ = [('ulChNo', ctypes.c_ulong),
                ('ulRange', ctypes.c_ulong)]

# Structure of Sampling Configuration  
# -----------------------------------
class ADSMPLREQ(pyinterface.Structure):
    _fields_ = [('ulChCount', ctypes.c_ulong),
                ('SmplChReq', ADSMPLCHREQ * 256),
                ('ulSamplingMode', ctypes.c_ulong),
                ('ulSingleDiff', ctypes.c_ulong),
                ('ulSmplNum', ctypes.c_ulong),
                ('ulSmplEventNum', ctypes.c_ulong),
                ('fSmplFreq', ctypes.c_float),
                ('ulTrigPoint', ctypes.c_ulong),
                ('ulTrigMode', ctypes.c_ulong),
                ('lTrigDelay', ctypes.c_long),
                ('ulTrigCh', ctypes.c_ulong),
                ('fTriglevel1', ctypes.c_float),
                ('fTriglevel2', ctypes.c_float),
                ('ulEClkEdge', ctypes.c_ulong),
                ('ulATrgPulse', ctypes.c_ulong),
                ('ulTrigEdge', ctypes.c_ulong),
                ('ulTrigDI', ctypes.c_ulong),
                ('ulFastMode', ctypes.c_ulong)]

# Structure of AdDeviceFind Data 
# ------------------------------
class AD_FIND_DEV(pyinterface.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('rsw', ctypes.c_int),
                ('subsys', ctypes.c_int)]

# Structure of Analog Trigger Config in BusMaster 
# -----------------------------------------------
class ADTRIGCHREQ(pyinterface.Structure):
    _fields_ = [('ulChNo', ctypes.c_ulong),
                ('fTrigLevel', ctypes.c_float),
                ('fHysteresis', ctypes.c_float)]


# Structure of Sampling Configuration  in BusMaster 
# -------------------------------------------------
class ADBMSMPLREQ(pyinterface.Structure):
    _fields_ = [('ulChCount', ctypes.c_ulong),
                ('SmplChReq', ADSMPLCHREQ * 256),
                ('ulSingleDiff', ctypes.c_ulong),
                ('ulSmplNum', ctypes.c_ulong),
                ('ulSmplEventNum', ctypes.c_ulong),
                ('ulSmplRepeat', ctypes.c_ulong),
                ('ulBufferMode', ctypes.c_ulong),
                ('fSmplFreq', ctypes.c_float),
                ('fScanFreq', ctypes.c_float),
                ('ulStartMode', ctypes.c_ulong),
                ('ulStopMode', ctypes.c_ulong),
                ('ulPreTrigDelay', ctypes.c_ulong),
                ('ulPostTrigDelay', ctypes.c_ulong),
                ('TrigChReq', ADTRIGCHREQ * 2),
                ('ulATrgMode', ctypes.c_ulong),
                ('ulATrgPulse', ctypes.c_ulong),
                ('ulStartTrigEdge', ctypes.c_ulong),
                ('ulStopTrigEdge', ctypes.c_ulong),
                ('ulTrigDI', ctypes.c_ulong),
                ('ulEClkEdge', ctypes.c_ulong),
                ('ulFastMode', ctypes.c_ulong),
                ('ulStatusMode', ctypes.c_ulong),
                ('ulErrCtrl', ctypes.c_ulong)]

# Structure of Sampling Configuration  in Memory    
# ----------------------------------------------
class ADMEMSMPLREQ(pyinterface.Structure):
    _fields_ = [('ulChCount', ctypes.c_ulong),
                ('SmplChReq', ADSMPLCHREQ * 256),
                ('ulSingleDiff', ctypes.c_ulong),
                ('fSmplFreq', ctypes.c_float),
                ('ulStopMode', ctypes.c_ulong),
                ('ulPreTrigDelay', ctypes.c_ulong),
                ('ulPostTrigDelay', ctypes.c_ulong),
                ('TrigChReq', ADTRIGCHREQ * 2),
                ('ulATrgMode', ctypes.c_ulong),
                ('ulATrgPulse', ctypes.c_ulong),
                ('ulStopTrigEdge', ctypes.c_ulong),
                ('ulEClkEdge', ctypes.c_ulong),
                ('ulFastMode', ctypes.c_ulong),
                ('ulStatusMode', ctypes.c_ulong),
                ('ulErrCtrl', ctypes.c_ulong)]

# function pointer
# ----------------
LPADCALLBACK = ctypes.CFUNCTYPE(ctypes.c_int)
ADCONVPROC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.c_void_p);


# ==========
# Identifers
# ==========

# sampling mode constants
# -----------------------
FLAG_SYNC = 1
FLAG_ASYNC = 2
FLAG_TRIGGER = 4
FLAG_MASTER_MODE = 5
FLAG_SLAVE_MODE = 6

# file type constants
# -------------------
FLAG_BIN = 1
FLAG_CSV = 2

# data formate type constants
# ---------------------------
CONV_BIN = 1
CONV_PHYS = 2

# sampling status constants
# -------------------------
AD_STATUS_STOP_SAMPLING = 1
AD_STATUS_WAIT_TRIGGER = 2
AD_STATUS_NOW_SAMPLING = 3

# sampling event constants
# ------------------------
AD_EVENT_SMPLNUM = 1
AD_EVENT_STOP_TRIGGER = 2
AD_EVENT_STOP_FUNCTION = 3
AD_EVENT_STOP_TIMEOUT = 4
AD_EVENT_STOP_SAMPLING = 5
AD_EVENT_STOP_SCER = 6
AD_EVENT_STOP_ORER = 7
AD_EVENT_SCER = 8
AD_EVENT_ORER = 9
AD_EVENT_STOP_LV_1 = 10
AD_EVENT_STOP_LV_2 = 11
AD_EVENT_STOP_LV_3 = 12
AD_EVENT_STOP_LV_4 = 13
AD_EVENT_RANGE = 14
AD_EVENT_STOP_RANGE = 15
AD_EVENT_OVPM = 16
AD_EVENT_STOP_OVPM = 17

# sampling method constants
# -------------------------
AD_INPUT_SINGLE = 1
AD_INPUT_DIFF = 2
AD_INPUT_GND = 3
AD_INPUT_REFP5V = 4
AD_INPUT_REFM5V = 5
AD_INPUT_DACONV = 6
AD_INPUT_REFP3V = 7
AD_INPUT_REFM3V = 8
AD_INPUT_DAC1 = 9
AD_INPUT_DAC2 = 10
AD_INPUT_DAC3 = 11
AD_INPUT_DAC4 = 12
AD_INPUT_DAC5 = 13
AD_INPUT_DAC6 = 14

# volume adjust constans
# ----------------------
AD_ADJUST_BIOFFSET = 1
AD_ADJUST_UNIOFFSET = 2
AD_ADJUST_BIGAIN = 3
AD_ADJUST_UNIGAIN = 4

# voleme adjust constants
# -----------------------
AD_ADJUST_UP = 1
AD_ADJUST_DOWN = 2
AD_ADJUST_STORE = 3
AD_ADJUST_STANDBY = 4
AD_ADJUST_NOT_STORE = 5
AD_ADJUST_STORE_INITAREA = 6

AD_ADJUST_READ_FACTORY = 1
AD_ADJUST_READ_USER = 2

# data conversion constants
# -------------------------
AD_DATA_PHYSICAL = 1
AD_DATA_BIN8 = 2
AD_DATA_BIN12 = 3
AD_DATA_BIN16 = 4
AD_DATA_BIN24 = 5
AD_DATA_BIN10 = 6

# data conversion constants
# -------------------------
AD_CONV_SMOOTH = 1
AD_CONV_AVERAGE1 = 2
AD_CONV_AVERAGE2 = 3

# sampling formula constants
# --------------------------
AD_IO_SAMPLING = 1
AD_FIFO_SAMPLING = 2
AD_MEM_SAMPLING = 4
AD_BM_SAMPLING = 8

# trigger point constants
# -----------------------
AD_TRIG_START = 1
AD_TRIG_STOP = 2
AD_TRIG_START_STOP = 3

# trigger constants
# -----------------
AD_FREERUN = 1
AD_EXTTRG = 2
AD_EXTTRG_DI = 3
AD_LEVEL_P = 4
AD_LEVEL_M = 5
AD_LEVEL_D = 6
AD_INRANGE = 7
AD_OUTRANGE = 8
AD_ETERNITY = 9
AD_SMPLNUM = 10

AD_START_SIGTIMER = 11
AD_START_DA_START = 12
AD_START_DA_STOP = 13
AD_START_DA_IO = 14
AD_START_DA_SMPLNUM = 15
AD_STOP_SIGTIMER = 11
AD_STOP_DA_START = 12
AD_STOP_DA_STOP = 13
AD_STOP_DA_IO = 14
AD_STOP_DA_SMPLNUM = 15

AD_START_P1 = 0x00000010
AD_START_M1 = 0x00000020
AD_START_D1 = 0x00000040
AD_START_P2 = 0x00000080
AD_START_M2 = 0x00000100
AD_START_D2 = 0x00000200
AD_STOP_P1 = 0x00000400
AD_STOP_M1 = 0x00000800
AD_STOP_D1 = 0x00001000
AD_STOP_P2 = 0x00002000
AD_STOP_M2 = 0x00004000
AD_STOP_D2 = 0x00008000
AD_ANALOG_FILTER = 0x00010000
AD_START_CNT_EQ = 0x00020000
AD_STOP_CNT_EQ = 0x00040000
AD_START_DI_EQ = 0x00080000
AD_STOP_DI_EQ = 0x00100000
AD_STOP_SOFT = 0x00200000
AD_START_Z_CLR = 0x00400000
AD_STOP_Z_CLR = 0x00800000
AD_START_SYNC = 0x01000000
AD_STOP_SYNC = 0x02000000
AD_START_SYNC1 = 0x10000000
AD_START_SYNC2 = 0x20000000
AD_STOP_SYNC1 = 0x40000000
AD_STOP_SYNC2 = 0x80000000

# trigger edge constants
# ----------------------
AD_DOWN_EDGE = 1
AD_UP_EDGE = 2
AD_EXTRG_IN = 3
AD_EXCLK_IN = 4
AD_LOW_LEVEL = 5
AD_HIGH_LEVEL = 6

AD_EDGE_P1 = 0x0010
AD_EDGE_M1 = 0x0020
AD_EDGE_D1 = 0x0040
AD_EDGE_P2 = 0x0080
AD_EDGE_M2 = 0x0100
AD_EDGE_D2 = 0x0200
AD_DISABLE = 0x80000000

AD_TRIG_MODE = 2
AD_BUSY_MODE = 3
AD_POST_MODE = 4
AD_ENABLE = 5
AD_SMP1_MODE = 6
AD_SMP2_MODE = 7
AD_ATRIG_MODE = 8

# analog trigger edge constants
# -----------------------------
AD_LOW_PULSE = 1
AD_HIGH_PULSE = 2

# fast mode constants
# -------------------
AD_NORMAL_MODE = 1
AD_FAST_MODE = 2

# status
# ------
AD_NO_STATUS = 1
AD_ADD_STATUS = 2

# error of busmaster clock
# ------------------------
AD_STOP_SCER = 2
AD_STOP_ORER = 4

# write way of busmaster data
# ---------------------------
AD_APPEND = 1
AD_OVERWRITE = 2

# Degital Filter
# --------------
AD_DF_8 = 0
AD_DF_16 = 1
AD_DF_32 = 2
AD_DF_64 = 3
AD_DF_128 = 4
AD_DF_256 = 5

# sampling range constants
# ------------------------
AD_0_1V = 0x00000001
AD_0_2P5V = 0x00000002
AD_0_5V = 0x00000004
AD_0_10V = 0x00000008
AD_1_5V = 0x00000010
AD_0_2V = 0x00000020
AD_0_0P125V = 0x00000040
AD_0_1P25V = 0x00000080
AD_0_0P625V = 0x00000100
AD_0_0P156V = 0x00000200
AD_0_20mA = 0x00001000
AD_4_20mA = 0x00002000
AD_20mA = 0x00004000
AD_1V = 0x00010000
AD_2P5V = 0x00020000
AD_5V = 0x00040000
AD_10V = 0x00080000
AD_20V = 0x00100000
AD_50V = 0x00200000
AD_0P125V = 0x00400000
AD_1P25V = 0x00800000
AD_0P625V = 0x01000000
AD_0P156V = 0x02000000
AD_1P25V_AC = 0x04000000
AD_0P625V_AC = 0x08000000
AD_0P156V_AC = 0x10000000
AD_AC_COUPLING = 0x40000000
AD_GND = 0x80000000

# isolation constants
# -------------------
AD_ISOLATION = 1
AD_NOT_ISOLATION = 2

# sync sampling constants
# -----------------------
AD_MASTER_MODE = 1
AD_SLAVE_MODE = 2

# sync Number constants
# ---------------------
AD_SYNC_NUM_1 = 0x0100
AD_SYNC_NUM_2 = 0x0200
AD_SYNC_NUM_3 = 0x0400
AD_SYNC_NUM_4 = 0x0800
AD_SYNC_NUM_5 = 0x1000
AD_SYNC_NUM_6 = 0x2000
AD_SYNC_NUM_7 = 0x4000

# calibration
# -----------
AD_SELF_CALIBRATION = 1
AD_ZEROSCALE_CALIBRATION = 2
AD_FULLSCALE_CALIBRATION = 3

# over/under range status
# -----------------------
AD_STATUS_UNDER_RANGE = 1
AD_STATUS_OVER_RANGE = 2

# compare data status
# -------------------
AD_STATUS_UP_DATA = 1
AD_STATUS_DOWN_DATA = 2

# PCI-3525 CN3,4 function
# -----------------------
AD_CN_FREE = 0
AD_CN_EXTRG_IN = 1
AD_CN_EXTRG_OUT = 2
AD_CN_EXCLK_IN = 3
AD_CN_EXCLK_OUT = 4
AD_CN_EXINT_IN = 5
AD_CN_ATRG_OUT = 6
AD_CN_DI = 7
AD_CN_DO = 8
AD_CN_EXSMP1_OUT = 12
AD_CN_EXSMP2_OUT = 13
AD_CN_DIO = 1
AD_CN_CONTROL = 2
AD_CN_CNT = 3

# CPZ-360810 function
# -------------------
AD_EX_DIO1 = 1
AD_EX_DIO2 = 2
AD_EX_DIO3 = 3
AD_EX_DIO4 = 4
AD_EX_DIO5 = 5
AD_EX_DIO6 = 6
AD_EX_DIO7 = 7
AD_EX_DIO8 = 8

# temperture
# ----------
AD_GET_CURRENT_TEMPERATURE = 1
AD_LOAD_TEMPERATURE = 2
AD_LOAD_FACTORY_SETTING_TEMPERATURE = 3
AD_SAVE_TEMPERATURE_USER = 4

# error code
# ----------
AD_ERROR_SUCCESS = 0
AD_ERROR_NOT_DEVICE = 0xC0000001
AD_ERROR_NOT_OPEN = 0xC0000002
AD_ERROR_INVALID_HANDLE = 0xC0000003
AD_ERROR_INVALID_DEVICENO = 0xC0000003
AD_ERROR_ALREADY_OPEN = 0xC0000004
AD_ERROR_INVALID_DEVICE_NUMBER = 0xC0000005
AD_ERROR_NOT_SUPPORTED = 0xC0000009
AD_ERROR_NOW_SAMPLING = 0xC0001001
AD_ERROR_STOP_SAMPLING = 0xC0001002
AD_ERROR_START_SAMPLING = 0xC0001003
AD_ERROR_SAMPLING_TIMEOUT = 0xC0001004
AD_ERROR_INVALID_PARAMETER = 0xC0001021
AD_ERROR_NULL_POINTER = 0xC0001023
AD_ERROR_GET_DATA = 0xC0001024
AD_ERROR_USED_DA = 0xC0001025
AD_ERROR_FILE_OPEN = 0xC0001041
AD_ERROR_FILE_CLOSE = 0xC0001042
AD_ERROR_FILE_READ = 0xC0001043
AD_ERROR_FILE_WRITE = 0xC0001044
AD_ERROR_INVALID_DATA_FORMAT = 0xC0001061
AD_ERROR_INVALID_AVERAGE_OR_SMOOTHING = 0xC0001062
AD_ERROR_INVALID_SOURCE_DATA = 0xC0001063
AD_ERROR_NOT_ALLOCATE_MEMORY = 0xC0001081
AD_ERROR_CALIBRATION = 0xC0001084
AD_ERROR_NOT_THREAD = 0xC0001090
AD_ERROR_NOT_DEVICE_NODE = 0xC0001091

AD_ERROR_USBIO_FAILED = 0xC0001085
AD_ERROR_USBIO_TIMEOUT = 0xC0001086
AD_ERROR_USBLIB_LOAD_FAILED = 0xC0001087


# =========
# Functions
# =========

SO_DIR = '/usr/lib'
SO_NAME = 'libgpg3100.so'
SO_PATH = os.path.join(SO_DIR, SO_NAME)

try:
    lib = ctypes.cdll.LoadLibrary(SO_PATH)
except OSError:
    pass
else:
    pyinterface.so_available.append(SO_PATH)
    
    _char_p = ctypes.c_char_p
    _ubyte = ctypes.c_ubyte
    _ushort = ctypes.c_ushort
    _int = ctypes.c_int
    _uint = ctypes.c_uint
    _long = ctypes.c_long
    _ulong = ctypes.c_ulong
    _float = ctypes.c_float
    _void_p = ctypes.c_void_p
    _P = ctypes.POINTER
    
    # int AdOpen(int nDevice);
    # ------------------------
    AdOpen = lib.AdOpen
    AdOpen.restype = _uint
    AdOpen.argtypes = (_uint,)

    # int AdClose(int nDevice);
    # -------------------------
    AdClose = lib.AdClose
    AdClose.restype = _uint
    AdClose.argtypes = (_uint,)
    
    # int AdGetDeviceInfo(int nDevice, PADBOARDSPEC pBoardSpec);
    # ----------------------------------------------------------
    AdGetDeviceInfo = lib.AdGetDeviceInfo
    AdGetDeviceInfo.restype = _uint
    AdGetDeviceInfo.argtypes = (_uint, _P(ADBOARDSPEC))
    
    # int AdSetBoardConfig(int nDevice, int reserved, PLPADCALLBACK 
    #                      pEventProc, int uData);
    # -------------------------------------------------------------
    AdSetBoardConfig = lib.AdSetBoardConfig
    AdSetBoardConfig.restype = _uint
    AdSetBoardConfig.argtypes = (_uint, _uint, _P(LPADCALLBACK), _int)

    # int AdGetBoardConfig(int nDevice, unsigned long *ulAdSmplEventFactor);
    # ----------------------------------------------------------------------
    AdGetBoardConfig = lib.AdGetBoardConfig
    AdGetBoardConfig.restype = _uint
    AdGetBoardConfig.argtypes = (_uint, _P(_ulong))
    
    # int AdSetSamplingConfig(int nDevice, PADSMPLREQ pSmplConfig);
    # -------------------------------------------------------------
    AdSetSamplingConfig = lib.AdSetSamplingConfig
    AdSetSamplingConfig.restype = _uint
    AdSetSamplingConfig.argtypes = (_uint, _P(ADSMPLREQ))

    # int AdGetSamplingConfig(int nDevice, PADSMPLREQ pSmplConfig);
    # -------------------------------------------------------------
    AdGetSamplingConfig = lib.AdGetSamplingConfig
    AdGetSamplingConfig.restype = _uint
    AdGetSamplingConfig.argtypes = (_uint, _P(ADSMPLREQ))
    
    # int AdGetSamplingData(int nDevice, void *pSmplData, unsigned long *ulSmplNum);
    # ------------------------------------------------------------------------------
    AdGetSamplingData = lib.AdGetSamplingData
    AdGetSamplingData.restype = _uint
    AdGetSamplingData.argtypes = (_uint, _void_p, _P(_ulong))

    # int AdFifoGetSamplingData(int nDevice, void *pSmplData, void *pDiData,
    #                           unsigned long *ulSmplNum);
    # ----------------------------------------------------------------------
    AdFifoGetSamplingData = lib.AdFifoGetSamplingData
    AdFifoGetSamplingData.restype = _uint
    AdFifoGetSamplingData.argtypes = (_uint, _void_p, _void_p, _P(_ulong))

    # int AdReadSamplingBuffer(int nDevice, long lOffset, unsigned long *ulSmplNum,
    #                          void *pSmplData);
    # -----------------------------------------------------------------------------
    AdReadSamplingBuffer = lib.AdReadSamplingBuffer
    AdReadSamplingBuffer.restype = _uint
    AdReadSamplingBuffer.argtypes = (_uint, _long, _P(_ulong), _void_p)

    # int AdClearSamplingData(int nDevice);
    # -------------------------------------
    AdClearSamplingData = lib.AdClearSamplingData
    AdClearSamplingData.restype = _uint
    AdClearSamplingData.argtypes = (_uint,)
    
    # int AdStartSampling(int nDevice, int uSyncFlag);
    # ------------------------------------------------
    AdStartSampling = lib.AdStartSampling
    AdStartSampling.restype = _uint
    AdStartSampling.argtypes = (_uint, _int)

    # int AdTriggerSampling(int nDevice, unsigned long ulChNo, unsigned long ulRange,
    #                       unsigned long ulSingleDiff, unsigned long ulTriggerMode,
    #                       unsigned long ulTrigEdge, unsigned long ulSmplNum);
    # -------------------------------------------------------------------------------
    AdTriggerSampling = lib.AdTriggerSampling
    AdTriggerSampling.restype = _uint
    AdTriggerSampling.argtypes = (_uint, _ulong, _ulong, _ulong, _ulong, _ulong, _ulong)

    # int AdMemTriggerSampling(int nDevice, unsigned long ulChCount, PADSMPLCHREQ SmplChReq,
    #                          unsigned long ulSmplNum, unsigned long ulRepeatCount,
    #                          unsigned long ulTrigEdge, float fSmplFreq,
    #                          unsigned long ulEClkEdge, unsigned long ulFastMode);
    # --------------------------------------------------------------------------------------
    AdMemTriggerSampling = lib.AdMemTriggerSampling
    AdMemTriggerSampling.restype = _uint
    AdMemTriggerSampling.argtypes = (_uint, _ulong, _P(ADSMPLCHREQ), _ulong, _ulong, 
                                     _ulong, _float, _ulong, _ulong)

    # int AdSyncSampling(int nDevice, unsigned long ulMode);
    # ------------------------------------------------------
    AdSyncSampling = lib.AdSyncSampling
    AdSyncSampling.restype = _uint
    AdSyncSampling.argtypes = (_uint, _ulong)
    
    # int AdStopSampling(int nDevice);
    # --------------------------------
    AdStopSampling = lib.AdStopSampling
    AdStopSampling.restype = _uint
    AdStopSampling.argtypes = (_uint,)

    # int AdGetStatus(int uDevice, unsigned long *ulAdSmplStatus,
    #                 unsigned long *ulAdSMplCount, unsigned long *ulAdAvailCount);
    # -----------------------------------------------------------------------------
    AdGetStatus = lib.AdGetStatus
    AdGetStatus.restype = _uint
    AdGetStatus.argtypes = (_uint, _P(_ulong), _P(_ulong), _P(_ulong))

    # int AdInputAD(int nDevice, unsigned long uCh, unsigned long ulSingleDiff,
    #               PADSMPLCHREQ pSmplChReq, void *pData);
    # -------------------------------------------------------------------------
    AdInputAD = lib.AdInputAD
    AdInputAD.restype = _uint
    AdInputAD.argtypes = (_uint, _ulong, _ulong, _P(ADSMPLCHREQ), _void_p)
    
    # int AdInputDI(int nDevice, unsigned long *uData);
    # -------------------------------------------------
    AdInputDI = lib.AdInputDI
    AdInputDI.restype = _uint
    AdInputDI.argtypes = (_uint, _P(_ulong))

    # int AdOutputDO(int nDevice, unsigned long uData);
    # -------------------------------------------------
    AdOutputDO = lib.AdOutputDO
    AdOutputDO.restype = _uint
    AdOutputDO.argtypes = (_uint, _ulong)
    
    # int AdDataConv(int nSrcFormCode, void *pSrcData, int nSrcSmplDataNum,
    #                PADSMPLREQ pSrcSmplReq, int nDestFormCode, void *pDestData,
    #                int *pnDestSmplDataNum, PADSMPLREQ pDestSmplReq, int nEffect,
    #                int nCount, PADCONVPROC lpfnConv);
    # ----------------------------------------------------------------------------
    AdDataConv = lib.AdDataConv
    AdDataConv.restype = _uint
    AdDataConv.argtypes = (_int, _void_p, _int, _P(ADSMPLREQ), _int, _void_p, 
                           _P(_int), _P(ADSMPLREQ), _int, _int, _P(ADCONVPROC))
    
    # int AdDeviceFind(PAD_FIND_DEV pDevTbl);
    # ---------------------------------------
    AdDeviceFind = lib.AdDeviceFind
    AdDeviceFind.restype = _uint
    AdDeviceFind.argtypes = (_P(AD_FIND_DEV),)
    
    # int AdSetRangeEvent(int nDevice, unsigned long ulEventMask,
    #                     unsigned long ulStopMode);
    # -----------------------------------------------------------
    AdSetRangeEvent = lib.AdSetRangeEvent
    AdSetRangeEvent.restype = _uint
    AdSetRangeEvent.argtypes = (_uint, _ulong, _ulong)

    # int AdResetRangeEvent(int nDevice);
    # -----------------------------------
    AdResetRangeEvent = lib.AdResetRangeEvent
    AdResetRangeEvent.restype = _uint
    AdResetRangeEvent.argtypes = (_uint,)

    # int AdGetRangeEventStatus(int nDevice, unsigned long *ulEventChNo,
    #                           unsigned long *ulEventStatus);
    # ------------------------------------------------------------------
    AdGetRangeEventStatus = lib.AdGetRangeEventStatus
    AdGetRangeEventStatus.restype = _uint
    AdGetRangeEventStatus.argtypes = (_uint, _P(_ulong), _P(_ulong))
    
    # int AdLvSetSamplingConfig(int nDevice, unsigned long ulChNo, unsigned long ulSmplNum,
    #                           float fSmplFreq, unsigned long ulRange, int reserved1, 
    #                           PLPADCALLBACK pEventProc, int reserved2);
    # -------------------------------------------------------------------------------------
    AdLvSetSamplingConfig = lib.AdLvSetSamplingConfig
    AdLvSetSamplingConfig.restype = _uint
    AdLvSetSamplingConfig.argtypes = (_uint, _ulong, _ulong, _float, _ulong, _int,
                                      _P(LPADCALLBACK), _int)

    # int AdLvGetSamplingConfig(int nDevice, unsigned long ulChNo, unsigned long *ulSmplNum,
    #                           float *fSmplFreq, unsigned long *ulRange);
    # --------------------------------------------------------------------------------------
    AdLvGetSamplingConfig = lib.AdLvGetSamplingConfig
    AdLvGetSamplingConfig.restype = _uint
    AdLvGetSamplingConfig.argtypes = (_uint, _ulong, _P(_ulong), _P(_float), _P(_ulong))

    # int AdLvCalibration(int nDevice, unsigned long ulChNo, unsigned long ulCalibration);
    # ------------------------------------------------------------------------------------
    AdLvCalibration = lib.AdLvCalibration
    AdLvCalibration.restype = _uint
    AdLvCalibration.argtypes = (_uint, _ulong, _ulong)

    # int AdLvGetSamplingData(int nDevice, unsigned long ulChNo, void *pSmplData,
    #                         unsigned long *ulSmplDataNum);
    # ---------------------------------------------------------------------------
    AdLvGetSamplingData = lib.AdLvGetSamplingData
    AdLvGetSamplingData.restype = _uint
    AdLvGetSamplingData.argtypes = (_uint, _ulong, _void_p, _P(_ulong))

    # int AdLvStartSampling(int nDevice, unsigned long ulCnNo);
    # ---------------------------------------------------------
    AdLvStartSampling = lib.AdLvStartSampling
    AdLvStartSampling.restype = _uint
    AdLvStartSampling.argtypes = (_uint, _ulong)

    # int AdLvStopSampling(int nDevice, unsigned long ulCnNo);
    # ---------------------------------------------
    AdLvStopSampling = lib.AdLvStopSampling
    AdLvStopSampling.restype = _uint
    AdLvStopSampling.argtypes = (_uint, _ulong)

    # int AdLvGetStatus(int nDevice, unsigned long ulChNo, unsigned long *ulAdSmplStatus,
    #                   unsigned long *ulAdSmplCount, unsigned long *ulAdAvailCount);
    # -----------------------------------------------------------------------------------
    AdLvGetStatus = lib.AdLvGetStatus
    AdLvGetStatus.restype = _uint
    AdLvGetStatus.argtypes = (_uint, _ulong, _P(_ulong), _P(_ulong), _P(_ulong))

    # int AdMeasureTemperature(int nDevice, float *fTemperature);
    # -----------------------------------------------------------
    AdMeasureTemperature = lib.AdMeasureTemperature
    AdMeasureTemperature.restype = _uint
    AdMeasureTemperature.argtypes = (_uint, _P(_float))
    
    # int AdBmSetSamplingConfig(int, PADBMSMPLREQ);
    # ---------------------------------------------
    AdBmSetSamplingConfig = lib.AdBmSetSamplingConfig
    AdBmSetSamplingConfig.restype = _uint
    AdBmSetSamplingConfig.argtypes = (_uint, _P(ADBMSMPLREQ))

    # int AdBmGetSamplingConfig(int, PADBMSMPLREQ);
    # ---------------------------------------------
    AdBmGetSamplingConfig = lib.AdBmGetSamplingConfig
    AdBmGetSamplingConfig.restype = _uint
    AdBmGetSamplingConfig.argtypes = (_uint, _P(ADBMSMPLREQ))

    # int AdBmGetSamplingData(int, void*, unsigned long*);
    # ----------------------------------------------------
    AdBmGetSamplingData = lib.AdBmGetSamplingData
    AdBmGetSamplingData.restype = _uint
    AdBmGetSamplingData.argtypes = (_uint, _void_p, _P(_ulong))
    
    # int AdGetOverRangeChStatus(int, unsigned long*);
    # ------------------------------------------------
    AdGetOverRangeChStatus = lib.AdGetOverRangeChStatus
    AdGetOverRangeChStatus.restype = _uint
    AdGetOverRangeChStatus.argtypes = (_uint, _P(_ulong))

    # int AdResetOverRangeCh(int);
    # ----------------------------
    AdResetOverRangeCh = lib.AdResetOverRangeCh
    AdResetOverRangeCh.restype = _uint
    AdResetOverRangeCh.argtypes = (_uint,)

    # int AdSetInterval(int, unsigned long);
    # --------------------------------------
    AdSetInterval = lib.AdSetInterval
    AdSetInterval.restype = _uint
    AdSetInterval.argtypes = (_uint, _ulong)

    # int AdGetInterval(int, unsigned long*);
    # ---------------------------------------
    AdGetInterval = lib.AdGetInterval
    AdGetInterval.restype = _uint
    AdGetInterval.argtypes = (_uint, _P(_ulong))

    # int AdSetFunction(int, unsigned int, unsigned long);
    # ----------------------------------------------------
    AdSetFunction = lib.AdSetFunction
    AdSetFunction.restype = _uint
    AdSetFunction.argtypes = (_uint, _uint, _ulong)

    # int AdGetFunction(int, unsigned int, unsigned long*);
    # -----------------------------------------------------
    AdGetFunction = lib.AdGetFunction
    AdGetFunction.restype = _uint
    AdGetFunction.argtypes = (_uint, _uint, _P(_ulong))
    
    # int AdSetFilter(int, unsigned long);
    # ------------------------------------
    AdSetFilter = lib.AdSetFilter
    AdSetFilter.restype = _uint
    AdSetFilter.argtypes = (_uint, _ulong)

    # int AdGetFilter(int, unsigned long*);
    # -------------------------------------
    AdGetFilter = lib.AdGetFilter
    AdGetFilter.restype = _uint
    AdGetFilter.argtypes = (_uint, _P(_ulong))

    # int AdCommonGetPciDeviceInfo(int, unsigned long*, unsigned long*, unsigned long*,
    #                              unsigned long*, unsigned long*, unsigned long*, 
    #                              unsigned long*, unsigned long*, unsigned long*,
    #                              unsigned long*, unsigned long*, unsigned long*,
    #                              unsigned long*, unsigned long*);
    # ---------------------------------------------------------------------------------
    AdCommonGetPciDeviceInfo = lib.AdCommonGetPciDeviceInfo
    AdCommonGetPciDeviceInfo.restype = _uint
    AdCommonGetPciDeviceInfo.argtypes = (_uint, _P(_ulong), _P(_ulong), _P(_ulong),
                                         _P(_ulong), _P(_ulong), _P(_ulong), _P(_ulong),
                                         _P(_ulong), _P(_ulong), _P(_ulong), _P(_ulong),
                                         _P(_ulong), _P(_ulong), _P(_ulong))
    
    # int AdMemSetSamplingConfig(int, PADMEMSMPLREQ);
    # -----------------------------------------------
    AdMemSetSamplingConfig = lib.AdMemSetSamplingConfig
    AdMemSetSamplingConfig.restype = _uint
    AdMemSetSamplingConfig.argtypes = (_uint, _P(ADMEMSMPLREQ))

    # int AdMemGetSamplingConfig(int, PADMEMSMPLREQ);
    # -----------------------------------------------
    AdMemGetSamplingConfig = lib.AdMemGetSamplingConfig
    AdMemGetSamplingConfig.restype = _uint
    AdMemGetSamplingConfig.argtypes = (_uint, _P(ADMEMSMPLREQ))

    # int AdSetOutMode(int, unsigned long, unsigned long);
    # ----------------------------------------------------
    AdSetOutMode = lib.AdSetOutMode
    AdSetOutMode.restype = _uint
    AdSetOutMode.argtypes = (_uint, _ulong, _ulong)

    # int AdGetOutMode(int, unsigned long*, unsigned long*);
    # ------------------------------------------------------
    AdGetOutMode = lib.AdGetOutMode
    AdGetOutMode.restype = _uint
    AdGetOutMode.argtypes = (_uint, _P(_ulong), _P(_ulong))

    # int AdMemSetDiPattern(int, unsigned long, unsigned long*);
    # ----------------------------------------------------------
    AdMemSetDiPattern = lib.AdMemSetDiPattern
    AdMemSetDiPattern.restype = _uint
    AdMemSetDiPattern.argtypes = (_uint, _ulong, _P(_ulong))

    # int AdMemGetDiPattern(int, unsigned long*);
    # -------------------------------------------
    AdMemGetDiPattern = lib.AdMemGetDiPattern
    AdMemGetDiPattern.restype = _uint
    AdMemGetDiPattern.argtypes = (_uint, _P(_ulong))
    
    # int AdOpenEx(unsigned short wType, unsigned short wSubSystemID,
    #              unsigned char bRSW1, int *pnDevice);
    # ---------------------------------------------------------------
    AdOpenEx = lib.AdOpenEx
    AdOpenEx.restype = _uint
    AdOpenEx.argtypes = (_ushort, _ushort, _ubyte, _P(_uint));

    # int AdSetInputADEx(int nDevice, unsigned long uCh,
    #                    unsigned long ulSingleDiff, PADSMPLCHREQ pSmplChReq);
    # ------------------------------------------------------------------------
    AdSetInputADEx = lib.AdSetInputADEx
    AdSetInputADEx.restype = _uint
    AdSetInputADEx.argtypes = (_uint, _ulong, _ulong, _P(ADSMPLCHREQ))

    # int AdInputADEx(int nDevice, void *pData);
    # ------------------------------------------
    AdInputADEx = lib.AdInputADEx
    AdInputADEx.restype = _uint
    AdInputADEx.argtypes = (_uint, _void_p)

    # int AdStartFileSampling(int nDevice, char *szPathName,
    #                         unsigned long ulFileFlag);
    # ------------------------------------------------------
    AdStartFileSampling = lib.AdStartFileSampling
    AdStartFileSampling.restype = _uint
    AdStartFileSampling.argtypes = (_uint, _char_p, _ulong)

    # int AdReadFile(char *PathName, void *pSmplData, unsigned long uFormCode);
    # -------------------------------------------------------------------------
    AdReadFile = lib.AdReadFile
    AdReadFile.restype = _uint
    AdReadFile.argtypes = (_char_p, _void_p, _ulong)

    # int AdBmStartFileSampling(int nDevice, char *szPathName, 
    #                           unsigned long uFileFlag);
    # --------------------------------------------------------
    AdBmStartFileSampling = lib.AdBmStartFileSampling
    AdBmStartFileSampling.restype = _uint
    AdBmStartFileSampling.argtypes = (_uint, _char_p, _ulong)

    # int AdStartSamplingEx(int nDevice, void *pBuffer, unsigned long BufferSize);
    # ----------------------------------------------------------------------------
    AdStartSamplingEx = lib.AdStartSamplingEx
    AdStartSamplingEx.restype = _uint
    AdStartSamplingEx.argtypes = (_uint, _void_p, _ulong)

    # int AdOutputSync(int uDevice, unsigned long Line, unsigned long TrgMode);
    # -------------------------------------------------------------------------
    AdOutputSync = lib.AdOutputSync
    AdOutputSync.restype = _uint
    AdOutputSync.argtypes = (_uint, _ulong, _ulong)

    # int AdCalibration(int uDevice, unsigned long ulChannel, unsigned long ulRange,
    #                   unsigned long ulSingleDiff);
    # ------------------------------------------------------------------------------
    AdCalibration = lib.AdCalibration
    AdCalibration.restype = _uint
    AdCalibration.argtypes = (_uint, _ulong, _ulong, _ulong)
