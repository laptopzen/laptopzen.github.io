---
layout: post
title: Memahami ifconfig
bahasa: bash
---

ifconfig ini fungsinya untuk melihat interface jaringan yang kita gunakan. Untuk lebih jelasnya, coba deh lihat output yang dihasilkan oleh ifconfig ini:

![Isi ifconfig](https://telegra.ph/file/41daa047d0a4fbd479761.png)

Yang pertama kita lihat adalah interface jaringannya dulu. Yaitu:

- ap0
- ccmni1
- lo
- wlan0

Nah, itu tuh ada yang bertindak sebagai interfacenya jaringan penangkap wifi (wlan0). Ada juga yang sebagai interface hotspot internet (ccmni1).

Khusus untuk interface hotspot internet, itu kalau tethering/hotspotnya nggak dinyalakan, itu interface nggak muncul pas kita cek di ifconfig.

Kemudian kita lihat IP address yang terbaca dari output di atas:

- 192.168.43.1
- 10.73.154.211
- 127.0.0.1

Kalau untuk 192.168.43.1 dan 127.0.0.1 itu linknya atau IP addressnya nggak akan berubah. Berbeda dengan 10.73.154.211 yang bisa berubah-ubah. Soalnya kan IP itu (10.73.154.211) adalah IP dari interface tethering. Artinya, dengan address tersebut, orang lain bisa mengakses HP kita sebagai yang membagikan internet.

Makanya IPnya sering ganti-ganti. Mungkin biar aman.

Nah, implementasinya seperti ini. Pertama, kamu nyalakan hotspot terlebih dahulu. Terus jalankan perintah ifconfig. Nah, catet tuh IP address yang berawalan angka 10 (misal 10.123.45.67).

Terus kamu jalankan server website di HP kamu (pakai Termux tentunya):

```bash
php -S 10.123.45.67:2020
```

Kemudian, di HP yang menangkap tethering dari HPmu, coba buka deh `http://10.123.45.67:2020` pasti akan terbuka tuh website yang servernya di HPmu. Mantap.

Sedangkan untuk 192.168.43.1 dan 127.0.0.1 itu localhost. Artinya ya kalau kamu jalankan server, cuma HPmu aja yang bisa buka. Begitu.