# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(464, 546)
        self.checkBox_zbid = QtGui.QCheckBox(Form)
        self.checkBox_zbid.setGeometry(QtCore.QRect(37, 90, 99, 22))
        self.checkBox_zbid.setObjectName(_fromUtf8("checkBox_zbid"))
        self.checkBox_zbwireshark = QtGui.QCheckBox(Form)
        self.checkBox_zbwireshark.setGeometry(QtCore.QRect(37, 140, 111, 22))
        self.checkBox_zbwireshark.setObjectName(_fromUtf8("checkBox_zbwireshark"))
        self.checkBox_zbdump = QtGui.QCheckBox(Form)
        self.checkBox_zbdump.setGeometry(QtCore.QRect(37, 190, 99, 22))
        self.checkBox_zbdump.setObjectName(_fromUtf8("checkBox_zbdump"))
        self.checkBox_zbreplay = QtGui.QCheckBox(Form)
        self.checkBox_zbreplay.setGeometry(QtCore.QRect(37, 240, 99, 22))
        self.checkBox_zbreplay.setObjectName(_fromUtf8("checkBox_zbreplay"))
        self.checkBox_zbstumbler = QtGui.QCheckBox(Form)
        self.checkBox_zbstumbler.setGeometry(QtCore.QRect(37, 290, 111, 22))
        self.checkBox_zbstumbler.setObjectName(_fromUtf8("checkBox_zbstumbler"))
        self.checkBox_zbpanidconflictflood = QtGui.QCheckBox(Form)
        self.checkBox_zbpanidconflictflood.setGeometry(QtCore.QRect(37, 340, 171, 22))
        self.checkBox_zbpanidconflictflood.setObjectName(_fromUtf8("checkBox_zbpanidconflictflood"))
        self.checkBox_zborphannotify = QtGui.QCheckBox(Form)
        self.checkBox_zborphannotify.setGeometry(QtCore.QRect(37, 390, 141, 22))
        self.checkBox_zborphannotify.setObjectName(_fromUtf8("checkBox_zborphannotify"))
        self.checkBox_zbrealign = QtGui.QCheckBox(Form)
        self.checkBox_zbrealign.setGeometry(QtCore.QRect(37, 440, 121, 22))
        self.checkBox_zbrealign.setObjectName(_fromUtf8("checkBox_zbrealign"))
        self.checkBox_zbdsniff = QtGui.QCheckBox(Form)
        self.checkBox_zbdsniff.setGeometry(QtCore.QRect(287, 290, 99, 22))
        self.checkBox_zbdsniff.setObjectName(_fromUtf8("checkBox_zbdsniff"))
        self.checkBox_zbwardrive = QtGui.QCheckBox(Form)
        self.checkBox_zbwardrive.setGeometry(QtCore.QRect(287, 390, 121, 22))
        self.checkBox_zbwardrive.setObjectName(_fromUtf8("checkBox_zbwardrive"))
        self.checkBox_zbscapy = QtGui.QCheckBox(Form)
        self.checkBox_zbscapy.setGeometry(QtCore.QRect(287, 440, 99, 22))
        self.checkBox_zbscapy.setObjectName(_fromUtf8("checkBox_zbscapy"))
        self.checkBox_zbfakebeacon = QtGui.QCheckBox(Form)
        self.checkBox_zbfakebeacon.setGeometry(QtCore.QRect(287, 90, 131, 22))
        self.checkBox_zbfakebeacon.setObjectName(_fromUtf8("checkBox_zbfakebeacon"))
        self.checkBox_zbassocflood = QtGui.QCheckBox(Form)
        self.checkBox_zbassocflood.setGeometry(QtCore.QRect(287, 190, 131, 22))
        self.checkBox_zbassocflood.setObjectName(_fromUtf8("checkBox_zbassocflood"))
        self.checkBox_zbconvert = QtGui.QCheckBox(Form)
        self.checkBox_zbconvert.setGeometry(QtCore.QRect(287, 240, 131, 22))
        self.checkBox_zbconvert.setObjectName(_fromUtf8("checkBox_zbconvert"))
        self.checkBox_zbopenear = QtGui.QCheckBox(Form)
        self.checkBox_zbopenear.setGeometry(QtCore.QRect(287, 140, 99, 22))
        self.checkBox_zbopenear.setObjectName(_fromUtf8("checkBox_zbopenear"))
        self.checkBox_zbgoodfind = QtGui.QCheckBox(Form)
        self.checkBox_zbgoodfind.setGeometry(QtCore.QRect(287, 340, 121, 22))
        self.checkBox_zbgoodfind.setObjectName(_fromUtf8("checkBox_zbgoodfind"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(220, 80, 31, 391))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton_SaveConfig = QtGui.QPushButton(Form)
        self.pushButton_SaveConfig.setGeometry(QtCore.QRect(290, 500, 161, 27))
        self.pushButton_SaveConfig.setObjectName(_fromUtf8("pushButton_SaveConfig"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 30, 201, 17))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Tool configuration", None))
        self.checkBox_zbid.setText(_translate("Form", "zbid", None))
        self.checkBox_zbwireshark.setText(_translate("Form", "zbwireshark", None))
        self.checkBox_zbdump.setText(_translate("Form", "zbdump", None))
        self.checkBox_zbreplay.setText(_translate("Form", "zbreplay", None))
        self.checkBox_zbstumbler.setText(_translate("Form", "zbstumbler", None))
        self.checkBox_zbpanidconflictflood.setText(_translate("Form", "zbpanidconflictflood", None))
        self.checkBox_zborphannotify.setText(_translate("Form", "zborphannotify", None))
        self.checkBox_zbrealign.setText(_translate("Form", "zbrealign", None))
        self.checkBox_zbdsniff.setText(_translate("Form", "zbdsniff", None))
        self.checkBox_zbwardrive.setText(_translate("Form", "zbwardrive", None))
        self.checkBox_zbscapy.setText(_translate("Form", "zbscapy", None))
        self.checkBox_zbfakebeacon.setText(_translate("Form", "zbfakebeacon", None))
        self.checkBox_zbassocflood.setText(_translate("Form", "zbassocflood", None))
        self.checkBox_zbconvert.setText(_translate("Form", "zbconvert", None))
        self.checkBox_zbopenear.setText(_translate("Form", "zbopenear", None))
        self.checkBox_zbgoodfind.setText(_translate("Form", "zbgoodfind", None))
        self.pushButton_SaveConfig.setText(_translate("Form", "Save Configuration", None))
        self.label.setText(_translate("Form", "Select tools to add to the UI", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

