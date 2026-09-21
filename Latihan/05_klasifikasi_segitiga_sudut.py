sudut1 = float(input("Masukkan sudut pertama: "))
sudut2 = float(input("Masukkan sudut kedua: "))
sudut3 = float(input("Masukkan sudut ketiga: "))

jumlah = sudut1 + sudut2 + sudut3

if sudut1 <= 0 or sudut2 <= 0 or sudut3 <= 0:
    print("Input tidak valid. Semua sudut harus lebih dari 0.")
elif jumlah != 180:
    print("Bukan segitiga. Jumlah sudut harus 180 derajat.")
elif sudut1 > 90 or sudut2 > 90 or sudut3 > 90:
    print("Segitiga tumpul")
elif sudut1 == 90 or sudut2 == 90 or sudut3 == 90:
    print("Segitiga siku-siku")
else:
    print("Segitiga lancip")