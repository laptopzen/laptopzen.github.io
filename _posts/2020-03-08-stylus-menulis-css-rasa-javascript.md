---
layout: post
title: "Stylus: Menulis CSS rasa Javascript"
bahasa: css
date: 2020-03-08 05:37:14 +0800
---

Pernah kesal dengan kode CSS yang membuat kita ngetiknya lama banget? Seperti kode di bawah ini:

```css 
.elemen {
  background: blue;
  color: red;
}

.elemen p {
  text-align: right;
}
```

Oke, mari kita lihat sintaks-sintaks yang jauh dari filosofi programmer yaitu DRY (don't repeat yourself). Kita lihat di sintaks CSS di atas bahwa kita mengulangi kode `.elemen` yaitu `.elemen p`.

Tau nggak sih kalau kita bisa menampilkan CSS dengan filosofi programmer? Wow. Caranya adalah dengan Stylus.

Kalau kode di atas ditulis dengan bahasa Stylus, maka akan berubah menjadi:

```scss
.elemen
  background blue 
  color red 
  
  p 
    text-align red 
```

Lah, memangnya Stylus bisa menggantikan CSS? Ya nggak sih. Cuma, Stylus nanti akan diolah menjadi CSS. So, kalau kamu ingin mencobanya, langsung saja menuju [docs Stylus.](https://stylus-lang.com/)