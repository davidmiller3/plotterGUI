# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 12:12:09 2016

@author: David
"""
from matplotlib.figure import Figure
class xyData():
    def __init__(self, folderName , x, y):
        self.folderName
        self.xData=x
        self.yData=y
        self.fig = Figure()
        ax1f1 = self.fig.add_subplot(111)
        ax1f1.plot(x,y)