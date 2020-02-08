---
layout: post
title: "Cara Menampilkan Data Berurutan dari Database"
bahasa: codeigniter
date: 2020-02-08 11:34:35 +0800
---

Codeigniter saat ini bisa dibilang sebagai tools yang powerful untuk mengolah website. Ya, dengan Codeigniter, kamu bisa membuat website apapun yang kamu suka dengan cepat. Salah satu yang kusuka dari Codeigniter ini adalah ukurannya yang kecil. Kalau nggak salah hanya sekita 3 MB. Bandingkan aja sama Laravel yang bisa 20an MB. Atau Nuxt JS yang bisa seratus MB lebih.

Wow.

Nah, kali ini kita akan mencoba mengambil data dari database lalu menampilkannya dengan berurutan.

## Struktur database

- id
- nama
- status

Oh iya, misalnya aja nama tablenya adalah `biodata`.

## Mengambil data secara berurutan berdasarkan nama

```php
$data = $this->db->order_by("nama")->get("biodata")->result();
```