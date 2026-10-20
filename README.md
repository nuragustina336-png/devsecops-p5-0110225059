# Aplikasi Pencatat Pengeluaran — DevSecOps

## 1. Nama dan fungsi aplikasi
Aplikasi Pencatat Pengeluaran adalah program Python sederhana yang berjalan di terminal. Pengguna memasukkan nama pengeluaran dan nominal rupiah. Program menampilkan daftar pengeluaran dan totalnya. Data hanya tersimpan selama program berjalan, belum disimpan ke database.

## 2. Bahasa dan tools
- Python 3
- `unittest` untuk pengujian otomatis
- Bandit untuk SAST
- GitHub Actions untuk pipeline otomatis

## 3. Cara menjalankan aplikasi
```powershell
py main.py
```
Masukkan nama pengeluaran, misalnya `Makan`, lalu masukkan nominal, misalnya `20000`. Untuk mengakhiri input, tekan Enter ketika diminta nama pengeluaran.

## 4. Menjalankan unit test
```powershell
py -m unittest tests
```

## 5. Menjalankan pemindaian SAST
Instal dependensi menggunakan perintah:

py -m pip install -r requirements.txt

Jalankan pemindaian keamanan kode Python menggunakan Bandit:

py -m bandit -r . -x .git,.github --severity-level medium

Bandit memeriksa kode dan melaporkan temuan dengan tingkat keparahan Medium atau High. Jika ditemukan masalah yang memenuhi ambang tersebut, Bandit mengembalikan exit code nonzero sehingga job SAST pada pipeline gagal.

## 6. Overview pipeline DevSecOps
Workflow .github/workflows/devsecops.yml berjalan ketika ada push ke branch main atau pull request menuju main. Pipeline terdiri dari dua job, yaitu build dan sast-scan. Job build memasang dependensi dan menjalankan unit test. Setelah job build berhasil, job sast-scan menjalankan Bandit untuk memindai kode Python menggunakan opsi -ll, yang menetapkan ambang keparahan Medium ke atas. Jika ditemukan isu yang memenuhi ambang tersebut, pemindaian gagal dan pipeline dinyatakan gagal.
