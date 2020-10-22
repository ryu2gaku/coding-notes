# 背景 Background

▎**background-image** - 在元素上设置一个或多个背景图像

```css
/* 初始值 none */
/* 继承 no */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  background-image: none;
  background-image: url('img.png');
  /* linear-gradient 线性渐变 */
  background-image: linear-gradient(
    to bottom,
    /* 渐变的方向 */ rgba(255, 255, 0, 0.5),
    /* 渐变的起止颜色 */ rgba(0, 0, 255, 0.5)
  );
}
```

第一个指定的图像绘制在最顶层，随后的每个图像绘制在前一个之后。

```css
.syntax {
  background-image: url('imgs.png'), url('img2.png');
}
```

▎**background-position** - 背景图像相对于背景定位区域（background positioning area）的初始位置

```css
/* 初始值 0% 0% */
/* 继承 no */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* Keyword values */
  /* 单值语法的第二个值为 center */
  background-position: top;
  background-position: bottom;
  background-position: left;
  background-position: right;
  background-position: center;

  /* <percentage> values */
  background-position: 25% 75%;

  /* <length> values */
  background-position: 0 0;
  background-position: 1cm 2cm;
  background-position: 10ch 8em;

  /* 边缘偏移值 */
  background-position: bottom 10px right 20px;
  background-position: right 3em bottom 10px;
  background-position: bottom 10px right;
  background-position: top right 10px;

  /* Multiple images */
  background-position: 0 0, center;
}
```

▎**background-size** - 元素背景图像的大小

```css
/* 初始值 auto auto */
/* 继承 no */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
/* 百分比 相对于背景定位区域（background positioning area）*/
.syntax {
  /* Keyword values */
  /* 按比例缩放背景图片以完全装入背景区 */
  background-size: cover;
  /* 按比例缩放背景图片以完全覆盖背景区 */
  background-size: contain;

  /* 单值语法 */
  /* 值为图像宽度，高度设为 auto */
  background-size: 50%;
  background-size: 3.2em;
  background-size: 12px;
  background-size: auto;

  /* 双值语法 */
  background-size: 50% auto;
  background-size: 3em 25%;
  background-size: auto 6px;
  background-size: auto auto;

  /* Multiple images */
  background-size: auto, auto;
  background-size: 50%, 25%, 25%;
  background-size: 6px, auto, contain;
}
```

▎**background-repeat** - 如何重复背景图像

```css
/* 初始值 repeat */
/* 继承 no */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* 单值语法 */
  background-repeat: repeat-x; /* = repeat no-repeat */
  background-repeat: repeat-y; /* = no-repeat repeat */
  background-repeat: repeat; /* = repeat repeat */
  background-repeat: space; /* = space space */
  /* 缩放以适应 */
  background-repeat: round; /* = round round */
  /* 两端均匀分布 */
  background-repeat: no-repeat; /* = no-repeat no-repeat */

  /* 双值语法 */
  /* horizontal | vertical */
  background-repeat: repeat space;
  background-repeat: repeat repeat;
  background-repeat: round space;
  background-repeat: no-repeat round;
}
```

▎**background-attachment** - 背景图像是否相对于视口固定，或者随着元素或其内容一起滚动

```css
/* 初始值 scroll */
/* 继承 no */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* Keyword values */
  /* 背景相对于元素本身固定，随元素一起滚动 */
  background-attachment: scroll;
  /* 背景相对于视口（viewport）固定 */
  background-attachment: fixed;
  /* 背景相对于元素的内容固定，随元素内容一起滚动 */
  background-attachment: local;
}
```

▎**background-origin** - 决定背景定位区域（background positioning area）

注意当 `background-attachment` 属性为 `fixed` 时忽略该属性

```css
/* 初始值 padding-box */
/* 继承 no */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* Keyword values */
  background-origin: border-box;
  background-origin: padding-box;
  background-origin: content-box;
}
```

▎**background-clip** - 决定背景绘制区域（background painting area），背景绘制在该区域内

```css
/* 初始值 border-box */
/* 继承 no */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* Keyword values */
  background-clip: border-box;
  background-clip: padding-box;
  background-clip: content-box;
}
```

▎**background-color** - 元素背景色

```css
/* 初始值 transparent */
/* 继承 no */
/* 适用于 所有元素，也适用于 ::first-letter 和 ::first-line */
.syntax {
  /* Keyword values */
  background-color: red;
  background-color: indigo;

  /* 十六进制值 */
  background-color: #bbff00; /* 完全不透明 */
  background-color: #bf0; /* 完全不透明 shorthand */
  background-color: #11ffee00; /* 完全透明 */
  background-color: #1fe0; /* 完全透明 shorthand  */
  background-color: #11ffeeff; /* 完全不透明 */
  background-color: #1fef; /* 完全不透明 shorthand  */

  /* RGB 值 */
  background-color: rgb(255, 255, 128); /* 不透明 */
  background-color: rgba(117, 190, 218, 0.5); /* 50% 透明 */

  /* HSL 值 */
  background-color: hsl(50, 33%, 25%); /* 不透明 */
  background-color: hsla(50, 33%, 25%, 0.75); /* 75% 透明 */

  /* Special keyword values */
  background-color: currentcolor;
  background-color: transparent;
}
```

▎**background** - 简写属性

```css
body {
  background:
     url(sweettexture.jpg)    /* image */
     top center / 200px 200px /* position / size */
     no-repeat                /* repeat */
     fixed                    /* attachment */
     padding-box              /* origin */
     content-box              /* clip */
     red;                     /* color */
}
```

## 参考

- [CSS Backgrounds and Borders - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Backgrounds_and_Borders)
