print("===== Kalkulator Akar dan Pangkat =====")
print("Pilihan menu :")
print("1. Pangkat 2 (Kuadrat)")
print("2. Pangkat 3 (Kubik)")
print("3. Akar kuadrat")
pilih= int(input("Masukkan menu yang anda pilih : "))
if pilih==1:
    bilangan=int(input("\nMasukkan bilangan yang ingin di pangkatkan : "))
    hasil=bilangan**2
    print("Hasil dari pemangkatan bilangan",bilangan,"dengan 2 (Kuadrat) adalah",hasil)

elif pilih==2:
    bilangan=int(input("\nMasukkan bilangan yang ingin di pangkatkan : "))
    hasil=bilangan**3
    print("Hasil dari pemangkatan bilangan",bilangan,"dengan 3 (Kubik) adalah",hasil)

elif pilih==3:
    bilangan=int(input("\nMasukkan bilangan yang ingin di akarkan : "))
    hasil=bilangan**0.5
    print("Hasil akar pangkat dari bilangan",bilangan,"adalah",hasil)

else:
    print("\nPilihan menu yang dimasukkan tidak sesuai!")