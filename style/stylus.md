# Stylus: Masa depan CSS

Kalau di CSS kan kita menggunakan sintaks seperti ini:

```css
.halo {
  background: blue;
  color: red;
}
```

Gimana kalau kita hilangkan `{`, `}`, `:`, dan `;`?

Jadinya seperti ini:

```stylus
.halo
  background blue
  color red
```

Keren kan? 

Jadi, itu namanya Stylus.

## Mencoba Stylus

```stylus
*
  word-wrap break-word
```

```css
* {
  word-wrap: break-word;
}
```

---

```stylus
.container
  width 80%
  margin auto
  
  p
    color blue
    background white
    
    a 
      color aqua
      background black
```

```css
.container {
  width: 80%;
  margin: auto;
}
.container p {
  color: #00f;
  background: #fff;
}
.container p a {
  color: #0ff;
  background: #000;
}
```

---

```stylus
a
  color blue
  
  &:hover
    color green
    
  &:active
    color red
    
  & p
    background magenta
```

```css
a {
  color: #00f;
}
a:hover {
  color: #008000;
}
a:active {
  color: #f00;
}
a p {
  background: #f0f;
}
```