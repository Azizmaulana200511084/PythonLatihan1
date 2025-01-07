from moduletabung import *
from modulekerucut import *
from modulebola import *

T = Tabung()
K = Kerucut()
B = Bola()

def showLPT():
    T.jarijaritabung = int(input("Masukkan Jari-jari Tabung : "))
    T.tinggitabung = int(input("Masukkan Tinggi Tabung : "))
    print(f"Luas Permukaan Tabung : {T.LuasPermukaanTabung()} cm")

def showVT():
    T.jarijaritabung = int(input("Masukkan Jari-jari Tabung : "))
    T.tinggitabung = int(input("Masukkan Tinggi Tabung : "))
    print(f"Volume Tabung : {T.VolumeTabung()} cm")

def showLPK():
    K.jarijarikerucut = int(input("Masukkan Jari-jari Kerucut : "))
    K.garispelukis = int(input("Masukkan Garis Pelukis Kerucut : "))
    print(f"Luas Permukaan Kerucut : {K.LuasPermukaanKerucut()} cm")

def showVK():
    K.jarijarikerucut = int(input("Masukkan Jari-jari Kerucut : "))
    K.tinggikerucut = int(input("Masukkan Tinggi Kerucut : "))
    print(f"Volume Kerucut : {K.VolumeKerucut()} cm")

def showLPB():
    B.jarijaribola = int(input("Masukkan Jari-jari Bola : "))
    print(f"Luas Permukaan Bola : {B.LuasPermukaanBola()} cm")

def showVB():
    B.jarijaribola = int(input("Masukkan Jari-jari Bola : "))
    print(f"Volume Bola : {B.VolumeBola()} cm")