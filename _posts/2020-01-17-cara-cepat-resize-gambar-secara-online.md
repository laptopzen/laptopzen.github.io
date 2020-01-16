---
layout: post
title: Cara Cepat Resize Gambar Secara Online
bahasa: html
---

Sebagai blogger, tentu saja ingin blog kita rame. Nah, salah satu yang membuat suatu blog rame tentu saja adalah waktu muat yang sangat cepat. Apalagi kalau blog kita banyak banget gambar dalam satu halaman, pasti lama banget tuh termuatnya.

Terus gimana solusinya? Nah, kita coba pakai fitur Google Image Cache.

Berikut ini adalah aturannya:

```html
https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&resize_w=<< lebar yang diinginkan >>&url=<< link gambar >>
```

Contohnya kita ingin membuat gambar yang beralamat di `https://situs.com/gambar.jpg` memiliki lebar 300 px, maka berikut ini adalah link gambarnya:

```html
https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&resize_w=300&url=https://situs.com/gambar.jpg
```