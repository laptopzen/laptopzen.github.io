---
layout: post
title: Berbagai Pengolahan String pada Javascript
bahasa: javascript
---

Javascript adalah bahasa pemrograman yang terus berkembang. Bahkan, saking berkembangnya ini bahasa, sekarang sampai dijadikan bahasa pemrograman untuk menjalankan server. Yaitu menggunakan Node JS yang berbasis Javascript V8 Google Engine. Di Mediumnya Bang Rian Yulianto bahkan disebutkan bahwa

> Semua akan menjadi Javascript pada akhirnya

Nah, sebagai pemula, tentu kita perlu mencoba dulu dong dasar-dasarnya, soalnya kalau kita belum sanggup menggunakan Javascript sebagai server, setidaknya kan kita sudah mencoba menggunakan Javascript untuk kehidupan sehari-hari. Nah, makanya aku buat postingan yang berisi pengolahan string menggunakan Javascript.

**Mengubah semua huruf vokal menjadi i**

Yang ini lagi ngetren nih.

_Kode_

```javascript
teks = "Kamu ngomong apa sih?"
console.log(teks.replace(/[aueo]/gi, "i"))
```

_Hasil_

```
Kimi ngiming ipi sih?
```