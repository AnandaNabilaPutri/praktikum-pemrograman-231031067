import os
os.system('clear')

nim = ['2','3','1','0','3','1','0','6','7']

print(nim)

print('item indeks 0 (pertama)',nim[0])
print('item indeks 1 (kedua)',nim[1])

print(f'item indeks 0 (pertama) {nim[0]}')
print(f'item indeks 1 (kedua) {nim[1]}')
print(f'item indeks terakhir) {nim[len(nim)-1]}')
print(f'item indeks terakhir {nim[-1]}')
print(f'item indeks (pertama) {nim[-len(nim)]}')

data = ['Ananda Nabila Putri',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])
print(f"{data[0]} status kuliah:{data[2]}")
print(f"data terbesar nilai adalah: {max(nilai)}")
print(f"data terkecil nilai adalah: {min(nilai)}")
x = sum(nilai) / len(nilai)
print("rata-rata nilai adalah:",x)

data = [   ['Ananda Nabila Putri',2023,'Aktif'],
       [90,89,93,97],
       (20,22),
       ('S1-Reguler','Ganjil')]
matkul = ['Matkul1',
          'matkul2',
          'matkul3',
          'matkul4',
          'matkul5']
sks = [2,3,2,3,3]
data.append(matkul)
data.append(sks)
print(data)
data[4].append('matkul6')
data[4].append('matkul7')
data[4].append('matkul8')
# mata kuliah 1; matkul1 dengan jumlah sks2
print(f'mata kuliah 1 : {data[4][0]} dengan jumlah {data[5][0]} sks')
# mata kuliah 2: matkul2 dengan sks 3
print(f'mata kuliah 2 : {data[4][1]} dengan jumlah {data[5][1]} sks')
# mata kuliah 3: matkul3 dengan sks 3
print(f'mata kuliah 3 : {data[4][2]} dengan jumlah {data[5][1]} sks')
# mata kuliah 4: matkul4 dengan sks 2
print(f'mata kuliah 4 : {data[4][3]} dengan jumlah {data[5][0]} sks')
print(f'mata kuliah 5 : {data[4][4]} dengan jumlah {data[5][1]} sks')
print(f'mata kuliah 6 : {data[4][5]} dengan jumlah {data[5][1]} sks')
print(f'mata kuliah 7 : {data[4][6]} dengan jumlah {data[5][0]} sks')
print(f'mata kuliah 8 : {data[4][7]} dengan jumlah {data[5][0]} sks')


print(data[0][0])
print(data[3][0])
print(data[2][0:]) 
