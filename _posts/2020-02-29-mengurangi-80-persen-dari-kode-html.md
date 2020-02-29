---
layout: post
title: "Mengurangi 80% dari kode HTML"
bahasa: html
date: 2020-02-29 21:03:48 +0800
---

Apakah kamu pernah merasa kesal dengan kode HTML yang panjang? Misalnya aja macam kode di bawah ini:

```html
<!DOCTYPE html>
<html>
<head>
	<title>Judul website</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
</head>
<body>
	<div class="container">
		<h1>Ini judul artikel</h1>
		<p>Paragraf pertama</p>
		<p><strong>Daftar belanjaan yang harus dibeli:</strong></p>
		<ol>
			<li>Sayur</li>
			<li>Pisang</li>
			<li>Beras</li>
		</ol>
	</div>
</body>
</html>
```

Panjang banget kan?

Nah, sekarang aku kenalin nih dengan yang namanya Pug. Kalau di Pug, kode HTML di atas itu bisa diringkas menjadi:

```slim
doctype html
head
  title Judul website
  meta(charset='utf-8')
  meta(name='viewport' content='width=device-width, initial-scale=1, user-scalable=no')
.container
  h1 Ini judul artikel
  p Paragraf pertama
  p
    strong Daftar belanjaan yang harus dibeli:
  ol
    li Sayur
    li Pisang
    li Beras
```

Wow. Lebih singkat kan?

Nah, kalau kamu penasaran sama Pug, bisa main ke [websitenya](https://pugjs.org/api/getting-started.html) karena menurutku sudah lengkap banget sih docsnya. Oh iya, untuk ringkasnya, ini caranya install Pug di devicemu:

- Install Node JS
- Jalankan `npm install -g pug-cli`
- Terus untuk menjalankan converter Pug ke HTML: `pug -w . -o ./html -P`