# Filter, Hitung & Cari Nilai Tertinggi
# Memakai muat_data() dari baca_data.py (satu folder), jadi tidak perlu
# variabel `data` yang dibuat manual.
from baca_data import muat_data

data = muat_data()

nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)
print(f"Rata-rata: {rata:.1f}")

lulus = [d["nama"] for d in data
         if d["nilai"] >= 75]
print("Lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("Tertinggi:", top["nama"])
