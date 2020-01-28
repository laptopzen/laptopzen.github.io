---
layout: post
title: Berkenalan dengan Python
bahasa: python
---

Jadi kisahnya aku nyoba install Python di HP. Pakai Termux tentunya. Dan kemudian aku dokumentasikan deh eksperimen dengan Python.

Cara installnya pun cukup mudah. Kamu hanya perlu mengetikkan `pkg install python` di Termux, maka dalam waktu beberapa menit saja, Termux sudah terinstall (tergantung kecepatan internet juga sih pastinya. Aku pakai Telkomsel).

Kemudian, untuk menggunakan Python di Termux, perintahnya adalah `python3 nama-file.py`.

Dan, inilah yang aku lakukan:

## Cobain input output sederhana

Untuk pemanasan, aku coba deh bermain input output sederhana.

Kode:

```python
nama = input("Siapa nama?\n")
print("Halo %s" % nama)
```

Atau bisa juga dengan:

```python
nama = input("Siapa nama?\n")
print(f"Halo {nama}")
```

Hasil:

```
Siapa nama?
Zen
Halo Zen
```

## Mengerjakan tugas hukuman nulis dari guru

Biasanya kan kalau anak SD nakal, dikasih tuh hukuman nulis satu kalimat yang _sangat memotivasi_ di papan tulis sebanyak beberapa kali. Andaikan aja hukumannya disuruh ngetik, mungkin kode ini bisa digunakan:

Kode:

```python
banyak = int(input("Disuruh guru nulis berapa kali?\n"))
for n in range(banyak):
    print("Aku janji nggak akan nakal lagi")
```

Hasil:

```
Disuruh guru nulis berapa kali?
5                                                     
Aku janji nggak akan nakal lagi
Aku janji nggak akan nakal lagi
Aku janji nggak akan nakal lagi
Aku janji nggak akan nakal lagi
Aku janji nggak akan nakal lagi
```

## Perpangkatan

Untuk perpangkatan, Python menggunakan sintaks `a ** b`. Berbeda dengan Javascript (yang versi lawas maksudku) harus menggunakan sintaks `Math.pow(a, b)`.

Kode:

```python
angka = int(input("Berapa angka yang ingin dipangkatkan?\n"))
pangkat = int(input("Dipangkatkan berapa?\n"))
hitung = angka ** pangkat

print("%s^%s = %s" % (angka, pangkat, hitung))
```

Hasil:

```
Berapa angka yang ingin dipangkatkan?
2
Dipangkatkan berapa?
3
2^3 = 8
```

Oke, itu aja sih nyoba-nyobanya. Semoga menghibur (hehehehe). Kalau ada yang nggak paham, komen di bawah ya.