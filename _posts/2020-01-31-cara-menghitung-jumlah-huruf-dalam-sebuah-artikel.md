---
layout: post
title: "Cara Menghitung Jumlah Huruf dalam Sebuah Artikel"
bahasa: python
date: 2020-01-31 14:03:59 +0800
---

Banyak hal yang bisa dilakukan oleh pemrograman. Salah satunya adalah dengan Python. Oh iya, tau nggak sih bahwa Python juga bisa loh untuk menghitung jumlah karakter (selain enter) pada suatu artikel?

## Kode

```python
import re

def inputbanyak():
  lines = []
  while True:
    line = input()
    if line != ':wq':
      lines.append(line)
    else:
      break
  return '\n'.join(lines)

print('''Masukkan artikel yang mau dihitung.
Lalu ketik :wq jika telah selesai.''')
artikel = inputbanyak()
artikel = re.sub('\n', '', artikel)

hitung = len(artikel)
print(f'''
Banyaknya huruf dalam artikel tersebut adalah: {hitung}''')
```

## Penjelasan

Pertama, kita import dulu modul regex (regular expression):

```python
import re
```

Kemudian, kita load dulu fungsi supaya kita bisa input banyak:

```python
def inputbanyak():
  lines = []
  while True:
    line = input()
    if line != ':wq':
      lines.append(line)
    else:
      break
  return '\n'.join(lines)
```

Lalu, kita masukkan teks sebagai instruksi:

```python
print('''Masukkan artikel yang mau dihitung.
Lalu ketik :wq jika telah selesai.''')
```

Terus kita tampilkan tuh form textarea (input banyak baris maksudnya, hehehehe):

```python
artikel = inputbanyak()
```

Lalu, kita hapus semua enter (pakai regex hapusnya):

```python
artikel = re.sub('\n', '', artikel)
```

Lalu, kita hitung jumlah artikelnya:

```python
hitung = len(artikel)
```

Terakhir, kita tampilkan hasilnya:

```python
print(f'''
Banyaknya huruf dalam artikel tersebut adalah: {hitung}''')
```

## Hasil

Sekarang kita coba deh. Jadi, aku ambil artikel [dari blogku](programming-blogging-dan-latihan-terus-menerus-tanpa-lelah-0130.html). Aku ambil paragraf pertamanya aja.

```
Masukkan artikel yang mau dihitung.
Lalu ketik :wq jika telah selesai.
Zaman sekarang bisa dikatakan adalah zamannya serba digital. Profesi yang unggul zaman sekarang juga otomatis segala hal yang berkaitan dengan digital. Bisa itu programmer maupun blogger. Nah, di sinilah bahwa kita melihat esensinya tetaplah sama walaupun masa telah berubah. Yaitu belajar terus-menerus.

Pernahkah kamu merasa lelah? Menyerah? Merasa tak mungkin? Lalu, bagaimana bisa kamu menjadi seorang programmer jika lelah sedikit saja kamu berhenti, jika letih sedikit saja kamu menyerah?

Eh, ini masih dalam niche teknologi kan? Belum masuk ranah psikologi kan? (Padahal aku mahasiswa psikologi). Apa perlu aku cuplik kode HTML biar tetap dalam niche programming? Hehehehe.
:wq

Banyaknya huruf dalam artikel tersebut adalah: 678
```

Ternyata, jumlah huruf dalam artikel tersebut adalah `678` huruf.