# Mudahnya membuat docs dengan Docsify

Bayangkan kamu membuat sebuah website semudah ini:

| Nama file | Hasil |
|-|-|
| README.md | situs.com |
| postingan/README.md | situs.com/postingan |
| makan.md | situs.com/makan |
| sepeda/wim-cycle.md | situs.com/sepeda/wim-cycle |

Jadi, kamu nggak perlu membuat desain tampilannya, desain database, algoritma, dan segala macam. Fokus aja di konten.

Mantap.

Itu pakai Docsify aku.

## Cara install

```bash
npm install -g docsify-cli
```

## Pemakaian pertama

Arahkan Terminalmu ke folder kosong yang mau kamu isi dengan Docsify. Lalu, di folder tersebut, jalankan:

```bash
docsify init
```

Maka, akan terbentuk:

- README.md 
- index.html
- .nojekyll

Nah, `.nojekyll` itu supaya file dan folder di situ nggak diolah dengan Jekyll (kalau di Github). `index.html` adalah kunci sistem ini. Jadi, jangan diubah-ubah kecuali kamu memang paham apa yang kamu ubah. `README.md` adalah halaman beranda website kita.

> Untuk selanjutnya, kita cuma bermain dengan file Markdown.

## Menjalankan server

Untuk menjalankan Docsify, sebenarnya sih kamu bisa menggunakan server apapun seperti standalone servernya PHP, Python, atau Ruby. Cuma, direkomendasikan menggunakan server dari Docsify. Kelebihannya adalah dia menggunakan liveserver. Sehingga, setiap ada perubahan pada document, kita nggak perlu reload. Dia akan reload otomatis.

Nah, kodenya yang perlu dijalankan di Terminal adalah:

```bash
docsify serve 
```

Maka, server akan dijalankan pada port 3000 (localhost:3000).