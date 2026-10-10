# Tuple: Data yang Tidak Berubah 
titik = (3, 7)
warna = (255, 128, 0)

x, y = titik            
print(f"x={x}, y={y}")
print(warna[0], len(warna))

#tuple tidak bisa diubah, tapi bisa diganti dengan variable lain 
try:
    titik[0] = 10       
except TypeError as e:
    print(f"TypeError: {e}")
