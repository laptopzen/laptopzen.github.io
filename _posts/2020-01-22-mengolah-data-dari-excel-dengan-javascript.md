---
layout: post
title: Mengolah Data dari Excel dengan Javascript
bahasa: javascript
---

Terkadang kita ingin mengolah data dengan cepat yaitu menggunakan Excel dan langsung diolah begitu saja; nggak pakai input satu per satu seperti web app pada umumnya. Nah, aku buat nih tutorial cara sederhana bagaimana cara menggunakan Excel sebagai basis data suatu website (offline) menggunakan Javascript.

Sebelumnya, ini adalah susunan file projectnya:

```
/
├── bootstrap.min.css
├── data.js
├── data.xlsx
├── index.html
└── jquery.min.js
```

Untuk Bootstrap, kamu bisa download dari <https://getbootstrap.com/docs/3.3/>. Untuk jQuery, kamu bisa download dari <https://jquery.com/download/>.

`data.xlsx` adalah sumber data yang ingin kita olah. Berikut ini adalah isinya:

![Gambar sumber data Excel yang akan diolah dengan Javascript](https://telegra.ph/file/9740701357398adeaf1a2.png)

Kemudian, dari `data.xlsx` itu kita salin ke dalam `data.js` dengan ini sebagai berikut:

```javascript
data = `Zen  Loa Janan
Yani  Samarinda
Anggi  Loa Janan
Ijul  Loa Janan`
```

Terlihat kan dari data di atas, bahwa aku copy paste isinya aja. Header tabelnya nggak kuambil. Nah, itu aku kasih nama variabel `data` untuk pemanggilan skripnya nanti. Terus aku pakai [template literal](ada-yang-pernah-pakai-template-literal-0121.html) sehingga bisa untuk menampung string dan enter.

Lalu, isi dari `index.html` adalah:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Olah Data</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
  <link rel="stylesheet" type="text/css" href="bootstrap.min.css">
</head>
<body>
  <br>
  <div class="container">
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>Nama</th>
          <th>Alamat</th>
        </tr>
      </thead>
      <tbody class="isi"></tbody>
    </table>
  </div>
  <script type="text/javascript" src="data.js"></script>
  <script type="text/javascript" src="jquery.min.js"></script>
  <script type="text/javascript">
    data = data.split(`\n`)
    for (n in data){
      data[n] = data[n].split(`\t`)
    }
    isi = ``
    for (x of data){
      isi += `<tr>
            <td>${x[0]}</td>
            <td>${x[1]}</td>
          </tr>`
    }
    $(`.isi`).html(isi)
  </script>
</body>
</html>
```

Tag `<!DOCTYPE html>` digunakan di awal untuk menerangkan bahwa kita menggunakan HTML5.

`<meta charset="utf-8">` untuk memberi tau browser bahwa kita menggunakan charset UTF-8.

`<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">` supaya tampilannya bagus di HP. Nggak pakai zoom-zoom gitu.

`<link rel="stylesheet" type="text/css" href="bootstrap.min.css">` berarti kita include Bootstrap.

`<br>` kasih jarak sekali enter.

`<div class="container"></div>` kasih jarak kanan kiri layar.

```html
<table class="table table-bordered">
  <thead>
    <tr>
      <th>Nama</th>
      <th>Alamat</th>
    </tr>
  </thead>
  <tbody class="isi"></tbody>
</table>
```

Dari kode di atas, berarti kita memanggil `table` dengan class `table` dan `table-bordered` untuk menggunakan tampilan table yang lebih rapi dengan menggunakan Bootstrap. Lalu, kita tentukan juga header tablenya yaitu Nama dan Alamat. Kemudian di bagian body table, kita hanya menggunakan class `isi` karena bagian itu nanti yang akan kita olah dengan jQuery.

```html
<script type="text/javascript" src="data.js"></script>
<script type="text/javascript" src="jquery.min.js"></script>
```

Itu artinya menginclude file `data.js` dan `jquery.min.js`.

`data = data.split(`\n`)` akan mengubah data menjadi:

```javascript
data = [
  'Zen  Loa Janan',
  'Yani  Samarinda',
  'Anggi  Loa Janan',
  'Ijul  Loa Janan'
]
```

```javascript
for (n in data){
  data[n] = data[n].split(`\t`)
}
```

Akan mengubah data menjadi:

```javascript
data = [
  ['Zen', 'Loa Janan'],
  ['Yani', 'Samarinda'],
  ['Anggi', 'Loa Janan'],
  ['Ijul', 'Loa Janan']
]
```

```javascript
isi = ``
for (x of data){
  isi += `<tr>
	        <td>${x[0]}</td>
	        <td>${x[1]}</td>
	      </tr>`
}
$(`.isi`).html(isi)
```

Skrip di atas akan mengambil `data` lalu menjadikannya tabel.

Ini hasilnya:

![Jadi](https://telegra.ph/file/5c56f11e4f7f21c8749b8.png)