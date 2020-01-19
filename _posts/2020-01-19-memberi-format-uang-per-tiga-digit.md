---
layout: post
title: Memberi Format Uang per Tiga Digit dari Belakang
bahasa: javascript
---

Misalnya aja ada uang sejumlah `1000`.

Masih gampang sih bacanya.

Lalu, ada lagi uang sejumlah `1000000`.

Masih gampang bacanya walaupun nolnya sudah mulai banyak.

Lalu bagaimana dengan `12984102319`? Bagaimana cara bacanya?

Nah, makanya kita perlu memberi angka titik per tiga digit seperti yang dulu pernah diajarkan pas SD (pas kelas 4 kalau nggak salah). Tapi kan kalau misalnya datanya ada banyak, capek dong kalau kita kasih tanda satu per satu? Nah, aku pun membuat skripnya supaya memudahkan:

```javascript
angka = 12984102319
console.log(angka.toLocaleString('id'))
```

Maka akan menghasilkan `12.984.102.319`. Cara membacanya? Gampang kan? Dua belas miliar sembilan ratus delapan puluh empat juta seratus dua ribu tiga ratus sembilan belas.

Banyak banget nominalnya eh. Semoga aku bisa mendapatkan sebanyak itu hari ini. Hehehehe.

Oh iya, untuk `id` dalam kode di atas, berarti penulisan uang dalam format Indonesia (namanya language tag). Kita bisa menggantinya dengan format negara lain. Berikut ini adalah language tag dari berbagai macam negara (kukutip dari <https://www.techonthenet.com/js/language_tags.php>):

| Language Tag | Language | Region |
|---|---|---|
| ar-SA | Arabic | Saudi Arabia |
| bn-BD | Bangla | Bangladesh |
| bn-IN | Bangla | India |
| cs-CZ | Czech | Czech Republic |
| da-DK | Danish | Denmark |
| de-AT | German | Austria |
| de-CH | German | Switzerland |
| de-DE | German | Germany |
| el-GR | Greek | Greece |
| en-AU | English | Australia |
| en-CA | English | Canada |
| en-GB | English | United Kingdom |
| en-IE | English | Ireland |
| en-IN | English | India |
| en-NZ | English | New Zealand |
| en-US | English | United States |
| en-ZA | English | South Africa |
| es-AR | Spanish | Argentina |
| es-CL | Spanish | Chile |
| es-CO | Spanish | Columbia |
| es-ES | Spanish | Spain |
| es-MX | Spanish | Mexico |
| es-US | Spanish | United States |
| fi-FI | Finnish | Finland |
| fr-BE | French | Belgium |
| fr-CA | French | Canada |
| fr-CH | French | Switzerland |
| fr-FR | French | France |
| he-IL | Hebrew | Israel |
| hi-IN | Hindi | India |
| hu-HU | Hungarian | Hungary |
| id-ID | Indonesian | Indonesia |
| it-CH | Italian | Switzerland |
| it-IT | Italian | Italy |
| jp-JP | Japanese | Japan |
| ko-KR | Korean | Republic of Korea |
| nl-BE | Dutch | Belgium |
| nl-NL | Dutch | The Netherlands |
| no-NO | Norwegian | Norway |
| pl-PL | Polish | Poland |
| pt-BR | Portugese | Brazil |
| pt-PT | Portugese | Portugal |
| ro-RO | Romanian | Romania |
| ru-RU | Russian | Russian Federation |
| sk-SK | Slovak | Slovakia |
| sv-SE | Swedish | Sweden |
| ta-IN | Tamil | India |
| ta-LK | Tamil | Sri Lanka |
| th-TH | Thai | Thailand |
| tr-TR | Turkish | Turkey |
| zh-CN | Chinese | China |
| zh-HK | Chinese | Hond Kong |
| zh-TW | Chinese | Taiwan |
{:.table.table-bordered}

Jadi misalnya kita mau coba nih pakai formatnya Korea, tinggal kita ubah aja kodenya jadi:

```javascript
angka = 12984102319
console.log(angka.toLocaleString('ko'))
```

Maka hasilnya adalah `12,984,102,319`.

Terus kita mau coba format Jepang:

```javascript
angka = 12984102319
console.log(angka.toLocaleString('jp'))
```

Jadinya `12,984,102,319`.

Kita mau coba format Rusia:

```javascript
angka = 12984102319
console.log(angka.toLocaleString('ru'))
```

Hasilnya `12 984 102 319` (oke, mulai beda saudara).

Coba lagi ah formatnya Arab:

```javascript
angka = 12984102319
console.log(angka.toLocaleString('ar'))
```

Hasilnya `١٢٬٩٨٤٬١٠٢٬٣١٩` (ini sih sudah beda huruf hehehehe).

Coba lagi formatnya Italia:

```javascript
angka = 12984102319
console.log(angka.toLocaleString('it'))
```

Jadinya `12.984.102.319` (mirip sama Indonesia ternyata).

Oke, itu aja sekilas tentang memberi format uang per tiga digit dari belakang. Kalau ada yang masih bingung dan ingin bertanya, silahkan komentar di bawah postingan ini.

So, keep ngoprek gaes.