---
layout: post
title: "Membuat Program Undian (Arisan Juga) dengan Python"
bahasa: python
date: 2020-01-30 09:05:14 +0800
---

Logika dari program undian ini adalah kita memasukkan nama-nama yang akan diundi. Lalu, kita akan mendapatkan satu nama yang beruntung.

Jadi, program ini cocok banget deh buat segala macam undian seperti arisan, doorprize, dan lain sebagainya. Untungnya, koding di Python sangatlah mudah sehingga lahirlah skrip ini. 

## Kode

Berikut ini adalah kode Pythonnya:

```python
import os, random
os.system("clear")

def inputbanyak():
    lines = []
    while True:
        line = input()
        if line != ":wq":
            lines.append(line)
        else:
            break
    return "\n".join(lines)

print("Masukkan nama-nama yang akan diundi:")
nama = inputbanyak()
nama = nama.split("\n")
print(f"""
Nama yang beruntung adalah: {random.choice(nama)}""")
```

## Penjelasan program

Pertama, aku import dulu modul yang dibutuhkan lalu menghapus semua tulisan yang ada di layar.

Modul os itu adalah modul yang mengizinkan kita mengakses perintah-perintah di Terminal. Atau bisa dibilang penghubung antara Python dengan Bash. Lalu, random berisi dengan berbagai fungsi pengacakan, baik list, tuple, maupun string.

```python
import os, random
os.system("clear")
```

Kemudian aku buat fungsi inputbanyak() supaya bisa input lebih dari satu baris.

Kode inputbanyak() ini sudah aku posting di [tulisanku sebelumnya](membuat-multi-input-di-python-0130.html). Jadi di sini aku cuma kopi paste aja.

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

Kemudian kita minta nama-namanya lalu diundi dengan kode `random.choice(list)`.

Jadi, kode `random.choice(list)` itu cara kerjanya adalah dari berbagai value list yang ada, dia akan mengambil satu value aja secara acak.

```python
print("Masukkan nama-nama yang akan diundi:")
nama = inputbanyak()
nama = nama.split("\n")
print(f"""
Nama yang beruntung adalah: {random.choice(nama)}""")
```

## Hasil

```python
Masukkan nama-nama yang akan diundi:      
Rey                                       
Ani
Andi
Zen
Ari
Yani
Yoga
Yudha
:wq

Nama yang beruntung adalah: Zen
```