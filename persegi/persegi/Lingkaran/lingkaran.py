
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
import math
import sys

qtcreator_file = "lingkaran.ui"
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
        luas = math.pi * (jari * jari)
        keliling = 2 * math.pi * jari
        self.txtLuas.setText(str(luas))
        self.txtKeliling.setText(str(keliling))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    persegi = MyPersegiWindow()
    persegi.show() # Show in normal mode
    sys.exit(app.exec_())