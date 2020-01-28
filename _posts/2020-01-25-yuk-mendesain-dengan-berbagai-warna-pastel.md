---
layout: post
title: "Yuk Mendesain dengan Berbagai Warna Pastel"
bahasa: css
date: 2020-01-25 11:12:43 +0800
---

Salah satu kendala bagi seorang desainer adalah menentukan warna yang tepat untuk produk desainnya. Nggak cuma desainer produk cetak sih, desainer web juga kadang mengalaminya. Nah, kalau di Corel Draw kan ada tuh warna-warna standar yang namanya Pantone. Sekarang, kita akan menjelajah warna-warna yang kuambil dari [Materialize CSS](https://materializecss.com/).

![Tampilan awal Materialize Color](https://telegra.ph/file/304e392882b2e3f802c8e.png)

Oh iya, kalau kamu mau mencobanya, klik aja <https://mzaini30.com/materialize-color/>.

## Cara menggunakannya

Kamu pilih aja warna yang kamu suka.

![Tampilan awal Materialize Color](https://telegra.ph/file/304e392882b2e3f802c8e.png)

Misalnya aku suka warna merah. Jadi kuklik aja `red`. Habis kuklik, muncul variasi warna merah.

![Berbagai variasi warna merah](https://telegra.ph/file/da3bb59f402cccee44ace.png)

Lalu kupilih `red darken-1`:

![red darken-1](https://telegra.ph/file/3ba3bccc55e0f75e7f368.png)

Nah, di situ kan muncul `rgb(229, 57, 53)` dan `#E53935`. Itu adalah kode warnanya. Yang pertama adalah kode warna RGB dan yang kedua adalah hexadecimal.

Nah, penerapannya di website, misalnya kita ingin kode tersebut dipakai sebagai warna untuk setiap tulisan tebal, maka kode CSSnya adalah:

```css
strong {
  color: #E53935;
}
```