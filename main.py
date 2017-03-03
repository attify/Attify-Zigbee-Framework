from PyQt4 import QtCore,QtGui
from UI.Main import Ui_MainWindow
from UI.Config import Ui_Form
import sys

class ZBMain(Ui_MainWindow):
	def __init__(self,dialog,parent=None):
		Ui_MainWindow.__init__(self)
		self.setupUi(dialog)

if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	dialog=QtGui.QMainWindow()
        app.setWindowIcon(QtGui.QIcon("UI/icon.png"))
	prog=ZBMain(dialog)
	dialog.show()
	sys.exit(app.exec_())
