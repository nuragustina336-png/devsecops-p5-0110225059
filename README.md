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
```powershell
py -m pip install -r requirements.txt
py -m bandit -r . -x .git,.github -ll
```

## 6. Overview pipeline DevSecOps
Workflow `.github/workflows/devsecops.yml` berjalan saat ada push ke branch `main` atau pull request menuju `main`. Job `build` menjalankan unit test. Setelah job tersebut berhasil, job `sast-scan` menjalankan Bandit. Pemindaian menggunakan `-ll` sehingga pipeline gagal jika ditemukan isu berkeparahan Medium atau High.
