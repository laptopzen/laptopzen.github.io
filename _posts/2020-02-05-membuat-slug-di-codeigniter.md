---
layout: post
title: "Membuat Slug di Codeigniter"
bahasa: codeigniter
date: 2020-02-05 05:37:35 +0800
---

Apa itu slug?

Gampangannya adalah jika kamu memiliki judul postingan `Wah Heboh! Ada Ikan Berkepala Lele`, maka slugnya adalah `wah-heboh-ada-ikan-berkepala-lele`.

Sudah paham lok?

Slug ni buat apa sih? Tentu saja supaya ketika ada link blog yang dibagikan, kita sudah tau maksud artikelnya tu tentang apa secara sekilas dengan hanya melihat linknya. Coba deh kamu bandingkan antara dua link ini, mana yang lebih mudah kita pahami isinya tentang apa:

- `situs.com/wah-heboh-ada-ikan-berkepala-lele`
- `situs.com/34`

Kelihatan kan kalau lebih mudah memahami yang pertama?

Nah, sekarang kita akan membuatnya di Codeigniter.

## Kode

```php
$teks = preg_replace('~[^-\w]+~', '-', $data->judul);
$teks = strtolower($teks);
if (empty($teks)){
	$teks = 'n-a';
}

$data->slug = $teks . '-' . rand(1, 99999);
```

## Penjelasan kode

Pertama, kita replace dulu semua karakter selain strip, a sampai z, dan nol sampai sembilan menjadi strip:

```php
$teks = preg_replace('~[^-\w]+~', '-', $data->judul);
```

Terus kita ubah teksnya jadi kecil:

```php
$teks = strtolower($teks);
```

Oh iya, kalau teksnya nggak ada, kita kasih `n-a`:

```php
if (empty($teks)){
	$teks = 'n-a';
}
```

Terakhir, kita kasih angka acak supaya kalau ada judul yang sama, bisa kita kasih slug yang berbeda:

```php
$data->slug = $teks . '-' . rand(1, 99999);
```

## Teknik lainnya

Barusan baca komennya Bang Fika (cek Disqus di bawah) ternyata bisa aja pakai skrip satu baris ini:

```php
url_title(strtolower($this->input->post('title')));
```

Wow menarik. Nanti aku coba lah.