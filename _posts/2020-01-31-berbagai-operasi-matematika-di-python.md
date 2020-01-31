---
layout: post
title: "Berbagai Operasi Matematika di Python"
bahasa: python
date: 2020-01-31 05:40:12 +0800
---

## Operasi penjumlahan, pengurangan, perkalian, pembagian, pangkat, dan akar

```python
import os
os.system("clear")

satu = int(input("""Masukkan angka pertama
> """))
dua = int(input("""Masukkan angka kedua
> """))
print(f"""
{satu} + {dua} = {satu + dua}
{satu} - {dua} = {satu - dua}
{satu} x {dua} = {satu * dua}
{satu} / {dua} = {satu / dua}
{satu} pangkat {dua} = {satu ** dua}
{satu} akar {dua} = {satu ** (1/dua)}""")
```

```
Masukkan angka pertama                    
> 5                                       
Masukkan angka kedua
> 3

5 + 3 = 8
5 - 3 = 2
5 x 3 = 15
5 / 3 = 1.6666666666666667
5 pangkat 3 = 125
5 akar 3 = 1.709975946676697
```

## Menghitung faktorial

```python
import os
os.system("clear")

angka = int(input("""Masukkan angka
> """))

def faktorial(x):
    if x == 1:
        return 1
    else:
        return x * faktorial(x - 1)

print(f"""
{angka}! = {faktorial(angka)}""")
```

```
Masukkan angka                            
> 53                
                      
53! = 4274883284060025564298013753389399649690343788366813724672000000000000
```

## Operasi deretan angka

```python
import os, functools, statistics
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

print("Masukkan angka:")
angka = inputbanyak()
angka = angka.split("\n")
angka = list(map(lambda x: int(x), angka))

banyak = len(angka)
jumlah = functools.reduce(lambda a, b: a + b, angka)
ratarata = statistics.mean(angka)
median = statistics.median(angka)
if len(set(angka)) != len(angka):
    modus = statistics.mode(angka)
else:
    modus = "Nggak ada"
tertinggi = max(angka)
terendah = min(angka)

print(f"""
Banyak angka: {banyak}
Jumlah semua angka: {jumlah}
Rata-rata: {ratarata}
Median: {median}
Modus: {modus}
Nilai tertinggi: {tertinggi}
Nilai terendah: {terendah}""")
```

```
Masukkan angka:                           
1                                         
1
3
5
3
6
2
4
2
2
7
:wq

Banyak angka: 11
Jumlah semua angka: 36
Rata-rata: 3.272727272727273
Median: 3
Modus: 2
Nilai tertinggi: 7
Nilai terendah: 1
```
