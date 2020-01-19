---
layout: post
title: Cara Membuat Judul untuk Blog Berbasis Jekyll
bahasa: javascript
---

Biasanya kan kalau blogging itu hanya mengenal dua, yaitu Blogspot dan Wordpress. Padahal, masih banyak lagi tools yang bisa kita gunakan untuk blogging. Salah satunya adalah Jekyll.

Keunggulan dari blogging menggunakan Jekyll adalah kamu bisa blogging secara offline. Artinya, nggak perlu terhubung terus ke internet. Cukup blogging dari laptop atau HP-mu aja terus nanti kalau ada internet, baru diupload menggunakan Git. Kodenya kurang lebih seperti ini:

```bash
git status
git add -A .
git commit -m "upload"
git push
```

Nah, kalau blogging menggunakan Jekyll, semua postingan kita ada di folder `_posts` dengan ketentuan nama file: `{% raw %}{{ tahun }}-{{ bulan }}-{{ tanggal }}-{{ judul postingan | pakai strip untuk memisahkan antarkata }}.md{% endraw %}`. Contohnya aja kalau blogku ini:

```
_posts/
├── 2020-01-12-apa-yang-membedakan-teknik-informatika-dengan-sistem-informatika.md
├── 2020-01-12-belajar-javascript-untuk-pemula.md
├── 2020-01-12-main-activity-untuk-aplikasi-android.md
├── 2020-01-12-tutorial-dasar-html-dan-css.md
├── 2020-01-15-bagaimana-cara-cepat-membuat-aplikasi-android-.md
├── 2020-01-16-berbagai-pengolahan-string-pada-javascript.md
├── 2020-01-17-cara-cepat-resize-gambar-secara-online.md
├── 2020-01-19-memberi-format-uang-per-tiga-digit.md
├── 2020-01-19-membuat-judul-untuk-jekyll.md
└── 2020-01-19-udah-kenal-termux-path-tools-powerful-untuk-hacking.md
```

Nah, kan capek tuh kalau kita harus mengikutin standar itu kalau mau buat postingan baru. Ya, kita harus tau dulu dong sekarang itu tahun berapa (pasti tau lah ya), bulan berapa, dan tanggal berapa. Belum lagi, judul postingan kita harus dikonversi jadi huruf kecil semua dan harus hanya berupa alphanumerik dan strip (ya nggak harus juga sih, tapi standarnya seperti itu). Lalu, bagaimana cara cepatnya?

Berikut ini adalah kodenya (pakai Javascript):

```javascript
judul = 'Mau Dikasih Judul Apa Ya Blognya? Hmmm.... Aku Bingung Deh. Kamu Pang?'

// setelah ini, jangan diubah

eye_of_agamoto = new Date()
tahun = eye_of_agamoto.getFullYear()
bulan = ('0' + eye_of_agamoto.getMonth() + 1).split('').splice(-2, 2).join('')
tanggal = ('0' + eye_of_agamoto.getDate()).split('').splice(-2, 2).join('')

judul = judul.replace(/[^a-z0-9]/gi, '-').replace(/-+/g, '-').toLowerCase()

selesai = `${tahun}-${bulan}-${tanggal}-${judul}.md`
console.log(selesai)
```

Hasilnya adalah `2020-01-19-mau-dikasih-judul-apa-ya-blognya-hmmm-aku-bingung-deh-kamu-pang-.md`.

Cukup mudah kan?

Kayaknya memang nggak salah sih kalau Jekyll ini platform bloggingnya programmer. Karena memang geek banget gitu kalau mau posting (lebih geek Gatsby JS sih tapi ntar lah kalau pengen). Untuk format penulisannya pakai Markdown. Terus templatingnya pakai Liquid (lebih mudah daripada templatingnya Hugo). Terus auto deploy di Github. Jadi ya, mau nggak mau harus bisa sedikit tentang Git sih (minimal tau cara uploadnya).

Oke begitu. Kalau ada yang mau ditanyakan langsung komen di bawah aja ya.

Bye.