from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
import sys

qtcreator_file = "search.ui"
Ui_PersegiWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyPersegiWindow(QtWidgets.QMainWindow, Ui_PersegiWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_PersegiWindow.__init__(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.btnCari.clicked.connect(self.cari)

    def hitung(self):
        Text = ("\n\t<<<Selamat datang di Kabupaten Cirebon>>>")
        print (Text)
        Search = float(self.txtSearch.text())
        Ganti = float(self.txtGanti.text())
        hasil = (Text.replace(Search, Ganti))
        self.txtCari.setText(str(hasil))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    persegi = MyPersegiWindow()
    persegi.show() # Show in normal mode
    sys.exit(app.exec_())