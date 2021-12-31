#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 17:58:30 2021

@author: erri
"""
import os
import numpy as np
# from itertools import combinations

########################################################################################################################
# SETUP FOLDERS
########################################################################################################################
# setup working directory and DEM's name
w_dir = '/home/erri/Documents/morphological_approach/3_output_data/q1.0_2/2_prc_laser/surveys/'
files=[]
for f in sorted(os.listdir(w_dir)):
    path = os.path.join(w_dir, f)
    if os.path.isfile(path) and f.endswith('.txt') and f.startswith('matrix_bed_norm'):
        files = np.append(files, f)
comb = []
for i in range (0, len(files)-1):
    for j in range (0, len(files)-1-i):
        DEM1=files[i]
        DEM2=files[i+1+j]
        print(DEM2, '-', DEM1)
        comb = np.append(comb, DEM2 + '-' + DEM1)