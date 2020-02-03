---
layout: post
title: "Menghubungkan Github Pages dengan Custom Domain"
bahasa: html
date: 2020-02-03 12:34:47 +0800
---

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