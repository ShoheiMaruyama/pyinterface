
import os
import ctypes

import pyinterface



# ===
# 
# ===

LPDACALLBACK = ctypes.CFUNCTYPE(ctypes.c_int)
DACONVPROC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.c_void_p)


# ==========
# Structures
# ==========

# Structure of Output Channel Config
# ----------------------------------
class DASMPLCHREQ(pyinterface.Structure):
    _fields_ = [('ulChNo', ctypes.c_ulong),
                ('ulRange', ctypes.c_ulong)]

# Structure of Sampling Config
# ----------------------------
class DASMPLREQ(pyinterface.Structure):
    _fields_ = [('ulChCount', ctypes.c_ulong),
                ('SmplChReq', DASMPLCHREQ * 256),
                ('ulSamplingMode', ctypes.c_ulong),
                ('fSmplFreq', ctypes.c_float),
                ('ulSmplRepeat', ctypes.c_ulong),
                ('ulTrigMode', ctypes.c_ulong),
                ('ulTrigPoint', ctypes.c_ulong),
                ('ulTrigDelay', ctypes.c_ulong),
                ('ulEClkEdge', ctypes.c_ulong),
                ('ulTrigEdge', ctypes.c_ulong),
                ('ulTrigDI', ctypes.c_ulong)]

# Structure of Sampling Config (FIFO TYPE)
# ----------------------------------------
class DAFIFOREQ(pyinterface.Structure):
    _fields_ = [('ulChCount', ctypes.c_ulong),
                ('SmplChReq', DASMPLCHREQ * 256),
                ('fSmplFreq', ctypes.c_float),
                ('ulSmplRepeat', ctypes.c_ulong),
                ('ulSmplNum', ctypes.c_ulong),
                ('ulStartTrigCondition', ctypes.c_ulong),
                ('ulStopTrigCondition', ctypes.c_ulong),
                ('ulEClkEdge', ctypes.c_ulong),
                ('ulTrigEdge', ctypes.c_ulong)]

# Structure of Port Information
# -----------------------------
class DABOARDSPEC(pyinterface.Structure):
    _fields_ = [('ulBoardType', ctypes.c_ulong),
                ('ulBoardID', ctypes.c_ulong),
                ('ulSamplingMode', ctypes.c_ulong),
                ('ulChCount', ctypes.c_ulong),
                ('ulResolution', ctypes.c_ulong),
                ('ulRange', ctypes.c_ulong),
                ('ulIsolation', ctypes.c_ulong),
                ('ulDi', ctypes.c_ulong),
                ('ulDo', ctypes.c_ulong)]

# 
# ----
class DAMODECHREQ(pyinterface.Structure):
    _fields_ = [('ulRange', ctypes.c_ulong),
                ('fVolt', ctypes.c_float),
                ('ulFilter', ctypes.c_ulong)]

# 
# ----
class DAMODEREQ(pyinterface.Structure):
    _fields_ = [('ModeChReq', DAMODECHREQ * 2),
                ('ulPulseMode', ctypes.c_ulong),
                ('ulSyntheOut', ctypes.c_ulong),
                ('ulInterval', ctypes.c_ulong),
                ('fIntervalCycle', ctypes.c_float),
                ('ulCounterClear', ctypes.c_ulong),
                ('ulDaLatch', ctypes.c_ulong),
                ('ulSamplingClock', ctypes.c_ulong),
                ('ulExControl', ctypes.c_ulong),
                ('ulExClock', ctypes.c_ulong)]

#
# ----
class DA_BOARD_SPEC(pyinterface.Structure):
    _fields_ = [('ulBoardType', ctypes.c_ulong),
                ('ulBoardID', ctypes.c_ulong),
                ('ulSamplingMode', ctypes.c_ulong),
                ('ulChCount', ctypes.c_ulong),
                ('ulResolution', ctypes.c_ulong),
                ('ulRange', ctypes.c_ulong),
                ('ulIsolation', ctypes.c_ulong),
                ('ulDi', ctypes.c_ulong),
                ('ulDo', ctypes.c_ulong),
                ('ulOutsideControl', ctypes.c_ulong),
                ('ulInterrupt', ctypes.c_ulong),
                ('ulRefOut', ctypes.c_ulong),
                ('ulRangeSet', ctypes.c_ulong),
                ('ulAdjustment', ctypes.c_ulong),
                ('ulSettlingTime', ctypes.c_ulong),
                ('ulDefRng', ctypes.c_ulong),
                ('ulOffsetMin', ctypes.c_ulong),
                ('ulOffsetMax', ctypes.c_ulong),
                ('ulMiddleMin', ctypes.c_ulong),
                ('ulMiddleMax', ctypes.c_ulong),
                ('ulGainMin', ctypes.c_ulong),
                ('ulGainMax', ctypes.c_ulong),
                ('precesion_0', ctypes.c_ubyte),
                ('precesion_1', ctypes.c_ubyte),
                ('precesion_2', ctypes.c_ubyte),
                ('precesion_3', ctypes.c_ubyte),
                ('precesion_4', ctypes.c_ubyte),
                ('precesion_5', ctypes.c_ubyte),
                ('precesion_6', ctypes.c_ubyte),
                ('precesion_7', ctypes.c_ubyte),
                ('precesion_8', ctypes.c_ubyte),
                ('precesion_9', ctypes.c_ubyte),
                ('precesion_10', ctypes.c_ubyte),
                ('precesion_11', ctypes.c_ubyte),
                ('precesion_12', ctypes.c_ubyte),
                ('precesion_13', ctypes.c_ubyte),
                ('precesion_14', ctypes.c_ubyte),
                ('precesion_15', ctypes.c_ubyte),
                ('precesion_16', ctypes.c_ubyte),
                ('precesion_17', ctypes.c_ubyte),
                ('precesion_18', ctypes.c_ubyte),
                ('precesion_19', ctypes.c_ubyte),
                ('precesion_20', ctypes.c_ubyte),
                ('precesion_21', ctypes.c_ubyte),
                ('precesion_22', ctypes.c_ubyte),
                ('precesion_23', ctypes.c_ubyte),
                ('precesion_24', ctypes.c_ubyte),
                ('precesion_25', ctypes.c_ubyte),
                ('precesion_26', ctypes.c_ubyte),
                ('precesion_27', ctypes.c_ubyte),
                ('precesion_28', ctypes.c_ubyte),
                ('precesion_29', ctypes.c_ubyte),
                ('precesion_30', ctypes.c_ubyte),
                ('precesion_31', ctypes.c_ubyte)]

# Structure of DaDeviceFind Data
# ------------------------------
class DA_FIND_DEV(pyinterface.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('rsw', ctypes.c_int),
                ('subsys', ctypes.c_int)]


# ==========
# Identifers
# ==========

# Overlapped Process Identifier
# -----------------------------
FLAG_SYNC = 1
FLAG_ASYNC = 2

# File Format Identifier
# ----------------------
FLAG_BIN = 1
FLAG_CSV = 2

# Data Format Identifier
# ----------------------
CONV_BIN = 1
CONV_PHYS = 2

# Analog Output Status Identifier
# -------------------------------
DA_STATUS_STOP_SAMPLING = 1
DA_STATUS_WAIT_TRIGGER = 2
DA_STATUS_NOW_SAMPLING = 3

# Event Factor Identifier
# -----------------------
DA_EVENT_STOP_TRIGGER = 1
DA_EVENT_STOP_FUNCTION = 2
DA_EVENT_STOP_SAMPLING = 3
DA_EVENT_RESET_IN = 4
DA_EVENT_CURRENT_OFF = 5
DA_EVENT_FIFO_EMPTY = 7
DA_EVENT_EX_INT = 8
DA_EVENT_EXOV_OFF = 9
DA_EVENT_OV_OFF = 10

# Range Identifier
# ----------------
DA_0_1V    = 0x00000001
DA_0_2P5V  = 0x00000002
DA_0_5V    = 0x00000004
DA_0_10V   = 0x00000008
DA_1_5V    = 0x00000010
DA_0_20mA  = 0x00001000
DA_4_20mA  = 0x00002000
DA_0_1mA   = 0x00004000
DA_0_100mA = 0x00008000
DA_1V      = 0x00010000
DA_2P5V    = 0x00020000
DA_5V      = 0x00040000
DA_10V     = 0x00080000
DA_20mA    = 0x01000000

# Data Transfer Architecture Identifier
# -------------------------------------
DA_IO_SAMPLING = 1
DA_FIFO_SAMPLING = 2
DA_MEM_SAMPLING = 4

# Trigger Point Identifier
# ------------------------
DA_TRIG_START = 1
DA_TRIG_STOP = 2
DA_TRIG_START_STOP = 3

# Trigger Level Identifier
# ------------------------
DA_FREERUN = 1
DA_EXTTRG = 2
DA_EXTTRG_DI = 3

# Polarity Identifier
# -------------------
DA_DOWN_EDGE = 1
DA_UP_EDGE = 2

# Pulse Polarity Identifier
# -------------------------
DA_LOW_PULSE = 1
DA_HIGH_PULSE = 2

# Simultaneous Output Set Identifier
# ----------------------------------
DA_NORMAL_MODE = 1
DA_FAST_MODE = 2

# Isolation Identifier
# --------------------
DA_ISOLATION = 1
DA_NOT_ISOLATION = 2

# Range Identifier
# ----------------
DA_RANGE_UNIPOLAR = 1
DA_RANGE_BIPOLAR = 2

# Filter Identifier
# -----------------
DA_FILTER_OFF = 1
DA_FILTER_ON = 2

# Waveform Generation Mode Identifier
# -----------------------------------
DA_MODE_CUT = 1
DA_MODE_SYNTHE = 2

# Repeat Mode Identifier
# ----------------------
DA_MODE_REPEAT = 1
DA_MODE_SINGLE = 2

# Repeat Mode Identifier
# ----------------------
DA_REPEAT_NONINTERVAL = 1
DA_REPEAT_INTERVAL = 2

# Counter Clear Identifier
# ------------------------
DA_COUNTER_CLEAR = 1
DA_COUNTER_NONCLEAR = 2

# DA Latch Identifier
# -------------------
DA_LATCH_CLEAR = 1
DA_LATCH_NONCLEAR = 2

# Clock Source Identifier
# -----------------------
DA_CLOCK_TIMER = 1
DA_CLOCK_FIXED = 2

# Configurations of the Connector Identifier
# ------------------------------------------
DA_EXTRG_IN = 1
DA_EXTRG_OUT = 2
DA_EXINT_IN = 3

# Configurations of the Connector Identifier
# ------------------------------------------
DA_EXCLK_IN = 1
DA_EXCLK_OUT = 2

# Reset Polarity Identifier
# -------------------------
DA_RESET_DOWN_EDGE = 0x04
DA_RESET_UP_EDGE = 0x08

# External trigger Polarity Identifier
# ------------------------------------
DA_EXTRG_DOWN_EDGE = 0x10
DA_EXTRG_UP_EDGE = 0x20

# Synchronous Analog Output Identifier
# ------------------------------------
DA_MASTER_MODE = 1
DA_SLAVE_MODE = 2

# Synchronous Number Identifier
# -----------------------------
DA_SYNC_NUM_1 = 0x0100
DA_SYNC_NUM_2 = 0x0200
DA_SYNC_NUM_3 = 0x0400
DA_SYNC_NUM_4 = 0x0800
DA_SYNC_NUM_5 = 0x1000
DA_SYNC_NUM_6 = 0x2000
DA_SYNC_NUM_7 = 0x4000

# After CloseEx output identifier
# -------------------------------
DA_OUTPUT_RESET = 0
DA_OUTPUT_MAINTAIN = 1

# RESET identifier
# ----------------
DA_RESET_ON = 1
DA_RESET_OFF = 2

# CPZ-360810 DIN/DOUT Function Identifier
# ---------------------------------------
DA_EX_DIO1 = 1
DA_EX_DIO2 = 2
DA_EX_DIO3 = 3
DA_EX_DIO4 = 4
DA_EX_DIO5 = 5

# PCI-3525 CN3 and CN4 Function Identifier
# ----------------------------------------
DA_CN_FREE = 0
DA_CN_EXTRG_IN = 1
DA_CN_EXTRG_OUT = 2
DA_CN_EXCLK_IN = 3
DA_CN_EXCLK_OUT = 4
DA_CN_EXINT_IN = 5
DA_CN_ATRG_IN = 6
DA_CN_DI = 7
DA_CN_DO = 8
DA_CN_DAOUT = 9
DA_CN_OPEN = 10
DA_CN_EX_OUT1 = 12
DA_CN_EX_OUT2 = 13

# PCI-3525 External Trigger Polarity Identifier
# ---------------------------------------------
DA_START_DOWN_EDGE = 1
DA_START_UP_EDGE = 2
DA_STOP_DOWN_EDGE = 4
DA_STOP_UP_EDGE = 8

# FIFO Trigger Level Identifier
# -----------------------------
DA_TRG_FREERUN = 0
DA_TRG_EXTTRG = 1
DA_TRG_ATRG = 2
DA_TRG_SIGTIMER = 3
DA_TRG_CNT_EQ = 4
DA_TRG_Z_CLR = 5
DA_TRG_AD_START = 5
DA_TRG_AD_STOP = 6
DA_TRG_AD_PRETRG = 7
DA_TRG_AD_POSTTRG = 8
DA_TRG_SMPLNUM = 9
DA_TRG_FIFO_EMPTY = 10
DA_TRG_SYNC1 = 14
DA_TRG_SYNC2 = 15
DA_FIFORESET = 0x0100
DA_RETRG = 0x0200

# Simultaneous Output Set Identifier
# ----------------------------------
DA_NORMAL_OUTPUT = 1
DA_SYNC_OUTPUT = 2

# Volume Identifier
# -----------------
DA_ADJUST_BIOFFSET = 1
DA_ADJUST_UNIOFFSET = 2
DA_ADJUST_BIGAIN = 3
DA_ADJUST_UNIGAIN = 4

# Calibration Item Identifier
# ---------------------------
DA_ADJUST_UP = 1
DA_ADJUST_DOWN = 2
DA_ADJUST_STORE = 3
DA_ADJUST_STANDBY = 4
DA_ADJUST_NOT_STORE = 5
DA_ADJUST_STORE_INITAREA = 6
DA_ADJUST_READ_FACTORY = 1
DA_ADJUST_READ_USER = 2

# Data Identifier
# ---------------
DA_DATA_PHYSICAL = 1
DA_DATA_BIN8 = 2
DA_DATA_BIN12 = 3
DA_DATA_BIN16 = 4
DA_DATA_BIN24 = 5
DA_DATA_BIN14 = 6

# Data Conversion Identifier
# --------------------------
DA_CONV_SMOOTH = 1
DA_CONV_AVERAGE1 = 2
DA_CONV_AVERAGE2 = 3

# error code
# ----------
DA_ERROR_SUCCESS               = 0x00000000
DA_ERROR_NOT_DEVICE            = 0xC0000001
DA_ERROR_NOT_OPEN              = 0xC0000002
DA_ERROR_INVALID_DEVICE_NUMBER = 0xC0000003
DA_ERROR_ALREADY_OPEN          = 0xC0000004
DA_ERROR_NOT_SUPPORTED         = 0xC0000009
DA_ERROR_NOW_SAMPLING          = 0xC0001001
DA_ERROR_STOP_SAMPLING         = 0xC0001002
DA_ERROR_START_SAMPLING        = 0xc0001003
DA_ERROR_SAMPLING_TIMEOUT      = 0xC0001004
DA_ERROR_INVALID_PARAMETER     = 0xC0001021
DA_ERROR_ILLEGAL_PARAMETER     = 0xC0001022
DA_ERROR_NULL_POINTER          = 0xC0001023
DA_ERROR_SET_DATA              = 0xC0001024
DA_ERROR_USED_AD               = 0xC0001025
DA_ERROR_FILE_OPEN             = 0xC0001041
DA_ERROR_FILE_CLOSE            = 0xC0001042
DA_ERROR_FILE_READ             = 0xC0001043
DA_ERROR_FILE_WRITE            = 0xC0001044
DA_ERROR_INVALID_DATA_FORMAT   = 0xC0001061
DA_ERROR_INVALID_AVERAGE_OR_SMOOTHING = 0xC0001062
DA_ERROR_INVALID_SOURCE_DATA   = 0xC0001063
DA_ERROR_NOT_ALLOCATE_MEMORY   = 0xC0001081
DA_ERROR_NOT_LOAD_DLL          = 0xC0001082
DA_ERROR_CALL_DLL              = 0xC0001083
DA_ERROR_CALIBRATION           = 0xC0001084
DA_ERROR_USBIO_FAILED          = 0xC0001085
DA_ERROR_USBIO_TIMEOUT         = 0xC0001086
DA_ERROR_USBLIB_LOAD_FAILED    = 0xC0001087


# =========
# Functions
# =========

# shared object
# -------------

SO_DIR = '/usr/lib'
SO_NAME = 'libgpg3300.so'
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
    _ulong = ctypes.c_ulong
    _ulong_p = ctypes.c_ulong
    _void_p = ctypes.c_void_p
    _P = ctypes.POINTER
    
    # int DaOpen(int nDevice);
    # ------------------------
    DaOpen = lib.DaOpen
    DaOpen.restype = _uint
    DaOpen.argtypes = (_int,)
    
    # int DaClose(int nDevice);
    # -------------------------
    DaClose = lib.DaClose
    DaClose.restype = _uint
    DaClose.argtypes = (_int,)
    
    # int DaCloseEx(int nDevice, int nFinalState);
    # --------------------------------------------
    DaCloseEx = lib.DaCloseEx
    DaCloseEx.restype = _uint
    DaCloseEx.argtypes = (_int, _int)
    
    # int DaGetDeviceInfo(int nDevice, PDABOARDSPEC pDaBoardSpec);
    # ------------------------------------------------------------
    DaGetDeviceInfo = lib.DaGetDeviceInfo
    DaGetDeviceInfo.restype = _uint
    DaGetDeviceInfo.argtypes = (_int, _P(DABOARDSPEC))
    
    # int DaSetBoardConfig(int nDevice, unsigned long ulSmplBufferSize,
    #                      void* pReserved, PLPDACALLBACK pEventProc, int dwUser);
    # ----------------------------------------------------------------------------
    DaSetBoardConfig = lib.DaSetBoardConfig
    DaSetBoardConfig.restype = _uint
    DaSetBoardConfig.argtypes = (_int, _ulong, _void_p, _P(LPDACALLBACK), _int)
    
    # int DaGetBoardConfig(int nDevice, unsigned long *ulSmplBufferSize,
    #                      unsigned long  *ulSmplEventFactor);
    # ------------------------------------------------------------------
    DaGetBoardConfig = lib.DaGetBoardConfig 
    DaGetBoardConfig.restype = _uint
    DaGetBoardConfig.argtypes = (_int, _P(_ulong), _P(_ulong))
    
    # int DaSetSamplingConfig(int nDevice, PDASMPLREQ pDaSmplConfig);
    # ---------------------------------------------------------------
    DaSetSamplingConfig = lib.DaSetSamplingConfig
    DaSetSamplingConfig.restype = _uint
    DaSetSamplingConfig.argtypes = (_int, _P(DASMPLREQ))
    
    # int DaGetSamplingConfig(int nDevice, PDASMPLREQ pDaSmplConfig);
    # ---------------------------------------------------------------
    DaGetSamplingConfig = lib.DaGetSamplingConfig
    DaGetSamplingConfig.restype = _uint
    DaGetSamplingConfig.argtypes = (_int, _P(DASMPLREQ))
    
    # int DaSetFifoConfig(int nDevice, PDAFIFOREQ pDaFifoConfig);
    # -----------------------------------------------------------
    DaSetFifoConfig = lib.DaSetFifoConfig
    DaSetFifoConfig.restype = _uint
    DaSetFifoConfig.argtypes = (_int, _P(DAFIFOREQ))

    # int DaGetFifoConfig(int nDevice, PDAFIFOREQ pDaFifoConfig);
    # -----------------------------------------------------------
    DaGetFifoConfig = lib.DaGetFifoConfig
    DaGetFifoConfig.restype = _uint
    DaGetFifoConfig.argtypes = (_int, _P(DAFIFOREQ))
    
    # int DaSetMode(int nDevice, PDAMODEREQ pDaMode);
    # -----------------------------------------------
    DaSetMode = lib.DaSetMode
    DaSetMode.restype = _uint
    DaSetMode.argtypes = (_int, _P(DAMODEREQ))
    
    # int DaGetMode(int nDevice, PDAMODEREQ pDaMode);
    # -----------------------------------------------
    DaGetMode = lib.DaGetMode
    DaGetMode.restype = _uint
    DaGetMode.argtypes = (_int, _P(DAMODEREQ))
    
    # int DaSetSamplingData(int nDevice, void * pSmplData, unsigned long ulSmplDataNum);
    # ----------------------------------------------------------------------------------
    DaSetSamplingData = lib.DaSetSamplingData
    DaSetSamplingData.restype = _uint
    DaSetSamplingData.argtypes = (_int, _void_p, _ulong)
    
    # int DaClearSamplingData(int nDevice);
    # -------------------------------------
    DaClearSamplingData = lib.DaClearSamplingData
    DaClearSamplingData.restype = _uint
    DaClearSamplingData.argtypes = (_int,)
    
    # int DaStartSampling(int nDevice, unsigned long ulSyncFlag);
    # -----------------------------------------------------------
    DaStartSampling = lib.DaStartSampling
    DaStartSampling.restype = _uint
    DaStartSampling.argtypes = (_int, _ulong)
    
    # int DaSyncSampling(int nDevice, unsigned long ulMode);
    # ------------------------------------------------------
    DaSyncSampling = lib.DaSyncSampling
    DaSyncSampling.restype = _uint
    DaSyncSampling.argtypes = (_int, _ulong)
    
    # int DaStopSampling(int nDevice);
    # --------------------------------
    DaStopSampling = lib.DaStopSampling
    DaStopSampling.restype = _uint
    DaStopSampling.argtypes = (_int,)
    
    # int DaGetStatus(int nDevice, unsigned long *ulDaSmplStatus, unsigned long *ulDaSmplCount,
    #                 unsigned long *ulDaAvailCount, unsigned long *ulDaAvailRepeat);
    # -----------------------------------------------------------------------------------------
    DaGetStatus = lib.DaGetStatus
    DaGetStatus.restype = _uint
    DaGetStatus.argtypes = (_int, _P(_ulong), _P(_ulong), _P(_ulong), _P(_ulong))
    
    # int DaGetOutputMode(int nDevice, unsigned long *ulMode);
    # --------------------------------------------------------
    DaGetOutputMode = lib.DaGetOutputMode
    DaGetOutputMode.restype = _uint
    DaGetOutputMode.argtypes = (_int, _P(_ulong))
    
    # int DaSetOutputMode(int nDevice, unsigned long ulMode);
    # -------------------------------------------------------
    DaSetOutputMode = lib.DaSetOutputMode
    DaSetOutputMode.restype = _uint
    DaSetOutputMode.argtypes = (_int, _ulong)
    
    # int DaOutputDA(int nDevice, unsigned long ulCh, PDASMPLCHREQ pDaSmplChReq, void * lpData);
    # ------------------------------------------------------------------------------------------
    DaOutputDA = lib.DaOutputDA
    DaOutputDA.restype = _uint
    DaOutputDA.argtypes = (_int, _ulong, _P(DASMPLCHREQ), _void_p)
    
    # int DaInputDI(int nDevice, unsigned long *ulData);
    # --------------------------------------------------
    DaInputDI = lib.DaInputDI
    DaInputDI.restype = _uint
    DaInputDI.argtypes = (_int, _P(_ulong))
    
    # int DaOutputDO(int nDevice, unsigned long ulData);
    # --------------------------------------------------
    DaOutputDO = lib.DaOutputDO
    DaOutputDO.restype = _uint
    DaOutputDO.argtypes = (_int, _ulong)
    
    # int DaSetInterval(int nDevice, unsigned long ulInterval);
    # ---------------------------------------------------------
    DaSetInterval = lib.DaSetInterval
    DaSetInterval.restype = _uint
    DaSetInterval.argtypes = (_int, _ulong)
    
    # int DaGetInterval(int nDevice, unsigned long *ulInterval);
    # ----------------------------------------------------------
    DaGetInterval = lib.DaGetInterval
    DaGetInterval.restype = _uint
    DaGetInterval.argtypes = (_int, _P(_ulong))
    
    
    # int DaSetFunction(int nDevice, unsigned int unCnNo, unsigned long ulFunction);
    # ------------------------------------------------------------------------------
    DaSetFunction = lib.DaSetFunction
    DaSetFunction.restype = _uint
    DaSetFunction.argtypes = (_int, _uint, _ulong)
    
    # int DaGetFunction(int nDevice, unsigned int unCnNo, unsigned long *ulFunction);
    # -------------------------------------------------------------------------------
    DaGetFunction = lib.DaGetFunction
    DaGetFunction.restype = _uint
    DaGetFunction.argtypes = (_int, _uint, _P(_ulong))
    
    # int DaDataConv(unsigned long, void *, unsigned long,  PDASMPLREQ,
    #                unsigned long, void*, unsigned long*, PDASMPLREQ,
    #                unsigned long, unsigned long, PDACONVPROC);
    # -----------------------------------------------------------------
    DaDataConv = lib.DaDataConv
    DaDataConv.restype = _uint
    DaDataConv.argtypes = (_ulong, _void_p, _ulong, _P(DASMPLREQ), _ulong, _void_p, _P(_ulong),
                           _P(DASMPLREQ), _ulong, _ulong, _P(DACONVPROC))
    
    ## int DaOpenEx(unsigned short wType, unsigned short wSubSystemID, unsigned char bRSW1, int * pnDevice);
    ## -----------------------------------------------------------------------------------------------------
    #DaOpenEx = lib.DaOpenEx
    #DaOpenEx.restype = _uint
    #DaOpenEx.argtypes = (_ushort, _ushort, _ubyte, _P(_int))
    
    # int DaSetCurrentDir(int nDevice, unsigned long Data);
    # -----------------------------------------------------
    DaSetCurrentDir = lib.DaSetCurrentDir
    DaSetCurrentDir.restype = _uint
    DaSetCurrentDir.argtypes = (_int, _ulong)
    
    # int DaGetCurrentDir(int nDevice, unsigned long *pData);
    # -------------------------------------------------------
    DaGetCurrentDir = lib.DaGetCurrentDir
    DaGetCurrentDir.restype = _uint
    DaGetCurrentDir.argtypes = (_int, _P(_ulong))
    
    # int DaSetPowerSupply(int nDevice, unsigned long ExOnOff);
    # ---------------------------------------------------------
    DaSetPowerSupply = lib.DaSetPowerSupply
    DaSetPowerSupply.restype = _uint
    DaSetPowerSupply.argtypes = (_int, _ulong)
    
    # int DaGetPowerSupply(int nDevice, unsigned long *ExOnOff);
    # ----------------------------------------------------------
    DaGetPowerSupply = lib.DaGetPowerSupply
    DaGetPowerSupply.restype = _uint
    DaGetPowerSupply.argtypes = (_int, _P(_ulong))
    
    # int DaSetExcessVoltage(int nDevice, unsigned long ExOnOff);
    # -----------------------------------------------------------
    DaSetExcessVoltage = lib.DaSetExcessVoltage
    DaSetExcessVoltage.restype = _uint
    DaSetExcessVoltage.argtypes = (_int, _ulong)
    
    # int DaGetRelayStatus(int nDevice, unsigned long *Status);
    # ---------------------------------------------------------
    DaGetRelayStatus = lib.DaGetRelayStatus
    DaGetRelayStatus.restype = _uint
    DaGetRelayStatus.argtypes = (_int, _P(_ulong))
    
    # int DaGetOVStatus(int nDevice, unsigned long *LowStatus, unsigned long *HighStatus);
    # ------------------------------------------------------------------------------------
    DaGetOVStatus = lib.DaGetOVStatus
    DaGetOVStatus.restype = _uint
    DaGetOVStatus.argtypes = (_int, _P(_ulong), _P(_ulong))
    
    # int DaStartFileSampling(int nDevice, char* pPathName, unsigned long ulFileFlag,
    #                         unsigned long ulSmplNum);
    # -------------------------------------------------------------------------------
    DaStartFileSampling = lib.DaStartFileSampling
    DaStartFileSampling.restype = _uint
    DaStartFileSampling.argtypes = (_int, _char_p, _ulong, _ulong)
    
    # int DaWriteFile(char* , void * , unsigned long, unsigned long, unsigned long);
    # ------------------------------------------------------------------------------
    DaWriteFile = lib.DaWriteFile
    DaWriteFile.restype = _uint
    DaWriteFile.argtypes = (_char_p, _void_p, _ulong, _ulong, _ulong)
    
    # int DaSetOutputDAEx(int nDevice, unsigned long ulCh, PDASMPLCHREQ pDaSmplChReq);
    # --------------------------------------------------------------------------------
    DaSetOutputDAEx = lib.DaSetOutputDAEx
    DaSetOutputDAEx.restype = _uint
    DaSetOutputDAEx.argtypes = (_int, _ulong, _P(DASMPLCHREQ))

    # int DaOutputDAEx(int nDevice, void * lpData);
    # ---------------------------------------------
    DaOutputDAEx = lib.DaOutputDAEx
    DaOutputDAEx.restype = _uint
    DaOutputDAEx.argtypes = (_int, _void_p)
    
    # int DaSetRelayData(int nDevice, unsigned long RelayData);
    # ---------------------------------------------------------
    DaSetRelayData = lib.DaSetRelayData
    DaSetRelayData.restype = _uint
    DaSetRelayData.argtypes = (_int, _ulong)
    
    pass




