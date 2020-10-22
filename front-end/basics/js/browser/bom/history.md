# History

History 保存着用户上网的历史记录，从窗口被打开的那一刻算起。

出于安全方面的考虑，开发人员无法得知用户浏览过的 URL。不过，借由用户访问过的页面列表，同样可以在不知道实际 URL 的情况下实现后退和前进。

## API 文档

---

<p align="center">History</p>

---

▎History.**length** - _readonly_ - 历史列表中的 URL 数（包括当前加载的页面）

▎History.**go** - 加载 history 列表中的第前或第后 delta 个 URL

```ts
history.go(delta: long = 0): void
```

▎History.**back** - 加载 history 列表中的前一个 URL

```ts
history.back(): void
```

▎History.**forward** - 加载 history 列表中的下一个 URL

```ts
history.forward(): void
```

## 参考

- [History - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/History)
