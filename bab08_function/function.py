# Anatomi Sebuah Function 
def hitung_luas(panjang, lebar):
    """Menghitung luas persegi panjang."""
    luas = panjang * lebar
    return luas

print(hitung_luas.__doc__)
hasil = hitung_luas(5, 3)
print(hasil)
print(hitung_luas(10, 2))
