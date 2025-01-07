def NilaiAkhir(kehadiran, tugas, uts, uas):
    na = ((0.1) * float(kehadiran) + (0.2) * float(tugas) + (0.3) * float(uts) + (0.4) * float(uas))
    return na

def NilaiMutu(nilai):
    if(na>=85):
        mutu = 'A'
    elif(na>=75):
        mutu = 'B'
    elif(na>=55):
        mutu = 'C'
    elif(na>=40):
        mutu = 'D'
    else:
        mutu = 'E'
    return mutu

kehadiran = input('Masukkan Nilai Kehadiran: ')
tugas = input('Masukkan Nilai Tugas: ')
uts = input('Masukkan Nilai UTS: ')
uas = input('Masukkan Nilai UAS: ')

na = NilaiAkhir(kehadiran, tugas, uts, uas)
print('Kehadiran : ', kehadiran)
print('Tugas : ', tugas)
print('UTS : ', uts)
print('UAS : ', uas)
print('Nilai Akhir : ', na)

mutu = NilaiMutu(na)

print('Nilai mutu :' , mutu)
