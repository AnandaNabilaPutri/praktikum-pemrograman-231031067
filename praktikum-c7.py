import os
os.system('clear')

pwd_benar = 'si23c'
a = True
Limit = 3
i = 0
while a:
    i += 1
    pwd = input('Masukkan password: ')
    if pwd == pwd_benar:
        print('selamat anda berhasil lpgin!')
        a = False
    else:
        if i < Limit:
            print('password salah! coba lagi')
            print(f'kesempatan anda tersisa {limit-1} kali')
            a = True 
        else:
            print('kesempatan anda habis!')
            a = False


    