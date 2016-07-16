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
Ui_MainFittingWindow, QMainFittingWindow = loadUiType('fittingwindow.ui')
#homedir="Z:\Group\Projects\FIBed Graphene Drumhead Resonators\Measurement Data\Lock-In Sweeps"
homedir=os.path.expanduser('~')
#homedir='Z:\Group\Projects\FIBed Graphene Drumhead Resonators\Measurement Data\Lock-In Sweeps\2016\03\15'
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
#data_dict stores all loaded data sets
        self.data_dict = {}
        self.mplfigs.itemSelectionChanged.connect(self.changefig)
        self.folderSelect.clicked.connect(self.onSelectFolder)
        self.saveFit.clicked.connect(self.onSaveFit)
        self.cancelFit.clicked.connect(self.onCancelFit)
        self.fitSelectedData.clicked.connect(self.onFit)
        self.fitSelectedData.setEnabled(False)
        self.selectPandasDB.clicked.connect(self.onSelectPandasDB)
        self.QEntry.setValidator(QtGui.QIntValidator(1,1000000)) 
        self.widthEdit.setValidator(QtGui.QIntValidator(1,10000))
        self.widthEdit.setText(str(0))
        self.powerType.setText(str(0))
        self.powerValue.setText(str(0))
        self.QEntry.setText(str(100))
        self.fNumber.setValue(1)
        self.degeneracySelect.setCurrentIndex(0)
        fig = Figure()
        self.addmpl(fig)
        self.activefig=None
        self.activeDataSet=None
        self.fittingWindow = None
        self.df=pd.DataFrame()
        self.testdf=pd.DataFrame()
    
    def onSelectPandasDB(self,):
        """Select a folder, the selected folder will be parsed for sub-folders.
        Each of these subfolders will be turned into a xyData class which is 
        then stored in main with the adddata command"""
        fileDialog=QtGui.QFileDialog(self)
        fileName=fileDialog.getSaveFileName(self,
        "Choose a pandasDB", homedir, filter ="csv (*.csv)")
        self.pathtopandas=fileName
        self.chipEdit.setText(self.pathtopandas)
        print self.pathtopandas
    def onSelectFolder(self,):
        """Select a folder, the selected folder will be parsed for sub-folders.
        Each of these subfolders will be turned into a xyData class which is 
        then stored in main with the adddata command"""
        self.fileDialog=QtGui.QFileDialog(self)
        folderName=self.fileDialog.getExistingDirectory(self,
        "Choose a folder", homedir, QtGui.QFileDialog.ShowDirsOnly)
        for i in os.listdir(folderName):
            for ii in os.listdir(os.path.join(folderName,i)):
                if ii[-4:] == ".csv":            
                    self.adddata(i, xyData(os.path.join(folderName,i)))        
                                    
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
        try:
            self.widthEdit.setText(str(self.data_dict[text].deviceWid))           
        except ValueError:
            pass
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        try:
            self.rowEdit.setValue(int(self.data_dict[text].deviceRow))          
        except ValueError:
            pass
        try:
            self.powerType.setText(str(self.data_dict[text].laserPowerType))          
        except ValueError:
            pass
        try:
            self.powerValue.setText(str(self.data_dict[text].laserPower))          
        except ValueError:
            pass
        try:
            self.columnEdit.setValue(int(self.data_dict[text].deviceCol))          
        except ValueError:
            pass
        try:
            ind = self.deviceType.findText(str(self.data_dict[text].deviceType).strip())        
            self.deviceType.setCurrentIndex(ind)          
        except ValueError:
            pass           
        self.activefig=fig
        self.activeDataSet=self.data_dict[text]

    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, self.mplwindow, coordinates=True)
        self.mplvl.addWidget(self.toolbar)
    
    def rmmpl(self,):
        self.mplvl.removeWidget(self.canvas)
        self.canvas.close()
        self.mplvl.removeWidget(self.toolbar)
        self.toolbar.close()
#        self.activefig.canvas.mpl_disconnect(self.cid)
    
#This has to be modified for data types other than a ZI data input
    def adddata(self, name, xyDataClass):
        self.data_dict[name] = xyDataClass
        self.mplfigs.addItem(name)
    
#Clcik on active MPL window    
    def onclick(self, event):
#        print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(event.button, event.x, event.y, event.xdata, event.ydata)
        print self.activeDataSet.find_nearestx(event.xdata)
#gca can get limits of zoomed widow
    def onFit(self,):
        self.disableForFit()
    
    def fitClick(self, event):
        self.cancelFit.setEnabled(True)
        print 'clicked'
        self.activefig.canvas.mpl_disconnect(self.cid)
        xi,xf = self.activeDataSet.fig.gca().get_xlim()
        xi, xvi = self.activeDataSet.find_nearestx(xi)
        xf, xvf = self.activeDataSet.find_nearestx(xf)
# General to this point, actual fit can vary below        
        x0 = event.xdata
        y0 = event.ydata        
        Q = float(self.QEntry.text())
        sigma=1/(2*Q)
        print xi,xf, [x0,y0,sigma]
        ip=[x0,y0,sigma]
        print self.activeDataSet
        out, params, outp, self.paramsp, dout = self.activeDataSet.fitDataSelection(xi,xf,ip)
        self.outfit=out
        self.currpars=params
        self.fitfig=Figure()
        ax=self.fitfig.add_subplot(1,1,1)
        axt=ax.twinx()
        ax.plot(self.activeDataSet.data.f[xi:xf+1], out.best_fit)
        axt.plot(dout[0], outp.best_fit, 'g')
        ax.plot(self.activeDataSet.data.f[xi:xf+1], self.activeDataSet.data.r[xi:xf+1], 'ro')
        axt.plot(dout[0], dout[1], 'go')
        idx=min(range(len(self.activeDataSet.data.f)), key=lambda x: abs(self.activeDataSet.data.f[x]-params[0]))
        ax.annotate('Q = '+ str(params[3]) + '\n' + 'w_0 = '+ str(params[0]), xy=(params[0],self.activeDataSet.data.r[idx]), textcoords = 'data', xycoords='data')
        self.rmmpl()
        self.addmpl(self.fitfig)
        self.activeFitParams = params
        self.saveFit.setEnabled(True)

#        plt.text(2, 0.65,'Q = '+ str(params[3]), fontdict=font)

    def disableForFit(self,):
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
        self.rmmpl()
        self.addmpl(self.activefig)
        self.cid =self.activefig.canvas.mpl_connect('button_press_event', self.onclick)
    def onSaveFit(self,):
        self.w0=self.activeFitParams[0]
        self.A=self.activeFitParams[1]
        self.Q=self.activeFitParams[3]
        self.lineInt=self.activeFitParams[4]
        self.lineSlope=self.activeFitParams[5]
        self.saveFit.setEnabled(False)
        self.cancelFit.setEnabled(False)
        curridx=self.mplfigs.currentItem().text()+'_'+str(self.fNumber.value())+'_' + self.degeneracySelect.currentText()        
        newrow=self.prepareDFRow(curridx)
        try:        
            master=pd.read_csv(self.pathtopandas, index_col=0)
            if curridx not in self.testdf.index:
                newmaster=master.append(newrow)
                print newmaster                
                newmaster.to_csv(self.pathtopandas[:-4]+'temp.csv')
                os.remove(self.pathtopandas)
                os.rename(self.pathtopandas[:-4]+'temp.csv',self.pathtopandas)
                
            else:
                print 'repeated fit'
        except IOError:
            newrow.to_csv(self.pathtopandas)
        self.enableAfterFit()
    def prepareDFRow(self, idx):
        df = pd.DataFrame({'Run Name' : self.mplfigs.currentItem().text(), 'Device Name' : self.chipEdit.text(), 'Row Number' : \
            self.rowEdit.value(), 'Column Number' : self.columnEdit.value(),\
            'Device Type' : self.deviceType.currentText(), 'Device Width' : \
                self.widthEdit.text(), 'Mode Order' : self.fNumber.value(), \
                'Mode Type': self.degeneracySelect.currentText(), 'Frequency' : self.w0, 'Amplitude' : self.A, \
                'Q' : self.Q, 'Bad Fit' : self.selectBadFit.checkState(), 'Power Measurement Type' : self.powerType.text(), 'Power (uW)' : self.powerValue.text(),\
                'Fit Notes' : self.fitNotes.text(), 'Date' : self.activeDataSet.date, 'Intercept': self.lineInt, 'Slope':self.lineSlope, 'w0p': self.paramsp[0],'Qp': self.paramsp[1],'pm': self.paramsp[2],'pb': self.paramsp[3]}, index=[idx] )
        print df
        return df
    def onCancelFit(self,):
        self.saveFit.setEnabled(False)
        self.cancelFit.setEnabled(False)
        self.enableAfterFit()
if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    import numpy as np
 
    app = QtGui.QApplication(sys.argv)
    main = Main()

    main.show()
    sys.exit(app.exec_())
    