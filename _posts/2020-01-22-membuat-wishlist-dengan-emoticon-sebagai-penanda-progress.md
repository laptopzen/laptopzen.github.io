---
layout: post
title: Membuat Wishlist dengan Emoticon Sebagai Penanda Progress
bahasa: javascript
---

Pernahkah kamu membuat wishlist? Itu tuh yang daftar keinginan yang ingin kita lakukan. Misalnya seperti:

- makan cempedak
- jalan-jalan
- nikah
- makan tempe

Atau mungkin bisa kita kasih persenan nih sebagai parameter sudah seberapa besar usaha yang kita lakukan untuk menggapai wishlist kita itu. Misalnya seperti:

- makan cempedak 50%
- jalan-jalan 10%
- nikah 90%
- makan tempe 70%

Tapi kayaknya bagusnya kita pakai emoticon deh:

- makan cempedak 😂😂😂😂😂
- jalan-jalan 😂
- nikah 😂😂😂😂😂😂😂😂😂
- makan tempe 😂😂😂😂😂😂😂

Terus gimana kalau untuk poin `nikah` masih 0%, kita kasih emoticon khusus deh:

- makan cempedak 😂😂😂😂😂
- jalan-jalan 😂
- nikah 😱
- makan tempe 😂😂😂😂😂😂😂

Eh tapi belum berurutan ding. Kita urutkan coba:

- jalan-jalan 😂
- makan cempedak 😂😂😂😂😂
- makan tempe 😂😂😂😂😂😂😂
- nikah 😱

Nah terus. Gimana kalau mau masukin wishlist baru? Nyesuaikan urutan lagi? Kasih emoticon lagi sesuai jumlah persenannya? Kan capek.

Jadi aku buat skripnya:

```javascript
data = `skripsi 5
lulus 0
menulis-buku 0
pelang 10
energen 0
sugeh 1
sedekah 0
layout 7`

// di bawah ini jangan diedit

ubah = `10 ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
1 👊
2 👊👊
3 👊👊👊
4 👊👊👊👊
5 👊👊👊👊👊
6 👊👊👊👊👊👊
7 👊👊👊👊👊👊👊
8 👊👊👊👊👊👊👊👊
9 👊👊👊👊👊👊👊👊👊
0 👩‍💻`

ubah = ubah.split("\n")
for (n in ubah){
	ubah[n] = ubah[n].split(" ")
}

data = data.split("\n")
data.sort()
for (n in data){
	for (o in ubah){
		data[n] = data[n].replace(` ${ubah[o][0]}`, ` ${ubah[o][1]}`)
	}
	data[n] = data[n].replace(/-/g, " ")
}
data = data.join("\n")

console.log(data)
```

Hasilnya:

![Screenshot kode](https://telegra.ph/file/342670aff9fcd1623ff75.png)