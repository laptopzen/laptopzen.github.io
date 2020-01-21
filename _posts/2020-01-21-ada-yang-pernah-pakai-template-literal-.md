---
layout: post
title: Ada yang Pernah Pakai Template Literal?
bahasa: javascript
---

Kalau biasanya kita mendeklarasikan variabel di Javascript lalu memanggilnya kan menggunakan sintaks di bawah ini:

```javascript
nama = "Zen"
console.log("Halo " + nama + ", kamu sudah siap?")
```

Maka akan menghasilkan:

```
Halo Zen, kamu sudah siap?
```

Tapi kamu tau nggak, kalau teknik di atas tu ribet dan repot banget. Coba deh sintaks di bawah ini:

```javascript
nama = `Zen`
console.log(`Halo ${nama}, kamu sudah siap?`)
```

Maka, akan menghasilkan output yang sama tapi dengan DX (developer experience) yang lebih baik.

Teknik penulisan di atas, namanya adalah _template literal_ atau template string.

Dengan teknik penulisan string ini, kode yang dihasilkan akan lebih indah dan nggak membuat pusing dilihatnya.

Oh iya, bisa juga loh kita mendeklarasikan variabel dengan string lebih daripada satu baris:

```javascript
nama =`Zen
Yani
Anggi
Gipeng`
console.log(`Nama-nama yang ikut jalan-jalan adalah:

${nama}`)
```

Hasilnya adalah:

```
Nama-nama yang ikut jalan-jalan adalah:

Zen
Yani
Anggi
Gipeng
```

Keren banget coba.

Oh iya, untuk mempelajari materi ini lebih mendalam, silahkan buka <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals>.

Kenapa baru tau sekarang ya? Hehehehe.