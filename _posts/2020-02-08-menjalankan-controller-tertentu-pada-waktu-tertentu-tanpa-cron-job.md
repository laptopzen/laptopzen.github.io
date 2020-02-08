---
layout: post
title: "Menjalankan Controller Tertentu pada Waktu Tertentu Tanpa Cron Job"
bahasa: codeigniter
date: 2020-02-08 12:16:35 +0800
---

Biasanya kan kita pakai Cron Job kalau ingin menjalankan skrip PHP tertentu dalam rentang waktu tertentu. Misalnya saja setiap 24 jam, backup database, atau reset database, atau setiap 30 hari, backup database. Nah, sekarang kita mau coba caranya tanpa menggunakan Cron Job.

## Logika pemrogramannya

Misalnya saja kita buat controller yang bernama `backup`. Nah, untuk menjalankan backup ini, kita cukup membuka `situs.com/backup`.

Namun...

Kalau misalnya kita punya banyak situs gimana?

Contohnya:

- `a.com/backup`
- `b.com/reset`
- `c.com/lacak`
- `d.com/hack-now`

Nah, kita coba nih untuk menjalankan semua itu dalam satu skrip aja.

## Pakai AJAX

Jadi, kita sekarang nggak perlu tuh membuka semua halaman itu satu per satu. Pakai aja AJAX.

Misalnya aja, kita buat di localhost, skrip berikut ini untuk mengakses semua halaman itu (di blog juga bisa):

- `a.com/backup`
- `b.com/reset`
- `c.com/lacak`
- `d.com/hack-now`

```javascript
$.get("https://a.com/backup")
$.get("https://b.com/reset")
$.get("https://c.com/lacak")
$.get("https://d.com/hack-now")
```

Nah keren kan. Jadi, dalam satu halaman aja, kamu bisa akses semua situs tersebut.

## Hanya pada waktu tertentu

Namun, masalah muncul.

Kan, berarti setiap kita membuka halaman tersebut, dia akan senantiasa menjalankan skripnya lok? Aku pengennya skrip tersebut dijalankan hanya pada jam 11:

```javascript
tanggal = new Date()
jam = tanggal.getHours()
jam == 11 ? (
	$.get("https://a.com/backup")
	$.get("https://b.com/reset")
	$.get("https://c.com/lacak")
	$.get("https://d.com/hack-now")
) : ""
```