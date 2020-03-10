# Pug: Solusi buat HTML yang serba ribet

Pernah nggak kamu merasa jengkel sama HTML? Ya, beneran jengkel. Soalnya kan untuk membuat suatu tampilan yang sederhana, kamu perlu mengetikkan kode HTML yang panjang. Misalnya aja seperti kode di bawah ini:

```html 
<!doctype html>
<html>
  <head>
    <title>Hello world</title>
  </head>
  <body>
    <h1>Hello world</h1>
    <p>Lorem ipsum <em>dolor</em> sit <strong>amet</strong></p>
  </body>
</html>
```

Panjang banget ya? Hehehehe.

Apalagi harus ada tag penutup. Ribet dah.

Coba kalau kita pakai Pug:

```pug 
doctype html
html 
  head 
    title Hello world
  body 
    h1 Hello world
    p Lorem ipsum #[em dolor] sit #[strong amet]
```

## Instalasi

```bash
npm install -g pug-cli
```

Kalau menggunakan Linux:

```bash
sudo npm install -g pug-cli
```

## Cara menggunakan

```bash
pug . -w
```

Titik itu artinya memilih semua file yang memiliki ekstensi `.pug`.

`-w` berarti watch. Artinya, setiap ada perubahan pada file pug, browser akan reload secara otomatis.

Tapi kalau kita ingin prettify, artinya kode HTML yang ditampilkan itu nggak numpuk jadi satu baris, kodeny berubah menjadi:

```bash
pug . -w -P
```

Kalau kita ingin output HTMLnya di folder tertentu, misalnya di folder `html`, maka kodenya berubah menjadi:

```bash
pug . -w -o html -P
```