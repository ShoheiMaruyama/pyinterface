
#include <stdio.h>
#include "fbiad.h"


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
		   unsigned short *Data, unsigned long numData)
{
  int ret = 0;
  unsigned int nRet;
  ADBOARDSPEC BoardSpec;
  unsigned long maxCh;
  ADSMPLCHREQ AdSmplChReq[128];
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
      return -1;
    }
  
  if(SingleDiff==AD_INPUT_SINGLE){ maxCh = BoardSpec.ulChCountS; }
  else if(SingleDiff==AD_INPUT_DIFF){ maxCh = BoardSpec.ulChCountD; }
  else
    {
      printf("GPG3100::Error, SingleDiff should be (S/E: 1 | Diff: 2), %lu\n", SingleDiff);
      return -1;
    }
  
  // GPG3100.AdInputAD()
  // -------------------
  for(i=0; i<maxCh; i++)
    {
      AdSmplChReq[i].ulChNo = i+1;
      AdSmplChReq[i].ulRange = Range;      
    }
  

  for(i=0; i<numData; i++){ Data[i] = 0; }

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

