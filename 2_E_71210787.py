suhu = float(input("Masukkan suhu tubuh anda : "))
if suhu>50:
    print("Anda bukan manusia :)")
elif suhu>37.5:
    print("Anda demam! Jangan berbergian ke tempat fasilitas umum")
elif suhu>=32:
    print("Suhu anda normal!")
else:
    print("Anda kedinginan! Silakan cari sesuatu yang hangat!")