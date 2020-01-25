---
layout: post
title: "Menghilangkan Elemen Tertentu di Blog"
bahasa: css
date: 2020-01-25 13:57:05 +0800
---

Berawal dari sebuah obrolan di WA:

![Sebuah pesan di grup blogger](https://telegra.ph/file/27c0fac4aa8789f5763b6.png)

Ini penampakan elemen blog yang mau dihilangkan:

![Penampakan blog](https://telegra.ph/file/cb364c71472948964b0dd.png)

Maka, yang kulakukan adalah melihat source codenya (bisa dengan `view-source:linknya`) lalu mencari kata-kata _about lutfi_:

![Mencari](https://telegra.ph/file/184d2f582fd06335a8857.png)

Dari situ ditemukan bahwa dia berada pada elemen `<div class="sora-author-box">`. Maka cara menghilangkannya adalah dengan menambahkan kode CSS ini:

```css
.sora-author-box {
  display: none;
}
```

Titik di awal itu maksudnya adalah _class_.

Cara memasukkan custom CSS adalah:

![Cara memasukkan custom CSS](https://telegra.ph/file/27c5eab5544dea6d90e5b.png)