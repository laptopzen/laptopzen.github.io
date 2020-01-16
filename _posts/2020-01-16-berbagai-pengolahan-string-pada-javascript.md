---
layout: post
title: Berbagai Pengolahan String pada Javascript
bahasa: javascript
---

**Mengubah semua huruf vokal menjadi i**

```javascript
teks = "Kamu ngomong apa sih?"
console.log(teks.replace(/[aueo]/gi, "i"))
```

Hasil:

```
Kimi ngiming ipi sih?
```