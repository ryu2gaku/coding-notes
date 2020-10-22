# 动画 Animation

▎<b>@keyframes</b>

```css
@keyframes slidein {
  /* 等价于 0% */
  from {
    transform: translateX(0%);
  }
  /* 等价于 100% */
  to {
    transform: translateX(100%);
  }
}

@keyframes identifier {
  0% {
    top: 0;
    left: 0;
  }
  30% {
    top: 50px;
  }
  68%,
  72% {
    left: 50px;
  }
  100% {
    top: 100px;
    left: 100%;
  }
}
```

▎**animation-name**

```css
/* 初始值 none */
/* 继承 no */
/* 适用于 所有元素，::before 和 ::after 伪元素 */
.syntax {
  /* Single animation */
  animation-name: none;
  animation-name: test_05;
  animation-name: -specific;
  animation-name: sliding-vertically;

  /* Multiple animations */
  animation-name: test1, animation4;
  animation-name: none, -moz-specific, sliding;
}
```

▎**animation-duration**

```css
/* 初始值 0s */
/* 继承 no */
/* 适用于 所有元素，::before 和 ::after 伪元素 */
.syntax {
  /* Single animation */
  animation-duration: 6s;
  animation-duration: 120ms;

  /* Multiple animations */
  animation-duration: 1.64s, 15.22s;
  animation-duration: 10s, 35s, 230ms;
}
```

▎**animation-timing-function**

```css
/* 初始值 ease */
/* 继承 no */
/* 适用于 所有元素，::before 和 ::after 伪元素 */
.syntax {
  /* Keyword values */
  animation-timing-function: ease;
  animation-timing-function: ease-in;
  animation-timing-function: ease-out;
  animation-timing-function: ease-in-out;
  animation-timing-function: linear;
  animation-timing-function: step-start;
  animation-timing-function: step-end;

  /* Function values */
  animation-timing-function: cubic-bezier(0.1, 0.7, 1, 0.1);
  animation-timing-function: steps(4, end);

  /* Multiple animations */
  animation-timing-function: ease, step-start, cubic-bezier(0.1, 0.7, 1, 0.1);
}
```

▎**animation-delay**

```css
/* 初始值 0s */
/* 继承 no */
/* 适用于 所有元素，::before 和 ::after 伪元素 */
.syntax {
  /* Single animation */
  animation-delay: 3s;
  animation-delay: 0s;
  animation-delay: -1500ms;

  /* Multiple animations */
  animation-delay: 2.1s, 480ms;
}
```

▎**animation-iteration-count** - 动画循环次数

```css
/* 初始值 1 */
/* 继承 no */
/* 适用于 所有元素，::before 和 ::after 伪元素 */
.syntax {
  /* Keyword value */
  /* 无限循环 */
  animation-iteration-count: infinite;

  /* <number> values */
  animation-iteration-count: 3;
  animation-iteration-count: 2.4;

  /* Multiple values */
  animation-iteration-count: 2, 0, infinite;
}
```

▎**animation-direction**

```css
/* 初始值 normal */
/* 继承 no */
/* 适用于 所有元素，::before 和 ::after 伪元素 */
.syntax {
  /* Single animation */
  /* 正方向 */
  animation-direction: normal;
  /* 反方向 */
  animation-direction: reverse;
  /* 正方向反方向交替 */
  animation-direction: alternate;
  /* 反方向正方向交替 */
  animation-direction: alternate-reverse;

  /* Multiple animations */
  animation-direction: normal, reverse;
  animation-direction: alternate, reverse, normal;
}
```

▎**animation-fill-mode** - 动画执行前后的状态

```css
/* 初始值 none */
/* 继承 no */
/* 适用于 所有元素，::before 和 ::after 伪元素 */
.syntax {
  /* Single animation */
  animation-fill-mode: none;
  /* 动画完成后，保持最后一个关键帧状态 */
  animation-fill-mode: forwards;
  /* 在动画延迟期间，应用动画第一个关键帧状态 */
  animation-fill-mode: backwards;
  animation-fill-mode: both;

  /* Multiple animations */
  animation-fill-mode: none, backwards;
  animation-fill-mode: both, forwards, none;
}
```

▎**animation-play-state** - 动画是否正在运行（running）或暂停（paused）

```css
/* 初始值 running */
/* 继承 no */
/* 适用于 所有元素，::before 和 ::after 伪元素 */
.syntax {
  /* Single animation */
  animation-play-state: running;
  animation-play-state: paused;

  /* Multiple animations */
  animation-play-state: paused, running, running;
}
```

▎**animation**

```css
.syntax {
  /* duration | timing-function | delay | 
iteration-count | direction | fill-mode | play-state | name */
  animation: 3s ease-in 1s 2 reverse both paused slidein;
  /* duration | timing-function | delay | name */
  animation: 3s linear 1s slidein;
  /* duration | name */
  animation: 3s slidein;
}
```

```html
<p>
  The Caterpillar and Alice looked at each other for some time in silence: at
  last the Caterpillar took the hookah out of its mouth, and addressed her in a
  languid, sleepy voice.
</p>
```

```css
p {
  animation-name: slidein;
  animation-duration: 3s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
@keyframes slidein {
  from {
    margin-left: 100%;
    width: 300%;
  }
  to {
    margin-left: 0%;
    width: 100%;
  }
}
```

## 参考

- [CSS Animations - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations)
