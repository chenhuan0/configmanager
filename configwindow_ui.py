# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configwindow.ui'
#
# Created: Sun Dec 22 18:54:44 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_configwindow(object):
    def setupUi(self, configwindow):
        configwindow.setObjectName(_fromUtf8("configwindow"))
        configwindow.resize(655, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        configwindow.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(configwindow)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_21 = QtGui.QVBoxLayout()
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(configwindow)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.acRadioButton = QtGui.QRadioButton(configwindow)
        self.acRadioButton.setChecked(True)
        self.acRadioButton.setObjectName(_fromUtf8("acRadioButton"))
        self.horizontalLayout.addWidget(self.acRadioButton)
        self.batteryRadioButton = QtGui.QRadioButton(configwindow)
        self.batteryRadioButton.setObjectName(_fromUtf8("batteryRadioButton"))
        self.horizontalLayout.addWidget(self.batteryRadioButton)
        self.horizontalLayout_18.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem)
        self.verticalLayout_21.addLayout(self.horizontalLayout_18)
        self.groupBox = QtGui.QGroupBox(configwindow)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.adapterIPv4Addr = QtGui.QLineEdit(self.groupBox)
        self.adapterIPv4Addr.setObjectName(_fromUtf8("adapterIPv4Addr"))
        self.verticalLayout_3.addWidget(self.adapterIPv4Addr)
        self.adapterIPv4Port = QtGui.QLineEdit(self.groupBox)
        self.adapterIPv4Port.setObjectName(_fromUtf8("adapterIPv4Port"))
        self.verticalLayout_3.addWidget(self.adapterIPv4Port)
        self.adapterIPv6Addr = QtGui.QLineEdit(self.groupBox)
        self.adapterIPv6Addr.setObjectName(_fromUtf8("adapterIPv6Addr"))
        self.verticalLayout_3.addWidget(self.adapterIPv6Addr)
        self.adapterIPv6Port = QtGui.QLineEdit(self.groupBox)
        self.adapterIPv6Port.setObjectName(_fromUtf8("adapterIPv6Port"))
        self.verticalLayout_3.addWidget(self.adapterIPv6Port)
        self.localIPv4Port = QtGui.QLineEdit(self.groupBox)
        self.localIPv4Port.setObjectName(_fromUtf8("localIPv4Port"))
        self.verticalLayout_3.addWidget(self.localIPv4Port)
        self.localIPv6Port = QtGui.QLineEdit(self.groupBox)
        self.localIPv6Port.setObjectName(_fromUtf8("localIPv6Port"))
        self.verticalLayout_3.addWidget(self.localIPv6Port)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)
        self.verticalLayout_21.addWidget(self.groupBox)
        self.gridLayout_2.addLayout(self.verticalLayout_21, 0, 0, 1, 1)
        self.verticalLayout_20 = QtGui.QVBoxLayout()
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.groupBox_5 = QtGui.QGroupBox(configwindow)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_13 = QtGui.QLabel(self.groupBox_5)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_10.addWidget(self.label_13)
        self.label_14 = QtGui.QLabel(self.groupBox_5)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_10.addWidget(self.label_14)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.cdmaUsername = QtGui.QLineEdit(self.groupBox_5)
        self.cdmaUsername.setObjectName(_fromUtf8("cdmaUsername"))
        self.verticalLayout_9.addWidget(self.cdmaUsername)
        self.cdmaPassword = QtGui.QLineEdit(self.groupBox_5)
        self.cdmaPassword.setText(_fromUtf8(""))
        self.cdmaPassword.setObjectName(_fromUtf8("cdmaPassword"))
        self.verticalLayout_9.addWidget(self.cdmaPassword)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_5)
        self.verticalLayout_20.addWidget(self.groupBox_5)
        self.groupBox_3 = QtGui.QGroupBox(configwindow)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_6.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_6.addWidget(self.label_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.segmac = QtGui.QLineEdit(self.groupBox_3)
        self.segmac.setObjectName(_fromUtf8("segmac"))
        self.verticalLayout_5.addWidget(self.segmac)
        self.scmac = QtGui.QLineEdit(self.groupBox_3)
        self.scmac.setText(_fromUtf8(""))
        self.scmac.setObjectName(_fromUtf8("scmac"))
        self.verticalLayout_5.addWidget(self.scmac)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_3)
        self.verticalLayout_20.addWidget(self.groupBox_3)
        self.gridLayout_2.addLayout(self.verticalLayout_20, 0, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(configwindow)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_18 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.AlertSwitc = QtGui.QLabel(self.groupBox_2)
        self.AlertSwitc.setObjectName(_fromUtf8("AlertSwitc"))
        self.horizontalLayout_6.addWidget(self.AlertSwitc)
        self.alertOn = QtGui.QRadioButton(self.groupBox_2)
        self.alertOn.setChecked(True)
        self.alertOn.setObjectName(_fromUtf8("alertOn"))
        self.horizontalLayout_6.addWidget(self.alertOn)
        self.alertOff = QtGui.QRadioButton(self.groupBox_2)
        self.alertOff.setObjectName(_fromUtf8("alertOff"))
        self.horizontalLayout_6.addWidget(self.alertOff)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_17.addLayout(self.horizontalLayout_10)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_25 = QtGui.QLabel(self.groupBox_2)
        self.label_25.setText(_fromUtf8(""))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout.addWidget(self.label_25, 0, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.groupBox_2)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 0, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.groupBox_2)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout.addWidget(self.label_19, 0, 2, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox_2)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout.addWidget(self.label_20, 1, 0, 1, 1)
        self.airTempUpper = QtGui.QLineEdit(self.groupBox_2)
        self.airTempUpper.setObjectName(_fromUtf8("airTempUpper"))
        self.gridLayout.addWidget(self.airTempUpper, 1, 1, 1, 1)
        self.airTempLower = QtGui.QLineEdit(self.groupBox_2)
        self.airTempLower.setObjectName(_fromUtf8("airTempLower"))
        self.gridLayout.addWidget(self.airTempLower, 1, 2, 1, 1)
        self.label_21 = QtGui.QLabel(self.groupBox_2)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout.addWidget(self.label_21, 2, 0, 1, 1)
        self.airHumiUpper = QtGui.QLineEdit(self.groupBox_2)
        self.airHumiUpper.setObjectName(_fromUtf8("airHumiUpper"))
        self.gridLayout.addWidget(self.airHumiUpper, 2, 1, 1, 1)
        self.airHumiLower = QtGui.QLineEdit(self.groupBox_2)
        self.airHumiLower.setObjectName(_fromUtf8("airHumiLower"))
        self.gridLayout.addWidget(self.airHumiLower, 2, 2, 1, 1)
        self.label_27 = QtGui.QLabel(self.groupBox_2)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout.addWidget(self.label_27, 3, 0, 1, 1)
        self.earthTempUpper = QtGui.QLineEdit(self.groupBox_2)
        self.earthTempUpper.setObjectName(_fromUtf8("earthTempUpper"))
        self.gridLayout.addWidget(self.earthTempUpper, 3, 1, 1, 1)
        self.earthTempLower = QtGui.QLineEdit(self.groupBox_2)
        self.earthTempLower.setObjectName(_fromUtf8("earthTempLower"))
        self.gridLayout.addWidget(self.earthTempLower, 3, 2, 1, 1)
        self.label_22 = QtGui.QLabel(self.groupBox_2)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout.addWidget(self.label_22, 4, 0, 1, 1)
        self.earthHumiUpper = QtGui.QLineEdit(self.groupBox_2)
        self.earthHumiUpper.setObjectName(_fromUtf8("earthHumiUpper"))
        self.gridLayout.addWidget(self.earthHumiUpper, 4, 1, 1, 1)
        self.earthHumiLower = QtGui.QLineEdit(self.groupBox_2)
        self.earthHumiLower.setObjectName(_fromUtf8("earthHumiLower"))
        self.gridLayout.addWidget(self.earthHumiLower, 4, 2, 1, 1)
        self.label_24 = QtGui.QLabel(self.groupBox_2)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout.addWidget(self.label_24, 5, 0, 1, 1)
        self.co2Upper = QtGui.QLineEdit(self.groupBox_2)
        self.co2Upper.setObjectName(_fromUtf8("co2Upper"))
        self.gridLayout.addWidget(self.co2Upper, 5, 1, 1, 1)
        self.co2Lower = QtGui.QLineEdit(self.groupBox_2)
        self.co2Lower.setObjectName(_fromUtf8("co2Lower"))
        self.gridLayout.addWidget(self.co2Lower, 5, 2, 1, 1)
        self.label_23 = QtGui.QLabel(self.groupBox_2)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout.addWidget(self.label_23, 6, 0, 1, 1)
        self.illumUpper = QtGui.QLineEdit(self.groupBox_2)
        self.illumUpper.setObjectName(_fromUtf8("illumUpper"))
        self.gridLayout.addWidget(self.illumUpper, 6, 1, 1, 1)
        self.illumLower = QtGui.QLineEdit(self.groupBox_2)
        self.illumLower.setObjectName(_fromUtf8("illumLower"))
        self.gridLayout.addWidget(self.illumLower, 6, 2, 1, 1)
        self.verticalLayout_17.addLayout(self.gridLayout)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_16.addWidget(self.label_15)
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_16.addWidget(self.label_16)
        self.label_17 = QtGui.QLabel(self.groupBox_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_16.addWidget(self.label_17)
        self.horizontalLayout_15.addLayout(self.verticalLayout_16)
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.phoneNum1 = QtGui.QLineEdit(self.groupBox_2)
        self.phoneNum1.setText(_fromUtf8(""))
        self.phoneNum1.setObjectName(_fromUtf8("phoneNum1"))
        self.verticalLayout_15.addWidget(self.phoneNum1)
        self.phoneNum2 = QtGui.QLineEdit(self.groupBox_2)
        self.phoneNum2.setText(_fromUtf8(""))
        self.phoneNum2.setObjectName(_fromUtf8("phoneNum2"))
        self.verticalLayout_15.addWidget(self.phoneNum2)
        self.phoneNum3 = QtGui.QLineEdit(self.groupBox_2)
        self.phoneNum3.setText(_fromUtf8(""))
        self.phoneNum3.setObjectName(_fromUtf8("phoneNum3"))
        self.verticalLayout_15.addWidget(self.phoneNum3)
        self.horizontalLayout_15.addLayout(self.verticalLayout_15)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_15)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem2)
        self.verticalLayout_17.addLayout(self.horizontalLayout_16)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.groupBox_4 = QtGui.QGroupBox(configwindow)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_8.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_8.addWidget(self.label_11)
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_8.addWidget(self.label_12)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.uploadPeriod = QtGui.QLineEdit(self.groupBox_4)
        self.uploadPeriod.setObjectName(_fromUtf8("uploadPeriod"))
        self.verticalLayout_7.addWidget(self.uploadPeriod)
        self.collectPeriod = QtGui.QLineEdit(self.groupBox_4)
        self.collectPeriod.setEnabled(False)
        self.collectPeriod.setObjectName(_fromUtf8("collectPeriod"))
        self.verticalLayout_7.addWidget(self.collectPeriod)
        self.collectTime = QtGui.QLineEdit(self.groupBox_4)
        self.collectTime.setEnabled(False)
        self.collectTime.setObjectName(_fromUtf8("collectTime"))
        self.verticalLayout_7.addWidget(self.collectTime)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_4)
        self.verticalLayout_14.addWidget(self.groupBox_4)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        spacerItem3 = QtGui.QSpacerItem(16, 137, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem3)
        self.groupBox_6 = QtGui.QGroupBox(configwindow)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_26 = QtGui.QLabel(self.groupBox_6)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_11.addWidget(self.label_26)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.localManuControl = QtGui.QRadioButton(self.groupBox_6)
        self.localManuControl.setChecked(True)
        self.localManuControl.setObjectName(_fromUtf8("localManuControl"))
        self.horizontalLayout_8.addWidget(self.localManuControl)
        self.localAutoControl = QtGui.QRadioButton(self.groupBox_6)
        self.localAutoControl.setObjectName(_fromUtf8("localAutoControl"))
        self.horizontalLayout_8.addWidget(self.localAutoControl)
        self.localControlOff = QtGui.QRadioButton(self.groupBox_6)
        self.localControlOff.setObjectName(_fromUtf8("localControlOff"))
        self.horizontalLayout_8.addWidget(self.localControlOff)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_8)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem4)
        self.networkControlOn = QtGui.QCheckBox(self.groupBox_6)
        self.networkControlOn.setChecked(True)
        self.networkControlOn.setObjectName(_fromUtf8("networkControlOn"))
        self.horizontalLayout_20.addWidget(self.networkControlOn)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem5)
        self.verticalLayout_12.addLayout(self.horizontalLayout_20)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.horizontalLayout_21.addWidget(self.groupBox_6)
        spacerItem6 = QtGui.QSpacerItem(16, 137, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem6)
        self.verticalLayout_14.addLayout(self.horizontalLayout_21)
        self.gridLayout_2.addLayout(self.verticalLayout_14, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem7)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.okButton = QtGui.QPushButton(configwindow)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_17.addWidget(self.okButton)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_17)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_19)

        self.retranslateUi(configwindow)
        QtCore.QMetaObject.connectSlotsByName(configwindow)
        configwindow.setTabOrder(self.acRadioButton, self.batteryRadioButton)
        configwindow.setTabOrder(self.batteryRadioButton, self.adapterIPv4Addr)
        configwindow.setTabOrder(self.adapterIPv4Addr, self.adapterIPv4Port)
        configwindow.setTabOrder(self.adapterIPv4Port, self.adapterIPv6Addr)
        configwindow.setTabOrder(self.adapterIPv6Addr, self.adapterIPv6Port)
        configwindow.setTabOrder(self.adapterIPv6Port, self.localIPv4Port)
        configwindow.setTabOrder(self.localIPv4Port, self.localIPv6Port)
        configwindow.setTabOrder(self.localIPv6Port, self.alertOn)
        configwindow.setTabOrder(self.alertOn, self.alertOff)
        configwindow.setTabOrder(self.alertOff, self.airTempUpper)
        configwindow.setTabOrder(self.airTempUpper, self.airTempLower)
        configwindow.setTabOrder(self.airTempLower, self.airHumiUpper)
        configwindow.setTabOrder(self.airHumiUpper, self.airHumiLower)
        configwindow.setTabOrder(self.airHumiLower, self.earthHumiUpper)
        configwindow.setTabOrder(self.earthHumiUpper, self.earthHumiLower)
        configwindow.setTabOrder(self.earthHumiLower, self.co2Upper)
        configwindow.setTabOrder(self.co2Upper, self.co2Lower)
        configwindow.setTabOrder(self.co2Lower, self.illumUpper)
        configwindow.setTabOrder(self.illumUpper, self.illumLower)
        configwindow.setTabOrder(self.illumLower, self.phoneNum1)
        configwindow.setTabOrder(self.phoneNum1, self.phoneNum2)
        configwindow.setTabOrder(self.phoneNum2, self.phoneNum3)
        configwindow.setTabOrder(self.phoneNum3, self.cdmaUsername)
        configwindow.setTabOrder(self.cdmaUsername, self.cdmaPassword)
        configwindow.setTabOrder(self.cdmaPassword, self.segmac)
        configwindow.setTabOrder(self.segmac, self.scmac)
        configwindow.setTabOrder(self.scmac, self.uploadPeriod)
        configwindow.setTabOrder(self.uploadPeriod, self.collectPeriod)
        configwindow.setTabOrder(self.collectPeriod, self.collectTime)
        configwindow.setTabOrder(self.collectTime, self.localManuControl)
        configwindow.setTabOrder(self.localManuControl, self.localAutoControl)
        configwindow.setTabOrder(self.localAutoControl, self.localControlOff)
        configwindow.setTabOrder(self.localControlOff, self.networkControlOn)
        configwindow.setTabOrder(self.networkControlOn, self.okButton)

    def retranslateUi(self, configwindow):
        configwindow.setWindowTitle(_translate("configwindow", "ConfigManager", None))
        self.label.setText(_translate("configwindow", "Gateway Power Type:", None))
        self.acRadioButton.setText(_translate("configwindow", "AC", None))
        self.batteryRadioButton.setText(_translate("configwindow", "Battery", None))
        self.groupBox.setTitle(_translate("configwindow", "Network", None))
        self.label_2.setText(_translate("configwindow", "Adapater IPv4 Address:", None))
        self.label_3.setText(_translate("configwindow", "Adapater IPv4 Port:", None))
        self.label_4.setText(_translate("configwindow", "Adapater IPv6 Address:", None))
        self.label_5.setText(_translate("configwindow", "Adapater IPv6 Port:", None))
        self.label_6.setText(_translate("configwindow", "Local IPv4 Port:", None))
        self.label_7.setText(_translate("configwindow", "Local IPv6 Port:", None))
        self.groupBox_5.setTitle(_translate("configwindow", "CDMA", None))
        self.label_13.setText(_translate("configwindow", "CDMA Username:", None))
        self.label_14.setText(_translate("configwindow", "CDMA Password:", None))
        self.groupBox_3.setTitle(_translate("configwindow", "Address", None))
        self.label_8.setText(_translate("configwindow", "SEGMAC:", None))
        self.label_9.setText(_translate("configwindow", "SCMAC:", None))
        self.groupBox_2.setTitle(_translate("configwindow", "Thold", None))
        self.AlertSwitc.setText(_translate("configwindow", "Alert On/Off:", None))
        self.alertOn.setText(_translate("configwindow", "On", None))
        self.alertOff.setText(_translate("configwindow", "Off", None))
        self.label_18.setText(_translate("configwindow", "Upper Limit", None))
        self.label_19.setText(_translate("configwindow", "Lower Limit", None))
        self.label_20.setText(_translate("configwindow", "Air Temp", None))
        self.label_21.setText(_translate("configwindow", "Air Humi", None))
        self.label_27.setText(_translate("configwindow", "Earth Temp", None))
        self.label_22.setText(_translate("configwindow", "Earth Humi", None))
        self.label_24.setText(_translate("configwindow", "CO2", None))
        self.label_23.setText(_translate("configwindow", "Illum", None))
        self.label_15.setText(_translate("configwindow", "Phone Number 1:", None))
        self.label_16.setText(_translate("configwindow", "Phone Number 2:", None))
        self.label_17.setText(_translate("configwindow", "Phone Number 3:", None))
        self.groupBox_4.setTitle(_translate("configwindow", "Period", None))
        self.label_10.setText(_translate("configwindow", "Upload Period(AC):", None))
        self.label_11.setText(_translate("configwindow", "Collect Period(Battery):", None))
        self.label_12.setText(_translate("configwindow", "Collect Time(Battery):", None))
        self.groupBox_6.setTitle(_translate("configwindow", "Control", None))
        self.label_26.setText(_translate("configwindow", "Local Control:", None))
        self.localManuControl.setText(_translate("configwindow", "Manual", None))
        self.localAutoControl.setText(_translate("configwindow", "Auto", None))
        self.localControlOff.setText(_translate("configwindow", "Off", None))
        self.networkControlOn.setText(_translate("configwindow", "Network Control", None))
        self.okButton.setText(_translate("configwindow", "OK", None))

