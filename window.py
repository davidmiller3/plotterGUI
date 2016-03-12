# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
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
        MainWindow.resize(957, 725)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mplwindow = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow.sizePolicy().hasHeightForWidth())
        self.mplwindow.setSizePolicy(sizePolicy)
        self.mplwindow.setObjectName(_fromUtf8("mplwindow"))
        self.mplvl = QtGui.QVBoxLayout(self.mplwindow)
        self.mplvl.setObjectName(_fromUtf8("mplvl"))
        self.gridLayout.addWidget(self.mplwindow, 0, 0, 1, 1)
        self.folderSelect = QtGui.QPushButton(self.centralwidget)
        self.folderSelect.setObjectName(_fromUtf8("folderSelect"))
        self.gridLayout.addWidget(self.folderSelect, 2, 0, 1, 1)
        self.renameSelectedData = QtGui.QPushButton(self.centralwidget)
        self.renameSelectedData.setObjectName(_fromUtf8("renameSelectedData"))
        self.gridLayout.addWidget(self.renameSelectedData, 4, 0, 1, 1)
        self.mplfigs = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplfigs.sizePolicy().hasHeightForWidth())
        self.mplfigs.setSizePolicy(sizePolicy)
        self.mplfigs.setMaximumSize(QtCore.QSize(200, 16777215))
        self.mplfigs.setObjectName(_fromUtf8("mplfigs"))
        self.gridLayout.addWidget(self.mplfigs, 1, 1, 1, 1)
        self.QEntry = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QEntry.sizePolicy().hasHeightForWidth())
        self.QEntry.setSizePolicy(sizePolicy)
        self.QEntry.setInputMethodHints(QtCore.Qt.ImhNone)
        self.QEntry.setObjectName(_fromUtf8("QEntry"))
        self.gridLayout.addWidget(self.QEntry, 4, 1, 1, 1)
        self.saveFit = QtGui.QPushButton(self.centralwidget)
        self.saveFit.setObjectName(_fromUtf8("saveFit"))
        self.gridLayout.addWidget(self.saveFit, 7, 0, 1, 1)
        self.fitSelectedData = QtGui.QPushButton(self.centralwidget)
        self.fitSelectedData.setObjectName(_fromUtf8("fitSelectedData"))
        self.gridLayout.addWidget(self.fitSelectedData, 2, 1, 1, 1)
        self.cancelFit = QtGui.QPushButton(self.centralwidget)
        self.cancelFit.setObjectName(_fromUtf8("cancelFit"))
        self.gridLayout.addWidget(self.cancelFit, 5, 1, 1, 1)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 1, 2, 1, 1)
        self.showAllFits = QtGui.QPushButton(self.centralwidget)
        self.showAllFits.setObjectName(_fromUtf8("showAllFits"))
        self.gridLayout.addWidget(self.showAllFits, 7, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 957, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.folderSelect.setText(_translate("MainWindow", "Load ZI XY Data Sets from Folder", None))
        self.renameSelectedData.setText(_translate("MainWindow", "Rename", None))
        self.saveFit.setText(_translate("MainWindow", "Save Fit", None))
        self.fitSelectedData.setText(_translate("MainWindow", "Fit Selected Data", None))
        self.cancelFit.setText(_translate("MainWindow", "Cancel Fit", None))
        self.showAllFits.setText(_translate("MainWindow", "Plot All Fits", None))

