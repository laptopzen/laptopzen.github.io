---
layout: post
title: "Menghubungkan Github Pages dengan Custom Domain"
bahasa: html
date: 2020-02-03 12:34:47 +0800
---

Sebagai seorang blogger, tentunya mau dong supaya blognya itu jadi TLD. Eh, tapi tau nggak, TLD itu apa? Jadi, TLD itu singkatan dari Top Level Domain. Atau, domain-domain seperti .com, .net, .org, .id, dan lain sebagainya.

Contoh dari situs-situs yang menggunakan TLD adalah <https://google.com>, <https://facebook.com>, dan tentunya <https://mzaini30.com>.

## Keuntungan menggunakan TLD (custom domain)

Apa sih keuntungan menggunakan TLD?

1. Blogmu gampang diingat sehingga pengunjung mudah menemukan blogmu kembali. Apalagi kalau kamu pakai yang .com, makin gampang lagi orang ngingetinnya. Soalnya kan zaman sekarang ni paling banyak orang-orang pakai .com, seperti <https://google.com>, <https://twitter.com>, dan <https://medium.com>. Makanya aku sewa domain yang berakhiran .com.
2. Kamu sebagai blogger kelihatan niat mengurusi blog. Soalnya kan, TLD itu bayar
3. Kelihatan profesional. Apalagi kalau kamu selalu menulis berdasarkan niche tertentu

## Setting custom domain di Github

Yang jadi masalah adalah ketika kamu menggunakan platform yang nggak familiar. Misalnya aja menggunakan Github Pages yang tutorial konekinnya ke custom domain tu nggak ketemu di Google.

Kalau ketemu juga bahasa Inggris. Hehehehehe...

Makanya nih, aku buat postingan ini buat kamu yang udah punya blog di Github Pages terus ingin menghubungkannya ke custom domain.

Yuk kita mulai.

Misalnya kamu memiliki data sebagai berikut:

| Custom Domain | Github Pages |
|-|-|
| situs.com | situs.github.io |

## Setting di hostingan

Masuk di bagian setting DNS di hostingan yang kamu sewa. Lalu setting seperti:

| Host | Type | Value |
|-|-|-|
| @ | A | 185.199.108.153 |
| @ | A | 185.199.109.153 |
| @ | A | 185.199.110.153 |
| @ | A | 185.199.111.153 |
| www | CNAME | situs.github.io |

## Setting di Github

Buat file `CNAME` yang isinya:

```
situs.com
```

Mudah kan ternyata? Ayo deh buat blog yang basisnya di Github Pages biar aku ada temennya. Hehehehhe.