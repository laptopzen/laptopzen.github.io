---
layout: post
title: Menggabungkan Banyak File Menjadi Satu di Linux dan Windows
bahasa: bash
---

Terkadang kita perlu menggabungkan banyak file menjadi satu file aja. Misalnya, aku ingin menjalankan `index.js` di Console tapi bakalan nggak efisien jika aku menulis semua kode dalam satu file. Maka, aku memecahnya menjadi dua yaitu `data.js` dan `proses.js`.

Lalu, bagaimana cara menggabungkannya?

**Untuk pengguna Linux**

Buat file `gabung.sh` yang berisikan:

```bash
cat data.js proses.js > index.js
```

Lalu untuk menjalankannya adalah dengan perintah: `bash gabung.sh`.

**Untuk pengguna Windows**

Buat file `gabung.bat` yang isinya:

```bash
copy /v /b data.js + proses.js index.js
```

Untuk menggunakannya, tinggal double click.