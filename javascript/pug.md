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

## Cara menggunakan

```bash
pug . -w
```