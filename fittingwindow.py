# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fittingwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(916, 751)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.saveFit = QtGui.QPushButton(self.centralwidget)
        self.saveFit.setObjectName(_fromUtf8("saveFit"))
        self.gridLayout.addWidget(self.saveFit, 2, 0, 1, 1)
        self.cancelFit = QtGui.QPushButton(self.centralwidget)
        self.cancelFit.setObjectName(_fromUtf8("cancelFit"))
        self.gridLayout.addWidget(self.cancelFit, 2, 1, 1, 1)
        self.mplFitWindow = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplFitWindow.sizePolicy().hasHeightForWidth())
        self.mplFitWindow.setSizePolicy(sizePolicy)
        self.mplFitWindow.setObjectName(_fromUtf8("mplFitWindow"))
        self.gridLayout.addWidget(self.mplFitWindow, 0, 0, 2, 1)
        self.displayBox = QtGui.QGroupBox(self.centralwidget)
        self.displayBox.setObjectName(_fromUtf8("displayBox"))
        self.selectDegenerate = QtGui.QRadioButton(self.displayBox)
        self.selectDegenerate.setGeometry(QtCore.QRect(70, 80, 82, 17))
        self.selectDegenerate.setObjectName(_fromUtf8("selectDegenerate"))
        self.selectFLower = QtGui.QRadioButton(self.displayBox)
        self.selectFLower.setGeometry(QtCore.QRect(70, 100, 82, 17))
        self.selectFLower.setObjectName(_fromUtf8("selectFLower"))
        self.selectFHigher = QtGui.QRadioButton(self.displayBox)
        self.selectFHigher.setGeometry(QtCore.QRect(70, 120, 82, 17))
        self.selectFHigher.setObjectName(_fromUtf8("selectFHigher"))
        self.fNumber = QtGui.QSpinBox(self.displayBox)
        self.fNumber.setGeometry(QtCore.QRect(70, 50, 31, 20))
        self.fNumber.setObjectName(_fromUtf8("fNumber"))
        self.fLabel = QtGui.QLabel(self.displayBox)
        self.fLabel.setGeometry(QtCore.QRect(100, 50, 46, 13))
        self.fLabel.setObjectName(_fromUtf8("fLabel"))
        self.fitNotes = QtGui.QTextEdit(self.displayBox)
        self.fitNotes.setGeometry(QtCore.QRect(10, 290, 311, 171))
        self.fitNotes.setObjectName(_fromUtf8("fitNotes"))
        self.sleectBadFit = QtGui.QCheckBox(self.displayBox)
        self.sleectBadFit.setGeometry(QtCore.QRect(70, 140, 70, 17))
        self.sleectBadFit.setObjectName(_fromUtf8("sleectBadFit"))
        self.noteLabel = QtGui.QLabel(self.displayBox)
        self.noteLabel.setGeometry(QtCore.QRect(10, 270, 46, 13))
        self.noteLabel.setObjectName(_fromUtf8("noteLabel"))
        self.rowDisplay = QtGui.QLineEdit(self.displayBox)
        self.rowDisplay.setGeometry(QtCore.QRect(70, 160, 113, 20))
        self.rowDisplay.setObjectName(_fromUtf8("rowDisplay"))
        self.rowLabel = QtGui.QLabel(self.displayBox)
        self.rowLabel.setGeometry(QtCore.QRect(190, 160, 61, 16))
        self.rowLabel.setObjectName(_fromUtf8("rowLabel"))
        self.columnDisplay = QtGui.QLineEdit(self.displayBox)
        self.columnDisplay.setGeometry(QtCore.QRect(70, 180, 113, 20))
        self.columnDisplay.setObjectName(_fromUtf8("columnDisplay"))
        self.columnLabel = QtGui.QLabel(self.displayBox)
        self.columnLabel.setGeometry(QtCore.QRect(190, 180, 81, 16))
        self.columnLabel.setObjectName(_fromUtf8("columnLabel"))
        self.widthDisplay = QtGui.QLineEdit(self.displayBox)
        self.widthDisplay.setGeometry(QtCore.QRect(70, 200, 113, 20))
        self.widthDisplay.setObjectName(_fromUtf8("widthDisplay"))
        self.widthLabel = QtGui.QLabel(self.displayBox)
        self.widthLabel.setGeometry(QtCore.QRect(190, 200, 71, 16))
        self.widthLabel.setObjectName(_fromUtf8("widthLabel"))
        self.gridLayout.addWidget(self.displayBox, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.saveFit.setText(_translate("MainWindow", "Save Fit", None))
        self.cancelFit.setText(_translate("MainWindow", "Cancel Fit", None))
        self.displayBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.selectDegenerate.setText(_translate("MainWindow", "Degenerate", None))
        self.selectFLower.setText(_translate("MainWindow", "f_lower", None))
        self.selectFHigher.setText(_translate("MainWindow", "f_higher", None))
        self.fLabel.setText(_translate("MainWindow", "f number", None))
        self.sleectBadFit.setText(_translate("MainWindow", "Bad Fit", None))
        self.noteLabel.setText(_translate("MainWindow", "Notes", None))
        self.rowLabel.setText(_translate("MainWindow", "Sample Row", None))
        self.columnDisplay.setText(_translate("MainWindow", "Sample Colu", None))
        self.columnLabel.setText(_translate("MainWindow", "Sample Column", None))
        self.widthDisplay.setText(_translate("MainWindow", "Sample Width", None))
        self.widthLabel.setText(_translate("MainWindow", "Sample Width", None))

