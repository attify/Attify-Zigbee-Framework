from PyQt4 import QtCore,QtGui
from src.ToolConfig import ToolConfig
from UI.Main import Ui_MainWindow
from UI.Config import Ui_Form
import sys

class ZBMain(Ui_MainWindow):
	def __init__(self,dialog,parent=None):
		Ui_MainWindow.__init__(self)
		self.setupUi(dialog)
		self.tabWidget.clear()
		self.config=None
		print("[*] Setting up the UI ")
		self.toolkit={
			"zbid":self.zbid,
			"zbwireshark":self.zbwireshark,
			"zbdump":self.zbdump,
			"zbreplay":self.zbreplay,
			"zbstumbler":self.zbstumbler,
			"zbpanidconflictflood":self.zbpanidconflictflood,
			"zborphannotify":self.zborphannotify,
			"zbrealign":self.zbrealign,
			"zbfakebeacon":self.zbfakebeacon,
			"zbopenear":self.zbopenear,
			"zbassocflood":self.zbassocflood,
			"zbconvert":self.zbconvert,
			"zbdsniff":self.zbdsniff,
			"zbgoodfind":self.zbgoodfind,
			"zbwardrive":self.zbwardrive,
			"zbscapy":self.zbscapy
		}
		if(self.CheckTools()==0):
			self.ConfigureTools()
		else:
			self.SetupTools()

	def CheckTools(self):
		file=open("AZF.cfg","r")
		out=file.read()
		file.close()
		if("+" in out):
			return 1
		else:
			return 0

	def ConfigureTools(self):
		if self.config is None:
			self.config=ToolConfig()
		self.config.show()

	def SetupTools(self):
		file=open("AZF.cfg","r")
		while(True):
			tab=file.readline().strip()
			if tab=="":
				break
			if '+' in tab:
				tab=tab.replace('+','')
				self.tabWidget.addTab(self.toolkit[tab],QtCore.QString(tab))
                               	print("[*] "+tab+" activated")
			else:
				tab=tab.replace('-','')
				print("[*] "+tab+" deactivated")



if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	dialog=QtGui.QMainWindow()
        app.setWindowIcon(QtGui.QIcon("UI/icon.png"))
	prog=ZBMain(dialog)
	dialog.show()
	sys.exit(app.exec_())
