#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:47:52 2022

@author: erri
"""

import numpy as np
from scipy import optimize as opt
import matplotlib.pyplot as plt

def interpolate(func, xData, yData, ic=None, bounds=(-np.inf, np.inf)):
    # Interpolate data by fitting a given function, then returns the interpolated curve as a 1d array.
    par, covar = opt.curve_fit(func, xData, yData, p0=ic, maxfev=8000, bounds=bounds)
    if len(par) == 2:
        intCurve = func(xData, par[0], par[1])
    elif len(par) == 3:
        intCurve = func(xData, par[0], par[1], par[2])
    elif len(par) == 4:
        intCurve = func(xData, par[0], par[1], par[2], par[3])
    else:
        print("Interpolation failed. The interpolation function must have 2 or 3 parameters")
        intCurve = -1 * np.ones(len(xData))
    return par, intCurve, covar

# Scour and deposition volumes interpolation function
def func(x,A,B):
    y = A*(1-np.exp(-x/B))
    return y

yData = np.array([6595700,7812280,6926250,7987720,8540780,6828000,6529800,6166120,6645980,11114100,10371400,10372100,11601400,11112900,8412380,8097170,8523100,12225800,10936900,11507100,12061200,12026000,9702880,10717800,12362500,12066500,11205900,13652900,13113300,11662600,13789500,12648200,12422900,14441200,14608100,14614500,13473200,13158600,15872800,15143100,14249600,14954000,15918000,15752700,17057200])
xData = np.array([1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,6,6,6,6,7,7,7,8,8,9])
ic=np.array([np.mean(yData),np.min(xData)]) # Initial parameter guess

par, intCurve, covar = interpolate(func, xData, yData, ic)


print()
print('Parameters:')
print('A=', par[0], 'Variance=', covar[0,0])
print('B=', par[1], 'Variance=', covar[1,1])


fig1, ax1 = plt.subplots(dpi=100)
ax1.scatter(xData, yData)
ax1.plot(xData, intCurve, c='red')
ax1.set_title('Interpolation')
ax1.set_xlabel('xData')
ax1.set_ylabel('yData')
plt.show()