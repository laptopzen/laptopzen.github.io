---
layout: post
title: "Berbagai Permasalahan yang Muncul Saat Upload Project Codeigniter ke Heroku dan Cara Mengatasinya"
bahasa: codeigniter
date: 2020-01-28 05:57:44 +0800
---

Yang namanya website menjadi kebutuhan setiap perusahaan untuk otomatisasi data yang dimiliki. Nah, sebagai seorang programmer, maka aku menawarkan kemampuanku dalam membuat berbagai macam website untuk membantu mereka dalam menyelesaikan pekerjaan mereka (yang segunung dan nggak selesai-selesai kalau dikerjakan secara manual).

Lalu, ketika kita ingin mengajukan proposal website kepada suatu perusahaan, tentu saja kita akan membuat website demonya dulu kan? Tentu kita membutuhkan hosting untuk menjalankan website kita. Tapi kan, duitnya belum ada. Hehehehe. Maka, aku upload websiteku yang berbasis Codeigniter ke Heroku.

Jadi, link websitenya itu adalah <https://blog-sederhana.herokuapp.com/> yang kugunakan untuk dijual (kamu mau beli kah?). Nah, ketika aku upload ke Heroku, muncul tuh berbagai permasalahan. What? Dan berikut ini permasalahan dan pemecahannya:

## PHP nggak bisa jalan

Jalankan `composer update`.

## Too many redirect

Buka `.htaccess`.

Pastikan nggak ada redirect HTTP ke HTTPS di dalam `.htaccess`.

Nah, seperti di bawah ini:

```
# RewriteEngine On
# RewriteCond %{HTTPS} off
# RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]\

RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.php/$1 [L]

Options -Indexes
<FilesMatch "\.(sqlite)$">
Deny from all
</FilesMatch>
```

Jadi, awalnya aku menggunakan kode di bawah ini untuk redirect HTTP ke HTTPS saat website serupa dihosting di Domainesia:

```
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]\
```

Namun ternyata menimbulkan permasalahan di Heroku. Jadi, kutambahin tanda `#` di depannya supaya dianggap sebagai komentar.

## Driver database (PDO) nggak ada

Tambahkan `"ext-pdo_sqlite": "*"` di dalam `composer.json` sehingga kodenya menjadi seperti ini:

```javascript
{
	"description": "The CodeIgniter framework",
	"name": "codeigniter/framework",
	"type": "project",
	"homepage": "https://codeigniter.com",
	"license": "MIT",
	"support": {
		"forum": "http://forum.codeigniter.com/",
		"wiki": "https://github.com/bcit-ci/CodeIgniter/wiki",
		"slack": "https://codeigniterchat.slack.com",
		"source": "https://github.com/bcit-ci/CodeIgniter"
	},
	"require": {
		"php": ">=5.3.7",
		"ext-pdo_sqlite": "*" // di bagian sini ya
	},
	"suggest": {
		"paragonie/random_compat": "Provides better randomness in PHP 5.x"
	},
	"require-dev": {
		"mikey179/vfsStream": "1.1.*",
		"phpunit/phpunit": "4.* || 5.*"
	}
}
```

Lalu jalankan `composer update`.

## Nggak bisa membuat session

Buka `/application/config/config.php` lalu pastikan kodenya seperti ini:

```php
$config['sess_save_path'] = sys_get_temp_dir();
```