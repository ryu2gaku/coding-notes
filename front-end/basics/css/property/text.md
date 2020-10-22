# 文本

▎**letter-spacing** - 文本字符之间的间距

```css
/* 初始值 normal */
/* 继承 yes */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* Keyword value */
  letter-spacing: normal;

  /* <length> values */
  letter-spacing: 0.3em;
  letter-spacing: 3px;
  letter-spacing: 0.3px;
}
```

▎**text-align** - 文本对齐方式

```css
/* 继承 yes */
/* 应用于 块容器 */
.syntax {
  /* Keyword values */
  text-align: left;
  text-align: right;
  text-align: center;
  /* 两侧对齐 */
  text-align: justify;
}
```

▎**text-indent** - 首行缩进

```css
/* 初始值 0 */
/* 继承 yes */
/* 应用于 块容器 */
/* 百分比 容器块的宽度 */
.syntax {
  /* <length> values */
  text-indent: 3mm;
  text-indent: 40px;

  /* <percentage> value
   relative to the containing block width */
  text-indent: 15%;
}
```

▎**text-shadow** - 给文字添加阴影效果

```css
/* 初始值 none */
/* 继承 yes */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* offset-x | offset-y | blur-radius | color */
  text-shadow: 1px 1px 2px black;
  /* color | offset-x | offset-y | blur-radius */
  text-shadow: #fc0 1px 0 10px;
  /* offset-x | offset-y | color */
  text-shadow: 5px 5px #558abb;
  /* color | offset-x | offset-y */
  text-shadow: white 2px 5px;
  /* offset-x | offset-y */
  /* Use defaults for color and blur-radius */
  text-shadow: 5px 10px;
}
/*
阴影离开文字的横方向距离，可指定负值
阴影离开文字的纵方向距离，可指定负值
阴影的模糊半径，代表阴影向外模糊时的模糊范围
阴影的颜色

指定多个阴影时使用逗号将多个阴影进行分隔
*/
```

▎**text-transform**

```css
/* 初始值 none */
/* 继承 yes */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* Keyword values */
  text-transform: none;
  /* 单词首字母大写 */
  text-transform: capitalize;
  /* 所有字母大写 */
  text-transform: uppercase;
  /* 所有字母小写 */
  text-transform: lowercase;
}
```

▎**white-space** - 元素中的空白处理方式

```css
/* 初始值 normal */
/* 继承 yes */
/* 适用于 所有元素 */
.syntax {
  /* Keyword values */
  /* 换行符、空格和制表符合并，文本会自动换行 */
  white-space: normal;
  /* 换行符、空格和制表符合并，文本不会自动换行 */
  white-space: nowrap;
  /* 换行符、空格和制表符保留，文本不会自动换行 */
  white-space: pre;
  /* 换行符、空格和制表符保留，文本会自动换行 */
  white-space: pre-wrap;
  /* 换行符保留，空格和制表符合并，文本会自动换行 */
  white-space: pre-line;
}
```

▎**word-spacing** - 单词间距

```css
/* 初始值 normal */
/* 继承 yes */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* Keyword value */
  word-spacing: normal;

  /* <length> values */
  word-spacing: 3px;
  word-spacing: 0.3em;

  /* <percentage> values */
  word-spacing: 50%;
  word-spacing: 200%;
}
```

▎**overflow-wrap**

```css
/* 初始值 normal */
/* 继承 yes */
/* 适用于 不可替换的内联元素 */
.syntax {
  /* Keyword values */
  overflow-wrap: normal;
  /* 单词过长时，单词内部可分割换行 */
  overflow-wrap: break-word;
}
```

`word-wrap` 是该属性的别名

▎**word-break**

```css
/* 初始值 normal */
/* 继承 yes */
/* 适用于 所有元素 */
.syntax {
  /* Keyword values */
  word-break: normal;
  word-break: break-all;
  /* 除了中日韩文不换行外，与 normal 表现相同 */
  word-break: keep-all;
}
```

## 文本装饰

▎**text-decoration-line**

```css
/* 初始值 none */
/* 继承 no */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* Single keyword */
  text-decoration-line: none;
  text-decoration-line: underline;
  text-decoration-line: overline;
  text-decoration-line: line-through;

  /* Multiple keywords */
  text-decoration-line: underline overline;
  text-decoration-line: overline underline line-through;
}
```

▎**text-decoration-style**

```css
/* 初始值 solid */
/* 继承 no */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* Keyword values */
  text-decoration-style: solid;
  text-decoration-style: double;
  text-decoration-style: dotted;
  text-decoration-style: dashed;
  text-decoration-style: wavy;
}
```

▎**text-decoration-color**

```css
/* 初始值 currentcolor */
/* 继承 no */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* <color> values */
  text-decoration-color: currentColor;
  text-decoration-color: red;
  text-decoration-color: #00ff00;
  text-decoration-color: rgba(255, 128, 128, 0.5);
  text-decoration-color: transparent;
}
```

▎**text-decoration** - `text-decoration-*` 的简写属性

```css
.syntax {
  text-decoration: underline overline #ff3028;
}
```

## 参考

- [CSS Text Decoration - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Text_Decoration)
- [CSS Text - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Text)
