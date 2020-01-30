---
layout: post
title: "Apa Itu MVC dalam Codeigniter?"
bahasa: codeigniter
date: 2020-01-30 18:34:44 +0800
---

Kalau kalian adalah pengguna framework PHP semacam Codeigniter, pasti nggak asing dengan istilah MVC. Namun, bagi kalian yang baru dengan istilah MVC, kita akan bahas di sini.

## Model

Model adalah sekumpulan kode yang berguna untuk pengolahan database. Jadi, database tuh mau diapain, Model yang bertanggung jawab. Apakah hanya mau ditampilkan? Atau disort? Atau ditambahkan ke database? Itu Model yang bertanggung jawab.

Tapi, bisa aja sih nggak pakai Model. Langsung diolah di Controllernya aja. Apalagi kalau kita cuma membuat website yang sistem pengolahan databasenya sederhana. Misalnya cuma menampilkan, mengedit, dan menghapus tanpa melakukan left join, right join, inner join, dan outer join.

## View

View itu adalah bagian untuk menampilkan view-view yang kita lihat di browser kita. Letaknya adalah di folder `application/views`. Kalau secara defaultnya, tampilan dari View kita seperti:

- index.php
- admin.php
- user.php

Di View, bisa juga kita meletakkan file di dalam folder seperti:

- admin/beranda.php
- admin/tambah-barang.php
- user/beranda.php

Namun, jika kita menggunakan [Codeigniter Twig](indahnya-twig-cara-mengkombinasikannya-dengan-codeigniter-0120.html), maka ekstensi filenya adalah Twig:

- index.twig
- user.twig
- login.twig

Jadi, bagus mana nih antara Codeigniter murni atau Codeigniter Twig? Ya sesuai selera aja sih. Kalau aku lebih suka Codeigniter Twig karena sudah bermain layout (kalau nggak salah sih Codeigniter 4 sudah bermain layout, cuma aku belum nyoba).

## Controller

Controller itu seperti namanya yaitu pengatur. Nah, Controller adalah inti sebuah framework yang bersistem MVC. Dengan Controller ini, Model dan View bisa digerakkan. Soalnya, ketika kita mengakses suatu link, maka yang dipanggil pertama adalah Controllernya. Misalnya aja link `http://localhost/admin/tampil/5`. Itu sama saja dengan mengakses:

```php
// nama file: Admin.php
<?php
class Admin extends CI_Controller {
  public function tampil($id){
    // kodenya di sini
  }
}
```

Jadi, sebenarnya bisa aja sih kita pakai Controller aja tanpa View dan Model. Tapi ya, bakalan dirty banget deh.