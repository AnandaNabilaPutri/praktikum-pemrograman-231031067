import os
import random as rd
os.system('clear')

warna = {'merah','putih','hitam'}
com = rd.choice(warna)
a = True 

while a:
    pilih = input('masukkan pilihan [merah,putih,hitam]:')
    if pilih == com:
        print(f'pilihan anda benar yaitu {pilih} \n')
        a = False 
else:
    print('Tebakan anda salah! coba lagi.')