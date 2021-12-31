#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 12:02:32 2021

@author: erri
"""
import numpy as np


data = np.array([0,1,2,3,4,5,6,7,8,9])
# Forward and backward mean
def  ward_mean(data, parameter):
    averaged_data=[]
    if parameter == 'f':
        print('Performing forward average...')
    elif parameter == 'b':
        print('Performing backward average...')
    else:
        print('Parameter must be a string:  f or b for Forward or Backward mean')
    # Loop all over data array
    for i in range(2, len(data)+1):
        if parameter == 'f':
            mean=np.sum(data[:i])/i 
        elif parameter == 'b':
            mean=np.sum(data[len(data)-i:])/i
        else:
            print('parameter error!')
            break
        # Append data to outcomes array
        averaged_data = np.append(averaged_data, mean)
    return averaged_data

ward_data_prc = ward_mean(data, parameter='b')