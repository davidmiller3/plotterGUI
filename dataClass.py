# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 12:12:09 2016

@author: David
"""
from matplotlib.figure import Figure
import matplotlib.pyplot as plt 
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
        
    def addFit(self, out, xi, xf, params, name=None):
        if name == None:
            name=self.folderName
        else:
            pass
        self.fits.append(fit(out, xi, xf, params, name))
    def viewFit(self, index):
        if len(self.fits)-1<index:
            pass
        else:
            self.fits[index].plotBest()
    def plotAllFits(self):
        plt.figure(1)        
        plt.plot(self.xData, self.yData, 'bo')        
        for i in self.fits:
            plt.plot(self.xData, i.out.best_fit)
            plt.annotate('Q = '+ str(self.params[3]), xy=(i.params[0],i.params[1]))

class fit():
    def __init__(self, out, xi, xf, params, name = None):
        self.name = name
        self.out = out
        self.xi=xi
        self.xf=xf
        self.params=params
    def plotBest(self):
        font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
        self.out.plot_fit()
        plt.title(self.name)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude')
        plt.annotate('Q = '+ str(self.params[3]), xy=(0.05, 0.95), xycoords='axes fraction')