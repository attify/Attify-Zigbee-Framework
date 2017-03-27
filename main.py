from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QAction
from PyQt4.QtCore import SIGNAL
from src.RunTool import RunTool
from src.ToolConfig import ToolConfig
from UI.Main import Ui_MainWindow
from UI.Config import Ui_Form
import os,fnmatch
import sys



zbdreplay_state=0


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
                if(self.CheckTools()==1):
                        self.SetupTools()
                self.actionTools.triggered.connect(self.ConfigureTools)
		self.actionExit.triggered.connect(self.exit)
		self.pushButton_zbidRefresh.clicked.connect(self.zbidRefresh)
		self.pushButton_zbdumpCapture.clicked.connect(self.zbdumpCapture)
		self.pushButton_zbwsStart.clicked.connect(self.zbwsstart)
		self.pushButton_zbstmblrStart.clicked.connect(self.zbstmblrStart)
		self.zbstumblerProc=QtCore.QProcess()
		self.zbstumblerProc.readyRead.connect(self.zbstumblerRead)
                #self.zbstumblerProc.readyReadStandardError.connect(self.zbstumblerError)
		self.pushButton_zbreplay.clicked.connect(self.zbreplayRun)
		self.zbreplay_updatePcap()
		self.zbreplayThread=None
		self.zbdumpThread=None

        def zbreplay_updatePcap(self):
                #Function checks for pcap files
                print("[*] UART_getport invoked ")
                #self.statusbar.showMessage("",2000)
                path="pcap/"
                pattern="*.pcap"
                result=[]
                for root, dirs, files in os.walk(path):
                        for name in files:
                                if fnmatch.fnmatch(name, pattern):
                                        result.append(os.path.join(root, name))
                self.comboBox_zbreplayPcap.clear()
                self.comboBox_zbreplayPcap.addItems(result)

	def exit(self):
		self.close()

	def CheckTools(self):
		file=open("cfg/tools.cfg","r")
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
	        QtCore.QObject.connect(self.config,QtCore.SIGNAL("update_tools(int)"), self.SetupTools)


	def SetupTools(self):
		self.tabWidget.clear()
		file=open("cfg/tools.cfg","r")
		while(True):
			tab=file.readline().strip()
			if tab=="":
				break
			if '+' in tab:
				tab=tab.replace('+','')
				self.tabWidget.addTab(self.toolkit[tab],QtCore.QString(tab))
		file.close()

	def zbidRefresh(self):
		self.zbidThread=RunTool("zbid",None)
		self.zbidThread.start()
                QtCore.QObject.connect(self.zbidThread,QtCore.SIGNAL("update_zbid(QString)"), self.zbidOutput)

	def zbidOutput(self,QString):
		item = QtGui.QListWidgetItem(str(QString))
		self.listWidget_zbid.addItem(item)

	def zbdumpCapture(self):
		if self.zbdumpThread==None:
			iface=str("-i "+self.lineEdit_zbdumpInterface.text()+" ")
			channel=str("-c "+self.comboBox_zbdumpChannel.currentText()+" ")
			count=str("-n "+self.lineEdit_zbdumpCount.text()+" ")
			output=str("-w pcap/"+self.lineEdit_zbdumpOutput.text())
			parameters=iface+channel+count+output
			self.zbdumpThread=RunTool("zbdump",parameters)
			self.zbdumpThread.start()
			self.pushButton_zbdumpCapture.setText("Stop Capture")
                	QtCore.QObject.connect(self.zbdumpThread,QtCore.SIGNAL("zbdump_complete(QString)"), self.zdumpOutput)
		else:
			self.pushButton_zbdumpCapture.setText("Start Capture")
			self.zbdumpThread.close()
			print "[*] Stopping zbdump"
			self.zbdumpThread=None

	def zdumpOutput(self,QString):
		print("[*] ZBDump complete ")
		self.zbreplay_updatePcap()

	def zbwsstart(self):
		iface=str("-i "+self.lineEdit_zbwsInterface.text()+" ")
                channel=str("-c "+self.comboBox_zbwsChannel.currentText()+" ")
                count=str("-n "+self.lineEdit_zbwscount.text())
		parameters=iface+channel+count
		self.zbwsThread=RunTool("zbwireshark",parameters)
		self.zbwsThread.start()

	def zbstmblrStart(self):
		cwd=os.getcwd()
		params=[]
		channel=self.comboBox_zbstmblrChannel.currentText()
		verbose=self.checkBox_zbstmblrVerbose.isChecked()
		parameters="None"
		self.zbstumblerProc.start("python",["killerbee/tools/zbstumbler","-v"])

        def zbstumblerRead(self):
		print "[*] Debug "
                cursor=self.textEdit_zbstmblrConsole.textCursor()
                cursor.movePosition(cursor.End)
                output=str(self.zbstumblerProc.readAll())
		if output:
			print "otpt"
                	cursor.insertText(output)
                self.textEdit_zbstmblrConsole.ensureCursorVisible()



	def zbreplayRun(self):
		if self.zbreplayThread == None:
			print "[*] Runningx zbreplay "
			pcap=str(self.comboBox_zbreplayPcap.currentText())
			channel=str(self.comboBox_zbreplayChannel.currentText())
			delay=str(self.lineEdit_zbreplayDelay.text())
			params="-c "+channel+" -s "+delay+" -r "+pcap
			self.zbreplayThread=RunTool("zbreplay",params)
			self.zbreplayThread.start()
                	QtCore.QObject.connect(self.zbreplayThread,QtCore.SIGNAL("zbreplay_complete(QString)"), self.zbreplayOutput)
			self.pushButton_zbreplay.setText("  Stop  ")
			zbreplay=1
		else:
			print "[*] Stopping zbreplay "
			self.pushButton_zbreplay.setText(" Replay ")
			self.zbreplayThread.close()
			zbreplay_state=0
			self.zbreplayThread=None


	def zbreplayOutput(self,QString):
		print "[*] Zbreplay Complete "
		print str(QString)



if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	dialog=QtGui.QMainWindow()
        app.setWindowIcon(QtGui.QIcon("UI/icon.png"))
	prog=ZBMain(dialog)
	dialog.show()
	sys.exit(app.exec_())
