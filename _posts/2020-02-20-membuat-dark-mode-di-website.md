---
layout: post
title: "Membuat Dark Mode di Website"
bahasa: javascript
date: 2020-02-20 04:46:19 +0800
---

Ini adalah skripnya yang diletakkan setelah kita memanggil jQuery:

```javascript
function dark() {
    let q = document.querySelectorAll('#nightify')
    if(q.length) {
        q[0].parentNode.removeChild(q[0])
        return false
    }
    var h = document.getElementsByTagName('head')[0],
        s = document.createElement('style');
    s.setAttribute('type', 'text/css');
    s.setAttribute('id', 'nightify');
    s.appendChild(document.createTextNode('html{-webkit-filter:invert(100%) hue-rotate(180deg) contrast(70%) !important; background: #fff;} .line-content {background-color: #fefefe;}'));
    h.appendChild(s); 
    return true
}

$(".dark").click(() => dark())

$("body").css("min-height", $(window).height())
```

Untuk memanggilnya, kita perlu menyiapkan sebuah class `.dark` yang nanti ketika kita klik, dia menjalankan kode untuk toggle antara light dan dark. Kalau aku sih meletakkannya di `.navbar-brand` tapi dikasih `.pull-right` sehingga kodenya jadi:

```html
<div class="navbar-brand pull-right"><div class="glyphicon glyphicon-adjust dark"></div></div>
```

Hasilnya:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ndos1m98girm9fz686bx.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/zx0oy7qs5raszqkm6jn3.png)

# Edit

Ini kalau sudah ditambahkan fitur `localStorage`:

```javascript
buat_dark = () => {
    // ini kalau q.length nggak jalan / elemen belum ada
    var h = document.getElementsByTagName('head')[0],
        s = document.createElement('style');
    s.setAttribute('type', 'text/css');
    s.setAttribute('id', 'nightify');
    s.appendChild(document.createTextNode('html{-webkit-filter:invert(100%) hue-rotate(180deg) contrast(70%) !important; background: #fff;} .line-content {background-color: #fefefe;}'));
    h.appendChild(s); 
    localStorage.setItem('dark', 'true')
    return true
}

localStorage.dark == 'true' ? buat_dark() : ''

function dark() {
    let q = document.querySelectorAll('#nightify')
    if(q.length) {
        // ini kalau elemen sudah ada
        q[0].parentNode.removeChild(q[0])
        localStorage.removeItem('dark')
        return false
        // false berarti hentikan proses
    }
    buat_dark()
}

$(".dark").click(() => dark())

$("body").css("min-height", $(window).height())
```