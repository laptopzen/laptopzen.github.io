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

## Pemakaian

Arahkan Terminalmu ke folder kosong yang mau kamu isi dengan Docsify. Lalu, di folder tersebut, jalankan:

```bash
docsify init
```

Maka, akan terbentuk:

- README.md 
- index.html
- .nojekyll

Nah, `.nojekyll` itu supaya file dan folder di situ nggak diolah dengan Jekyll (kalau di Github). `index.html` adalah kunci sistem ini. Jadi, jangan diubah-ubah. `README.md` adalah halaman beranda website kita.