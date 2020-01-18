---
layout: post
title: Cara Cepat Resize Gambar Secara Online
bahasa: html
---

Sebagai blogger, tentu saja ingin blog kita rame. Nah, salah satu yang membuat suatu blog rame tentu saja adalah waktu muat yang sangat cepat. Apalagi kalau blog kita banyak banget gambar dalam satu halaman, pasti lama banget tuh termuatnya.

Terus gimana solusinya? Nah, kita coba pakai fitur Google Image Cache.

Berikut ini adalah aturannya:

```
{% raw %}https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&resize_w={{ lebar yang diinginkan }}&url={{ link gambar }}{% endraw %}
```

Contohnya kita ingin membuat gambar yang beralamat di `https://situs.com/gambar.jpg` memiliki lebar 300 px, maka berikut ini adalah link gambarnya:

```
https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&resize_w=300&url=https://situs.com/gambar.jpg
```

Jadi, teknik ini aku pakai untuk [website Panglima Delivery](https://panglimadelivery.com). Soalnya kan di website itu, tampil semua produknya di halaman awal. Jadi, harus diresize gambarnya supaya halaman cepat dimuatnya.

![tampilan website panglima delivery](https://telegra.ph/file/ac62330f4db4f87af6cdf.png)

Dan ini kode HTMLnya:

```html
...
<div class="panel-body">							<p><img src="https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&resize_w=300&url=https://panglimadelivery.com/aset/gambar-roti/21d964f7e7e267626fc754136343fbee.png"></p>							<!-- <p><img src="https://panglimadelivery.com/img/21d964f7e7e267626fc754136343fbee.png?w=300"></p> -->							<div class="keterangan">								<p class="judul">Coklat </p>																<p><input type="tel" value="12000" disabled="" class="bukan-input tebal harga" data-harga='12000' name=""></p>
...
```

Nah, kelihatan kan kalau aku menggunakan teknik di tutorial ini.