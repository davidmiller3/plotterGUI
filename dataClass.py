# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 12:12:09 2016

@author: David
"""
from matplotlib.figure import Figure
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import math
import os
import lmPeakFit as lpf
class xyData():
    def __init__(self, pathToDataFolder):
#Path to data
        self.path=pathToDataFolder
#Look for a .csv and .txt file. This needs to be edited for other applictions
        for i in os.listdir(self.path):
            if i[-4:] == ".csv":
#Read data file. Names columns based on ZI Lock in sweep labview in output 
#(Time, Frequency, R amplitude, Phase)
                self.data = pd.read_csv((os.path.join(self.path,i)), names=['t','f', 'r', 'th']) 
            if i[-4:] == ".txt":
                self.info = pd.read_table((os.path.join(self.path,i)), delimiter = ':', nrows=7, header =  None)
        self.laserPowerType = self.info.loc[0,1]   
        self.laserPower = self.info.loc[1,1]
        self.deviceType = self.info.loc[2,1]
        self.deviceRow = self.info.loc[3,1]
        self.deviceCol = self.info.loc[4,1]
        self.deviceWid = self.info.loc[5,1]
        self.date = self.info.loc[6,1]
#        self.imagePath = os.path.join("Z:\Group\Projects\FIBed Graphene Drumhead Resonators\Images\Device_Images", self.deviceRow +'_'+ self.deviceCol)
        self.fits={}
        self.fig=Figure()
#Create a MPL plot to show in fitting window. self.fig is the plot
        ax=self.fig.add_subplot(1,1,1)
        axt=ax.twinx()
        ax.plot(self.data.f, self.data.th)
        axt.plot(self.data.f, self.data.r, 'g')
    def plotData(self,):
        fig = Figure()
        ax1f1 = fig.add_subplot(111)
        ax1f1.plot(self.data['f'],self.data['r'])
        plt.show()                      
        return fig
    def fitDataSelection(self, xi, xf, ip):
#Fit a portion of the data. Fit from xi to xf. [xi], ip are the expected parameters
        x0=ip[0]
        y0=ip[1]
        sigma=ip[2]
        out, params=lpf.lmDDOFit(self.data['f'][xi:xf+1],self.data['r'][xi:xf+1],[x0,2*sigma*y0,sigma])               
        return out, params
    def storeLorFit(self, out, xi, xf, params, omega):
#Stores a lorentzian fit in a dictionary of fitted values. out is the fit, xi
#and xf are initial and final values, params if the output fit params, and Omega
#is the guessed resonance         
        key='w' + str(omega)        
        self.fits[key]=[fit(out, xi, xf, params)]
        self.xData=x
        self.yData=y
        self.fig = Figure()
        self.fits = []
        ax1f1 = self.fig.add_subplot(111)
        ax1f1.plot(x,y)
        
    def find_nearestx(self, value):
        idx = (np.abs(self.data.f-value)).argmin()
        return idx, self.data.f[idx]
        
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
#idx is x value closes to center
            idx=min(range(len(self.xData)), key=lambda x: abs(self.xData[x]-i.params[0]))
            print i.params[0],i.params[1]
            plt.plot(self.xData[i.xi:i.xf+1], i.out.best_fit)
            plt.annotate('Q = '+ str(i.params[3]) + '\n' + 'w_0 = '+ str(i.params[0]), xy=(i.params[0],self.yData[idx]), textcoords = 'data', xycoords='data')
        plt.show()
"""
class fit():
    def __init__(self, out, xi, xf, params, name = None):
        self.out = out
        self.xi=xi
        self.xf=xf
        self.w0=params[0]
        self.y0=params[1]
        self.Q=params[3] 
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
   """