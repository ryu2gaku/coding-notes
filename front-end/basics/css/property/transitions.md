# 过渡 Transition

▎**transition-property** - 当指定的 CSS 属性改变时，过渡效果开始

```css
/* 初始值 all */
/* 继承 no */
/* 适用于 所有元素，::before 和 ::after 伪元素 */
.syntax {
  /* Keyword values */
  /* 没有属性会获得过渡效果 */
  transition-property: none;
  /* 所有属性都将获得过渡效果 */
  transition-property: all;

  /* 定义应用过渡效果的 CSS 属性名称列表，列表以逗号分隔 */
  transition-property: margin-right, color;
}
```

▎**transition-duration**

```css
/* 初始值 0s */
/* 继承 no */
/* 适用于 所有元素，::before 和 ::after 伪元素 */
.syntax {
  /* <time> values */
  transition-duration: 6s;
  transition-duration: 120ms;
  transition-duration: 1s, 15s;
  transition-duration: 10s, 30s, 230ms;
}
```

▎**transition-timing-function**

```css
/* 初始值 ease */
/* 继承 no */
/* 适用于 所有元素，::before 和 ::after 伪元素 */
.syntax {
  /* Keyword values */
  transition-timing-function: ease;
  transition-timing-function: ease-in;
  transition-timing-function: ease-out;
  transition-timing-function: ease-in-out;
  transition-timing-function: linear;
  transition-timing-function: step-start;
  transition-timing-function: step-end;

  /* Function values */
  transition-timing-function: steps(4, jump-end);
  transition-timing-function: cubic-bezier(0.1, 0.7, 1, 0.1);

  /* Multiple timing functions */
  transition-timing-function: ease, step-start, cubic-bezier(0.1, 0.7, 1, 0.1);
}
```

▎**transition-delay**

```css
/* 初始值 0s */
/* 继承 no */
/* 适用于 所有元素，::before 和 ::after 伪元素 */
.syntax {
  /* <time> values */
  transition-delay: 3s;
  transition-delay: 2s, 4ms;
}
```

▎**transition** - `transition-*` 的简写方法

```css
.syntax {
  /* Apply to 1 property */
  /* property name | duration */
  transition: margin-right 4s;
  /* property name | duration | delay */
  transition: margin-right 4s 1s;
  /* property name | duration | timing function */
  transition: margin-right 4s ease-in-out;
  /* property name | duration | timing function | delay */
  transition: margin-right 4s ease-in-out 1s;

  /* Apply to 2 properties */
  transition: margin-right 4s, color 1s;

  /* Apply to all changed properties */
  transition: all 0.5s ease-out;
}
```

```css
#delay {
  font-size: 14px;
  transition-property: font-size;
  transition-duration: 4s;
  transition-delay: 2s;
}
#delay:hover {
  font-size: 36px;
}
```

## 参考

- [CSS Transitions - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions)
- [Using CSS transitions - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)
