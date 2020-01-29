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