#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from configwindow import *

if __name__ == "__main__":
    codec = QtCore.QTextCodec.codecForName("System")
    QtCore.QTextCodec.setCodecForCStrings(codec)
    QtCore.QTextCodec.setCodecForLocale(codec)
    QtCore.QTextCodec.setCodecForTr(codec)

    trans = QtCore.QTranslator()
    trans.load("langs/zh_CN.qm")
    qtTrans = QtCore.QTranslator()
    qtTrans.load("langs/qt_zh_CN.qm")
    
    app = QtGui.QApplication(sys.argv)
    app.installTranslator(trans)
    app.installTranslator(qtTrans)
    configwindow = ConfigWindow()
    configwindow.show()
    app.exec_()