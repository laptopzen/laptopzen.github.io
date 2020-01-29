---
layout: post
title: "Membuat Multi Input di Python"
bahasa: python
date: 2020-01-30 06:59:54 +0800
---

Salah satu yang menjadi kendala di Python adalah ketika kita memanggil perintah input, maka kita cuma bisa input satu baris. Nggak bisa banyak baris. Ya nggak masalah sih kalau datanya itu cuma nama, alamat, nomor HP. Tapi kalau misalnya mau copas data dari Excel ke Python, kan banyak baris tuh.

Biasanya kalau kita mau input di Python itu perintahnya:

```python
input("Masukkan namamu: ")
```

Itu kan cuma bisa input satu baris aja. Terus, gimana kalau mau input banyak baris?

Ini kodenya:

```python
def inputbanyak():
    lines = []
    while True:
        line = input()
        if line != ":wq":
            lines.append(line)
        else:
            break
    return "\n".join(lines)
```

## Penjelasan kode

Nah, kode di atas adalah fungsi `inputbanyak()`. Untuk memanggilnya, tentu kita harus memanggil fungsi tersebut.

Kemudian, dia membuat list lines yang isinya nggak ada. Lalu, menjalankan `while True` yang artinya loop secara terus-menerus. Nah, bagaimana cara menghentikannya? Nanti, di dalam `while True` itu ada `break` yang akan menghentikannya.

Di dalam loop tak terbatas itu, ada `input()` yang artinya, input biasa yang cuma satu baris itu. Namun, karena berada di dalam loop tak terbatas, maka dia ngulang-ngulang terus.

Nah, logika di dalam loop tak terbatas itu seperti ini:

- Terima input
- Kalau nggak ada `:wq`, hasil inputnya tadi dimasukkan ke list `lines`
- Begitu terus sampai ada teks `:wq`
- Kalau ada `:wq`, loop tak terbatas (milik Dr Strange) itu hancur berkeping-keping
- Lalu menggabungkan semua value list `lines` itu ke dalam sebuah string yang dipisahkan oleh baris baru
- Nah, string itu yang akan direturn

Kenapa pakai `:wq`? Ya, stylenya VIM sih. Tapi kalau mau diganti juga bisa. Misalnya dengan `selesai`.

## Penerapan kode

```python
def inputbanyak():
    lines = []
    while True:
        line = input()
        if line != ":wq":
            lines.append(line)
        else:
            break
    return "\n".join(lines)

print("Yang terlambat ke masjid:")
teks = inputbanyak()

print("")
print("Maka, yang terlambat ke masjid adalah:")
print(teks)
```

Dijalankan:

```
Yang terlambat ke masjid:                 
Hani                                      
Masykur
Wiryo
Rey
Ari
Zen
:wq

Maka, yang terlambat ke masjid adalah:
Hani
Masykur
Wiryo
Rey
Ari
Zen
```