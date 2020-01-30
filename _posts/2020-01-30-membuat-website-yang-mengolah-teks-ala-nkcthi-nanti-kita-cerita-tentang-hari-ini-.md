---
layout: post
title: "Membuat Website yang Mengolah Teks ala NKCTHI (Nanti Kita Cerita tentang Hari Ini)"
bahasa: css
date: 2020-01-30 19:18:53 +0800
---

Jadi sebelumnya, NKCTHI itu apa ya? Kok bisa-bisa viral gitu loh? Eh, tapi masih viral kah? Aku nggak ada update medsos soalnya. Cuma denger-denger aja sih rame.

Sebenarnya sih, aku jadi pengen buat website semacam ini tu dari sebuah obrolan di grup WA Caraka Publishing. Waktu itu Mbak Hiday bilang bahwa gimana kalau style bab salah satu buku itu dibuat ala-ala NKCTHI. Wah, ide bagus tuh. Lalu, aku cari-cari kan fontnya buat dipasang di buku (BTW, aku layouter buku loh). Akhirnya ketemu tuh fontnya. Tapi, daripada cuma dipakai untuk hiasan buku aja, aku buat juga deh untuk website.

## Logika website

Jadi, di website ini tuh, kita mengetikkan suatu teks, lalu akan menampilkan kembali teks tersebut namun ala-ala NKCTHI.

Ini tampilannya:

![Hasil akhir website Nanti Kita Cerita tentang Hari Ini](https://telegra.ph/file/a8517e59e90e4651139ba.png)

Nah, lihat lok, di bagian bawah itu adalah tempat kita mengetikkan teksnya. Lalu, di atasnya akan terketik kembali teks tersebut namun dengan style ala-ala NKCTHI.

Untuk demonya, silahkan buka <https://mzaini30.com/nkcthi>. Sedangkan untuk source codenya, letaknya di <https://github.com/laptopzen/nkcthi>. Nah, di source code tersebut sudah ada fontnya, Bootstrap, dan jQuery.

## Bahas kode

Nah, kita masuk ke bagian yang paling ditunggu-tunggu yaitu bedah kode. Maka, kita mulai dari `index.html`:

```html
<!DOCTYPE html>
<html>
<head>
	<title>Nanti Kita Cerita tentang Hari Ini</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
	<style>
		* {
			word-wrap: break-word;
		}

		@font-face {
			font-family: nkcthi;
			src: url('font/GoodFoot - Font-NKCTHI.ttf');
		}

		h1 {
			font-family: nkcthi;
		}

		.navbar-fixed-bottom .table {
			margin-bottom: 0;
		}

		.navbar-fixed-bottom .table,
		.navbar-fixed-bottom td {
			border: none !important;
		}

		.hapus {
			cursor: pointer;
    		user-select: none;
		}

		body {
			padding-bottom: 50px;
		}
	</style>
</head>
<body>
	<div class="container">
		<h1 class="hasil"></h1>
	</div>
	<div class="navbar navbar-default navbar-fixed-bottom">
		<div class="container">
			<table class="table table-bordered">
				<tr>
					<td>
						<div class="input-group">
							<input type="text" class="form-control input">
							<div class="input-group-addon hapus">&times;</div>
						</div>
					</td>
				</tr>
			</table>
		</div>
	</div>
	<script src="vendor/jquery/jquery.min.js"></script>
	<script>
		$('.hapus').each(function(){
			$(this).click(function(){
				$(this).parent().find('.form-control').val('')
				$('.hasil').html('')
			})
		})

		$('.input').on('keyup', () => $('.hasil').html($('.input').val()))
	</script>
</body>
</html>
```

Oke itu HTMLnya. Lalu, file apa lagi? Ya nggak ada. Satu file itu aja sih. Hehehe. Jadi, langsung bedah aja ya.

Yang pertama tentu saja deklarasikan dulu bahwa kita pakai HTML 5.

```html
<!DOCTYPE html>
<html>
<head>
```

Lalu, kita atur judulnya dan viewport tampilan mobile (supaya di HP nggak zoom-zoom):

```html
	<title>Nanti Kita Cerita tentang Hari Ini</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
```

Terus kita panggil Bootstrap CSS:

```html
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
```

Nah, sekarang kita mulai bahas CSSnya.

Diatur dulu bahwa semua elemen nggak boleh ada yang nabrak layar. Kalau nabrak, harus dipotong:

```css
		* {
			word-wrap: break-word;
		}
```

Kemudian kita panggil fontnya dan tetapkan bahwa setiap H1, fontnya harus pakai NKCTHI:

```css
		@font-face {
			font-family: nkcthi;
			src: url('font/GoodFoot - Font-NKCTHI.ttf');
		}

		h1 {
			font-family: nkcthi;
		}
```

Terus, sedikit pengaturan untuk bagian menu bawah:

```css
		.navbar-fixed-bottom .table {
			margin-bottom: 0;
		}

		.navbar-fixed-bottom .table,
		.navbar-fixed-bottom td {
			border: none !important;
		}

		.hapus {
			cursor: pointer;
    		user-select: none;
		}

		body {
			padding-bottom: 50px;
		}
```

Sekarang kembali bahas HTMLnya.

Kita gunakan `.container` agar ada jarak kanan dan kiri:

```html
	<div class="container">
```

Lalu, kita buat H1 dengan class `.hasil`:

```html
		<h1 class="hasil"></h1>
```

Lalu, bagian menu bawah:

```html
	<div class="navbar navbar-default navbar-fixed-bottom">
		<div class="container">
			<table class="table table-bordered">
				<tr>
					<td>
						<div class="input-group">
							<input type="text" class="form-control input">
							<div class="input-group-addon hapus">&times;</div>
						</div>
					</td>
				</tr>
			</table>
		</div>
	</div>
```

Sekarang, kita include jQuery dan akan kita bahas penggunaan Javascript:

```html
	<script src="vendor/jquery/jquery.min.js"></script>
```

Setiap kali ngeklik tombol `x`, maka dia akan menghapus inputan di sebelahnya:

```javascript
		$('.hapus').each(function(){
			$(this).click(function(){
				$(this).parent().find('.form-control').val('')
				$('.hasil').html('')
			})
		})
```

Kemudian, setiap kali kita ketikkan teks di inputan bawah, maka akan ditampilkan pula di dalam tag H1 yang memiliki class `.hasil` tadi:

```javascript
		$('.input').on('keyup', () => $('.hasil').html($('.input').val()))
```

Oh iya, sintaks

```javascript
() => $(".hasil").html($(".input").val())
```

Itu sama saja dengan:

```javascript
function(){
  $(".hasil").html($(".input").val())
}
```

Teknik penulisan itu namanya arrow function dan sudah kujelaskan [di postinganku sebelumnya](mengenal-fungsi-di-javascript-0124.html).