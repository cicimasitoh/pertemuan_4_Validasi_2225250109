try:
    ujian = float(input("Masukkan nilai ujian: "))
    tugas = float(input("Masukkan nilai tugas: "))
    kehadiran = float(input("Masukkan persentase kehadiran: "))

    if ujian < 0 or ujian > 100:
        print("Nilai ujian harus berada antara 0 dan 100.")

    elif tugas < 0 or tugas > 100:
        print("Nilai tugas harus berada antara 0 dan 100.")

    elif kehadiran < 0 or kehadiran > 100:
        print("Persentase kehadiran harus berada antara 0 dan 100.")

    else:
        nilai_akhir = 0.6 * ujian + 0.4 * tugas

        print(f"Nilai akhir: {nilai_akhir:.2f}")

        if kehadiran < 80:
            print("Predikat: Tidak memenuhi syarat kehadiran")
            print("Status: Belum lulus")

        else:
            if nilai_akhir >= 85:
                predikat = "A"
            elif nilai_akhir >= 70:
                predikat = "B"
            elif nilai_akhir >= 60:
                predikat = "C"
            elif nilai_akhir >= 50:
                predikat = "D"
            else:
                predikat = "E"

            if predikat in ["A", "B", "C"]:
                status = "Lulus"
            else:
                status = "Belum lulus"

            print(f"Predikat: {predikat}")
            print(f"Status: {status}")

except ValueError:
    print("Input tidak valid. Semua input harus berupa angka.")