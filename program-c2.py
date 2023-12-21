cprint("Nama:Ananda Nabila Putri")
print("NIM:231031067")
print("Prodi:Sistem Informasi")
print("Tanggal Lahir:18-02-2005")

# Operasi aritmatika
a=67
print("Nilai a =",a )
a=67
a+=1
print("Nilai a +=1 akan menjadi ",a)
a=67
a-=1
print("Nilai a -=1 akan menjadi ",a)
a =67
a*=2
print("Nilai a *=2 akan menjadi ",a)
a=67
a/=2
print("Nilai a /=2 akan menjadi ",a)
a=67
a%=2
print("Nilai a %=2 akan menjadi ",a)
a=67
a//=2
print("Nilai a //=2 akan menjadi ",a)
a=67
a**=2
print("Nilai a **=2 akan menjadi ",a)
#OR
b=True
print("Nilai b =",b)
b|=False
print("Nilai b|=False akan menjadi ",b)
b=False
print("Nilai b =",b)
b|=False
print("Nilai b|=False akan menjadi ",b)
# AND
b =True
print("Nilai b =",b)
b&=False
print("Nilai b&=False akan menjadi ",b)
b=False
print("Nilai b =",b)
b&=False
print("Nilai b&=False akan menjadi ",b)
# XOR
b=True
print("Nilai b =",b)
b^=False
print("Nilai b^=False akan menjadi ",b)
b=False
print("Nilai b =",b)
b^=False
print("Nilai b^=False akan menjadi ",b)
#Shifting
c=0b0100
print("Nilai c =',format (c ,' 04b ")
c>>=1
print("Nilai c > >=1 akan menjadi ',format (c , '04b")
c=0b0100
c<<=1
print("Nilai c < <=1 akan menjadi ',format (c , '04b")

a=7
b=12
print("================== Besar dari 12")
hasil=a>12
print(a ,"> 12 adalah ", hasil)
hasil=b >12
print(b ,"> 12 adalah ", hasil)
print("================== Kecil dari 12")
hasil=a <12
print(a ,"< 12 adalah ", hasil)
hasil=b <12
print(b ,"< 12 adalah ", hasil)
print(" ================== Besar atau sama dari 12")
hasil=a >=12
print(a ," >= 12 adalah ", hasil)
hasil=b >=12
print(b ," >= 12 adalah ", hasil )
print("================== Besar atau sama dari 12")
hasil=a <=12
print(a ," <= 12 adalah ", hasil)
hasil=b <=12
print(b ," <= 12 adalah ", hasil)
print("================== Sama dengan 12")
hasil=a ==12
print(a ,"== 12 adalah ", hasil)
hasil=b ==12
print(b ,"== 12 adalah ", hasil)

print("================== Tidak sama dengan 12")
hasil=a !=12
print(a ,"!= 12 adalah ", hasil)
hasil=b !=12
print(b ,"!= 12 adalah ", hasil)

print("============= NOT =============")
a=True
c=not a
print("a adalah ",a)
print("------c = not a- - - -- - - NOT ")
print("c adalah ",c)
print("============= OR =============")
a=True
b=True
c=a or b
print(a ,"OR ",b ,"menjadi ",c)
a=True
b=False
c=a or b
print(a ,"OR ",b ,"menjadi ",c)
a=False
b=True
c=a or b
print(a ,"OR ",b ,"menjadi ",c)
a=False
b=False
c=a or b
print(a ,"OR ",b ,"menjadi ",c)
print("============= AND ============= ")
a=True
b=True
c=a and b
print(a ,"AND ",b ,"menjadi ",c)
a=True
b=False
c=a and b
print(a ,"AND ",b ,"menjadi ",c)
a=False
b=True
c=a and b
print(a ,"AND ",b ,"menjadi ",c)
a=False
b=False
c=a and b
print(a ,"AND ",b ,"menjadi ",c)
print("============= XOR =============")
a=True
b=True
c=a ^ b
print (a ,"^",b ,"menjadi ",c)
a=True
b=False
c=a ^ b
print(a ,"^",b ,"menjadi" ,c )
a= False
b= True
c = a ^ b
print (a ,"^",b ,'menjadi',c )
a= False
b = False
c = a ^ b
print (a ,'^',b ,'menjadi',c )
# TUGAS
# Buat kode untuk masing masing operator berikut
print (" ============= NAND ============= ")
a=True
b=True
c=not(a and b)
print(a ,"NAND ",b ,"menjadi ",c)
a=True
b=False
c=not(a and b)
print(a ,"NAND ",b ,"menjadi ",c)
a=False
b=True
c=not(a and b)
print(a ,"NAND ",b ,"menjadi ",c)
a=False
b=False
c=not(a and b)
print(a ,"NAND ",b ,"menjadi ",c)
print (" ============= NOR ============== ")
a=True
b=True
c=not(a or b)
print(a ,"NOR ",b ,"menjadi ",c)
a=True
b=False
c=not(a or b)
print(a ,"NOR ",b ,"menjadi ",c)
a=False
b=True
c=not(a or b)
print(a ,"NOR ",b ,"menjadi ",c)
a=False
b=False
c=not(a or b)
print(a ,"NOR ",b ,"menjadi ",c)
print (" ============= NXOR ============= ")
a=True
b=True
c=not(a ^ b)
print(a ,"NXOR ",b ,"menjadi ",c)
a=True
b=False
c=not(a ^ b)
print(a ,"NXOR ",b ,"menjadi ",c)
a=False
b=True
c=not(a ^ b)
print(a ,"NXOR ",b ,"menjadi ",c)
a=False
b=False
c=not(a ^ b)
print(a ,"NXOR ",b ,"menjadi ",c)

print (" ======================= IN ")
nama_lengkap = " Bacharuddin Jusuf Habibie "
test = "a"
cek = test in nama_lengkap
print ( test +" terdapat di "+ nama_lengkap +" adalah "+ str( cek ))
test = "rud "
cek = test in nama_lengkap
print ( test +" terdapat di "+ nama_lengkap +" adalah "+ str( cek ))
test = "bac "
cek = test in nama_lengkap
print ( test +" terdapat di "+ nama_lengkap +" adalah "+ str( cek ))
print (" ======================= NOT IN ")
nama_lengkap = " Bacharuddin Jusuf Habibie "
test = "a"
cek = test not in nama_lengkap
print ( test +" tidak terdapat di "+ nama_lengkap +" adalah "+str ( cek ))
test = "rud "
cek = test not in nama_lengkap
print ( test +" tidak terdapat di "+ nama_lengkap +" adalah "+str ( cek ))
test = "bac "
cek = test not in nama_lengkap
print ( test +" tidak terdapat di "+ nama_lengkap +" adalah "+str ( cek ))

# TUGAS
# Dengan cara yang sama buat operator in dan not in , ubah nama lengkap menjadi nama masing - masing dengan uji test
print("==========IN======") 
nama = "Ananda Nabila Putri"

test = "an"
cek = test in nama
print(test,"terdapat di",nama,"adalah",cek)

test = "na"
cek = test in nama
print(test,"terdapat di",nama,"adalah",cek)
print()
test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama
print(test1,"terdapat di",nama,"adalah",cek)
cek = test2 in nama
print(test2,"terdapat di",nama,"adalah",cek)
cek = test3 in nama
print(test3,"terdapat di",nama,"adalah",cek)
cek = test4 in nama
print(test4,"terdapat di",nama,"adalah",cek)
cek = test5 in nama
print(test5,"terdapat di",nama,"adalah",cek)
print('=========NOT IN======')
#Tugas lanjutkan untuk NOT iN dengan cara yang sama
nama = "Ananda Nabila Putri"
test = "an"
cek = test not in nama
print(test,"terdapat di",nama,"adalah",cek)
test = "na"
cek = test not in nama
print(test,"terdapat di",nama,"adalah",cek)
print()
test1 = "a"
test2 = "i"
test3 = "u"
test4 = "e"
test5 = "o"

cek = test1 not in nama
print(test1,"terdapat di",nama,"adalah",cek)
cek = test2 not in nama
print(test2,"terdapat di",nama,"adalah",cek)
cek = test3 not in nama
print(test3,"terdapat di",nama,"adalah",cek)
cek = test4 not in nama
print(test4,"terdapat di",nama,"adalah",cek)
cek = test5 not in nama
print(test5,"terdapat di",nama,"adalah",cek)

a=18 
a+=60
b=2 
b+= 90
print ("============================= OR ")
print ("Nilai ",a ,"dalam biner = ", format (a ,"08b"))
print ("Nilai ",b ,"dalam biner = ", format (b ,"08b"))
print (" - - - - - - - - - - - - - - - - - - - - - - - - - - - -(|)")
hasil = a | b
print ("Nilai ",a ,"|",b ,"dalam biner = ", format ( hasil ,"08b"))
print ("============================= AND")
print ("Nilai ",a ,"dalam biner = ", format (a ,"08b"))
print ("Nilai ",b ,"dalam biner = ", format (b ,"08b"))
print (" - - - - - - - - - - - - - - - - - - - - - - - - - - - -(&)")
hasil = a & b
print ("Nilai ",a ,"&",b ,"dalam biner = ", format ( hasil ,"08b"))
print ("============================= XOR ")
print ("Nilai ",a ,"dalam biner = ", format (a ,"08b"))
print ("Nilai ",b ,"dalam biner = ", format (b ,"08b"))
print (" - - - - - - - - - - - - - - - - - - - - - - - - - - - -(^)")
hasil = a ^ b
print ("Nilai ",a ,"^",b ,"dalam biner = ", format ( hasil ,"08b"))
print ("============================= NOT")
print ("Nilai ",a ,"dalam biner = ", format (a ,"08b"))
print (" - - - - - - - - - - - - - - - - - - - - - - - -(~a)")
hasil = ~a
print ("Nilai ~",a ,"dalam biner = ", format ( hasil ,"08b"))
print ("Nilai ",b ,"dalam biner = ", format (b ,"08b"))
print (" - - - - - - - - - - - - - - - - - - - - - - - -(~b)")
hasil = ~b
print ("Nilai ~",b ,"dalam biner = ", format ( hasil ,"08b"))
print ("============================= > > ")
print ("Nilai ",a ,"dalam biner = ", format (a ,"08b"))
print (" - - - - - - - - - - - - - - - - - - - - - - - - - -( > >2)")
hasil = a >> 2
print ("Nilai ",a ," > >2 dalam biner = ", format ( hasil ,"08b"))
print ("Nilai ",b ,"dalam biner = ", format (b ,"08b"))
print (" - - - - - - - - - - - - - - - - - - - - - - - - - -( > >2)")
hasil = b >> 2
print ("Nilai ",b ," > >2 dalam biner = ", format ( hasil ,"08b"))

#Tugas
print("=============================NOT AND")
print("=============================NOT OR")
print("=============================NOT XOR")
print("=============================NOT (>>2)")
print("=============================NOT (<<2)")

#jawaban
print()
a=18 # ubah menjadi tanggal lahir 
a +=60
b=2 # ubah menjadi bulan lahir
b+= 90

print("=============================NOT AND")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~&)")
hasil=~(a&b)
print("Nilai",a,"~&",b,"dalam biner =", format(hasil,"08b"))

print()
print("=============================NOT OR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~|)")
hasil=~(a|b)
print("Nilai",a,"~|",b,"dalam biner =", format(hasil,"08b"))

print()
print("=============================NOT XOR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~^)")
hasil=~(a^b)
print("Nilai",a,"~^",b,"dalam biner =", format(hasil,"08b"))

print()
print( "----------------------------NOT (>>2)")
hasil= ~(a >> 2)
print("Nilai",a,"~>>2 dalam biner =", format(hasil,"08b"))

print("Nilai",b,"dalam biner     =", format(b,"08b"))
print( "----------------------------NOT (>>2)")
hasil= ~(b >> 2)
print("Nilai",b,"~>>2 dalam biner =", format(hasil,"08b"))

print()
print( "----------------------------NOT (<<2)")
hasil= ~(a << 2)
print("Nilai",a,"~<<2 dalam biner =", format(hasil,"08b"))

print("Nilai",b,"dalam biner     =", format(b,"08b"))
print( "----------------------------NOT (<<2)")
hasil= ~(b << 2)
print("Nilai",b,"~<<2 dalam biner =", format(hasil,"08b"))




