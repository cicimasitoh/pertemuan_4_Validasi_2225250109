try:
    nilai = float(input("Masukkan nilai: "))

    if nilai < 0 or nilai > 100:
        print("Input tidak valid. Nilai harus berada antara 0 sampai 100.")
    else:
        print(f"Nilai valid: {nilai:.2f}")

except ValueError:
    print("Input tidak valid. Masukkan angka.")