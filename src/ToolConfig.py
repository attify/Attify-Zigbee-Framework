from PyQt4 import QtCore, QtGui
from UI.Config import Ui_Form
from PyQt4.QtCore import SIGNAL
import os

class ToolConfig(QtGui.QWidget, Ui_Form):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)
		print("[*] Starting Configuration Widget ")
		self.pushButton_SaveConfig.clicked.connect(self.SaveConfig)
		self.controls={
			"zbid":self.checkBox_zbid,
			"zbwireshark":self.checkBox_zbwireshark,
			"zbdump":self.checkBox_zbdump,
			"zbreplay":self.checkBox_zbreplay,
			"zbstumbler":self.checkBox_zbstumbler,
			"zbpanidconflictflood":self.checkBox_zbpanidconflictflood,
			"zborphannotify":self.checkBox_zborphannotify,
			"zbrealign":self.checkBox_zbrealign,
			"zbfakebeacon":self.checkBox_zbfakebeacon,
			"zbopenear":self.checkBox_zbopenear,
			"zbassocflood":self.checkBox_zbassocflood,
			"zbconvert":self.checkBox_zbconvert,
			"zbdsniff":self.checkBox_zbdsniff,
			"zbgoodfind":self.checkBox_zbgoodfind,
			"zbwardrive":self.checkBox_zbwardrive,
			"zbscapy":self.checkBox_zbscapy,
		}
		self.setup()

	def setup(self):
		print("[*] Setting up Configuration Tool")
		file=open("AZF.cfg")
		while(True):
			tab=file.readline().strip()
			if(tab==""):
				break
			if '+' in tab:
				tab=tab.replace('+','')
				self.controls[tab].click()
			else:
				tab=tab.replace('-','')
		file.close()

	def SaveConfig(self):
		print("[*] Saving new configuration ")
		os.remove("AZF.cfg")
		file=open("AZF.cfg","w")
		for i in self.controls.keys():
			if(self.controls[i].isChecked()):
				file.write("+"+i+"\n")
			else:
				file.write("-"+i+"\n")
		file.close()
                self.emit(SIGNAL('update_tools(int)'), 1)
		self.close()

