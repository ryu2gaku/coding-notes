# Transforms

▎**transform**

```css
/* 初始值 none */
/* 继承 no */
/* 适用于 transformable 元素 */
.syntax {
  /* Keyword values */
  transform: none;

  /* Function values */
  transform: matrix(1, 2, 3, 4, 5, 6);
  transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);

  transform: perspective(17px);

  transform: rotate(0.5turn);
  transform: rotate3d(1, 2, 3, 10deg);
  transform: rotateX(10deg);
  transform: rotateY(10deg);
  transform: rotateZ(10deg);

  transform: translate(12px, 50%);
  transform: translate3d(12px, 50%, 3em);
  transform: translateX(2em);
  transform: translateY(3in);
  transform: translateZ(2px);

  transform: scale(2, 0.5);
  transform: scale3d(2.5, 1.2, 0.3);
  transform: scaleX(2);
  transform: scaleY(0.5);
  transform: scaleZ(0.3);

  transform: skew(30deg, 20deg);
  transform: skewX(30deg);
  transform: skewY(1.07rad);

  /* Multiple function values */
  transform: translateX(10px) rotate(10deg) translateY(5px);
  transform: perspective(500px) translate(10px, 0, 20px) rotateY(3deg);
}
```

▎**transform-origin** - 变换的原点

例如 `rotate()` 函数的 `transform-origin` 是旋转的中心点

```css
/* 初始值 50% 50% 0 */
/* 继承 no */
/* 适用于 transformable 元素 */
.syntax {
  /* One-value syntax */
  transform-origin: 2px;
  transform-origin: bottom;

  /* x-offset | y-offset */
  transform-origin: 3cm 2px;
  /* x-offset-keyword | y-offset */
  transform-origin: left 2px;
  /* x-offset-keyword | y-offset-keyword */
  transform-origin: right top;
  /* y-offset-keyword | x-offset-keyword */
  transform-origin: top right;

  /* x-offset | y-offset | z-offset */
  transform-origin: 2px 30% 10px;
  /* x-offset-keyword | y-offset | z-offset */
  transform-origin: left 5px -3px;
  /* x-offset-keyword | y-offset-keyword | z-offset */
  transform-origin: right bottom 2cm;
  /* y-offset-keyword | x-offset-keyword | z-offset */
  transform-origin: bottom right 2cm;
}
```

## 变换函数

### 矩阵变换

▎**matrix**

```js
matrix(a, b, c, d, tx, ty)
```

▎**matrix3d**

```js
matrix3d(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3, a4, b4, c4, d4)
```

### 透视

▎**perspective**

```js
perspective(d)
```

### 平移

▎**translate**

```js
translate(tx, ty)

translate(2) = translate(2, 0)
```

▎**translate3d**

```js
translate3d(tx, ty, tz)
```

▎**translateX**

```js
translateX(tx) = translate(tx, 0) = translate3d(tx, 0, 0)
```

▎**translateY**

```js
translateY(ty) = translate(0, ty) = translate3d(0, ty, 0)
```

▎**translateZ**

```js
translateZ(tz) = translate3d(0, 0, tz)
```

### 旋转

▎**rotate**

```js
rotate(angle)
// deg  - 角度
// grad - 梯度
// rad  - 弧度
// turn - 圈、圆
// 90deg = 100grad = 0.25turn ≈ 1.5708rad
```

▎**rotate3d**

```js
rotate3d(x, y, z, a)
```

▎**otateX**

```js
rotateX(a) = rotate3d(1, 0, 0, a)
```

▎**rotateY**

```js
rotateY(a) = rotate3d(0, 1, 0, a)
```

▎**rotateZ**

```js
rotateZ(a) = rotate(a) = rotate3d(0, 0, 1, a)
```

### 缩放

▎**scale**

```js
scale(sx, sy)

scale(0.7) = scaleX(0.7) scaleY(0.7)
scale(2, 0.5) = scaleX(2) scaleY(0.5)
```

▎**scale3d**

```js
scale3d(sx, sy, sz)
```

▎**scaleX**

```js
scaleX(sx) = scale(sx, 1) = scale3d(sx, 1, 1)
```

▎**scaleY**

```js
scaleY(sy) = scale(1, sy) = scale3d(1, sy, 1)
```

▎**scaleZ**

```js
scaleZ(sz) = scale3d(1, 1, sz)
```

### 倾斜

▎**skew**

```js
skew(ax, ay)

skew(10deg) = skewX(10deg)
```

▎**skewX**

```js
skewX(angle)
```

▎**skewY**

```js
skewY(angle)
```

## 参考

- [CSS Transforms - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transforms)
