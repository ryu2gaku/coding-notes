# 颜色

▎**color** - 文本颜色

```css
/* 继承 yes */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* Keyword values */
  color: currentcolor;

  /* <named-color> values */
  color: red;
  color: orange;

  /* <hex-color> values */
  color: #090;
  color: #009900;

  /* <rgb()> values */
  color: rgb(34, 12, 64, 0.6);

  /* <hsl()> values */
  color: hsl(30, 100%, 50%, 0.6);
}
```

▎**opacity** - 不透明度

```css
/* 初始值 1.0 */
/* 继承 no */
/* 应用于 所有元素 */
.syntax {
  opacity: 1; /* 完全不透明 */
  opacity: 0; /* 完全透明 */

  opacity: 0.5;
  filter: alpha(opacity=50); /* IE8 及之前版本 */
}
```

## 参考

- [CSS Color - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Color)
