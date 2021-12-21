#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:02:43 2021

@author: erri
"""
import numpy as np
from scipy import optimize as opt
import matplotlib.pyplot as plt

xData = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
yData = np.array([6.04, 8.86, 10.18, 11.12, 12.4, 13.13, 13.58, 14.62])


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

def func(x,A,B):
    y = A*(1-np.exp(-x/B))
    return y

par, intCurve, covar = interpolate(func, xData, yData)

print()
print('Parameters:')
print('A=', par[0], 'Variance=', covar[0,0])
print('B=', par[1], 'Variance=', covar[1,1])


fig1, ax1 = plt.subplots(dpi=100)
ax1.scatter(xData, yData, c='red')
ax1.plot(xData, intCurve)
ax1.set_title('Interpolation')
ax1.set_xlabel('xData')
ax1.set_ylabel('yData')
plt.show()