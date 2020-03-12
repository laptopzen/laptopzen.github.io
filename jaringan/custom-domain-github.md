# Menghubungkan github pages dengan custom domain

## Di Github 

Buat file dengan nama `CNAME` di root yang isinya:

```
situs.com 
```

## Di provider domain

Atur DNS

| host name | type | value |
|-|-|-|
| @ | A | 185.199.108.153 |
| @ | A | 185.199.109.153 |
| @ | A | 185.199.110.153 |
| @ | A | 185.199.111.153 |
| www | CNAME | situs.github.io |