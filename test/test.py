# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:46:28 2016

@author: David
"""
from PyQt4.uic import loadUiType
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import math

Ui_MainWindow1, QMainWindow1 = loadUiType('testwindow1.ui')
Ui_MainWindow2, QMainWindow2 = loadUiType('testwindow2.ui')

#homedir="Z:\Group\Projects\FIBed Graphene Drumhead Resonators\Measurement Data\Lock-In Sweeps"
#homedir=os.path.expanduser('~')
homedir='smb://cas-fs1/Material-Science-Institute/Aleman-Lab/Group/Projects/FIBed Graphene Drumhead Resonators/Measurement Data/Lock-In Sweeps/3_12_16/12'
class Main1(QMainWindow1, Ui_MainWindow1):
    def __init__(self, ):
        super(Main1, self).__init__()
        self.setupUi(self)
#data_dict stores all loaded data sets
        self.createButton.clicked.connect(self.onConnect)
        self.window2 = None
    def onConnect(self):        
        if self.window2 is None:
            self.window2 = Main2()
        self.window2.show()
class Main2(QMainWindow2, Ui_MainWindow2):
    def __init__(self, ):
        super(Main2, self).__init__()
        self.setupUi(self)
#data_dict stores all loaded data sets
        self.closeButton.clicked.connect(self.onClose)
    def onClose(self):
        self.close()
        
if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    import numpy as np
 
    app = QtGui.QApplication(sys.argv)
    main = Main1()

    main.show()
    sys.exit(app.exec_())