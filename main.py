from moduletabung import *
from modulekerucut import *
from modulebola import *
from modulefunction import *

while True:
    print("""
    ===============================
    Daftar Menu
    ===============================
    0. Keluar Program
    1. Luas Permukaan Tabung
    2. Volume Tabung
    3. Luas Permukaan Kerucut
    4. Volume Kerucut
    5. Luas Permukaan Bola
    6. Volume Bola
    """)

    menu = int(input("Masukkan Pilihan Anda: "))
    if menu == 0:
        break
    elif menu == 1:
        showLPT()
    elif menu == 2:
        showVT()
    elif menu == 3:
        showLPK()
    elif menu == 4:
        showVK()
    elif menu == 5:
        showLPB()
    elif menu == 6:
        showVB()
    else:
        print("Menu Tidak Tersedia")

print("Program Selesai")