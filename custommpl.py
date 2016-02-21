# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 17:21:56 2016

@author: David
"""
from PyQt4.uic import loadUiType
import os
from dataClass import xyData
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

Ui_MainWindow, QMainWindow = loadUiType('window.ui')



class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.data_dict = {}
        self.mplfigs.itemClicked.connect(self.changefig)
        self.folderSelect.clicked.connect(self.onSelectFolder)
        fig = Figure()
        self.addmpl(fig)
        self.activefig=None
        
    def changefig(self, item):
        if self.activefig==None:
            pass
        else:
            self.activefig.canvas.mpl_disconnect(self.cid)
        text = item.text()
        self.rmmpl()
        fig=self.data_dict[text].fig
        self.addmpl(fig)
        self.cid = fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.activefig=fig
        
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
    
    def onSelectFolder(self,):
        self.fileDialog=QtGui.QFileDialog(self)
        self.folderName=self.fileDialog.getExistingDirectory()
        print 1
        for i in os.listdir(self.folderName):
            x=np.random(5)
            y=np.random(5)
            print i
            self.adddata(i, xyData(i, x, y))

#Clcik on active MPL window    
    def onclick(self, event):
        print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(event.button, event.x, event.y, event.xdata, event.ydata)

    
if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    import numpy as np
 
    app = QtGui.QApplication(sys.argv)
    main = Main()

    main.show()
    sys.exit(app.exec_())
    