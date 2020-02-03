---
layout: post
title: "Cara Menjaga Peserta Ujian Nggak Membuka Google Saat Ujian Online"
bahasa: javascript
date: 2020-02-03 20:02:29 +0800
---

Biasanya kan kalau untuk kampus-kampus yang paperless, maunya segalanya serba online. Salah satunya adalah ujian online.

Namun, yang jadi masalah itu adalah jika ketika ujian, peserta/mahasiswa membuka Google untuk mencari jawaban. Atau, membuka WA untuk bertanya jawabannya. Jadi, gimana solusinya supaya peserta ujian fokus saja sama halaman ujiannya?

Tambahkan kode Javascript berikut ini di halaman web ujian online

```javascript
$(window).on("blur", () => /* skrip yang mau dijalankan */)
```

Oh iya, kode di atas diletakkan setelah memanggil jQuery ya.

Contohnya: <https://mzaini30.com/window-blur>