---
layout: post
title: Cara Cepat Coding Codeigniter
bahasa: codeigniter
---

Setiap programmer tentunya ingin membuat aplikasinya dengan cepat. Apalagi kalau ada proyek menumpuk yang menunggu untuk diselesaikan. Mau nggak mau ya harus cepat sih ngerjainnya. Bahkan, kalau bisa, dalam sehari setidaknya ada 10 proyek diselesaikan.

Mantap jiwa. Hehehehehe.

Nah, salah satu cara yang biasa dilakukan programmer adalah copy paste skrip atau proyek serupa yang pernah dikerjakan. Tapi, gimana dong kalau misalnya kamu dapat proyek baru yang belum pernah dikerjain? Ya mau nggak mau sih ngerjain lagi dari awal.

Nah, berikut ini ada beberapa trik supaya kamu koding di Codeigniter dengan cepat (untuk framework dan bahasa pemrograman lainnya menyusul ya):

**Gunakan template engine**

_Menggunakan Codeigniter Twig_

Menggunakan template engine akan mengurangi ketikan kita di bagian view. Soalnya, kita hanya cukup sekali aja membuat view templatenya. Baru setelah itu kan kita cukup menambahkan view yang diubah aja.

Misalnya saja kita memiliki file `layout.twig` yang isinya:

```twig
Header
{% raw %}
{% block isi %}
  Ini adalah bagian isi
{% endblock %}
{% endraw %}
Footer
```

Nah, misalnya kita ada file `konten.twig` dan kita ambil layout dari `layout.twig`, yang diubah cuma di bagian isi. Maka, isi dari `konten.twig` adalah:

```twig
{% raw %}
{% extends "layout.twig" %}
{% block isi %}
  Isinya beda
{% endblock %}
{% endraw %}
```

Untuk mempelajari lebih lanjut tentang penggunaan Codeigniter Twig ini, silahkan [baca postinganku yang membahas tentang ini](indahnya-twig-cara-mengkombinasikannya-dengan-codeigniter-0120.html).

_Menggunakan Blade Codeigniter_

Konsepnya sama seperti Codeigniter Twig di atas. Yaitu, menggabungkan Codeigniter dengan salah satu template engine. Kalau di bagian ini, aku menggabungkannya dengan Blade. Tau lok Blade itu apa? Yap. Template enginenya Laravel. Nah, buat kamu yang nggak menggunakan Laravel, bisa mencicipinya dengan Blade Codeigniter ini. Untuk mencobanya, silahkan [download repositorinya](https://github.com/mzaini30/blade-codeigniter).

Setelah kamu mendownload repositori ini, yang pertama kamu lakukan adalah menjalankan perintah `composer update` agar Bladenya bisa berjalan.

Nanti akan muncul folder vendor yang sizenya sekitar 9 MB.

**Controller untuk form hanya satu function**

Nah, dicoba deh skrip di bawah ini:

```php
public function form(){
  if (!$_POST){
    $this->twig->display("form");
  } else {
    // jika form sudah dipost
  }
}
```

Dengan skrip seperti itu, kita nggak perlu lagi membuat dua function untuk satu form seperti:

```php
public function form(){
  $this->twig->display("form");
}

public function form_do(){
  // perintah yang dijalankan setelah form dipost
}
```

**Mendapatkan semua nilai post dari form**

Biasanya kan kita menggunakan sintaks seperti ini untuk mendapatkan data dari form:

```php
$nama = $this->input->post("nama");
$alamat = $this->input->post("alamat");
$status = $this->input->post("status");

$this->db->insert("database", array(
  "nama" => $nama,
  "alamat" => $alamat,
  "status" => $status
);
```

Sebenarnya bisa disingkat menjadi:

```php
$data = (array) $this->input->post();
$this->db->insert("database", $data);
```

**Menyingkat array**

Kalau biasanya kan array itu seperti ini:

```php
array(
  "nama" => $nama,
  "alamat" => $alamat
);
```

Bisa disingkat menjadi:

```php
compact("nama", "alamat");
```

Oke itu aja. Semoga kamu suka. Kalau ada yang nggak paham (atau sekedar mau sapa _hi_) bisa komen di bawah. Kayaknya aku habis ini mau mempelajari server dengan Javascript. Jadi tunggu aja artikelnya.

Bye.