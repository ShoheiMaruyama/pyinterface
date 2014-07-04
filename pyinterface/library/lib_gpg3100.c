
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "fbiad.h"

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

int get_device_info(int nDevice, ADBOARDSPEC *pBoardSpec)
{
  unsigned int nRet;
  
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
  printf("GPG3100::AdGetDeviceInfo(%d, pBoardSpec)\n", nDevice);
  nRet = AdGetDeviceInfo(nDevice, pBoardSpec);
  if(nRet!=AD_ERROR_SUCCESS)
    {
      printf("GPG3100::Error, AdGetDeviceInfo(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  printf("GPG3100::DeviceInfo, BoardType: %lu\n", pBoardSpec->ulBoardType);
  printf("GPG3100::DeviceInfo, BoardID: %lu\n", pBoardSpec->ulBoardID);
  printf("GPG3100::DeviceInfo, SamplingMode: %lu\n", pBoardSpec->ulSamplingMode);
  printf("GPG3100::DeviceInfo, Resolution: %lu\n", pBoardSpec->ulResolution);
  printf("GPG3100::DeviceInfo, ChCountS: %lu\n", pBoardSpec->ulChCountS);
  printf("GPG3100::DeviceInfo, ChCountD: %lu\n", pBoardSpec->ulChCountD);
  printf("GPG3100::DeviceInfo, Range: %lu\n", pBoardSpec->ulRange);
  printf("GPG3100::DeviceInfo, Isolation: %lu\n", pBoardSpec->ulIsolation);
  printf("GPG3100::DeviceInfo, DI: %lu\n", pBoardSpec->ulDI);
  printf("GPG3100::DeviceInfo, DO: %lu\n", pBoardSpec->ulDO);
    
  // GPG3100.AdClose()
  // -----------------
  printf("GPG3100::AdClose(%d)\n", nDevice);
  nRet = AdClose(nDevice);
  if(nRet!=AD_ERROR_SUCCESS)
    {
      printf("GPG3100::Error, AdClose(%d), %ul\n", nDevice, nRet);
      return -1;
    }
  
  return 0;
}


int get_oneshot_ad(int nDevice, unsigned long SingleDiff, unsigned long Range,
		   unsigned short *Data)
{
  int ret = 0;
  unsigned int nRet;
  ADBOARDSPEC BoardSpec;
  unsigned long maxCh;
  ADSMPLCHREQ AdSmplChReq[256];
  int i;
  
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
  
  if(SingleDiff==AD_INPUT_SINGLE){ maxCh = BoardSpec.ulChCountS; }
  else if(SingleDiff==AD_INPUT_DIFF){ maxCh = BoardSpec.ulChCountD; }
  else
    {
      printf("GPG3100::Error, SingleDiff should be (S/E: 1 | Diff: 2), %lu\n", SingleDiff);
      ret = -1;
      goto finalize;
    }
  
  // GPG3100.AdInputAD()
  // -------------------
  for(i=0; i<maxCh; i++)
    {
      AdSmplChReq[i].ulChNo = i+1;
      AdSmplChReq[i].ulRange = Range;      
    }
  

  for(i=0; i<maxCh; i++){ Data[i] = 0; }

  printf("GPG3100::AdInputAD(%d, %lu, %lu, &AdSmplChReq, &Data)\n", nDevice, maxCh, SingleDiff);
  nRet = AdInputAD(nDevice, maxCh, SingleDiff, &AdSmplChReq[0], &Data[0]);
  if(nRet!=AD_ERROR_SUCCESS)
    {
      printf("GPG3100::Error, AdInputAD(%d, %lu, %lu, &AdSmplChReq, &Data), %u\n",
	     nDevice, maxCh, SingleDiff, nRet);
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

