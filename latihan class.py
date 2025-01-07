import math
class Tabung:
    def __init__(self):
        self.__jarijari = None
        self.__tinggi = None
        self.__phi = 3.14

    #Atribut Jari-jari
    @property
    def jarijari(self):
        return self.__jarijari

    @jarijari.setter
    def jarijari(self, value):
        self.__jarijari = value

    #Atribut tinggi
    @property
    def tinggi(self):
        return self.__tinggi

    @tinggi.setter
    def tinggi(self, value):
        self.__tinggi = value

    #Metode 
    def Volume(self):
        V = self.__phi * self.__jarijari * self.__jarijari * self.__tinggi
        return V

    def Luas(self):
        L = 2 * self.__phi * self.__jarijari + (self.__jarijari + self.__tinggi)
        return L

T = Tabung()
j = float(input('Masukkan jari-jari Tabung :'))
t = float(input('Masukkan tinggi Tabung :'))
T.jarijari = j
T.tinggi = t
V = T.Volume()
L = T.Luas()
print('Jari-jari Tabung : ', j)
print('tinggi Tabung : ', t)
print('volume Tabung : ', V)
print('Luas Tabung : ', L)