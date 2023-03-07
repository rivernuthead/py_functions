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

xData = np.array([47,47,47,47,47,47,47,47,47,94,94,94,94,94,94,94,94,141,141,141,141,141,141,141,188,188,188,188,188,188,235,235,235,235,235,282,282,282,282,329,329,329,376,376])
yData=np.array([6.5957e+06,1.11141e+07,1.22258e+07,1.23625e+07,1.37895e+07,1.46145e+07,1.51431e+07,1.5918e+07,1.70572e+07,7.81228e+06,1.03714e+07,1.09369e+07,1.20665e+07,1.26482e+07,1.34732e+07,1.42496e+07,1.57527e+07,6.92625e+06,1.03721e+07,1.15071e+07,1.12059e+07,1.24229e+07,1.31586e+07,1.4954e+07,7.98772e+06,1.16014e+07,1.20612e+07,1.36529e+07,1.44412e+07,1.58728e+07,8.54078e+06,1.11129e+07,1.2026e+07,1.31133e+07,1.46081e+07,6.828e+06,8.41238e+06,9.70288e+06,1.16626e+07,6.5298e+06,8.09717e+06,1.07178e+07,6.16612e+06,8.5231e+06])

xData = np.array([47,47,47,47,47,47,47,47,47,94,94,94,94,94,94,94,94,141,141,141,141,141,141,141,188,188,188,188,188,188,235,235,235,235,235,282,282,282,282,329,329,329,376,376])
yData=np.array([0.65957,1.11141,1.22258,1.23625,1.37895,1.46145,1.51431,1.5918,1.70572,0.781228,1.03714,1.09369,1.20665,1.26482,1.34732,1.42496,1.57527,0.692625,1.03721,1.15071,1.12059,1.24229,1.31586,1.4954,0.798772,1.16014,1.20612,1.36529,1.44412,1.58728,0.854078,1.11129,1.2026,1.31133,1.46081,0.6828,0.841238,0.970288,1.16626,0.65298,0.809717,1.07178,0.616612,0.85231])

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