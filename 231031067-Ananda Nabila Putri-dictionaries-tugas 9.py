biodata = {"nama"   : "Ananda Nabila Putri",
           "nim"    : 231031067,
           "prodi"  : "Sistem Informasi C",
           "umur"   : 18,
           "hobi"   : {"hb1" : "Menyanyi",
                       "hb2" : "Memasak" },
           "asal"   : "Parepare",
           "alamat" : "Jalan Sejahtera km.2"
           }

print(f"""
Nama Saya  : {biodata['nama']}
Dengan NIM : {biodata['nim']}
Dari Prodi : {biodata['prodi']}
Umur saya  : {biodata['umur']}
Hobi Saya  : {biodata['hobi']["hb2"]}
Asal saya  : {biodata['asal']}
Alamat saya: {biodata['alamat']}
""")
