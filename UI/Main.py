# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/main.ui'
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
        MainWindow.resize(811, 613)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 791, 541))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.zbid = QtGui.QWidget()
        self.zbid.setObjectName(_fromUtf8("zbid"))
        self.tabWidget.addTab(self.zbid, _fromUtf8(""))
        self.zbstumbler = QtGui.QWidget()
        self.zbstumbler.setObjectName(_fromUtf8("zbstumbler"))
        self.tabWidget.addTab(self.zbstumbler, _fromUtf8(""))
        self.zbwireshark = QtGui.QWidget()
        self.zbwireshark.setObjectName(_fromUtf8("zbwireshark"))
        self.tabWidget.addTab(self.zbwireshark, _fromUtf8(""))
        self.zbdump = QtGui.QWidget()
        self.zbdump.setObjectName(_fromUtf8("zbdump"))
        self.tabWidget.addTab(self.zbdump, _fromUtf8(""))
        self.zbreplay = QtGui.QWidget()
        self.zbreplay.setObjectName(_fromUtf8("zbreplay"))
        self.tabWidget.addTab(self.zbreplay, _fromUtf8(""))
        self.zbpanidconflictflood = QtGui.QWidget()
        self.zbpanidconflictflood.setObjectName(_fromUtf8("zbpanidconflictflood"))
        self.tabWidget.addTab(self.zbpanidconflictflood, _fromUtf8(""))
        self.zborphannotify = QtGui.QWidget()
        self.zborphannotify.setObjectName(_fromUtf8("zborphannotify"))
        self.tabWidget.addTab(self.zborphannotify, _fromUtf8(""))
        self.zbrealign = QtGui.QWidget()
        self.zbrealign.setObjectName(_fromUtf8("zbrealign"))
        self.tabWidget.addTab(self.zbrealign, _fromUtf8(""))
        self.zbfakebeacon = QtGui.QWidget()
        self.zbfakebeacon.setObjectName(_fromUtf8("zbfakebeacon"))
        self.tabWidget.addTab(self.zbfakebeacon, _fromUtf8(""))
        self.zbopenear = QtGui.QWidget()
        self.zbopenear.setObjectName(_fromUtf8("zbopenear"))
        self.tabWidget.addTab(self.zbopenear, _fromUtf8(""))
        self.zbassocflood = QtGui.QWidget()
        self.zbassocflood.setObjectName(_fromUtf8("zbassocflood"))
        self.tabWidget.addTab(self.zbassocflood, _fromUtf8(""))
        self.zbconvert = QtGui.QWidget()
        self.zbconvert.setObjectName(_fromUtf8("zbconvert"))
        self.tabWidget.addTab(self.zbconvert, _fromUtf8(""))
        self.zbdsniff = QtGui.QWidget()
        self.zbdsniff.setObjectName(_fromUtf8("zbdsniff"))
        self.tabWidget.addTab(self.zbdsniff, _fromUtf8(""))
        self.zbgoodfind = QtGui.QWidget()
        self.zbgoodfind.setObjectName(_fromUtf8("zbgoodfind"))
        self.tabWidget.addTab(self.zbgoodfind, _fromUtf8(""))
        self.zbwardrive = QtGui.QWidget()
        self.zbwardrive.setObjectName(_fromUtf8("zbwardrive"))
        self.tabWidget.addTab(self.zbwardrive, _fromUtf8(""))
        self.zbscapy = QtGui.QWidget()
        self.zbscapy.setObjectName(_fromUtf8("zbscapy"))
        self.tabWidget.addTab(self.zbscapy, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionTools = QtGui.QAction(MainWindow)
        self.actionTools.setObjectName(_fromUtf8("actionTools"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionTools)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(10)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Attify Zigbee Exploitation Tool", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbid), _translate("MainWindow", "zbid", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbstumbler), _translate("MainWindow", "zbstumbler", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbwireshark), _translate("MainWindow", "zbwireshark", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbdump), _translate("MainWindow", "zbdump", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbreplay), _translate("MainWindow", "zbreplay", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbpanidconflictflood), _translate("MainWindow", "zbpanidconflictflood", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zborphannotify), _translate("MainWindow", "zborphannotify", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbrealign), _translate("MainWindow", "zbrealign", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbfakebeacon), _translate("MainWindow", "zbfakebeacon", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbopenear), _translate("MainWindow", "zbopenear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbassocflood), _translate("MainWindow", "zbassocflood", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbconvert), _translate("MainWindow", "zbconvert", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbdsniff), _translate("MainWindow", "zbdsniff", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbgoodfind), _translate("MainWindow", "zbgoodfind", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbwardrive), _translate("MainWindow", "zbwardrive", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zbscapy), _translate("MainWindow", "zbscapy", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuView.setTitle(_translate("MainWindow", "Settings", None))
        self.actionTools.setText(_translate("MainWindow", "Tools", None))
        self.actionTools.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

