---
layout: post
title: Udah Kenal Termux Path? Tools Powerful untuk Hacking
bahasa: bash
---

Biasanya kan kalau untuk hacking menggunakan HP, kita menggunakan Termux. Nah, Termux ini bisa dibilang ya Linuxnya Android walaupun hanya kita ambil dari segi Terminalnya aja.

Nah, pernah nggak sih kamu menemukan perintah yang panjang? Misalnya seperti kode di bawah ini:

```bash
git status
git add -A .
git commit -m "upload"
git push
```

Lalu, bagaimana cara mengetikkannya di Termux? Apakah menuliskannya secara full empat baris di atas? Bagaimana jika kita ingin memasukkan kode tersebut berkali-kali? Berarti mengetikkan empat baris di atas berkali-kali dong?

Nah, makanya aku membuat Termux Path.

Dengan Termux Path, aku bisa menyederhanakan perintah panjang di atas hanya dengan `upload`.

Ini buktinya:

![contoh hasil dari termux path](https://telegra.ph/file/91ccf04a6b1d068ca2e61.png)

Kelihatan kan kalau aku hanya menggunakan perintah `upload`?

Oke, sekarang kita akan coba menggunakan Termux Path. Pertama, kita [download dulu Termux Pathnya](https://apkzen.github.io/termux-path.html).

Lalu, kita buka dan kita masukkan kode seperti ini:

![contoh mengisi termux path](https://telegra.ph/file/4d9051821023f25475018.png)

Lalu, kita salin kode yang dihasilkan ke dalam Termux:

![salin kode di termux path](https://telegra.ph/file/88992c8c349a70b429cd6.png)

![salin kode ke termux](https://telegra.ph/file/70d6df798326d7348c56b.png)

Nah, kemudian di Termux, kita cukup memanggil kode empat baris itu dengan `upload`.