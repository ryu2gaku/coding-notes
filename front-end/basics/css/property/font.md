# 字体

▎**font-style** - 字体样式

```css
/* 初始值 normal */
/* 继承 yes */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  font-style: normal;
  font-style: italic;
  font-style: oblique;
}
```

▎**font-variant** - 是否以小型的大写字母展示

```css
/* 初始值 normal */
/* 继承 yes */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  font-variant: normal;
  font-variant: small-caps;
}
```

▎**font-weight** - 字体粗细

```css
/* 初始值 normal */
/* 继承 yes */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* Keyword values */
  font-weight: normal; /* = 400 */
  font-weight: bold; /* = 700 */

  /* Keyword values relative to the parent */
  font-weight: lighter;
  font-weight: bolder;

  /* Numeric keyword values */
  font-weight: 100;
  font-weight: 200;
  font-weight: 300;
  font-weight: 400;
  font-weight: 500;
  font-weight: 600;
  font-weight: 700;
  font-weight: 800;
  font-weight: 900;
}
```

▎**font-size** - 字体大小

```css
/* 初始值 medium */
/* 继承 yes */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
/* 百分比 父元素的字体大小 */
.syntax {
  /* <absolute-size> values */
  font-size: xx-small;
  font-size: x-small;
  font-size: small;
  font-size: medium;
  font-size: large;
  font-size: x-large;
  font-size: xx-large;

  /* <relative-size> values */
  font-size: smaller;
  font-size: larger;

  /* <length> values */
  font-size: 12px;
  font-size: 0.8em;

  /* <percentage> values */
  font-size: 80%;
}
```

▎**line-height** - 行高

```css
/* 初始值 normal */
/* 继承 yes */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
/* 百分比 元素本身的字体大小 */
.syntax {
  /* Keyword value */
  line-height: normal;

  /* unitless values: use this number multiplied
by the element's font size */
  /* 当前元素字体大小的倍数，非负 */
  line-height: 3.5;
  /* <length> values */
  line-height: 3em;
  /* <percentage> values */
  line-height: 34%;
}
```

▎**font-family**

```css
/* 继承 yes */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* A font family name and a generic family name */
  font-family: 'Goudy Bookletter 1911', sans-serif;

  /* A generic family name only */
  font-family: serif;
  font-family: sans-serif;
  font-family: monospace;
  font-family: cursive;
  font-family: fantasy;
}
```

▎**font** - 简写属性

```css
p {
  font: normal small-caps normal 16px/1.4 Georgia;
}

/* 等价于 */
p {
  font-family: Georgia;
  line-height: 1.4;
  font-weight: normal;
  font-stretch: normal;
  font-variant: small-caps;
  font-size: 16px;
}
```

## 参考

- [CSS Fonts - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts)
