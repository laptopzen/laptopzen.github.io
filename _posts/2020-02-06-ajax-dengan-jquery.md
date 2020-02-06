---
layout: post
title: "AJAX dengan jQuery"
bahasa: javascript
date: 2020-02-06 08:23:10 +0800
---

Apa sih yang terkenal dari namanya sebuah website?

Yap, loading.

Maka, ada tuh sampai yang membuat jargon bahwa kepanjangan WWW adalah world wait web. Hahahahhahaha.

Tapi, bisa nggak sih kita membuat suatu web tanpa loading?

Ya...

Nggak bisa. Hahahahahahaha...

Tapi kalau misalnya loadingnya hanya di pemuatan awal aja sih bisa. Nama teknik ini adalah AJAX.

## Apa itu AJAX?

AJAX adalah suatu teknik untuk mengambil data dari web tanpa loading. Jadi ya yang dimuat atau diolah itu datanya aja, nggak perlu keseluruhan web. Nggak perlu muat ulang lagi semua skrip, semua style, semua gambar, semua video. Pasti bakalan loading banget tuh.

Oh iya, kalau kamu sudah membaca [artikelku sebelumnya tentang beralih halaman tanpa loading](membuat-halaman-tanpa-loading-saat-peralihan-halaman-seperti-nuxt-js-0202.html), itu sebenarnya juga memakai teknik AJAX yaitu `.load()`. Nah, `.load()` itu fungsinya adalah memuat sebuah link, terus ditampilkan pada elemen tertentu di halaman tersebut.

Misalnya aja kita ada elemen `.artikel`, terus mau kita muat di situ halaman dari `berita.html`, maka perintahnya adalah:

```javascript
$(".artikel").load("berita.html")
```

Oke, sesimpel itu.

Tapi, teknik AJAX ini harus melalui protokol http. Maka, kalau dari protokol file, ssh, mailto, tentu saja nggak bisa jalan. Jadi, kalau misalnya kamu mau bermain AJAX di lokal (laptop/HP), jalankan dulu aja server localhostnya. Kalau di PHP, kodenya:

```bash
php -S localhost:2020
# lalu buka http://localhost:2020 di browser
```

## Perintah AJAX yang lainnya

Nah, kalau load tadi kan memuat halaman tertentu secara penuh. Lalu, bagaimana jika kita hanya ingin menerima datanya?

Kita bisa menggunakan `$.post()` dan `$.get()`. Kalau kamu sudah terbiasa dengan form di HTML, tentu sudah nggak asing lagi dengan kedua istilah ini.

Kalau post, biasanya untuk mengirim data ke server. Sedangkan get, buat menerima data dari server.

Oke, langsung aja kodenya.

```javascript
// mengirim data
$.post("/proses.php", $(".form").serialize(), () => $(".notice").html("Data telah dikirim"))

// menerima data
$.get("/data.php", () => $(".notice").html("Data telah diterima"))
```

Mengapa aku menggunakan panah? Itu namanya arrow function. Monggo baca artikelku tentang [berbagai bentuk fungsi dai Javascript](mengenal-fungsi-di-javascript-0124.html).