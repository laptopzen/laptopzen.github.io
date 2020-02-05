---
layout: post
title: "Kenapa Aku Masih Pakai jQuery?"
bahasa: javascript
date: 2020-02-05 20:04:07 +0800
---

Perkembangan bahasa pemrograman saat ini sangatlah pesat. Bahkan, ada yang bilang bahwa setiap satu menit, framework Javascript baru tercipta. Lah, aku masih pewe sama jQuery. Hahahahahha.

![Yang terjadi dalam satu menit](https://miro.medium.com/max/1104/1*wHL7jB5xRBUdcOebneHHyg.jpeg)

Tapi, kenapa aku masih pakai jQuery padahal kawan-kawan lainnya (thanks buat kalian kawan-kawan di Javascript Indonesia) menyarankan untuk menggunakan Vanilla JS atau framework Javascript yang lebih modern seperti RGB (Angular, Vue, dan React)? Jadi, aku akan mengungkapkan alasannya.

## Udah hapal mati kodenya. Hahahaha

Ya misalnya kalau ingin menambahkan CSS, tinggal buat kode seperti:

```javascript
$(".class").css("background", "blue")
```

Atau kalau ingin menambah banyak CSS:

```javascript
$(".elemen").css({
	"background": "blue",
	"color": "red",
	"text-decoration": "underline"
})
```

Gampang aja lok kodenya buat dihapal?

Atau misalnya aku ingin menghilangkan suatu elemen:

```javascript
$(".halo").hide()
```

Lalu ingin memunculkannya lagi:

```javascript
$(".ehem").show()
```

Misalnya juga ingin menambah class:

```javascript
$(".sesuatu").addClass("iya")
```

Atau menghilangkan class:

```javascript
$(".sesuatu").removeClass("sembunyi")
```

Atau aku ingin bermain AJAX (HTTP Request):

```javascript
$.get("/data.php", () => $(".pesan").html("Data sudah diterima"))

$.post("/posting.php", $("form").serialize(), () => $(".pesan").html("Data terkirim"))
```

Atau ingin mengambil elemen di atas kita:

```javascript
$(".sesuatu").parent()
```

Atau ingin mengambil sesuatu di bawah kita:

```javascript
$(".elemen").find(".makan")
```

Apalagi ya? Banyak sih masih. Masak iya sih aku tunjukkan semua? Hahahahahhaa.