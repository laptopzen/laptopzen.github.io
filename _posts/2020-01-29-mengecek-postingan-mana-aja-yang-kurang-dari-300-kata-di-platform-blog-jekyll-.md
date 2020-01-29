---
layout: post
title: "Mengecek Postingan Mana Aja yang Kurang dari 300 Kata (di Platform Blog Jekyll)"
bahasa: python
date: 2020-01-29 19:39:56 +0800
---

Sebagai seorang blogger tentu saja ingin postingan yang dibuat itu rame dan banyak yang berkunjung + berkomentar. Nah, salah satu cara supaya rame pengunjung tentu saja dengan memperhatikan aspek SEO sehingga banyak pengunjung dari Google yang datang. Kalau kata Yoast SEO, salah satu aspek dari SEO adalah jumlah kata dalam setiap postingan adalah lebih dari 300 kata. Nah, itu yang mau kita buat.

Pertama, kita pahami dulu platform blog yang akan kita analisa. Di sini aku menggunakan Jekyll sehingga semua postingan berada di dalam folder _posts.

## Kodenya

```python
import os, re

minimal_kata = 300

postingan = os.listdir("_posts")

kata = []
for x in postingan:
    file = open(f"_posts/{x}", "r")
    data = file.read()
    regex = re.compile("\W+").split(data)
    regex = list(filter(None, regex))
    jumlah = len(regex)
    kata.append(jumlah)
    file.close()

nggak_lolos = []
kata_nggak_lolos = []
for n, x in enumerate(kata):
    if x < minimal_kata:
        nggak_lolos.append(postingan[n])
        kata_nggak_lolos.append(kata[n])

print(f"""Postingan yang kurang dari {minimal_kata} kata:
""")
for n, x in enumerate(nggak_lolos):
    print(f"- {x} ({kata_nggak_lolos[n]} kata)")
```

## Penjelasan kode

Pertama, kita import dulu modul-modul yang dibutuhkan:

```python
import os, re
```

Lalu kita tentukan minimal kata berapa:

```python
minimal_kata = 300
```

Lalu kita list nama file postingan di blog:

```python
postingan = os.listdir("_posts")
```

Kemudian dari masing-masing file postingan itu, kita tanya tuh berapa kata di masing-masing file terus masukkan ke list:

```python
kata = []
for x in postingan:
    file = open(f"_posts/{x}", "r")
    data = file.read()
    regex = re.compile("\W+").split(data)
    regex = list(filter(None, regex))
    jumlah = len(regex)
    kata.append(jumlah)
    file.close()
```

Terus kita cari postingan mana aja yang nggak lolos persyaratan (di bawah 300 kata):

```python
nggak_lolos = []
kata_nggak_lolos = []
for n, x in enumerate(kata):
    if x < minimal_kata:
        nggak_lolos.append(postingan[n])
        kata_nggak_lolos.append(kata[n])
```

Baru kita tampilkan ke layar, postingan-postingan yang nggak lolos persyaratan:

```python
print(f"""Postingan yang kurang dari {minimal_kata} kata:
""")
for n, x in enumerate(nggak_lolos):
    print(f"- {x} ({kata_nggak_lolos[n]} kata)")
```

## Hasil program

```
Postingan yang kurang dari 300 kata:
                              
- 2020-01-12-tutorial-dasar-html-dan-css.md (53 kata)
- 2020-01-12-main-activity-untuk-aplikasi-android.md (241 kata)
- 2020-01-12-belajar-javascript-untuk-pemula.md (155 kata)
- 2020-01-15-bagaimana-cara-cepat-membuat-aplikasi-android-.md (30 kata)
- 2020-01-17-cara-cepat-resize-gambar-secara-online.md (247 kata)
- 2020-01-19-udah-kenal-termux-path-tools-powerful-untuk-hacking.md (221 kata)
- 2020-01-21-yuk-berkenalan-dengan-markdown.md (136 kata)
- 2020-01-21-ada-yang-pernah-pakai-template-literal-.md (189 kata)
- 2020-01-22-menggabungkan-banyak-file-menjadi-satu-di-linux-dan-windows.md (109 kata)
- 2020-01-22-membuat-wishlist-dengan-emoticon-sebagai-penanda-progress.md (236 kata)
- 2020-01-22-memahami-ifconfig.md (277 kata)
- 2020-01-23-ingin-berkontribusi-di-blog-ini-.md (176 kata)
- 2020-01-24-mengenal-fungsi-di-javascript.md (187 kata)
- 2020-01-24-benarkah-teknologi-mengancam-kemanusiaan-.md (114 kata)
- 2020-01-24-mencari-nilai-1000-faktorial-dengan-javascript.md (208 kata)
- 2020-01-25-embed-video-dari-youtube-ke-blog.md (161 kata)
- 2020-01-25-yuk-mendesain-dengan-berbagai-warna-pastel.md (203 kata)
- 2020-01-25-menghilangkan-elemen-tertentu-di-blog.md (125 kata)
- 2020-01-26-berbagai-macam-penyimpanan-offline-dengan-javascript.md (287 kata)
```