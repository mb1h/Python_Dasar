# Python Dasar

## Deskripsi Proyek

Proyek ini saya buat untuk mempraktikkan materi **Python Dasar** yang terdiri dari 11 bab dalam file PDF perkuliahan. Saya menyusun contoh-contoh program berdasarkan topik setiap bab agar lebih mudah dipelajari, dijalankan, dan diperiksa kembali.

Saya memisahkan kode ke dalam folder dan file berdasarkan fungsinya. Dengan susunan ini, setiap materi dapat dipelajari secara bertahap, mulai dari program pertama, variabel, operator, percabangan, dan perulangan, sampai function, module, package, serta pengolahan data sederhana.

Pada beberapa contoh, saya juga mengatur kode agar lebih mudah dijalankan sebagai file terpisah. Contohnya terdapat pada Bab 11, ketika proses membaca data CSV digunakan kembali oleh program untuk menghitung rata-rata, mencari nilai tertinggi, dan membuat rekap nilai berdasarkan kelas.

Proyek ini berfokus pada latihan dasar Python, bukan pada pembuatan satu aplikasi besar.

## Tujuan Pembelajaran

Melalui proyek ini, saya berlatih untuk:

1. Menulis dan menjalankan program Python dari terminal.
2. Menggunakan variabel dan memahami tipe data dasar.
3. Menerima input pengguna serta menampilkan output.
4. Menggunakan operator aritmatika, perbandingan, logika, penugasan, dan keanggotaan.
5. Membuat keputusan menggunakan `if`, `elif`, `else`, dan `match-case`.
6. Menggunakan perulangan `for` dan `while`, serta `break`, `continue`, dan `pass`.
7. Mengelola kumpulan data menggunakan `list`, `tuple`, `set`, dan `dictionary`.
8. Membuat function dengan parameter, return value, `*args`, `**kwargs`, dan `lambda`.
9. Memahami dan menangani error menggunakan `try`, `except`, `else`, `finally`, dan `raise`.
10. Menggunakan module serta menyusun package Python sederhana.
11. Membaca file CSV, menyaring data, menghitung rata-rata, mencari nilai tertinggi, dan membuat rekap menggunakan Python serta pandas.

## Cakupan Materi

Materi dalam proyek ini dibagi menjadi 11 bab sesuai urutan materi Python Dasar.

| Bab | Materi | Folder |
|---|---|---|
| 01 | Pengenalan Python | `bab01_pengenalan/` |
| 02 | Variabel dan Tipe Data | `bab02_variabel_tipe_data/` |
| 03 | Input dan Output | `bab03_input_output/` |
| 04 | Operator | `bab04_operator/` |
| 05 | Percabangan | `bab05_percabangan/` |
| 06 | Perulangan | `bab06_perulangan/` |
| 07 | Struktur Data Koleksi | `bab07_koleksi_data/` |
| 08 | Function | `bab08_function/` |
| 09 | Error Handling | `bab09_error_handling/` |
| 10 | Module dan Package | `bab10_module_package/` |
| 11 | Pengolahan Data Sederhana | `bab11_pengolahan_data/` |

## Struktur Folder Proyek

Berikut susunan folder dan file yang saya gunakan beserta fungsi masing-masing.

```text
Python_Dasar/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .venv/                         # Lingkungan lokal
│
├── bab01_pengenalan/
│   └── hello.py
│
├── bab02_variabel_tipe_data/
│   ├── variabel.py
│   ├── casting.py
│   └── string.py
│
├── bab03_input_output/
│   ├── output.py
│   └── input.py
│
├── bab04_operator/
│   ├── aritmatika.py
│   ├── logika.py
│   └── operator.py
│
├── bab05_percabangan/
│   ├── if_else.py
│   ├── grade.py
│   ├── nested.py
│   ├── ternary.py
│   └── match.py
│
├── bab06_perulangan/
│   ├── for_loop.py
│   ├── while_loop.py
│   └── kontrol.py
│
├── bab07_koleksi_data/
│   ├── list.py
│   ├── tuple.py
│   ├── set.py
│   └── dictionary.py
│
├── bab08_function/
│   ├── function.py
│   ├── parameter.py
│   ├── lambda.py
│   └── scope.py
│
├── bab09_error_handling/
│   ├── try_except.py
│   └── raise.py
│
├── bab10_module_package/
│   ├── pakai_module.py
│   └── proyek/
│       ├── main.py
│       └── utils/
│           ├── __init__.py
│           ├── hitung.py
│           └── teks.py
│
└── bab11_pengolahan_data/
    ├── nilai.csv
    ├── baca_data.py
    ├── olah_data.py
    ├── rekap.py
    └── pakai_pandas.py
```

### Penjelasan File Utama

#### 1. Konfigurasi Proyek

- `README.md`: Dokumentasi proyek yang menjelaskan tujuan, struktur folder, persiapan lingkungan, dan cara menjalankan program.
- `requirements.txt`: Daftar package Python beserta versi yang tercatat dalam lingkungan pengembangan.
- `.gitignore`: Daftar file dan folder yang tidak perlu dilacak oleh Git, seperti `.venv`, `__pycache__`, dan file bytecode Python.
- `.venv/`: Virtual environment yang digunakan di komputer pengembangan. Folder ini bersifat lokal dan tidak perlu disertakan dalam repositori atau arsip pengumpulan.

#### 2. Bab 01 — Pengenalan Python

Folder `bab01_pengenalan/` berisi:

- `hello.py`: Program pertama untuk menampilkan teks menggunakan `print()`. Contoh ini juga memperlihatkan komentar, variabel, perbandingan sederhana, dan indentasi.

#### 3. Bab 02 — Variabel dan Tipe Data

Folder `bab02_variabel_tipe_data/` berisi:

- `variabel.py`: Membahas pembuatan variabel, aturan penamaan, assignment, dan tipe data dasar.
- `casting.py`: Mempraktikkan konversi tipe data dengan `int()`, `float()`, `str()`, dan `bool()`.
- `string.py`: Membahas pengolahan string menggunakan `len()`, `upper()`, slicing, `split()`, dan f-string.

#### 4. Bab 03 — Input dan Output

Folder `bab03_input_output/` berisi:

- `output.py`: Menampilkan beberapa nilai menggunakan `print()`, mengatur pemisah dan akhir output dengan `sep` dan `end`, serta memformat angka.
- `input.py`: Menerima nama dan umur pengguna, mengonversi input umur menjadi integer, lalu menampilkan hasilnya.

File `input.py` bersifat interaktif karena membutuhkan masukan dari pengguna.

#### 5. Bab 04 — Operator

Folder `bab04_operator/` berisi:

- `aritmatika.py`: Mempraktikkan operator matematika, termasuk penjumlahan, pengurangan, perkalian, pembagian, modulus, pembagian bulat, dan pangkat.
- `logika.py`: Membahas operator perbandingan serta operator logika `and`, `or`, dan `not`.
- `operator.py`: Mempraktikkan operator penugasan seperti `+=` dan `*=`, serta operator keanggotaan `in` dan `not in`.

#### 6. Bab 05 — Percabangan

Folder `bab05_percabangan/` berisi:

- `if_else.py`: Mengambil keputusan berdasarkan satu kondisi.
- `grade.py`: Menentukan grade berdasarkan beberapa kondisi menggunakan `if`, `elif`, dan `else`.
- `nested.py`: Mempraktikkan percabangan bersarang atau `nested if`.
- `ternary.py`: Menulis ekspresi kondisi dalam satu baris.
- `match.py`: Menggunakan `match-case` untuk memilih tindakan berdasarkan nilai tertentu.

#### 7. Bab 06 — Perulangan

Folder `bab06_perulangan/` berisi:

- `for_loop.py`: Mengulang data menggunakan `for` dan `range()`.
- `while_loop.py`: Mengulang program selama kondisi bernilai `True`.
- `kontrol.py`: Mempraktikkan `break`, `continue`, dan `pass` untuk mengatur alur perulangan.

#### 8. Bab 07 — Struktur Data Koleksi

Folder `bab07_koleksi_data/` berisi:

- `list.py`: Membuat dan mengubah list, menambahkan atau menghapus elemen, serta mengurutkan data.
- `tuple.py`: Mempraktikkan tuple, indexing, unpacking, dan contoh kesalahan ketika mencoba mengubah elemen tuple.
- `set.py`: Mengelola kumpulan nilai unik menggunakan operasi union, intersection, dan difference.
- `dictionary.py`: Menyimpan data dalam pasangan key-value, mengakses nilai, memperbarui data, dan mengulangi pasangan key-value.

#### 9. Bab 08 — Function

Folder `bab08_function/` berisi:

- `function.py`: Membuat function dengan `def`, parameter, `return`, dan docstring untuk menghitung luas persegi panjang.
- `parameter.py`: Membahas parameter default, keyword argument, `*args`, dan `**kwargs`.
- `lambda.py`: Menggunakan lambda untuk membuat function sederhana serta memilih data berdasarkan suatu nilai.
- `scope.py`: Memperlihatkan perbedaan variabel lokal dan global.

#### 10. Bab 09 — Error Handling

Folder `bab09_error_handling/` berisi:

- `try_except.py`: Menangani input yang tidak valid dan pembagian dengan nol menggunakan `try`, `except`, `else`, dan `finally`.
- `raise.py`: Memunculkan `ValueError` ketika umur yang diberikan tidak valid, lalu menangani error tersebut.

#### 11. Bab 10 — Module dan Package

Folder `bab10_module_package/` berisi:

- `pakai_module.py`: Menggunakan module bawaan Python, yaitu `math`, `random`, dan `datetime`.
- `proyek/main.py`: Program utama yang mengimpor function `rata_rata()` dari package `utils` dan menampilkan rata-rata data.
- `proyek/utils/__init__.py`: File penanda package `utils`.
- `proyek/utils/hitung.py`: Berisi function `rata_rata()` untuk menghitung rata-rata sekumpulan angka.
- `proyek/utils/teks.py`: Berisi function tambahan `huruf_besar()` untuk mengubah teks menjadi huruf kapital.

Pada contoh ini, saya memisahkan function ke dalam module agar dapat digunakan dari file lain melalui `import`. File `teks.py` menjadi latihan tambahan untuk memahami pembuatan module sendiri.

#### 12. Bab 11 — Pengolahan Data Sederhana

Folder `bab11_pengolahan_data/` berisi:

- `nilai.csv`: File data siswa yang berisi nama, kelas, dan nilai.
- `baca_data.py`: Membaca file CSV menggunakan `csv.DictReader`, mengubah nilai menjadi integer, dan menyediakan function `muat_data()` untuk digunakan kembali.
- `olah_data.py`: Menghitung rata-rata seluruh nilai, menampilkan daftar siswa yang memenuhi nilai minimum 75, dan mencari siswa dengan nilai tertinggi.
- `rekap.py`: Mengelompokkan nilai berdasarkan kelas, menghitung jumlah siswa, dan menghitung rata-rata setiap kelas.
- `pakai_pandas.py`: Mempraktikkan pengolahan data yang sama menggunakan pandas, termasuk `read_csv()`, `groupby()`, filtering, dan pengurutan data.

Pada bab ini, data dibaca dari satu file CSV agar contoh pengolahan data menggunakan sumber yang sama.

## Persyaratan Sistem

Untuk menjalankan contoh program dalam proyek ini, saya menggunakan:

- Python 3.11 atau lebih baru.
- Visual Studio Code atau editor kode Python lainnya.
- Terminal PowerShell pada Windows untuk contoh perintah di bawah.
- Package eksternal yang tercantum dalam `requirements.txt`, terutama pandas untuk contoh pada Bab 11.

Contoh `match-case` pada Bab 05 membutuhkan Python 3.10 atau lebih baru. Saya menyarankan penggunaan versi Python yang kompatibel dengan semua dependency dalam `requirements.txt`.

## Persiapan Lingkungan

Virtual environment `.venv` sudah tersedia pada komputer pengembangan saya. Langkah berikut ditujukan jika proyek dijalankan pada komputer lain atau jika lingkungan perlu dibuat kembali.

Jalankan perintah berikut dari folder utama `Python_Dasar` di PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Perintah pertama membuat virtual environment. Perintah kedua mengaktifkannya, sedangkan perintah ketiga memasang package yang tercatat dalam `requirements.txt`.

Untuk memeriksa versi Python yang sedang digunakan:

```powershell
python --version
```

Untuk memeriksa lokasi interpreter Python:

```powershell
python -c "import sys; print(sys.executable)"
```

Jika virtual environment sudah aktif, lokasi interpreter seharusnya mengarah ke folder `.venv`.

## Cara Menjalankan Program

Semua perintah berikut dijalankan dari folder utama `Python_Dasar`, yaitu folder yang berisi `README.md`.

### Bab 01 — Pengenalan Python

```powershell
python bab01_pengenalan\hello.py
```

### Bab 02 — Variabel dan Tipe Data

```powershell
python bab02_variabel_tipe_data\variabel.py
python bab02_variabel_tipe_data\casting.py
python bab02_variabel_tipe_data\string.py
```

### Bab 03 — Input dan Output

```powershell
python bab03_input_output\output.py
python bab03_input_output\input.py
```

Pada `input.py`, masukkan nama ketika diminta, kemudian masukkan umur dalam bentuk angka.

### Bab 04 — Operator

```powershell
python bab04_operator\aritmatika.py
python bab04_operator\logika.py
python bab04_operator\operator.py
```

### Bab 05 — Percabangan

```powershell
python bab05_percabangan\if_else.py
python bab05_percabangan\grade.py
python bab05_percabangan\nested.py
python bab05_percabangan\ternary.py
python bab05_percabangan\match.py
```

### Bab 06 — Perulangan

```powershell
python bab06_perulangan\for_loop.py
python bab06_perulangan\while_loop.py
python bab06_perulangan\kontrol.py
```

### Bab 07 — Struktur Data Koleksi

```powershell
python bab07_koleksi_data\list.py
python bab07_koleksi_data\tuple.py
python bab07_koleksi_data\set.py
python bab07_koleksi_data\dictionary.py
```

### Bab 08 — Function

```powershell
python bab08_function\function.py
python bab08_function\parameter.py
python bab08_function\lambda.py
python bab08_function\scope.py
```

### Bab 09 — Error Handling

```powershell
python bab09_error_handling\try_except.py
python bab09_error_handling\raise.py
```

Untuk menguji `try_except.py`, saya dapat memasukkan nilai `0`, teks `abc`, atau angka `5`. Setiap input memperlihatkan cara program menangani kondisi yang berbeda.

### Bab 10 — Module dan Package

```powershell
python bab10_module_package\pakai_module.py
python bab10_module_package\proyek\main.py
```

Program `pakai_module.py` menggunakan angka acak, sehingga nilai yang tercetak dapat berbeda setiap kali dijalankan. Program `proyek/main.py` menjalankan contoh penggunaan function `rata_rata()` dari package `utils`.

### Bab 11 — Pengolahan Data Sederhana

```powershell
python bab11_pengolahan_data\baca_data.py
python bab11_pengolahan_data\olah_data.py
python bab11_pengolahan_data\rekap.py
python bab11_pengolahan_data\pakai_pandas.py
```

File `nilai.csv` dibaca oleh program di dalam folder yang sama. Data tersebut digunakan untuk menghitung rata-rata, menentukan siswa yang memenuhi nilai minimum 75, mencari nilai tertinggi, dan membuat rekap nilai per kelas.

## Pengujian Program

Saya memeriksa program berdasarkan fungsi masing-masing file dan membandingkan hasilnya dengan tujuan contoh pada materi.

Untuk memeriksa sintaks semua file Python, jalankan perintah berikut dari folder utama:

```powershell
python -m compileall -q bab01_pengenalan bab02_variabel_tipe_data bab03_input_output bab04_operator bab05_percabangan bab06_perulangan bab07_koleksi_data bab08_function bab09_error_handling bab10_module_package bab11_pengolahan_data
```

Jika tidak ada pesan error, pemeriksaan sintaks berhasil. Namun, pemeriksaan ini hanya memeriksa sintaks dan tidak menggantikan pengujian program saat dijalankan.

Beberapa contoh memerlukan perlakuan khusus:

- `input.py` membutuhkan input dari pengguna.
- `try_except.py` perlu diuji dengan input yang berbeda untuk melihat setiap jalur penanganan error.
- `tuple.py` menampilkan `TypeError` yang memang disengaja ketika program mencoba mengubah elemen tuple. Error tersebut ditangkap agar program dapat menampilkan pesannya lalu berakhir normal.
- `raise.py` menampilkan pesan ketika umur yang diberikan tidak valid.
- `pakai_module.py` menampilkan angka acak, sehingga hasil angka tidak selalu sama.
- Urutan elemen yang ditampilkan oleh `set.py` dapat berbeda, tetapi anggota set-nya tetap sesuai dengan data.
- `pakai_pandas.py` membutuhkan pandas yang terpasang pada lingkungan Python yang digunakan.

## Dependensi

Python menyediakan beberapa module bawaan yang dipakai dalam proyek ini, seperti `csv`, `math`, `random`, `datetime`, dan `pathlib`. Module tersebut tidak perlu dipasang secara terpisah.

Package eksternal dicatat dalam `requirements.txt`. Di antaranya:

| Package | Penggunaan |
|---|---|
| `pandas` | Membaca, memfilter, mengelompokkan, dan meringkas data CSV pada Bab 11. |
| `requests` | Dicantumkan dalam contoh instalasi package pada materi Bab 10; belum digunakan secara langsung oleh file program dalam proyek ini. |

Package lain dalam `requirements.txt` merupakan dependency yang diperlukan oleh package yang tercatat di sana.

## Catatan Penggunaan

- Folder `.venv` hanya digunakan pada lingkungan lokal. Folder ini tidak perlu diunggah ke GitHub atau disertakan dalam arsip pengumpulan karena lingkungan dapat dibuat kembali.
- File `.gitignore` membantu Git mengabaikan folder lingkungan dan file sementara. File ini tidak menghapus file dari komputer.
- File `requirements.txt` digunakan untuk memasang dependency proyek pada lingkungan yang baru.
- Struktur folder dibuat mengikuti urutan bab agar setiap contoh lebih mudah ditemukan dan diperiksa.
- Jika saya menambahkan atau mengubah contoh, saya akan memperbarui dokumentasi agar nama file dan fungsinya tetap sesuai dengan isi proyek.

