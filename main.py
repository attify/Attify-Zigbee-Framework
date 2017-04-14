#!/usr/bin/python

############################
## Attify Zigbee Framework #
############################

from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QAction,QIcon
from PyQt4.QtCore import SIGNAL
from UI.Base import Ui_MainWindow
from src.kbi import RavenRefresh,ZBDumpThread,ZBReplayThread
from src.ztmThread import ZBStumblerThread
import sys,subprocess

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class AZFMain(Ui_MainWindow):
        def __init__(self,dialog,parent=None):
                Ui_MainWindow.__init__(self)
                self.setupUi(dialog)
		self.ToolIcon.setPixmap(QtGui.QPixmap(_fromUtf8('UI/icon.png')))
		self.zbstumblerThread=None
		self.zbdumpThread=None
		self.zbreplayThread=None
		self.ravenRefresh()
		self.pushButton_Refresh.clicked.connect(self.ravenRefresh)
		self.pushButton_zbstumbler.clicked.connect(self.zbstumblerRun)
		self.pushButton_Zbdump.clicked.connect(self.zdump)
		self.pushButton_Zbreplay.clicked.connect(self.zbreplay)

	def ravenRefresh(self):
		print "[*] Executing Raven Refresh "
                self.statusbar.showMessage(" AZF | Refreshing devices",2000)
		self.ravenRefreshThread=RavenRefresh()
		self.ravenRefreshThread.start()
		QtCore.QObject.connect(self.ravenRefreshThread,QtCore.SIGNAL("ravenrefresh_update(QString)"), self.update_refresh_status)

	def update_refresh_status(self,QString):
		if len(str(QString)) > 50:
			self.labelDeviceStatus.setText("Connected")
			string=str(QString).split("\n")
			output=[]
			for i in string:
				output.append(i.strip())
			QString=output[0]+"\n"+output[1]
			self.labelDeviceDetails.setText(QString)
		else:
			self.labelDeviceStatus.setText("Disconnected")
                self.ravenRefreshThread.close()

	def zbstumblerRun(self):
		if self.zbstumblerThread==None:
                	self.statusbar.showMessage(" AZF | Starting zbstumbler",2000)
			print "[*] Starting zbstumbler"
			self.pushButton_zbstumbler.setText("Stop")
			channel=self.zbstumbler_Channel.currentText()
			if channel=="Select Channel":
				channel=11
			self.zbstumblerConsole.append("\n[ * ] Scanning channel : "+channel+"\n")
			self.zbstumblerThread=ZBStumblerThread(int(channel))
			self.zbstumblerThread.start()
	                QtCore.QObject.connect(self.zbstumblerThread,QtCore.SIGNAL("stumbler_update(QString)"), self.update_zbstumbler)
		else:
                        print "[*] Stopping zbstumbler"
                	self.statusbar.showMessage(" AZF | Stopping zbstumbler",2000)
                        self.pushButton_zbstumbler.setText("Start")
                        self.zbstumblerThread.close()
			self.zbstumblerThread=None

	def update_zbstumbler(self,QString):
		if(str(QString)=="Complete"):
                        print "[*] Stopping zbstumbler"
                        self.statusbar.showMessage(" AZF | Stopping zbstumbler",2000)
                        self.pushButton_zbstumbler.setText("Start")
                        self.zbstumblerThread.close()
                        self.zbstumblerThread=None
                        self.zbstumblerConsole.append("\n[ * ] Scanning complete")
		else:
			self.zbstumblerConsole.append(QString)

	def zdump(self):
		channel=self.zbdumpChannel.currentText()
		file=self.zbdumpFile.text()
		count=self.zbdumpCount.text()
		if self.zbdumpThread==None:
                        print "[*] Starting ZBdump"
                        self.statusbar.showMessage(" AZF | Starting zbdump",1500)
			self.pushButton_Zbdump.setText("Stop Capture")
			self.zbdumpThread=ZBDumpThread(channel,file,count)
			self.zbdumpThread.start()
                        QtCore.QObject.connect(self.zbdumpThread,QtCore.SIGNAL("zbdump_update(QString)"), self.zbdump_complete)
		else:
			print "[*] Stopping ZBdump"
                        self.statusbar.showMessage(" AZF | Stopping zbdump",1500)
			self.pushButton_Zbdump.setText("Start Capture")
			self.zbdumpThread.close()
			self.zbdumpThread=None

	def zbdump_complete(self):
                self.zbdumpThread.close()
		print "[*] Stopping ZBdump"
		self.statusbar.showMessage(" AZF | Stopping zbdump",1500)
                self.pushButton_Zbdump.setText("Start Capture")
                self.zbdumpThread=None


	def zbreplay(self):
 		channel=self.zbreplayChannel.currentText()
                file=self.zbreplayFile.text()
                count=self.zbreplayCount.text()
		delay=self.zbreplayDelay.text()
                if self.zbreplayThread==None:
                        print "[*] Starting ZBreplay"
                        self.statusbar.showMessage(" AZF | Starting zbreplay",1500)
                        self.pushButton_Zbreplay.setText("Stop Replay")
                        self.zbreplayThread=ZBReplayThread(channel,file,count,delay)
                        self.zbreplayThread.start()
                        QtCore.QObject.connect(self.zbreplayThread,QtCore.SIGNAL("zreplay_update(QString)"), self.replay_complete)
                else:
                        print "[*] Stopping ZBreplay"
                        self.statusbar.showMessage(" AZF | Stopping zbreplay",1500)
                        self.pushButton_Zbreplay.setText("Start Replay")
                        self.zbreplayThread.close()
                        self.zbreplayThread=None

	def replay_complete(self):
                self.zbreplayThread.close()
       		print "[*] Stopping ZBreplay"
                self.statusbar.showMessage(" AZF | Stopping zbreplay",1500)
                self.pushButton_Zbreplay.setText("Start Replay")
                self.zbreplayThread=None


if __name__=="__main__":
        app=QtGui.QApplication(sys.argv)
        dialog=QtGui.QMainWindow()
        app.setWindowIcon(QIcon("UI/icon.png"))
        prog=AZFMain(dialog)
        dialog.show()
        sys.exit(app.exec_())
