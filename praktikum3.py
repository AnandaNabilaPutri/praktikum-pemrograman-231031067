print('praktikum 3')

nama = 'ananda nabila putri'
nim = '231031067'
meet = 'praktikum 3'
prodi = 'Sistem Informasi C'
email = 'anandanabilaputri365@gmail.com'
sp =40
print('-'*sp)
print(nama.center(sp))
print(nim.center(sp))
print('-'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.lower().rjust(sp))

print(f''' Halo,nama saya Ananda Nabila Putri dengan NIM 231031067 dari prodi Sistem Informasi, ini adalah file praktikum c3. Terima Kasih.\n''')

print(f'''Biodata saya,
Nama\t =('Ananda Nabila Putri.upper())'
NIM\t ='(231031067')
Prodi\t ='Sistem Informasi C'
TTL\t ='(Parepare,18 Februari 2005)'
Alamat\t ='(Jl.Sejahtera)'
Asal\t ='(Parepare)'
Hobi\t ='(Memasak)'
Tinggi =150
''')
 
stat1 = 'duFort Frankel Sir Issac'
up = stat1.split(" ")
print(up[-1]," ".join(up[0:3]))
# Issac duFort Frankel Sir

stat2 = 'duFort Frankel Sir Issac'
up2 = stat2.split(" ")
print(f'{up2[0][0]} {up2[1][0]} {up2[2][0]} {up2[3]}')
# d F S Issac

stat3 = 'duFort Frankel Sir Issac'
up3 = stat3.split(" ")
print(f'{up3[0]} {up3[1][0]} {up3[2][0]} {up3[3][0]}')
# duFort F S I

stat4 = 'duFort Frankel Sir Issac'
up4 = stat4.split(" ")
print(f'{up4[3][0]} {up4[0]} {up4[1]} {up4[2]}')
# I duFort Frankel Sir

stat5 = 'duFort Frankel Sir Issac'
up5 =stat5.split(" ")
print(f'{up5[3]} {up5[0][0]} {up5[1][0]} {up5[2][0]}')
# Issac d F S

stat6 = 'duFort Frankel Sir Issac'
up6 = stat6.upper().split(" ")
print(f'{up6[3]} {up6[0][0]} {up6[1][0]} {up6[2][0]}')
# ISSAC D F S

stat7 = '#duFort Frankel Sir Issac$'
up7 = stat7.split(" ")
print(f'{up7[0].strip("#")} {up7[1]} {up7[2]} {up7[3].upper().strip("$")}')
# duFort Frankel Sir Issac

stat8 = '#duFort-Frankel-Sir-Issac$'
up8 = stat8.split("-")
print(f'{up8[0].strip("#")} {up8[1]} {up8[2]} {up8[3].strip("$")}')
# duFort Frankel Sir Issac

stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
up9 = stat9.split(" ")
print(up9)
print(f'{up9[0].strip("#@")} {up9[1].strip("^*")} {up9[2].strip("(")} {up9[3].strip("($")}')
# duFort Frankel Sir Issac

stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
up10 = stat10.upper().split("-")
print(f'{up10[0].strip("#@")} {up10[1].strip("^*")} {up10[2].strip("(")} {up10[3].strip("($")}')
# DUFORT FRANKEL SIR ISSAC





