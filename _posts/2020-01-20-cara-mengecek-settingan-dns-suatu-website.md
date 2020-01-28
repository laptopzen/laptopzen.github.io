---
layout: post
title: Cara Mengecek Settingan DNS Suatu Website
bahasa: bash
---

Ada loh cara cepat untuk mengecek apakah suatu website itu diblokir atau nggak yaitu dengan cara mengecek DNSnya. Kalau misalnya diblokir, biasanya ada tulisan `blocked` di DNSnya.

Misalnya aja seperti DNS di Netflix:

```
;netflix.com.                   IN      A
netflix.com.            5       IN      CNAME   mypage.blocked.bltsel.
mypage.blocked.bltsel.  3600    IN      A       114.121.254.4
```

Kelihatan kan kalau dari teks di atas bahwa Netflix diblokir sama Telkomsel.

Di tutorial ini aku menggunakan [Termux Path](udah-kenal-termux-path-tools-powerful-untuk-hacking-0119.html). Jadi, kalau ada yang belum paham dengan Termux Path, silahkan baca artikelnya dulu.

Dan tentunya juga pakai Termux.

Nah, command dari cara mengecek DNS adalah `dig situs.com +nocomments +nostat +nocmd`. Simpel kan? Tapi tentu saja panjang banget itu kalau kita ketik di Termux. Maunya kan singkat seperti `cek situs.com`.

Maka, kita buka Termux Path dan isi bagian `Perintah` dengan `cek` dan isi `Kode Program` dengan `dig $1 +nocomments +nostat +nocmd`.

Nah, sekarang, kita tinggal menjalankan `cek situs.com` aja di Termux.

# Nyoba-nyoba ngecek

_mzaini30.com_

```
;mzaini30.com.                  IN      A
mzaini30.com.           14440   IN      A       185.199.111.153
mzaini30.com.           14440   IN      A       185.199.108.153
mzaini30.com.           14440   IN      A       185.199.110.153
mzaini30.com.           14440   IN      A       185.199.109.153
```

_netflix.com_ (yang diblokir tadi)

```
;netflix.com.                   IN      A
netflix.com.            5       IN      CNAME   mypage.blocked.bltsel.
mypage.blocked.bltsel.  3600    IN      A       114.121.254.4
```

_www.ajenangelina.com_

```
;www.ajenangelina.com.          IN      A
www.ajenangelina.com.   300     IN      CNAME   ghs.google.com.
ghs.google.com.         269     IN      A       74.125.24.121
```

_www.tokopedia.com_

```
;www.tokopedia.com.             IN      A
www.tokopedia.com.      91      IN      CNAME   www.tokopedia.com.edgekey.net.
www.tokopedia.com.edgekey.net. 95 IN    CNAME   e10893.a.akamaiedge.net.
e10893.a.akamaiedge.net. 14     IN      A       104.93.222.106
```

_bukalapak.com_

```
;bukalapak.com.                 IN      A
bukalapak.com.          58      IN      A       103.117.82.33
bukalapak.com.          58      IN      A       103.117.82.28
bukalapak.com.          58      IN      A       103.117.83.35
bukalapak.com.          58      IN      A       103.117.82.37
bukalapak.com.          58      IN      A       103.117.82.24
bukalapak.com.          58      IN      A       103.117.83.26
bukalapak.com.          58      IN      A       103.117.83.30
bukalapak.com.          58      IN      A       103.117.83.39
```

_infoastronomy.org_

```
;infoastronomy.org.             IN      A
infoastronomy.org.      3600    IN      A       216.239.36.21
infoastronomy.org.      3600    IN      A       216.239.38.21
infoastronomy.org.      3600    IN      A       216.239.34.21
infoastronomy.org.      3600    IN      A       216.239.32.21
```

_japanesestation.com_

```
;japanesestation.com.           IN      A
japanesestation.com.    300     IN      A       104.24.114.116
japanesestation.com.    300     IN      A       104.24.115.116
```

_ngejulid.com_

```
;ngejulid.com.                  IN      A
ngejulid.com.           600     IN      A       172.105.125.184
```

_nurhidayatunnisa.com_

```
;nurhidayatunnisa.com.          IN      A
nurhidayatunnisa.com.   1200    IN      A       216.239.36.21
nurhidayatunnisa.com.   1200    IN      A       216.239.34.21
nurhidayatunnisa.com.   1200    IN      A       216.239.38.21
nurhidayatunnisa.com.   1200    IN      A       216.239.32.21
```

_www.nodiwa.com_

```
;www.nodiwa.com.                        IN      A
www.nodiwa.com.         14400   IN      CNAME   ghs.google.com.
ghs.google.com.         9       IN      A       74.125.24.121
```

_www.kompasiana.com_

```
;www.kompasiana.com.            IN      A
www.kompasiana.com.     209     IN      CNAME   dwspjfw4m84z1.cloudfront.net.
dwspjfw4m84z1.cloudfront.net. 10 IN     A       13.227.243.13
dwspjfw4m84z1.cloudfront.net. 10 IN     A       13.227.243.34
dwspjfw4m84z1.cloudfront.net. 10 IN     A       13.227.243.87
dwspjfw4m84z1.cloudfront.net. 10 IN     A       13.227.243.16
```

_codepolitan.com_

```
;codepolitan.com.               IN      A
codepolitan.com.        300     IN      A       104.27.182.231
codepolitan.com.        300     IN      A       104.27.183.231
```

_petanikode.com_

```
;petanikode.com.                        IN      A
petanikode.com.         300     IN      A       104.27.144.216
petanikode.com.         300     IN      A       104.27.145.216
```