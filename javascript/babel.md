Pernah nggak kamu mau menggunakan fitur yang keren dan simpel banget tapi browser nggak dukung?

Misalnya aja kamu mau menggunakan arrow function bersamaan dengan string literal di Javascript seperti contoh di bawah ini:

```javascript
let sebut = nama => console.log(`Halo ${nama}`)
```

Tapi sayang sih untuk browser-browser lawas yang nggak update-update, fitur itu nggak bisa digunakan. Jadi ya harus menggunakan kode seperti di bawah ini:

```javascript
"use strict";

var sebut = function sebut(nama) {
  return console.log("Halo ".concat(nama));
};
```

Lebih ribet dan nggak indah ya? Tapi ya memang begitu sih kodenya kalau mau mendukung berbagai macam browser.

> Tapi untungnya sekarang ada Babel...

Dengan Babel, kamu bisa mengetik kode seperti biasa. Entah itu kamu menggunakan Ecmascript versi 2015, 2016, 2017, dan berbagai versi lainnya, Babel akan mengkonversinya menjadi format Javascript yang paling lawas sehingga kamu nggak perlu khawatir apakah kodemu bisa dijalankan atau nggak. Serahkan saja semua ke Babel.

Untuk mulai menggunakan Babel, silahkan [kunjungi situsnya.](https://babeljs.io/)