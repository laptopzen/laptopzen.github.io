---
layout: post
title: "Mencari Nilai 1000 Faktorial dengan Javascript"
bahasa: javascript
date: 2020-01-24 19:59:45 +0800
---

Kalau [di postingan sebelumnya](benarkah-teknologi-mengancam-kemanusiaan-0124.html) aku menjelaskan bahwa sebagian kehidupan kita telah dikerjakan sama teknologi. Nah, termasuk satu hal yang sudah dilakukan oleh teknologi dan kita nggak perlu repot lagi melakukannya adalah perhitungan matematika. Apalagi menghitung berapa nilai dari 1000 faktorial. Gila aja. Hahahahaha.

Nah, aku pun menggunakan Javascript untuk menemukan hasilnya:

```javascript
faktorial = (x) => x == 1 ? BigInt(x) : BigInt(x) * faktorial(x - 1)

console.log(faktorial(1000))
```

Ini hasilnya:

![Hasil dari faktorial 1000](https://telegra.ph/file/4d9a44b560520f31214f4.png)

Oke, sekarang kita jabarkan deh kode di atas.

```javascript
faktorial = (x) => x == 1 ? BigInt(x) : BigInt(x) * faktorial(x - 1)
```

Itu sama dengan:

```javascript
faktorial = (x) => (x == 1) ? BigInt(x) : BigInt(x) * faktorial(x - 1)
```

Sama dengan:

```javascript
faktorial = (x) => {
  (x == 1) ? BigInt(x) : BigInt(x) * faktorial(x - 1)
}
```

Atau:

```javascript
faktorial = (x) => {
  if (x == 1) {
    BigInt(x)
  } else {
    BigInt(x) * faktorial(x - 1)
  }
}
```

Bisa dijabarkan lagi:

```javascript
faktorial = function (x) {
  if (x == 1) {
    BigInt(x)
  } else {
    BigInt(x) * faktorial(x - 1)
  }
}
```

# Mengapa pakai BigInt()?

Soalnya kalau integer biasa, dia hasilnya adalah Infinity soalnya rentang angkanya nggak sampai untuk memuat nilai dari faktorial 1000.