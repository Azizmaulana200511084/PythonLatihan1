from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
import sys

qtcreator_file = "balok.ui"
Ui_PersegiWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyPersegiWindow(QtWidgets.QMainWindow, Ui_PersegiWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_PersegiWindow.__init__(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.btnHitung.clicked.connect(self.hitung)

    def hitung(self):
        panjang = float(self.txtLebar.text())
        lebar = float(self.txtLebar.text())
        tinggi = float(self.txtTinggi.text())
        luas_permukaan = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
        volume = panjang * lebar * tinggi
        self.txtLuas.setText(str(luas_permukaan))
        self.txtVolume.setText(str(volume))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    persegi = MyPersegiWindow()
    persegi.show() # Show in normal mode
    sys.exit(app.exec_())