# try - except - else - finally
# Program ini interaktif. Coba tiga jenis masukan: 0, abc, dan 5.
try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka
except ValueError:
    print("Harus berupa angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi nol!")
else:
    print(f"Hasil: {hasil}")
finally:
    print("Selesai.")
