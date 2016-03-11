# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 17:21:56 2016

@author: David
"""
from PyQt4.uic import loadUiType
import os
from dataClass import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import lmPeakFit as lpf
import math

Ui_MainWindow, QMainWindow = loadUiType('window.ui')

homedir="Z:\Group\Projects\FIBed Graphene Drumhead Resonators\Measurement Data\Lock-In Sweeps"
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
#data_dict stores all loaded data sets
        self.data_dict = {}
        self.mplfigs.itemSelectionChanged.connect(self.changefig)
        self.folderSelect.clicked.connect(self.onSelectFolder)
        self.renameSelectedData.clicked.connect(self.onRenameSelectedData)
        self.saveFit.clicked.connect(self.onSaveFit)
        self.cancelFit.clicked.connect(self.onCancelFit)
        self.fitSelectedData.clicked.connect(self.onFit)
        self.fitSelectedData.setEnabled(False)
        self.saveFit.setEnabled(False)
        self.cancelFit.setEnabled(False)
        self.QEntry.setValidator(QtGui.QIntValidator(1,1000000)) 
        self.QEntry.setText(str(100))
        fig = Figure()
        self.addmpl(fig)
        self.activefig=None
        self.activeDataSet=None
        
    def changefig(self, ):
        item=self.mplfigs.currentItem()
        
        if self.activefig==None:
            pass
        else:
            self.activefig.canvas.mpl_disconnect(self.cid)
        if self.fitSelectedData.isEnabled()==True:
            pass
        else:
            self.fitSelectedData.setEnabled(True)        
        text = item.text()
        self.rmmpl()
        fig=self.data_dict[text].fig
        self.addmpl(fig)
        self.cid = fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.activefig=fig
        self.activeDataSet=self.data_dict[text]
    def adddata(self, name, xyDataClass):
        self.data_dict[name] = xyDataClass
        self.mplfigs.addItem(name)
        

    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, self.mplwindow, coordinates=True)
        self.mplvl.addWidget(self.toolbar)
        self.activefig=fig
    
    def rmmpl(self,):
        self.mplvl.removeWidget(self.canvas)
        self.canvas.close()
        self.mplvl.removeWidget(self.toolbar)
        self.toolbar.close()
#        self.activefig.canvas.mpl_disconnect(self.cid)
    
#This has to be modified for data types other than a ZI data input
    def onSelectFolder(self,):
        self.fileDialog=QtGui.QFileDialog(self)
        folderName=self.fileDialog.getExistingDirectory(self,
        "Choose a folder", homedir, QtGui.QFileDialog.ShowDirsOnly)
        for i in os.listdir(folderName):
            fullpath=folderName + "\\"+ i
            for ii in os.listdir(fullpath):
                if ii[-4:] == ".csv":
                    data = np.genfromtxt(fullpath+ "\\" + ii, delimiter=',')
            xy=xyData(i, data[:,1], data[:,2])
            self.adddata(i, xy)
    def onRenameSelectedData(self,):
        print "Not Implemented"
#Clcik on active MPL window    
    def onclick(self, event):
        print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(event.button, event.x, event.y, event.xdata, event.ydata)
        print self.activeDataSet.find_nearestx(event.xdata)
#gca can get limits of zoomed widow
    def onFit(self,):
        self.disableForFit()
    
    def fitClick(self, event):
        self.saveFit.setEnabled(True)
        self.cancelFit.setEnabled(True)
        self.activefig.canvas.mpl_disconnect(self.cid)
        xi,xf = self.activeDataSet.fig.gca().get_xlim()
        xi, xvi = self.activeDataSet.find_nearestx(xi)
        xf, xvf = self.activeDataSet.find_nearestx(xf)
# General to this point, actual fit can vary below        
        x=self.activeDataSet.xData
        y=self.activeDataSet.yData
        x0 = event.xdata
        y0 = event.ydata        
        Q = int(self.QEntry.text())
        fwhm=x0/Q
        out, params=lpf.lmLorFit(x[xi:xf],y[xi:xf],[x0,y0*fwhm/2*math.pi,fwhm])
        self.activeDataSet.addFit(out, xi,xf, params)
        fig = self.activeDataSet.fits[-1].plotBest()
#        plt.text(2, 0.65,'Q = '+ str(params[3]), fontdict=font)
              
        

    def disableForFit(self,):
        self.toolbar.setEnabled(False)
        self.mplfigs.setEnabled(False)
        self.fitSelectedData.setEnabled(False)
        self.folderSelect.setEnabled(False)
        self.activefig.canvas.mpl_disconnect(self.cid)
        self.cid =self.activefig.canvas.mpl_connect('button_press_event', self.fitClick)

    def enableAfterFit(self,):
        self.toolbar.setEnabled(True)
        self.mplfigs.setEnabled(True)
        self.fitSelectedData.setEnabled(True)
        self.folderSelect.setEnabled(True)
        self.activefig.canvas.mpl_disconnect(self.cid)
        self.cid =self.activefig.canvas.mpl_connect('button_press_event', self.onclick)
    def onSaveFit(self,):
        self.saveFit.setEnabled(False)
        self.cancelFit.setEnabled(False)
        self.enableAfterFit()
    def onCancelFit(self,):
        self.saveFit.setEnabled(False)
        self.cancelFit.setEnabled(False)
        self.activeDataSet.fits.pop()
        self.enableAfterFit()
if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    import numpy as np
 
    app = QtGui.QApplication(sys.argv)
    main = Main()

    main.show()
    sys.exit(app.exec_())
    