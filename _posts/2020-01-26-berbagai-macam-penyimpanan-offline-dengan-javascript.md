---
layout: post
title: "Berbagai Macam Penyimpanan Offline dengan Javascript"
bahasa: javascript
date: 2020-01-26 21:55:56 +0800
---

Salah satu elemen dari sebuah aplikasi adalah database. Kan database yang kita tau itu yang berjalan di sebuah server seperti MySQL, MongoDB, PostgreSQL, dan database lainnya yang begitu banyak. Atau, bisa juga standalone macam SQLite. Namun, pernah nggak berpikir bahwa kita bisa memanfaatkan browser untuk menjadi sebuah wadah database?

Wow.

Jadi, coba deh kita bahas berbagai teknik menjadikan browser sebagai database.

## localStorage

localStorage itu berarti satu variabel cuma bisa diisi dengan satu value. 

Contoh menambahkan suatu value di localStorage:

```javascript
localStorage.setItem("nama", "Zen")
localStorage.setItem("alamat", "Loa Janan")
```

Sedangkan untuk memanggilnya:

```javascript
localStorage.getItem("nama")
localStorage.getItem("alamat")

// atau bisa juga dengan

localStorage.nama
localStorage.alamat
```

Oh iya, untuk localStorage ini, kalau di bagian setItemnya diganti valuenya, maka di database juga berubah. Contohnya:

```javascript
localStorage.setItem("nama", "Zen")

// ketika dipanggil, valuenya adalah Zen

localStorage.setItem("nama", "Yani")

// valuenya berubah menjadi Yani
```

### Menambah data JSON ke dalam localStorage

Untuk menambahkan data JSON, maka kamu harus mengkonversi data JSON itu menjadi string terlebih dahulu dengan sintaks `JSON.stringify`. Sedangkan untuk mengubah string menjadi JSON, gunakan `JSON.parse`. Contohnya seperti berikut:

```javascript
nama = ["Zen", "Loka", "Angga", "Anggi"]

// memasukkan nama ke dalam storage:

localStorage.setItem("nama", JSON.stringify(nama))

// mengambil nama dari storage:

JSON.parse(localStorage.nama)
```

## sessionStorage

Untuk sessionStorage sintaksnya sama dengan localStorage. Namun, penggunaannya yang berbeda.

Kalau localStorage, data-data yang tersimpan di dalamnya itu permanen dan akan hilang jika dihapus seperti `localStorage.removeItem("nama")`. Sedangkan kalau sessionStorage, data yang ada di situ hanya tampil sekali. Setelah direload, data akan terhapus. Jadi, sessionStorage ini fungsinya untuk memberi tau user kalau dia sudah login atau data yang diisi sudah dikirim.