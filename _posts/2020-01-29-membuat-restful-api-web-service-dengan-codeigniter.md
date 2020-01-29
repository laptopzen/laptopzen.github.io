---
layout: post
title: "Membuat RESTful API Web Service dengan Codeigniter"
bahasa: codeigniter
date: 2020-01-29 16:31:11 +0800
---

Sebelumnya, apa itu RESTful API Web Service? 

Namanya aja bikin bingung dah maksudnya apa.

Jadi, maksudnya itu lah, kita mau membuat suatu website yang hanya menampilkan JSONnya aja atau datanya aja. Seperti:

```javascript
[{"id":"1","nama":"Zen"},{"id":"2","nama":"Yani"},{"id":"3","nama":"Aziz"}]
```

Gunanya, itu dengan data mentah itu kita bisa olah mau ditampilkan, hapus kah, edit kah, macem-macem lah pokoknya.

Jadi, proses pemuatan website akan menjadi lebih cepat. Karena bagian datanya itu terpisah. Jadi, kali ini kita buat di bagian pengolahan datanya aja dan menampilkannya dalam bentuk JSON tadi itu.

## Mulai koding

Pertama, download dulu [Codeigniter Twig](https://github.com/mzaini30/codeigniter-twig).

Lalu, kita buka `database.sqlite` dan kita buat table baru, namanya `biodata`. Isinya itu:

| Name | Type | PK | AI |
|-|-|-|-|
| id | INTEGER | yes | yes |
| nama | TEXT | | |

![Tabel biodata untuk database RESTful API Web Service](https://telegra.ph/file/745b311c0de65d31f72af.jpg)

Lalu, kita isi dulu di bagian nama dengan tiga nama terserah aja.

![Tiga nama di table biodata](https://telegra.ph/file/0fcd39962d2a851ba8503.jpg)

Buat controller baru yang nama filenya `Json.php` (letaknya di `application/controllers`).

Isi `Json.php` itu dengan:

```php
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Json extends MY_Controller {
	public function index(){
		$data = $this->db->get('biodata')->result();
		echo json_encode($data);
	}

	public function tambah($nama){
		$this->db->insert('biodata', compact('nama'));
		$data = $this->db->get('biodata')->result();
		echo json_encode($data);	
	}

	public function hapus($id){
		$this->db->delete('biodata', compact('id'));
		$data = $this->db->get('biodata')->result();
		echo json_encode($data);	
	}

	public function ubah($id, $nama){
		$this->db->update('biodata', compact('nama'), compact('id'));
		$data = $this->db->get('biodata')->result();
		echo json_encode($data);	
	}
}
```

Lalu, buka route (letaknya di `application/config/routes.php`). Kemudian isi dengan:

```php
$route['default_controller'] = 'json';
$route['tambah/(:any)'] = 'json/tambah/$1';
$route['hapus/(:any)'] = 'json/hapus/$1';
$route['ubah/(:any)/(:any)'] = 'json/ubah/$1/$2';
```

Untuk `default_controller`, karena dari sananya sudah ada, ganti aja valuenya dengan `default_controller` yang ini.

Jalankan server dengan mengetik kode berikut di Terminal:

```bash
php -S localhost:2020
```

Lalu buka `http://localhost:2020` di browser.

## Tampilan program

Misalnya, ingin menampilkan semua data, buka aja `http://localhost:2020`. Maka akan menampilkan:

```javascript
[{"id":"1","nama":"Zen"},{"id":"2","nama":"Yani"},{"id":"3","nama":"Aziz"}]
```

Ingin menambah data? Buka aja `http://localhost:2020/tambah/Kucing`. Maka akan menampilkan:

```javascript
[{"id":"1","nama":"Zen"},{"id":"2","nama":"Yani"},{"id":"3","nama":"Aziz"},{"id":"6","nama":"Kucing"}]
```

Ingin menghapus data yang idnya 6? Buka aja `http://localhost:2020/hapus/6`:

```javascript
[{"id":"1","nama":"Zen"},{"id":"2","nama":"Yani"},{"id":"3","nama":"Aziz"}]
```

Ingin mengubah data yang memiliki id 3 dengan nama Rey? Buka aja `http://localhost:2020/ubah/3/Rey`:

```javascript
[{"id":"1","nama":"Zen"},{"id":"2","nama":"Yani"},{"id":"3","nama":"Rey"}]
```

## Demo program

Untuk demo program ini, kamu bisa buka <http://api-codeigniter.herokuapp.com/>. Dan untuk source code, buka aja <https://github.com/mzaini30/api-codeigniter>.