#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:09:04 2023
'' script to sort AMT 23 ship uway data into daily files

@author: tjor
"""

import sys
import os
import numpy as np
#from monda.sorad import access, plots, qc
import logging
import pandas as pd

import shutil

if __name__ == '__main__':

    jdays = np.arange(288,326,1)

    for i in range(len(jdays)):
         dir_i = '2012' + str(jdays[i])
         print(dir_i)
         os.mkdir('/data/datasets/cruise_data/active/AMT22/OSU/Ship_data/Original/underway_daily/' + dir_i)


    jdays = np.arange(289,326,1)
    for i in range(len(jdays)):
        file_i = '/data/datasets/cruise_data/active/AMT22/OSU/Ship_data/Original/daily_1s_' + str(jdays[i]) + '.txt'
        dist_i =  '/data/datasets/cruise_data/active/AMT22/OSU/Ship_data/Original/underway_daily/2012' + str(jdays[i]) + '/daily_1s_gps_meta.txt'
        
        shutil.copy(file_i,dist_i, follow_symlinks=True)
        
   
   # fn = '/data/datasets/cruise_data/active/AMT23/AMT23/underway/Ships_underway_data/underway_data_Seatex-gga_new.txt'
  #  data = pd.read_csv(fn, sep='\t', header=None)
#
    # fn = '/data/datasets/cruise_data/active/AMT23/AMT23/underway/Ships_underway_data/underway_data_Seatex-gga.txt'
    # data = pd.read_csv(fn, sep='\t', skiprows=2, header=None)
    
    # create directories
   # jdays = np.arange(295,296,1)
   # for i in range(len(jdays)):
    #     dir_i = '2013' + str(jdays[i])
     #    print(dir_i)
      #   os.mkdir('/data/datasets/cruise_data/active/AMT23/AMT23/underway/Ships_underway_data/seatex_daily/' + str(dir_i))
        
 #   for i in range(len(jdays)):
  #      data_i = data[np.floor(data[1])==jdays[i]]
   #     dir_i = '2013' + str(jdays[i])
    #    print(len(data_i))
     #   data_i.to_csv('/data/datasets/cruise_data/active/AMT23/AMT23/underway/Ships_underway_data/underway_daily/' + str(dir_i) + '/seatex-gga.csv') 
    
    #fn = '/data/datasets/cruise_data/active/AMT23/AMT23/underway/Ships_underway_data/underway_data_oceanlogger_new.txt'
    #data = pd.read_csv(fn, sep='\t')
    
    
    #for i in range(len(jdays)):
     #   data_i = data[np.floor(data['#julian date and decimal time'])==jdays[i]]
      #  dir_i = '2013' + str(jdays[i])
       # print(len(data_i))
        #data_i.to_csv('/data/datasets/cruise_data/active/AMT23/AMT23/underway/Ships_underway_data/underway_daily/' + str(dir_i) + '/oceanlogger.csv') 