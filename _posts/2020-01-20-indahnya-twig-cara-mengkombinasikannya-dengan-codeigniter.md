---
layout: post
title: Indahnya Twig + Cara Mengkombinasikannya dengan Codeigniter
bahasa: twig
---

Apakah kamu adalah orang yang masih menggunakan `<?= $data->nama ?>` di halaman view PHP? Atau bahkan yang lebih parah lagi `<?php $data["nama"]; ?>`. Asli eh ribet banget. Kenapa nggak pakai `{% raw %}{{ data.nama }}{% endraw %}`? Lebih simpel kan?

Eh emang bisa ya?

Bisa dong. Itu namanya Twig. Salah satu template engine. Sekarang sih jadi favoritku karena sintaksnya yang sederhana dan sebagian besar template engine sekarang sintaksnya mirip-mirip itu (kecuali Blade tentunya). Contoh yang menggunakan sintaks serupa adalah Liquid punyanya Jekyll dan Vue JS.

Kalau kamu mau lebih mendalami Twig, bisa main ke [websitenya](https://twig.symfony.com/). Di artikel ini hanya sekilas aja sih.

# Sintaks Twig

_Menampilkan variabel_

```twig
{% raw %}{{ data }}{% endraw %}
```

Bandingkan dengan cara PHP menampilkan data:

```php
<?= $data ?>
```

Oh iya, kalau di Twig, semua value variabel diconvert HTML Spesial Karakter ya sehingga nggak gampang dideface. Misalnya aja `<!--` akan diubah menjadi `&lt;!--`. Jadi aman ya.

Tapi kalau misalnya mau tetap; `<!--` tetap `<!--`, maka sintaks Twignya menjadi `{% raw %}{{ data | e }}{% endraw %}`.

# Looping

Kalau di Twig:

```twig
{% raw %}
{% for x in data %}
  {{ x.nama }}
{% endfor %}
{% endraw %}
```

Bandingin yah kalau di PHP biasa:

```php
<?php foreach ($data as $x): ?>
  <?= $x["nama"] ?> 
  <!-- atau bisa juga <?= $x->nama ?> -->
<?php endforeach ?>
```

Lebih rumit yang PHP kan?

# Template

Sesuai dengan namanya, yaitu template engine PHP, maka template adalah fitur andalannya. Sintaksnya seperti:

```twig
{% raw %}
{% extends "layout.twig" %}
{% block isi %}
  Ini isinya...
{% endblock %}
{% endraw %}
```

Kalau di PHP, nggak ada fitur ini.

**Menggabungkan Twig dengan Codeigniter**

Nah, untuk menggabungkan Twig dengan PHP, kamu bisa menggunakan [Codeigniter Twig](https://github.com/mzaini30/codeigniter-twig). Petunjuk pemakaiannya ada di repositori tersebut.

Nah, kalau di CI biasanya kan kalau mau memanggil view dengan kode `$this->load->view("admin/beranda", $data);`. Kalau di CI Twig ini beda lagi. Kalau di sini, kita pakai `$this->twig->display("admin/beranda", $data);`.

Nah terus, kalau biasanya di CI kan kita naroh view kita di folder view. Yang ini juga sih. Cuma, dia ekstensinya `.twig`, bukan `.php`. Lalu, kita menggunakan kode-kode Twig di dalamnya.