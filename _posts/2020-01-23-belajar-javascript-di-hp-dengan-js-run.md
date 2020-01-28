---
layout: post
title: Belajar Javascript di HP dengan JS Run
bahasa: javascript
---

Zaman sekarang ni belajar sangat mudah. Apalagi belajar pemrograman. Salah satunya adalah aplikasi JS Run yang bisa kamu dapatkan di Play Store. Dengan aplikasi ini, kamu bisa menjalankan Javascript dan belajar menggunakannya.

![Aplikasi JS Run di Play Store](https://telegra.ph/file/e34cc62888b0d902916fc.png)

Dan ini adalah contoh kode Javascript yang dijalankan dengan aplikasi tersebut:

![Contoh kode yang dijalankan di JS Run](https://telegra.ph/file/8e5f192ae8077511913f0.png)

Nah, kita coba deh belajar dengan aplikasi tersebut. Yuk lah. Kita mulai dari yang paling dasar.

## Berbagai tipe di Javascript

```javascript
teks = "Zen"
angka = 2
kondisi = true
list = ["satu", "dua", 3]
obyek = {"nama": "Zen", "alamat": "Loa Janan"}

console.log(teks)
console.log(angka)
console.log(kondisi)
console.log(list)
console.log(obyek)
```

Oh iya, salin kode di atas ke JS Run ya.

Jadi, kode di atas adalah berbagai tipe yang bisa dimasukkan ke Javascript. Yang pertama adalah string atau yang biasa kita sebut dengan teks. Lalu, angka. Terus boolean atau true dan false. Kemudian array (list) dan object.

Lalu, perintah `console.log()` itu untuk mencetak hasilnya ke layar.

Hasilnya adalah:

```
Zen
2
true
[
  "satu",
  "dua",
  3
]
{
  "nama": "Zen",
  "alamat": "Loa Janan"
}
```

_String dengan lebih dari satu baris_

Oh iya, untuk string (yaitu yang diapit oleh dua kutip itu), cuma bisa dalam satu baris. Kalau lebih dari satu baris, pakai teknik yang telah kujabarkan di [postingan tentang string literal](ada-yang-pernah-pakai-template-literal-0121.html). Contoh penerapan dari string literal adalah:

```javascript
nama = `Zen
Anggi
Wawan`

hasil = `Nama yang hadir adalah:

${nama}`

console.log(hasil)
```

Hasilnya adalah:

```
Nama yang hadir adalah:

Zen
Anggi
Wawan
```

## Kondisi

```javascript
angka = 3

if (angka == 1){
	sebut = "satu"
} else if (angka >= 2){
	sebut = "lebih atau sama dengan daripada 2"
} else if (angka == 3){
	sebut = "tiga"
} else {
	sebut = "terus angka berapa?"
}

console.log(sebut)
```

Kondisi itu berarti if else (jika x, jika tidak x). Nah, di atas adalah kode untuk jika maka. Yang pertama kan kita kasih nilai dulu angka adalah 3. Lalu kita tanya apakah angka adalah 1. Jika iya, variabel sebut dikasih nilai 1. Jika tidak, lihat lagi apakah angka lebih besar atau sama dengan 2. Jika iya, variabel sebut dikasih nilai lebih atau sama dengan 2. Lalu cek lagi begitu seterusnya hingga ke sintaks `else` maksudnya adalah jika semua kondisional sebelumnya itu salah, maka `else` ini dijalankan, yang nilai dari sebut adalah terus angka berapa?

Baru di akhir kita cetak sebut di console.

Hasilnya adalah:

```
lebih atau sama dengan daripada 2
```

Bisa juga sintaks kondisional seperti ini:

```javascript
angka = 5
sebut = angka < 4 ? "di bawah empat" : "di atas empat"

console.log(sebut)
```

Hasilnya adalah 

```
di atas empat
```

Jadi, maksud kode di atas adalah jika angka di bawah 4, maka nilai dari sebut adalah `di bawah empat` jika tidak maka nilai dari sebut adalah `di atas empat`.

Kemudian kita cetak sebut ke layar.