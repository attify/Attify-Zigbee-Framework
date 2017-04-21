from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL
import subprocess
from killerbee import *
from StringIO import StringIO
import sys


class RavenRefresh(QtCore.QThread):
        def __init__(self):
                super(RavenRefresh,self).__init__()

        def __del__(self):
                self.wait()

        def close(self):
                self.terminate()

        def run(self):
        	try:
			old_stdout = sys.stdout
			result = StringIO()
			sys.stdout = result
			show_dev()
			sys.stdout = old_stdout
			result_string = result.getvalue()
                	self.emit(SIGNAL('ravenrefresh_update(QString)'),QtCore.QString(str(result_string)))

		except Exception as e:
               		self.emit(SIGNAL('ravenrefresh_update(QString)'),QtCore.QString("0"))
                        print "[*] Thread Exception : "+str(e)


class ZBDumpThread(QtCore.QThread):
        def __init__(self,channel,file,count):
                super(ZBDumpThread,self).__init__()
		self.channel=channel
		self.file=file
		self.count=count

        def __del__(self):
                self.wait()

        def close(self):
                self.terminate()

	def run(self):
		print "[*] Running ZBDump Thread"
		p1=subprocess.Popen(str("python killerbee/tools/zbdump -c "+str(self.channel)+" -w pcap/"+str(self.file)+" -n "+str(self.count)).split())
		while 1:
			if p1.poll() is not None:
				self.emit(SIGNAL('zbdump_update(QString)'),QtCore.QString("complete"))


class ZBReplayThread(QtCore.QThread):
        def __init__(self,channel,file,count,delay):
                super(ZBReplayThread,self).__init__()
                self.channel=channel
                self.file=file
                self.count=count
		self.delay=delay

        def __del__(self):
                self.wait()

        def close(self):
                self.terminate()

        def run(self):
                print "[*] Running ZBReplay Thread"
                p1=subprocess.Popen(str("python killerbee/tools/zbreplay -c "+str(self.channel)+" -r pcap/"+str(self.file)+" -n "+str(self.count)+" -s "+str(self.delay)).split())
                while 1:
                        if p1.poll() is not None:
                                self.emit(SIGNAL('zbreplay_update(QString)'),QtCore.QString("complete"))



class ZBWireShark(QtCore.QThread):
        def __init__(self,channel,count):
                super(ZBWireShark,self).__init__()
                self.channel=channel
                self.count=count

        def __del__(self):
                self.wait()

        def close(self):
                self.terminate()

        def run(self):
                print "[*] Running ZBWireshark Thread"
		if self.count == None:
			string=" -n "+str(count)
		else:
			string=""
                p1=subprocess.Popen(str("python killerbee/tools/zbwireshark -c "+str(self.channel)+string).split())
