#!/usr/bin/env python
# -*- coding:  utf-8 -*-

import sys
from configwindow_ui import  *
from PyQt4 import QtGui, QtCore
from config import *
from struct import *

class ConfigWindow(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_configwindow()
        self.ui.setupUi(self)
        self.loadConfig()

        QtCore.QObject.connect(self.ui.okButton, QtCore.SIGNAL("clicked()"), self.outputConfig)
        QtCore.QObject.connect(self.ui.acRadioButton, QtCore.SIGNAL("toggled(bool)"), self.powerchange)
        QtCore.QObject.connect(self.ui.alertOn, QtCore.SIGNAL("toggled(bool)"), self.alertchange)

    def powerchange(self):
        if self.ui.acRadioButton.isChecked():
            ac = True
        else:
            ac = False

        if ac:
            self.ui.uploadPeriod.setEnabled(True)
            self.ui.collectPeriod.setEnabled(False)
            self.ui.collectTime.setEnabled(False)
        else:
            self.ui.uploadPeriod.setEnabled(False)
            self.ui.collectPeriod.setEnabled(True)
            self.ui.collectTime.setEnabled(True)

    def alertchange(self):
        if self.ui.alertOn.isChecked():
            alert = True
        else:
            alert = False

        if alert:
            self.ui.airTempUpper.setEnabled(True)
            self.ui.airTempLower.setEnabled(True)
            self.ui.airHumiUpper.setEnabled(True)
            self.ui.airHumiLower.setEnabled(True)
            self.ui.earthHumiUpper.setEnabled(True)
            self.ui.earthHumiLower.setEnabled(True)  
            self.ui.earthTempUpper.setEnabled(True)
            self.ui.earthTempLower.setEnabled(True)    
            self.ui.co2Upper.setEnabled(True)
            self.ui.co2Lower.setEnabled(True)
            self.ui.illumUpper.setEnabled(True)
            self.ui.illumLower.setEnabled(True)
            self.ui.phoneNum1.setEnabled(True)      
            self.ui.phoneNum2.setEnabled(True)
            self.ui.phoneNum3.setEnabled(True)                               
        else:
            self.ui.airTempUpper.setEnabled(False)
            self.ui.airTempLower.setEnabled(False)
            self.ui.airHumiUpper.setEnabled(False)
            self.ui.airHumiLower.setEnabled(False)
            self.ui.earthHumiUpper.setEnabled(False)
            self.ui.earthHumiLower.setEnabled(False)  
            self.ui.earthTempUpper.setEnabled(False)
            self.ui.earthTempLower.setEnabled(False)    
            self.ui.co2Upper.setEnabled(False)
            self.ui.co2Lower.setEnabled(False)
            self.ui.illumUpper.setEnabled(False)
            self.ui.illumLower.setEnabled(False)
            self.ui.phoneNum1.setEnabled(False)      
            self.ui.phoneNum2.setEnabled(False)
            self.ui.phoneNum3.setEnabled(False)  


    def outputConfig(self):
        if self.check() == False:
            return 

        if self.ui.acRadioButton.isChecked():
            gw_power_state = pack("<I", 1)
        if self.ui.batteryRadioButton.isChecked():
            gw_power_state = pack("<I", 2)

        gw_add4 = pack("<16s", str(self.ui.adapterIPv4Addr.text()))
        gw_remote_port4 = pack("<H", int(self.ui.adapterIPv4Port.text()))
        gw_local_port4 = pack("<H", int(self.ui.localIPv4Port.text()))
        gw_add6 = pack("<40s", str(self.ui.adapterIPv6Addr.text()))
        gw_remote_port6 = pack("<H", int(self.ui.adapterIPv6Port.text()))
        gw_local_port6 = pack("<H", int(self.ui.localIPv6Port.text()))

        segmac = pack("<I", self.convertmac(str(self.ui.segmac.text())))
        scmac = pack("<Q", self.convertmac(self.ui.scmac.text()))
        scmac_h = scmac[4:]
        scmac_l = scmac[:4]

        period_time = pack("<H", int(self.ui.uploadPeriod.text()))
        senser_period_time = pack("<H", int(self.ui.collectPeriod.text()))
        gw_update_time_set = pack("<B", int(self.ui.collectTime.text()))
        gw_update_time = pack("<B", 0)

        username = pack("<30s", str(self.ui.cdmaUsername.text()))
        password = pack("<30s", str(self.ui.cdmaPassword.text()))

        telnum1 = pack("<12s", str(self.ui.phoneNum1.text()))
        telnum2 = pack("<12s", str(self.ui.phoneNum2.text()))
        telnum3 = pack("<12s", str(self.ui.phoneNum3.text()))

        if self.ui.alertOn.isChecked():
            thold_flag = pack("<B", 1)
        if self.ui.alertOff.isChecked():
            thold_flag = pack("<B", 0)
        light_thold_h = pack("<H", int(self.ui.illumUpper.text()))
        light_thold_l = pack("<H", int(self.ui.illumLower.text()))
        air_temp_thold_h = pack("<H", int(self.ui.airTempUpper.text()))
        air_temp_thold_l = pack("<H", int(self.ui.airTempLower.text()))
        air_humi_thold_h = pack("<H", int(self.ui.airHumiUpper.text()))
        air_humi_thold_l = pack("<H", int(self.ui.airHumiLower.text()))
        co2_thold_h = pack("<H", int(self.ui.co2Upper.text()))
        co2_thold_l = pack("<H", int(self.ui.co2Lower.text()))
        soil_thold_h = pack("<H", int(self.ui.earthHumiUpper.text()))
        soil_thold_l = pack("<H", int(self.ui.earthHumiLower.text()))
        soil_temp_thold_h = pack("<H", int(self.ui.earthTempUpper.text()))
        soil_temp_thold_l = pack("<H", int(self.ui.earthTempLower.text()))        

        if self.ui.localManuControl.isChecked():
            gw_local_control = pack("<I", 1)
            gw_auto_control = pack("<I", 2)
        if self.ui.localAutoControl.isChecked():
            gw_local_control = pack("<I", 2)
            gw_auto_control = pack("<I", 1)
        if self.ui.localControlOff.isChecked():
            gw_local_control = pack("<I", 2)
            gw_auto_control = pack("<I", 2)

        if self.ui.networkControlOn.isChecked():
            gw_net_control = pack("<I", 1)
        else:
            gw_net_control = pack("<I", 2)

        gw_msg_switch = pack("<I", 1)
        history_num = pack("<I", 0)
        net_state = pack("<B", 1)
        hisreport_state = pack("<B", 0)

        outputstr = gw_power_state + gw_add4 + gw_remote_port4 + gw_local_port4 + gw_add6 + gw_remote_port6 + gw_local_port6 + segmac + scmac_h + scmac_l + period_time + senser_period_time + gw_update_time_set + gw_update_time + username + password + telnum1 + telnum2 + telnum3 + thold_flag + light_thold_h + light_thold_l + air_temp_thold_h + air_temp_thold_l + air_humi_thold_h + air_humi_thold_l + co2_thold_h + co2_thold_l + soil_thold_h + soil_thold_l + soil_temp_thold_h + soil_temp_thold_l + gw_local_control + gw_net_control + gw_auto_control + gw_msg_switch + history_num + net_state + hisreport_state
        output = open(OUTPUT_FILE, "wb")
        output.write(outputstr)
        output.close()

        self.saveConfig()
        self.close()

    def saveConfig(self):
        settings = QtCore.QSettings(INI_FILE, QtCore.QSettings.IniFormat)
    
        if self.ui.acRadioButton.isChecked():
            settings.setValue("gw_power_state", 1)
        if self.ui.batteryRadioButton.isChecked():
            settings.setValue("gw_power_state", 2)

        settings.setValue("gw_add4", self.ui.adapterIPv4Addr.text())
        settings.setValue("gw_remote_port4", self.ui.adapterIPv4Port.text())
        settings.setValue("gw_local_port4", self.ui.localIPv4Port.text())
        settings.setValue("gw_add6", self.ui.adapterIPv6Addr.text())
        settings.setValue("gw_remote_port6", self.ui.adapterIPv6Port.text())
        settings.setValue("gw_local_port6", self.ui.localIPv6Port.text())

        settings.setValue("segmac", self.ui.segmac.text())
        settings.setValue("scmac", self.ui.scmac.text())

        settings.setValue("period_time", self.ui.uploadPeriod.text())
        settings.setValue("senser_period_time", self.ui.collectPeriod.text())
        settings.setValue("gw_update_time_set", self.ui.collectTime.text())

        settings.setValue("username", self.ui.cdmaUsername.text())
        settings.setValue("password", self.ui.cdmaPassword.text())

        settings.setValue("telnum1", self.ui.phoneNum1.text())
        settings.setValue("telnum2", self.ui.phoneNum2.text())
        settings.setValue("telnum3", self.ui.phoneNum3.text())

        if self.ui.alertOn.isChecked():
            settings.setValue("thold_flag", 1)
        if self.ui.alertOff.isChecked():
            settings.setValue("thold_flag", 0)

        settings.setValue("light_thold_h", self.ui.illumUpper.text())
        settings.setValue("light_thold_l", self.ui.illumLower.text())
        settings.setValue("air_temp_thold_h", self.ui.airTempUpper.text())
        settings.setValue("air_temp_thold_l", self.ui.airTempLower.text())
        settings.setValue("air_humi_thold_h", self.ui.airHumiUpper.text())
        settings.setValue("air_humi_thold_l", self.ui.airHumiLower.text())
        settings.setValue("co2_thold_h", self.ui.co2Upper.text())
        settings.setValue("co2_thold_l", self.ui.co2Lower.text())
        settings.setValue("soil_thold_h", self.ui.earthHumiUpper.text())
        settings.setValue("soil_thold_l", self.ui.earthHumiLower.text())
        settings.setValue("soil_temp_thold_h", self.ui.earthTempUpper.text())
        settings.setValue("soil_temp_thold_l", self.ui.earthTempLower.text())

        if self.ui.localManuControl.isChecked():
            settings.setValue("gw_local_control", 1)
            settings.setValue("gw_auto_control", 2)
        if self.ui.localAutoControl.isChecked():
            settings.setValue("gw_local_control", 2)
            settings.setValue("gw_auto_control", 1)
        if self.ui.localControlOff.isChecked():
            settings.setValue("gw_local_control", 2)
            settings.setValue("gw_auto_control", 2)            

        if self.ui.networkControlOn.isChecked():
            settings.setValue("gw_net_control", 1)
        else:
            settings.setValue("gw_net_control", 2)

    def loadConfig(self):
        settings = QtCore.QSettings(INI_FILE, QtCore.QSettings.IniFormat)
        
        if settings.value("gw_power_state") == 1:
            self.ui.acRadioButton.setChecked(True)
        elif settings.value("gw_power_state") == 2:
            self.ui.batteryRadioButton.setChecked(True)

        self.ui.adapterIPv4Addr.setText(settings.value("gw_add4", "219.141.189.156").toString())
        self.ui.adapterIPv4Port.setText(settings.value("gw_remote_port4", "502").toString())
        self.ui.localIPv4Port.setText(settings.value("gw_local_port4", "502").toString())
        self.ui.adapterIPv6Addr.setText(settings.value("gw_add6", "2001:0C68:3402:3069:0000:000C:385B:6D01").toString())
        self.ui.adapterIPv6Port.setText(settings.value("gw_remote_port6", "502").toString())
        self.ui.localIPv6Port.setText(settings.value("gw_local_port6", "502").toString())

        self.ui.segmac.setText(settings.value("segmac", "241.0.0.1").toString())
        self.ui.scmac.setText(settings.value("scmac", "0.0.0.241.0.0.0.1").toString())

        self.ui.uploadPeriod.setText(settings.value("period_time", "60").toString())
        self.ui.collectPeriod.setText(settings.value("senser_period_time", "10").toString())
        self.ui.collectTime.setText(settings.value("gw_update_time_set", "5").toString())

        self.ui.cdmaUsername.setText(settings.value("username", "ctnet@mycdma.cn").toString())
        self.ui.cdmaPassword.setText(settings.value("password", "vnet.mobi").toString())

        self.ui.phoneNum1.setText(settings.value("telnum1", "00000000000").toString())
        self.ui.phoneNum2.setText(settings.value("telnum2", "00000000000").toString())
        self.ui.phoneNum3.setText(settings.value("telnum3", "00000000000").toString())

        if settings.value("thold_flag") == 1:
            self.ui.alertOn.setChecked(True)
        elif settings.value("thold_flag") == 0:
            self.ui.alertOff.setChecked(True)

        self.ui.illumUpper.setText(settings.value("light_thold_h", "2000").toString())
        self.ui.illumLower.setText(settings.value("light_thold_l", "100").toString())
        self.ui.airTempUpper.setText(settings.value("air_temp_thold_h", "40").toString())
        self.ui.airTempLower.setText(settings.value("air_temp_thold_l", "10").toString())
        self.ui.airHumiUpper.setText(settings.value("air_humi_thold_h", "80").toString())
        self.ui.airHumiLower.setText(settings.value("air_humi_thold_l", "30").toString())
        self.ui.co2Upper.setText(settings.value("co2_thold_h", "2000").toString())
        self.ui.co2Lower.setText(settings.value("co2_thold_l", "200").toString())
        self.ui.earthHumiUpper.setText(settings.value("soil_thold_h", "80").toString())
        self.ui.earthHumiLower.setText(settings.value("soil_thold_l", "30").toString())
        self.ui.earthTempUpper.setText(settings.value("soil_temp_thold_h", "80").toString())
        self.ui.earthTempLower.setText(settings.value("soil_temp_thold_l", "10").toString())


        if settings.value("gw_local_control") == 1:
            self.ui.localManuControl.setChecked(True)
        if settings.value("gw_auto_control") == 1:
            self.ui.localAutoControl.setChecked(True)  
        if settings.value("gw_auto_control") == 2 and settings.value("gw_local_control") == 2:
            self.ui.localControlOff.setChecked(True)  

        if settings.value("gw_net_control") == 1:
            self.ui.networkControlOn.setChecked(True)
        elif settings.value("gw_net_control") == 2:
            self.ui.networkControlOn.setChecked(False)
 

        self.powerchange()
        self.alertchange()                    

    def check(self):
        ip = self.ui.adapterIPv4Addr.text().split(".")
        if len(ip) != 4:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in adapter IPv4 addr"))
            return False
        for every in ip:
            try:
                if int(every) > 255 or int(every) < 0:
                    QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in adapter IPv4 addr"))
                    return False
            except:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in adapter IPv4 addr"))
                return False

        port = self.ui.adapterIPv4Port.text()
        try:
            if int(port) > 65535 or int(port) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in adapter IPv4 port"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in adapter IPv4 port"))
            return False
        port = self.ui.adapterIPv6Port.text()
        try:
            if int(port) > 65535 or int(port) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in adapter IPv4 port"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in adapter IPv6 port"))
            return False
        port = self.ui.localIPv4Port.text()
        try:
            if int(port) > 65535 or int(port) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in local IPv4 port"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in local IPv4 port"))
            return False
        port = self.ui.localIPv6Port.text()
        try:
            if int(port) > 65535 or int(port) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in local IPv6 port"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in local IPv6 port"))
            return False     

        segmac = self.ui.segmac.text().split(".")
        if len(segmac) != 4:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in SEGMAC"))
            return False
        for every in segmac:
            try:
                if int(every) > 255 or int(every) < 0:
                    QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in SEGMAC"))
                    return False
            except:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in SEGMAC"))
                return False

        scmac = self.ui.scmac.text().split(".")
        if len(scmac) != 8:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in SCMAC"))
            return False
        for every in scmac:
            try:
                if int(every) > 255 or int(every) < 0:
                    QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in SCMAC"))
                    return False
            except:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in SCMAC"))
                return False

        tel1 = 0 if len(self.ui.phoneNum1.text()) == 0 else self.ui.phoneNum1.text()
        try:
            rubbish = int(tel1)
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "No digit found in TEL1"))
            return False
        tel2 = 0 if len(self.ui.phoneNum2.text()) == 0 else self.ui.phoneNum2.text()
        try:
            rubbish = int(tel2)
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "No digit found in TEL2"))
            return False
        tel3 = 0 if len(self.ui.phoneNum3.text()) == 0 else self.ui.phoneNum3.text()
        try:
            rubbish = int(tel3)
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "No digit found in TEL3"))
            return False

        uploadPeriod = self.ui.uploadPeriod.text()
        try:
            if int(uploadPeriod) > 65535 or int(uploadPeriod) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in upload period"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in upload period"))
            return False

        collectPeriod = self.ui.collectPeriod.text()
        try:
            if int(collectPeriod) > 65535 or int(collectPeriod) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in collect period"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in collect period"))
            return False

        collectTime = self.ui.collectTime.text()
        try:
            if int(collectTime) > 255 or int(collectTime) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in collect time"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in collect time"))
            return False            

        airTempUpper = self.ui.airTempUpper.text()
        try:
            if int(airTempUpper) > 65535 or int(airTempUpper) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in air temp upper"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in air temp upper"))
            return False     

        airTempLower = self.ui.airTempLower.text()
        try:
            if int(airTempLower) > 65535 or int(airTempLower) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in air temp lower"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in air temp lower"))
            return False  

        airHumiUpper = self.ui.airHumiUpper.text()
        try:
            if int(airTempLower) > 65535 or int(airTempLower) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in air humi upper"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in air humi upper"))
            return False      

        airHumiLower = self.ui.airHumiLower.text()
        try:
            if int(airHumiLower) > 65535 or int(airHumiLower) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in air humi lower"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in air humi lower"))
            return False           

        earthHumiUpper = self.ui.earthHumiUpper.text()
        try:
            if int(earthHumiUpper) > 65535 or int(earthHumiUpper) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in earth humi upper"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in earth humi upper"))
            return False      

        earthHumiLower = self.ui.earthHumiLower.text()
        try:
            if int(earthHumiLower) > 65535 or int(earthHumiLower) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in earth humi lower"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in earth humi lower"))
            return False   

        earthTempUpper = self.ui.earthTempUpper.text()
        try:
            if int(earthTempUpper) > 65535 or int(earthTempUpper) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in earth temp upper"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in earth temp upper"))
            return False      

        earthTempLower = self.ui.earthTempLower.text()
        try:
            if int(earthTempLower) > 65535 or int(earthTempLower) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in earth temp lower"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in earth temp lower"))
            return False 

        co2Upper = self.ui.co2Upper.text()
        try:
            if int(co2Upper) > 65535 or int(co2Upper) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in co2 upper"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in co2 upper"))
            return False      

        co2Lower = self.ui.co2Lower.text()
        try:
            if int(co2Lower) > 65535 or int(co2Lower) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in co2 lower"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in co2 lower"))
            return False         

        illumUpper = self.ui.illumUpper.text()
        try:
            if int(illumUpper) > 65535 or int(illumUpper) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in illum upper"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in illum upper"))
            return False      

        illumLower = self.ui.illumLower.text()
        try:
            if int(illumLower) > 65535 or int(illumLower) <= 0:
                QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in illum lower"))
                return False
        except:
            QtGui.QMessageBox.critical(self, QtGui.QApplication.translate('config', "Error"), QtGui.QApplication.translate('config', "Error in illum lower"))
            return False                                        

    def convertmac(self, mac):
        mac = mac.split(".")
        bytestr = ""
        for byte in mac:
            byte = int(byte)
            byte = "%02x" % byte
            bytestr += byte

        bytestr = "0x" + bytestr
        return int(bytestr, 16)