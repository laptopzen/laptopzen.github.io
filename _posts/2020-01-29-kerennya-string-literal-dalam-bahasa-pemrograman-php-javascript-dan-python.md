---
layout: post
title: "Kerennya String Literal dalam Bahasa Pemrograman PHP, Javascript, dan Python"
bahasa: python
date: 2020-01-29 14:14:15 +0800
---

Biasanya kan untuk menggabungkan suatu string dengan variabel, pakai tanda khusus seperti `+` untuk Javascript dan `.` untuk PHP. Contohnya saja seperti ini:

```javascript
console.log('Halo ' + nama + ', di mana kamu tinggal?')
```

Namun, kamu tau nggak kalau sebenarnya bisa dibuat lebih keren lagi, yaitu tanpa memisahkan stringnya:

```javascript
console.log(`Halo ${nama}, di mana kamu tinggal?`)
```

## Dalam bahasa pemrograman PHP

Kalau dalam bahasa pemrograman PHP, sintaksnya adalah:

```php
$nama = 'Zen';
echo "Namaku adalah {$nama}";

// hasil: Namaku adalah Zen
```

Aku nggak tau sih ini mulai bisa digunakan sejak kapan. Tapi sih kalau aku cari-cari di Google, nggak ketemu. Kemungkinan memang fitur ini sudah ada sejak awal PHP itu ada. 

Kalau sintaks biasanya kan seperti ini:

```php
$nama = 'Zen';
echo 'Namaku adalah ' . $nama;

// hasil: Namaku adalah Zen
```

Harap diperhatikan, bahwa untuk menggunakan string literal di PHP, harus menggunakan kutip dua (`"`), bukan kutip satu (`'`). Soalnya, kalau menggunakan kutip satu, kodenya nggak jalan. Contohnya:

```php
$nama = 'Zen';
echo 'Namaku adalah {$nama}';

// hasil: Namaku adalah {$nama}
```

## Dalam bahasa pemrograman Javascript

Sintaks string literal dalam bahasa pemrograman Javascript:

```javascript
nama = 'Zen'
console.log(`Namaku adalah ${nama}`)
```

String literal dalam Javascript ini baru ada sejak tahun 2015 atau Ecmascript versi 6 (ES6). Jadi, memang termasuk fitur yang baru. Namun, kamu nggak perlu khawatir karena sekarang rata-rata browser sudah mendukung Ecmascript 6.

## Dalam bahasa pemrograman Python

Kalau dalam bahasa Python:

```python
nama = 'Zen'
print(f'Namaku adalah {nama}')
```

String literal dalam bahasa Python ini baru ada sejak Python versi 3.6 atau mulai diluncurkannya pada tahun 2015. Kalau kamu belum menggunakan versi 3.6, coba langkah-langkah di bawah ini untuk menginstallnya:

Tambahkan dulu repositori untuk Python 3.6:

```bash
sudo add-apt-repository ppa:jonathonf/python-3.6
```

Lalu, update dan install:

```bash
sudo apt update
sudo apt install python3.6
```

Untuk menjalankannya, cukup dengan perintah:

```bash
python3.6 nama-file.py
```

Itu untuk Linux. Tapi kalau kamu pengguna Windows, bisa download langsung aja dari situsnya Python.