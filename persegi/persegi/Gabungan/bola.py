
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
import sys

qtcreator_file = "bola.ui"
Ui_PersegiWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyPersegiWindow(QtWidgets.QMainWindow, Ui_PersegiWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_PersegiWindow.__init__(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.btnHitung.clicked.connect(self.hitung)

    def hitung(self):
        jari = float(self.txtJari.text())
        phi=(22/7)
        volume = int((4/3)*phi*(jari*jari*jari))
        luas = int(4*phi*(jari*jari))
        self.txtLuas.setText(str(luas))
        self.txtVolume.setText(str(volume))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    persegi = MyPersegiWindow()
    persegi.show() # Show in normal mode
    sys.exit(app.exec_())