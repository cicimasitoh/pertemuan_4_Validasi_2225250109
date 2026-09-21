sudut = float(input("Masukkan besar sudut: "))

if sudut < 0 or sudut > 180:
    print("Input tidak valid. Sudut harus berada antara 0 dan 180 derajat.")
elif sudut == 180:
    print("Sudut lurus")
elif sudut > 90:
    print("Sudut tumpul")
elif sudut == 90:
    print("Sudut siku-siku")
else:
    print("Sudut lancip")