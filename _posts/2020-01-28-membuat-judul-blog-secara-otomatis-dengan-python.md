---
layout: post
title: "Membuat Judul Blog Jekyll Secara Otomatis dengan Python"
bahasa: python
date: 2020-01-28 16:41:55 +0800
---

Kan kalau belajar pemrograman itu lebih baik kalau langsung mengerjakan studi kasus. Kenapa? Soalnya lok, kalau kita belajar bahasa pemrograman dengan studi kasus, maka kita akan lebih cepat paham sintaksnya dan hapal secara otomatis. Seperti katanya [Petani Kode](https://www.instagram.com/p/B7nd552lFoe/?igshid=1nvyt6ul8xlht) bahwa tahu (bulat) itu berbeda dengan bisa (ular). Kalau tau ya cuma sekedar tau belum tentu bisa membuat. Kalau bisa, berarti bisa membuat aplikasinya.

Nah, sekarang kita akan membuat skrip Python untuk membuat judul blog berbasis Jekyll.

## Mengapa Python?

Bukan karena aku pythoniak atau apalah namanya itu ya. Tapi kan aku terkadang blogging menggunakan HP, dan aku butuh tools untuk mempermudah pengerjaanku sehari-hari; salah satunya adalah blogging.

Nah, aku dah nyoba lok pakai Javascript, pakai Node JS gitu. Namun, ketika aku mencoba `hello world`, dia ada loadingnya gitu. Jadi, di sintaks Node JS, aku mengisi kode:

```javascript
console.log("hello")
```

Itu ada loading dulu beberapa detik baru muncul tulisan `hello`. Ya, nggak bagus banget lah. Aku maunya yang cepat gitu.

Akhirnya aku coba lok pakai Python untuk mengetes kecepatannya:

```python
print("hello")
```

Dan ternyata, apa yang terjadi? Kode yang kubuat itu, langsung dieksekusi tanpa jeda. Mantap.

Mungkin kalau Node JS di Termux itu berlapis-lapis mungkin interpreternya sehingga lama memprosesnya.

Akhirnya, aku memilih Python untuk membuat aplikasi di HP.

## Logika program

Sudah tau Jekyll? Jadi, Jekyll adalah semacam platform blog berbasis file, seperti Hugo dan Gatsby JS. Nah, di Jekyll, kalau membuat postingan, kita harus membuat file yang letaknya di folder `_posts` dan contoh nama filenya itu `2020-01-28-ini-nama-filenya.md`. Terus, khusus di blogku, di dalam file postingannya, isinya itu diawali dengan (contoh):

```yaml
---
layout: post
title: "Membuat Judul Blog Jekyll Secara Otomatis dengan Python"
bahasa: python
date: 2020-01-28 16:41:55 +0800
---
```

Nah, berarti logikanya:

1. Cari dulu jam, menit, detik, tanggal, bulan, dan tahun saat ini
2. Tanya dulu mau nulis judulnya apa
3. Pakai bahasa pemrograman apa
4. Buat filenya di dalam `_posts`
5. Awali isi filenya dengan contoh di atas

## Source code

Berikut ini adalah source code aplikasinya yang letaknya di root Jekyll:

```python
import time, re

tahun = time.localtime().tm_year
bulan = time.localtime().tm_mon
tanggal = time.localtime().tm_mday
jam = time.localtime().tm_hour
menit = time.localtime().tm_min
detik = time.localtime().tm_sec

if bulan < 10:
    bulan = f"0{bulan}"

if tanggal < 10:
    tanggal = f"0{tanggal}"

if jam < 10:
    jam = f"0{jam}"

if menit < 10:
    menit = f"0{menit}"

if detik < 10:
    detik = f"0{detik}"

judul = input("""Apa judul postinganmu?
> """)
bahasa = input("""Bahasa pemrograman apa?
> """)
judul2 = re.sub("[^a-zA-Z0-9]", "-", judul.lower())
judul2 = re.sub("-+", "-", judul2)

nama_file = f"{tahun}-{bulan}-{tanggal}-{judul2}.md"
isi = f"""---
layout: post
title: "{judul}"
bahasa: {bahasa}
date: {tahun}-{bulan}-{tanggal} {jam}:{menit}:{detik} +0800
---

"""

file = open(f"_posts/{nama_file}", "w")
file.write(isi)
file.close

print("Selesai")
```

## Penjelasan source code

### Diawali dengan import

```python
import time, re
```

Pertama, kita import dulu modul time yang akan menunjukkan waktu. Dan re yang menunjukkan regular expression (regex).

Oh iya, aku ada contoh untuk pengolahan string terutama di penggunaan regular expression. Cuma untuk Javascript sih. Baca aja: <https://mzaini30.com/berbagai-pengolahan-string-pada-javascript-0116.html>.

### Mendapatkan elemen-elemen waktu

```python
tahun = time.localtime().tm_year
bulan = time.localtime().tm_mon
tanggal = time.localtime().tm_mday
jam = time.localtime().tm_hour
menit = time.localtime().tm_min
detik = time.localtime().tm_sec
```

Nah, kalau tadi kita memanggil modul time, maka di sinilah penggunaannya. Jadi kita mengambil tahun, bulan, tanggal, jam, menit, dan detik sekarang.

### Mengolah elemen-elemen waktu

```python
if bulan < 10:
    bulan = f"0{bulan}"

if tanggal < 10:
    tanggal = f"0{tanggal}"

if jam < 10:
    jam = f"0{jam}"

if menit < 10:
    menit = f"0{menit}"

if detik < 10:
    detik = f"0{detik}"
```

Kalau tadi kita mengambil waktu aja, sekarang kita olah tuh waktunya. Kalau waktu di bawah 10, maka kita tambahkan 0 di depannya.

Oh iya, kan itu aku pakai string literal. Coba deh perhatikan pada bagian:

```python
menit = f"0{menit}"
```

Kalau menggunakan teknik penggabungan string biasa, harusnya:

```python
menit = "0" + str(menit)
```

Lebih panjang kan?

Oh iya, kalau kamu mau baca string literal dalam Javascript, kamu bisa baca: <https://mzaini30.com/ada-yang-pernah-pakai-template-literal-0121.html>

### Mengambil inputan

```python
judul = input("""Apa judul postinganmu?
> """)
bahasa = input("""Bahasa pemrograman apa?
> """)
```

Jadi, kita mengambil nilai judul dan bahasa dari inputan.

Mengapa aku menggunakan kutip tiga kali?

Nah, kutip tiga kali itu untuk memuat string yang ada enternya.

### Menggunakan regex

```python
judul2 = re.sub("[^a-zA-Z0-9]", "-", judul.lower())
judul2 = re.sub("-+", "-", judul2)
```

Nah, judul itu misalnya `Aku mau makan`. Lalu, diolah dengan kode di atas, akan menciptakan variabel `judul2` yang isinya berubah menjadi `aku-mau-makan`.

Coba perhatikan pada bagian `[^a-zA-Z0-9]`. Iru artinya karakter apapun selain a-z, A-Z, dan 0-9, diubah menjadi strip. Kok bisa? Karena parameter `[^x]` di dalam regex artinya adalah mengambil semuanya kecuali yang ada di dalam kurung tersebut.

Lalu, di regex yang kedua (-+) artinya adalah:

```
-
--
---
----

dan seterusnya
```

Itu diubah menjadi satu strip aja.

### Menggunakan string literal lagi

```python
nama_file = f"{tahun}-{bulan}-{tanggal}-{judul2}.md"
isi = f"""---
layout: post
title: "{judul}"
bahasa: {bahasa}
date: {tahun}-{bulan}-{tanggal} {jam}:{menit}:{detik} +0800
---

"""
```

### Membuat file dan memasukkan isi ke dalam file

```python
file = open(f"_posts/{nama_file}", "w")
file.write(isi)
file.close
```

## Hasil (screenshot)

![](https://telegra.ph/file/9c83e3d24adf7a71bd7a3.png)

![](https://telegra.ph/file/564bdcc66a6afb29c0c48.png)

![](https://telegra.ph/file/9eb4f7dc1959bd900bb0a.png)