# Membuat Module & Package saya  
# Jalankan dari folder proyek/ atau dari folder mana pun:
"""Contoh penggunaan module dan package utils."""

# Contoh asli dari slide 43
from utils.hitung import rata_rata

# Contoh tambahan untuk menggunakan teks.py
from utils.teks import huruf_besar

nilai = [80, 90, 70]
print(rata_rata(nilai))

teks = "belajar python"
print(huruf_besar(teks))