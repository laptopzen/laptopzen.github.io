# Paper css tabs

## Problem

I was try to create tabs with your code in docs:

```pug
doctype html
html
  head
    title Paper CSS
    meta(charset='utf-8')
    meta(name='viewport' content='width=device-width, initial-scale=1, user-scalable=no')
    link(rel='stylesheet' href='https://cdn.jsdelivr.net/npm/papercss@1.6.1/dist/paper.min.css')
  body
    .container
      center
        h3 Tabs
      .row.flex-spaces.tabs
        input#tab1(type='radio' name='tabs' checked)
        label(for='tab1') tab 1
        input#tab2(type='radio' name='tabs')
        label(for='tab2') tab 2
        .content#content1 content 1
        .content#content2 content 2
```

But, the result is content in right of tabs; not in bottom of tabs.

![image](https://user-images.githubusercontent.com/7939342/76570199-c6977f00-64ef-11ea-8a11-9e803d4baafe.png)

![image](https://user-images.githubusercontent.com/7939342/76570200-c8f9d900-64ef-11ea-9ba6-7d7d4160b6fe.png)

## Solution

I create `break` class and I define it to break flex.

```pug
doctype html
html
  head
    title Paper CSS
    meta(charset='utf-8')
    meta(name='viewport' content='width=device-width, initial-scale=1, user-scalable=no')
    link(rel='stylesheet' href='https://cdn.jsdelivr.net/npm/papercss@1.6.1/dist/paper.min.css')

    style
      :stylus
        .break
          flex-basis 100%
          height 0

  body
    .container
      center
        h3 Tabs
      .row.flex-spaces.tabs
        input#tab1(type='radio' name='tabs' checked)
        label(for='tab1') tab 1
        input#tab2(type='radio' name='tabs')
        label(for='tab2') tab 2

        .break

        .content#content1 content 1
        .content#content2 content 2
```

![image](https://user-images.githubusercontent.com/7939342/76570389-3148ba80-64f0-11ea-92d0-dc0cd48ac8e8.png)

![image](https://user-images.githubusercontent.com/7939342/76570413-3a398c00-64f0-11ea-9c95-d451e1c20b5e.png)

> I will you include this solution in your docs/wiki.