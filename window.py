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
        MainWindow.resize(1004, 829)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mplwindow = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow.sizePolicy().hasHeightForWidth())
        self.mplwindow.setSizePolicy(sizePolicy)
        self.mplwindow.setObjectName(_fromUtf8("mplwindow"))
        self.mplvl = QtGui.QVBoxLayout(self.mplwindow)
        self.mplvl.setObjectName(_fromUtf8("mplvl"))
        self.gridLayout.addWidget(self.mplwindow, 0, 0, 1, 1)
        self.cancelFit = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelFit.sizePolicy().hasHeightForWidth())
        self.cancelFit.setSizePolicy(sizePolicy)
        self.cancelFit.setMinimumSize(QtCore.QSize(100, 0))
        self.cancelFit.setObjectName(_fromUtf8("cancelFit"))
        self.gridLayout.addWidget(self.cancelFit, 6, 2, 1, 1)
        self.QLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QLabel.sizePolicy().hasHeightForWidth())
        self.QLabel.setSizePolicy(sizePolicy)
        self.QLabel.setObjectName(_fromUtf8("QLabel"))
        self.gridLayout.addWidget(self.QLabel, 7, 3, 1, 1)
        self.fitSelectedData = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fitSelectedData.sizePolicy().hasHeightForWidth())
        self.fitSelectedData.setSizePolicy(sizePolicy)
        self.fitSelectedData.setObjectName(_fromUtf8("fitSelectedData"))
        self.gridLayout.addWidget(self.fitSelectedData, 9, 2, 1, 1)
        self.saveFit = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveFit.sizePolicy().hasHeightForWidth())
        self.saveFit.setSizePolicy(sizePolicy)
        self.saveFit.setObjectName(_fromUtf8("saveFit"))
        self.gridLayout.addWidget(self.saveFit, 6, 3, 1, 1)
        self.QEntry = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QEntry.sizePolicy().hasHeightForWidth())
        self.QEntry.setSizePolicy(sizePolicy)
        self.QEntry.setInputMethodHints(QtCore.Qt.ImhNone)
        self.QEntry.setObjectName(_fromUtf8("QEntry"))
        self.gridLayout.addWidget(self.QEntry, 7, 2, 1, 1)
        self.folderSelect = QtGui.QPushButton(self.centralwidget)
        self.folderSelect.setObjectName(_fromUtf8("folderSelect"))
        self.gridLayout.addWidget(self.folderSelect, 10, 0, 1, 1)
        self.selectPandasDB = QtGui.QPushButton(self.centralwidget)
        self.selectPandasDB.setObjectName(_fromUtf8("selectPandasDB"))
        self.gridLayout.addWidget(self.selectPandasDB, 10, 2, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(-10, 30, 291, 201))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 0, 251, 181))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.rowEdit = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.rowEdit.setObjectName(_fromUtf8("rowEdit"))
        self.gridLayout_2.addWidget(self.rowEdit, 3, 0, 1, 1)
        self.widthLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.widthLabel.setObjectName(_fromUtf8("widthLabel"))
        self.gridLayout_2.addWidget(self.widthLabel, 1, 1, 1, 1)
        self.powerType = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.powerType.setObjectName(_fromUtf8("powerType"))
        self.gridLayout_2.addWidget(self.powerType, 6, 0, 1, 1)
        self.deviceTypeLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.deviceTypeLabel.setObjectName(_fromUtf8("deviceTypeLabel"))
        self.gridLayout_2.addWidget(self.deviceTypeLabel, 5, 1, 1, 1)
        self.rowLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.rowLabel.setObjectName(_fromUtf8("rowLabel"))
        self.gridLayout_2.addWidget(self.rowLabel, 3, 1, 1, 1)
        self.columnEdit = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.columnEdit.setObjectName(_fromUtf8("columnEdit"))
        self.gridLayout_2.addWidget(self.columnEdit, 2, 0, 1, 1)
        self.columnLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.columnLabel.setObjectName(_fromUtf8("columnLabel"))
        self.gridLayout_2.addWidget(self.columnLabel, 2, 1, 1, 1)
        self.widthEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.widthEdit.setObjectName(_fromUtf8("widthEdit"))
        self.gridLayout_2.addWidget(self.widthEdit, 1, 0, 1, 1)
        self.chipLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.chipLabel.setObjectName(_fromUtf8("chipLabel"))
        self.gridLayout_2.addWidget(self.chipLabel, 0, 1, 1, 1)
        self.deviceType = QtGui.QComboBox(self.verticalLayoutWidget)
        self.deviceType.setObjectName(_fromUtf8("deviceType"))
        self.deviceType.addItem(_fromUtf8(""))
        self.deviceType.addItem(_fromUtf8(""))
        self.deviceType.addItem(_fromUtf8(""))
        self.deviceType.addItem(_fromUtf8(""))
        self.deviceType.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.deviceType, 5, 0, 1, 1)
        self.chipEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.chipEdit.setText(_fromUtf8(""))
        self.chipEdit.setObjectName(_fromUtf8("chipEdit"))
        self.gridLayout_2.addWidget(self.chipEdit, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 6, 1, 1, 1)
        self.powerValue = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.powerValue.setObjectName(_fromUtf8("powerValue"))
        self.gridLayout_2.addWidget(self.powerValue, 7, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 7, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.fitBox = QtGui.QGroupBox(self.groupBox_2)
        self.fitBox.setGeometry(QtCore.QRect(10, 250, 211, 131))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fitBox.sizePolicy().hasHeightForWidth())
        self.fitBox.setSizePolicy(sizePolicy)
        self.fitBox.setObjectName(_fromUtf8("fitBox"))
        self.mplfigs = QtGui.QListWidget(self.groupBox_2)
        self.mplfigs.setGeometry(QtCore.QRect(10, 460, 200, 161))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplfigs.sizePolicy().hasHeightForWidth())
        self.mplfigs.setSizePolicy(sizePolicy)
        self.mplfigs.setMaximumSize(QtCore.QSize(200, 16777215))
        self.mplfigs.setObjectName(_fromUtf8("mplfigs"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 270, 201, 181))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.fNumber = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.fNumber.setObjectName(_fromUtf8("fNumber"))
        self.gridLayout_3.addWidget(self.fNumber, 2, 0, 1, 1)
        self.fLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.fLabel.setObjectName(_fromUtf8("fLabel"))
        self.gridLayout_3.addWidget(self.fLabel, 2, 2, 1, 1)
        self.selectBadFit = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.selectBadFit.setObjectName(_fromUtf8("selectBadFit"))
        self.gridLayout_3.addWidget(self.selectBadFit, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 4, 2, 1, 1)
        self.degeneracySelect = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.degeneracySelect.setObjectName(_fromUtf8("degeneracySelect"))
        self.degeneracySelect.addItem(_fromUtf8(""))
        self.degeneracySelect.addItem(_fromUtf8(""))
        self.degeneracySelect.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.degeneracySelect, 4, 0, 1, 1)
        self.noteLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.noteLabel.setObjectName(_fromUtf8("noteLabel"))
        self.gridLayout_3.addWidget(self.noteLabel, 5, 2, 1, 1)
        self.fitNotes = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.fitNotes.setObjectName(_fromUtf8("fitNotes"))
        self.gridLayout_3.addWidget(self.fitNotes, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.cancelFit.setText(_translate("MainWindow", "Cancel Fit", None))
        self.QLabel.setText(_translate("MainWindow", "Expected Q", None))
        self.fitSelectedData.setText(_translate("MainWindow", "Fit Selected Data", None))
        self.saveFit.setText(_translate("MainWindow", "Save Fit", None))
        self.folderSelect.setText(_translate("MainWindow", "Load ZI XY Data Sets from Folder", None))
        self.selectPandasDB.setText(_translate("MainWindow", "PushButton", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox", None))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.widthLabel.setText(_translate("MainWindow", "Sample Width", None))
        self.deviceTypeLabel.setText(_translate("MainWindow", "Device Type", None))
        self.rowLabel.setText(_translate("MainWindow", "Sample Row", None))
        self.columnLabel.setText(_translate("MainWindow", "Sample Column", None))
        self.widthEdit.setText(_translate("MainWindow", "Sample Width", None))
        self.chipLabel.setText(_translate("MainWindow", "Chip Label", None))
        self.deviceType.setItemText(0, _translate("MainWindow", "Cross", None))
        self.deviceType.setItemText(1, _translate("MainWindow", "Drumhead", None))
        self.deviceType.setItemText(2, _translate("MainWindow", "Beam", None))
        self.deviceType.setItemText(3, _translate("MainWindow", "H", None))
        self.deviceType.setItemText(4, _translate("MainWindow", "Other", None))
        self.label_2.setText(_translate("MainWindow", "Power Type", None))
        self.label_3.setText(_translate("MainWindow", "Power", None))
        self.fitBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.fLabel.setText(_translate("MainWindow", "f number", None))
        self.selectBadFit.setText(_translate("MainWindow", "Bad Fit", None))
        self.label.setText(_translate("MainWindow", "Mode Type", None))
        self.degeneracySelect.setItemText(0, _translate("MainWindow", "Degenerate", None))
        self.degeneracySelect.setItemText(1, _translate("MainWindow", "f_lower", None))
        self.degeneracySelect.setItemText(2, _translate("MainWindow", "f_higher", None))
        self.noteLabel.setText(_translate("MainWindow", "Notes", None))

