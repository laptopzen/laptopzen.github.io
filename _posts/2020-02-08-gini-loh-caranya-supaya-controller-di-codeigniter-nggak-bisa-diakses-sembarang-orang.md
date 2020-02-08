---
layout: post
title: "Gini Loh Caranya Supaya Controller di Codeigniter Nggak Bisa Diakses Sembarang Orang"
bahasa: codeigniter
date: 2020-02-08 10:49:44 +0800
---

Biasanya kan kita bisa mengakses controller Codeigniter hanya dengan linknya. Misalnya aja ada controller yang namanya Admin. Maka, kita aksesnya dengan link `situs.com/admin`. Tapi kan, bahaya dong kalau sembarang orang bisa akses. Iya kan? Nah, terus gimana tuh supaya nggak sembarangan orang mengakses controller tersebut?

Kalau cara yang paling gampang ya buat nama controller aneh-aneh. Misalnya aja: Ini_bukan_controller_admin_jadi_jangan_masuk.

Asli eh aneh banget nama controllernya. Hehehehe...

Tapi, kalau cara yang paling tepat ya kita buat semacam auth. Jadi, hanya admin sajalah yang bisa akses.

Misalnya saja di controller Admin. Kita tambahkan skrip di bawah ini di dalamnya controller Admin:

```php
public function __construct(){
	parent::__construct();
	if ($this->session->userdata("status") != "admin"){
		redirect("/login");
	}
}
```

## Penjelasan kode

Di awal kode, kita menggunakan:

```php
public function __construct(){
```

Nah, fungsi __construct adalah fungsi yang dijalankan sebelum menjalankan fungsi lainnya.

```php
parent::__construct();
```

Mengapa menggunakan parent __construct?

Karena kan aslinya itu fungsi __construct sudah ada di corenya Codeigniter. Nah, makanya dikasih parent yang artinya di bagian situ akan mengimport isi dari fungsi __construct yang sudah ada lalu akan diisi dengan kode yang kita buat.

```php
if ($this->session->userdata("status") != "admin"){
	redirect("/login");
}
```

Nah, di situ kita buat fungsi yaitu jika userdata status bukan admin, maka akan redirect ke halaman /login.

## Cara membuat userdata

Untuk membuat userdata, bisa dengan kode berikut:

```php
$this->session->set_userdata("status", "admin");
```

Nah, terus kode itu kita taroh di mana?

Tentu saja di halaman login. Yaitu ketika pengunjung memasukkan username dan password yang benar, maka kita jalankan kode tersebut.

## Menghapus semua session

Untuk menghapus semua session:

```php
$this->session->sess_destroy();
```