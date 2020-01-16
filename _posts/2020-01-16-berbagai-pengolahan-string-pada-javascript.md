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

**Huruf besar dan huruf kecil selang-seling**

_Kode_

```javascript
teks = "Ingin menjadi apa setelah dewasa. Ingin menjadi apa. Tak terbayangkan."
pecah = teks.split("")
teks_baru = ""
for (n in pecah){
  if (n % 2 == 0){
    teks_baru += pecah[n].toUpperCase()
  } else {
    teks_baru += pecah[n].toLowerCase()
  }
}
console.log(teks_baru)
```

_Hasil_

```
InGiN MeNjAdI ApA SeTeLaH DeWaSa. InGiN MeNjAdI ApA. tAk tErBaYaNgKaN.
```

**Menghapus karakter ketiga dari belakang**

_Kode_

```javascript
console.log("031".split("").splice(-2, 2).toString().replace(",", ""))
```

_Hasil_

```
31
```