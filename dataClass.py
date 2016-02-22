# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 12:12:09 2016

@author: David
"""
from matplotlib.figure import Figure
import numpy as np
class xyData():
    def __init__(self, folderName , x, y):
        self.folderName=folderName
        self.xData=x
        self.yData=y
        self.fig = Figure()
        self.fits = []
        ax1f1 = self.fig.add_subplot(111)
        ax1f1.plot(x,y)
        
    def find_nearestx(self, value):
        idx = (np.abs(self.xData-value)).argmin()
        return idx,self.xData[idx]
    def addFit(self, out, xi, xf, name = None):
        self.fits.append(fit(out, xi, xf, name))

class fit():
    def __init__(self, out, xi, xf, name = None):
        self.name = name
        self.out = out
        self.xi=xi
        self.xf=xf
    def plotBest(self):
        self.out.plot_fit()