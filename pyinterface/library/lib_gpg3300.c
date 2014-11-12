
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "fbida.h"

double get_time()
{
  struct timeval tv;
  gettimeofday(&tv, NULL);
  return tv.tv_sec + tv.tv_usec*1e-6;
}

void wait_until(double target_time)
{
  while(1)
    {
      if(get_time() >= target_time){ break; }
      usleep(100);
    }
}

int get_device_info(int nDevice, DABOARDSPEC *pBoardSpec)
{
  unsigned int nRet;
  
  // GPG3300.DaOpen()
  // ----------------
  printf("GPG3300::DaOpen(%d)\n", nDevice);
  nRet = DaOpen(nDevice);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaOpen(%d), %ul\n", nDevice, nRet);
      return -1;
    }

  // GPG3300.DaGetDeviceInfo()
  // -------------------------
  printf("GPG3300::DaGetDeviceInfo(%d, pBoardSpec)\n", nDevice);
  nRet = DaGetDeviceInfo(nDevice, pBoardSpec);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaGetDeviceInfo(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  printf("GPG3300::DeviceInfo, BoardType: %lu\n", pBoardSpec->ulBoardType);
  printf("GPG3300::DeviceInfo, BoardID: %lu\n", pBoardSpec->ulBoardID);
  printf("GPG3300::DeviceInfo, SamplingMode: %lu\n", pBoardSpec->ulSamplingMode);
  printf("GPG3300::DeviceInfo, ChCount: %lu\n", pBoardSpec->ulChCount);
  printf("GPG3300::DeviceInfo, Resolution: %lu\n", pBoardSpec->ulResolution);
  printf("GPG3300::DeviceInfo, Range: %lu\n", pBoardSpec->ulRange);
  printf("GPG3300::DeviceInfo, Isolation: %lu\n", pBoardSpec->ulIsolation);
  printf("GPG3300::DeviceInfo, DI: %lu\n", pBoardSpec->ulDi);
  printf("GPG3300::DeviceInfo, DO: %lu\n", pBoardSpec->ulDo);
  
  // GPG3300.DaClose()
  // -----------------
  printf("GPG3300::AdClose(%d)\n", nDevice);
  nRet = DaClose(nDevice);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaClose(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  
  return 0;
}

int open(int nDevice)
{
  int ret = 0;
  unsigned int nRet;
  
  // GPG3300.DaOpen()
  // ----------------
  printf("GPG3300::DaOpen(%d)\n", nDevice);
  nRet = DaOpen(nDevice);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaOpen(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  
  return ret;
}

int close(int nDevice)
{
  int ret = 0;
  unsigned int nRet;
  
  // GPG3300.DaClose()
  // -----------------
  printf("GPG3300::DaClose(%d)\n", nDevice);
  nRet = DaClose(nDevice);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaClose(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  return ret;
}

int output_da(int nDevice, unsigned long maxCh, unsigned long *ChNo,
		   unsigned long *Range, unsigned short *Data)
{
  int ret = 0;
  unsigned int nRet;
  int i;
  
  DASMPLCHREQ DaSmplChReq[maxCh];
  
  // GPG3300.DaOutputDA()
  // --------------------
  for(i=0; i<maxCh; i++)
    {
      DaSmplChReq[i].ulChNo = ChNo[i];
      DaSmplChReq[i].ulRange = Range[i];
      printf("GPG3300::INFO, ch=%lu, range=%lu, data=%u\n", ChNo[i], Range[i], Data[i]);
    }
  
  printf("GPG3300::DaOutputDA(%d, %lu, &DaSmplChReq, &Data)\n", nDevice, maxCh);
  nRet = DaOutputDA(nDevice, maxCh, &DaSmplChReq[0], &Data[0]);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaOutputDA(%d, %lu, &DaSmplChReq, &Data), %ul\n",
	     nDevice, maxCh, nRet);
      ret = -1;
    }  
  
  return ret;
}

/*
int output_da(int nDevice, unsigned long maxCh, unsigned long *ChNo,
		   unsigned long *Range, unsigned short *Data)
{
  int ret = 0;
  unsigned int nRet;
  int i;
  
  DASMPLCHREQ DaSmplChReq[maxCh];
  
  // GPG3300.DaOpen()
  // ----------------
  printf("GPG3300::DaOpen(%d)\n", nDevice);
  nRet = DaOpen(nDevice);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaOpen(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  
  // GPG3300.DaOutputDA()
  // --------------------
  for(i=0; i<maxCh; i++)
    {
      DaSmplChReq[i].ulChNo = ChNo[i];
      DaSmplChReq[i].ulRange = Range[i];
      printf("GPG3300::INFO, ch=%lu, range=%lu, data=%u\n", ChNo[i], Range[i], Data[i]);
    }
  
  printf("GPG3300::DaOutputDA(%d, %lu, &DaSmplChReq, &Data)\n", nDevice, maxCh);
  nRet = DaOutputDA(nDevice, maxCh, &DaSmplChReq[0], &Data[0]);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaOutputDA(%d, %lu, &DaSmplChReq, &Data), %ul\n",
	     nDevice, maxCh, nRet);
      ret = -1;
      goto finalize;
    }  
  
  // GPG3300.DaClose()
  // -----------------
 finalize:
  printf("GPG3300::DaClose(%d)\n", nDevice);
  nRet = DaClose(nDevice);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaClose(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  return ret;
}
*/
int set_oneshot_da(int nDevice, unsigned long maxCh, unsigned long *ChNo,
		   unsigned long *Range, unsigned short *Data,
		   unsigned long SamplingMode)
{
  int ret = 0;
  unsigned int nRet;
  int i;
  
  DASMPLREQ DaSmplConfig;
  
  // GPG3300.DaOpen()
  // ----------------
  printf("GPG3300::DaOpen(%d)\n", nDevice);
  nRet = DaOpen(nDevice);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaOpen(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  
  // GPG3300.DaOutputDA()
  // --------------------
  printf("GPG3300::DaSetBoardConfig(%d, 1, NULL, NUL, 0)\n", nDevice);
  nRet = DaSetBoardConfig(nDevice, 1, NULL, NULL, 0);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaSetBoardConfig(%d, 1, NULL, NULL, 0), %u\n",
	     nDevice, nRet);
      ret = -1;
      goto finalize;
    }
  
  DaSmplConfig.ulChCount = maxCh;
  for(i=0; i<maxCh; i++)
    {
      DaSmplConfig.SmplChReq[i].ulChNo = ChNo[i];
      DaSmplConfig.SmplChReq[i].ulRange = Range[i];
      printf("GPG3300::INFO, ch=%lu, range=%lu, data=%u\n", ChNo[i], Range[i], Data[i]);
    }
  DaSmplConfig.ulSamplingMode = SamplingMode;
  DaSmplConfig.fSmplFreq = 1.0;
  DaSmplConfig.ulSmplRepeat = 0;
  DaSmplConfig.ulTrigMode = DA_FREERUN;
  DaSmplConfig.ulTrigPoint = DA_TRIG_START;
  DaSmplConfig.ulTrigDelay = 0;
  DaSmplConfig.ulEClkEdge = DA_DOWN_EDGE;
  DaSmplConfig.ulTrigEdge = DA_DOWN_EDGE;
  DaSmplConfig.ulTrigDI = 0;
  
  printf("GPG3300::DaSetSamplingConfig(%d, &DaSmplConfig)\n", nDevice);
  nRet = DaSetSamplingConfig(nDevice, &DaSmplConfig);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, GPG3300::DaSetSamplingConfig(%d, &DaSmplConfig), %u\n",
	     nDevice, nRet);
      ret = -1;
      goto finalize;
    }  
  
  printf("GPG3300::DaClearSamplingData(%d)\n", nDevice);
  nRet = DaClearSamplingData(nDevice);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaClearSamplingData(%d), %u\n",
	     nDevice, nRet);
      ret = -1;
      goto finalize;
    }  
  
  printf("GPG3300::DaSetSamplingData(%d, &Data, 1)\n", nDevice);
  nRet = DaSetSamplingData(nDevice, &Data, 1);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaSetSamplingData(%d, &Data, 1), %u\n",
	     nDevice, nRet);
      ret = -1;
      goto finalize;
    }  
  
  printf("GPG3300::DaStartSampling(%d, FLAG_ASYNC)\n", nDevice);
  nRet = DaStartSampling(nDevice, FLAG_ASYNC);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaStartSampling(%d, FLAG_ASYNC), %u\n",
	     nDevice, nRet);
      ret = -1;
      goto finalize;
    }  
  
  // GPG3300.DaClose()
  // -----------------
 finalize:
  /*
  printf("GPG3300::DaClose(%d)\n", nDevice);
  nRet = DaClose(nDevice);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaClose(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  */
  return ret;
}


int stop_sampling(int nDevice)
{
  unsigned int nRet;
  
  /*
  // GPG3300.DaOpen()
  // ----------------
  printf("GPG3300::DaOpen(%d)\n", nDevice);
  nRet = DaOpen(nDevice);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaOpen(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  */

  // GPG3300.DaGetDeviceInfo()
  // -------------------------
  printf("GPG3300::DaStopSampling(%d)\n", nDevice);
  nRet = DaStopSampling(nDevice);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaStopSampling(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  
  // GPG3300.DaClose()
  // -----------------
  printf("GPG3300::AdClose(%d)\n", nDevice);
  nRet = DaClose(nDevice);
  if(nRet!=DA_ERROR_SUCCESS)
    {
      printf("GPG3300::Error, DaClose(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  
  return 0;
}


/*
int get_ad(int nDevice, unsigned long SingleDiff, unsigned long Range,
	   unsigned long SmplNum, float SmplFreq, double StartTime, unsigned short *Data)
{
  int ret = 0;
  unsigned int nRet;
  ADBOARDSPEC BoardSpec;
  unsigned long maxCh;
  ADSMPLREQ AdSmplConfig;
  int i, j;
  
  // GPG3100.AdOpen()
  // ----------------
  printf("GPG3100::AdOpen(%d)\n", nDevice);
  nRet = AdOpen(nDevice);
  if(nRet!=AD_ERROR_SUCCESS)
    {
      printf("GPG3100::Error, AdOpen(%d), %ul\n", nDevice, nRet);
      return -1;
    }


  // GPG3100.AdGetDeviceInfo()
  // -------------------------
  printf("GPG3100::AdGetDeviceInfo(%d, &BoardSpec)\n", nDevice);
  nRet = AdGetDeviceInfo(nDevice, &BoardSpec);
  if(nRet!=AD_ERROR_SUCCESS)
    {
      printf("GPG3100::Error, AdGetDeviceInfo(%d), %ul\n", nDevice, nRet);
      ret = -1;
      goto finalize;
    }
  
  // prepare maxCh
  if(SingleDiff==AD_INPUT_SINGLE){ maxCh = BoardSpec.ulChCountS; }
  else if(SingleDiff==AD_INPUT_DIFF){ maxCh = BoardSpec.ulChCountD; }
  else
    {
      printf("GPG3100::Error, SingleDiff should be (S/E: 1 | Diff: 2), %lu\n", SingleDiff);
      ret = -1;
      goto finalize;
    }
  
  
  // GPG3100.AdGetSamplingData()
  // ---------------------------
  printf("GPG3100::AdGetSamplingConfig(%d, &AdSmplConfig)\n", nDevice);
  nRet = AdGetSamplingConfig(nDevice, &AdSmplConfig);
  if(nRet!=AD_ERROR_SUCCESS)
    {
      printf("GPG3100::Error, AdGetSamplingConfig(%d, &AdSmplConfig), %ul\n", nDevice, nRet);
      ret = -1;
      goto finalize;
    }
  
  //printf(" -- AdSmplConfig.ulChCount: %lu\n", maxCh);
  AdSmplConfig.ulChCount = maxCh;
  for(i=0; i<maxCh; i++)
    {
      AdSmplConfig.SmplChReq[i].ulChNo = (unsigned long)(i + 1);
      AdSmplConfig.SmplChReq[i].ulRange = Range;
    }
  //AdSmplConfig.ulSamplingMode = SamplingMode;
  AdSmplConfig.ulSingleDiff = SingleDiff;
  AdSmplConfig.ulSmplNum = SmplNum;
  AdSmplConfig.ulSmplEventNum = 0;
  AdSmplConfig.fSmplFreq = SmplFreq;
  AdSmplConfig.ulTrigPoint = AD_TRIG_START;
  AdSmplConfig.ulTrigMode = AD_FREERUN;
  AdSmplConfig.lTrigDelay = 0;
  AdSmplConfig.ulTrigCh = 1;
  AdSmplConfig.fTriglevel1 = 0.0;
  AdSmplConfig.fTriglevel2 = 0.0;
  AdSmplConfig.ulEClkEdge = AD_DOWN_EDGE;
  AdSmplConfig.ulATrgPulse = AD_LOW_PULSE;
  AdSmplConfig.ulTrigEdge = AD_DOWN_EDGE;
  AdSmplConfig.ulTrigDI = 1;
  AdSmplConfig.ulFastMode = AD_NORMAL_MODE;
  
  printf("GPG3100::AdSetSamplingConfig(%d, &AdSmplConfig)\n", nDevice);
  nRet = AdSetSamplingConfig(nDevice, &AdSmplConfig);
  if(nRet!=AD_ERROR_SUCCESS)
    {
      printf("GPG3100::Error, AdSetSamplingConfig(%d, &AdSmplConfig), %ul\n", nDevice, nRet);
      ret = -1;
      goto finalize;
    }
  
  for(i=0; i<SmplNum; i++)
    {
      for(j=0; j<maxCh; j++)
	{
	  Data[i*maxCh + j] = 0;
	}
    }
  
  wait_until(StartTime);
  
  printf("GPG3100::AdStartSampling(%d, FLAG_SYNC)\n", nDevice);
  nRet = AdStartSampling(nDevice, FLAG_SYNC);
  if(nRet!=AD_ERROR_SUCCESS)
    {
      printf("GPG3100::Error, AdStartSampling(%d, FLAG_SYNC), %ul\n", nDevice, nRet);
      ret = -1;
      goto finalize;
    }
  
  printf("GPG3100::AdGetSamplingData(%d, &Data, %lu)\n", nDevice, SmplNum);
  nRet = AdGetSamplingData(nDevice, &Data[0], &SmplNum);
  if(nRet!=AD_ERROR_SUCCESS)
    {
      printf("GPG3100::Error, AdGetSamplingData(%d, &Data,%lu), %ul\n", nDevice, SmplNum, nRet);
      ret = -1;
      goto finalize;
    }
  
  
  // GPG3100.AdClose()
  // -----------------
 finalize:
  printf("GPG3100::AdClose(%d)\n", nDevice);
  nRet = AdClose(nDevice);
  if(nRet!=AD_ERROR_SUCCESS)
    {
      printf("GPG3100::Error, AdClose(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  
  return ret;
}

*/
