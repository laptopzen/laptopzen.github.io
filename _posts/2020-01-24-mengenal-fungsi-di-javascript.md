---
layout: post
title: Mengenal Fungsi di Javascript
bahasa: javascript
---

Fungsi adalah cara untuk mengkapsulasi suatu perintah Javascript supaya kita nggak ngulang-ngulang nulisnya. Misalnya aja kita ada kode Javascript seperti ini:

```javascript
console.log("Namaku adalah Zen")
console.log("Namaku adalah Anggi")
console.log("Namaku adalah Anhar")
```

Bukannya kode di atas itu sebenarnya sama aja cuma berbeda di bagian akhir?

Nah, makanya kita menggunakan fungsi supaya hemat kode. Nggak nulis ngulang-ngulang gitu.

Dengan cara fungsi, kode di atas bisa diubah menjadi:

```javascript
function sebut(nama){
	console.log(`Namaku adalah ${nama}`)
}

sebut("Zen")
sebut("Anggi")
sebut("Anhar")
```

Nah, kelihatan kan kalau kita mempersingkat kodenya hanya menjadi `sebut(namanya)`.

Oh iya, kode di atas aku menggunakan [template literal](ada-yang-pernah-pakai-template-literal-0121.html) supaya lebih cepat nulisnya.

Oh iya, fungsi di atas bisa juga diubah menjadi:

```javascript
sebut = function(nama){
	console.log(`Namaku adalah ${nama}`)
}

sebut("Zen")
sebut("Anggi")
sebut("Anhar")
```

Atau

```javascript
sebut = (nama) => {
	console.log(`Namaku adalah ${nama}`)
}

sebut("Zen")
sebut("Anggi")
sebut("Anhar")
```

Atau yang lebih singkat lagi:

```javascript
sebut = (nama) => console.log(`Namaku adalah ${nama}`)

sebut("Zen")
sebut("Anggi")
sebut("Anhar")
```