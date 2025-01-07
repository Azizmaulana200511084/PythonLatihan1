
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
import sys

qtcreator_file = "segitiga.ui"
Ui_PersegiWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyPersegiWindow(QtWidgets.QMainWindow, Ui_PersegiWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_PersegiWindow.__init__(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.btnHitung.clicked.connect(self.hitung)

    def hitung(self):
        alas = float(self.txtAlas.text())
        tinggi = float(self.txtTinggi.text())
        sisi_a = float(self.txtSisia.text())
        sisi_b = float(self.txtSisib.text())
        sisi_c = float(self.txtSisic.text())
        luas= 0.5 * alas * tinggi
        keliling = sisi_a + sisi_b + sisi_c
        self.txtLuas.setText(str(luas))
        self.txtKeliling.setText(str(keliling))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    persegi = MyPersegiWindow()
    persegi.show() # Show in normal mode
    sys.exit(app.exec_())