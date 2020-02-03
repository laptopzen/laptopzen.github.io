---
layout: post
title: "Cara Menjaga Peserta Ujian Nggak Membuka Google Saat Ujian Online"
bahasa: javascript
date: 2020-02-03 20:02:29 +0800
---

Biasanya kan kalau untuk kampus-kampus yang paperless, maunya segalanya serba online. Salah satunya adalah ujian online.

Namun, yang jadi masalah itu adalah jika ketika ujian, peserta/mahasiswa membuka Google untuk mencari jawaban. Atau, membuka WA untuk bertanya jawabannya. Jadi, gimana solusinya supaya peserta ujian fokus saja sama halaman ujiannya?

Tambahkan kode Javascript berikut ini di halaman web ujian online: (jadi ya, kamu harus paham sih saat baca source codenya)

```javascript
$(window).on("blur", () => /* skrip yang mau dijalankan */)
```

Oh iya, kode di atas diletakkan setelah memanggil jQuery ya.

Contohnya: <https://mzaini30.com/window-blur>

## Implementasi kode

Oke, sekarang aku bahas ya yang untuk di bagian `skrip yang mau dijalankan`.

Oh iya, untuk kode di atas, itu jika skrip yang mau dijalankan itu hanya satu baris. Jika skrip yang mau dijalankan itu terdiri dari banyak baris, maka kodenya berubah menjadi:

```javascript
$(window).on("blur", () => {
	/* skrip yang mau dijalankan */
})
```

Misalnya aja kita ingin membuat jika peserta itu membuka tab lain, dia akan mengosongkan semua input maupun textarea. Maka kode di dalam `skrip yang mau dijalankan` adalah:

```javascript
$("input, textarea").val("")
```

Atau misalnya kita ingin memberi peringatan, maka skripnya adalah:

```javascript
alert("Kamu mau nyari di Google ya?")
```

Atau misalnya kedua kode di atas mau digabungkan nih. Habis kasih peringatan, semua jawabannya dihapus:

```javascript
alert(`Maaf, jawaban kamu terpaksa aku hapus.\n
Kamu sih mau nyontek. Aku nggak suka.`)
$("input, textarea").val("")
```

## Bug di dalam kode ini

Kan maunya aku, kode yang berisi peringatan itu akan jalan jika peserta membuka tab baru atau membuka aplikasi selain browser. Namun, ketika kode ini dijalankan, yang berfungsi adalah ketika peserta membuka tab baru. Saat membuka aplikasi lainnya, kode nggak jalan. Mungkin ada kawan yang bisa membantu, monggo komentar di bawah.