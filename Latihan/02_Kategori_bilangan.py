bilangan = int(input("Masukkan bilangan: "))

if bilangan < 0:
    kategori = "Negatif"
elif bilangan == 0:
    kategori = "Nol"
elif bilangan % 2 == 0:
    kategori = "Positif Genap"
else:
    kategori = "Positif Ganjil"

print(f"Bilangan: {bilangan}")
print(f"Kategori: {kategori}")