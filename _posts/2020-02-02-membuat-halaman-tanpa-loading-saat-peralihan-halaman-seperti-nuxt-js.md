---
layout: post
title: "Membuat Halaman Tanpa Loading Saat Peralihan Halaman Seperti Nuxt JS"
bahasa: javascript
date: 2020-02-02 13:22:07 +0800
---

Letakkan skrip berikut di bawahnya jQuery:

```javascript
halaman_pertama = 'a'
bagian_komponen = '.komponen'

lokasi = () => {
	!location.hash ? location.href = `/#/${halaman_pertama}` : ''
	komponen = location.hash.split('#/')[1]
	$(bagian_komponen).load(`/${komponen}`)
}
lokasi()
$(window).on('hashchange', () => {
	lokasi()
})
```

Lalu, untuk menulis linknya: `/#/halaman-yang-akan-dituju`.

Demo: <https://seperti-nuxt-js.herokuapp.com>

Source code: <https://github.com/mzaini30/seperti-nuxt-js>