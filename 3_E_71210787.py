nama= input("Masukkan daftar siswa : ") 
nama_kapital= nama.title()
array_nama=nama_kapital.split(", ")

print(array_nama)
nama_2= input("Masukkan siswa yang ingin ditambahkan : ")
nama_2_kapital= nama_2.title()
array_nama_2= nama_2_kapital.split()

if array_nama[0] == nama_2_kapital:
    print("Siswa atas nama",nama_2_kapital.upper(),"sudah berada dalam daftar siswa")
elif array_nama[1] == nama_2_kapital:
    print("Siswa atas nama",nama_2_kapital.upper(),"sudah berada dalam daftar siswa")
elif array_nama[2] == nama_2_kapital:
    print("Siswa atas nama",nama_2_kapital.upper(),"sudah berada dalam daftar siswa")
else:
    nama_2_kapital= nama_2.upper()
    array_nama.append(nama_2_kapital)
    print("Hasil penambahan daftar nama siswa",array_nama)