#Membaca Data dari File CSV 
# Path nilai.csv dibangun dari lokasi file ini, sehingga program dapat
# dijalankan dari folder kerja mana pun.
import csv
from pathlib import Path

NILAI_CSV = Path(__file__).resolve().with_name("nilai.csv")


def muat_data(path=NILAI_CSV):
    """Membaca nilai.csv dan mengembalikan list of dict (nilai sudah int)."""
    data = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for baris in reader:
            baris["nilai"] = int(baris["nilai"])
            data.append(baris)
    return data


if __name__ == "__main__":
    data = muat_data()
    print(len(data), "baris")
    print(data[0])
