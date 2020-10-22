# Text 与 Comment

## API 文档

CharacterData 为抽象接口，这意味着没有任何 CharacterData 类型的对象。Text 和 Comment 都继承与该接口。

---

<p align="center">CharacterData ➠ Node</p>

---

▎ CharacterData.**data** - 每个继承 `CharacterData` 接口的节点有一个相关联的可变字符串 `data`

▎ CharacterData.**length** - _readonly_ - `data` 大小

▎ CharacterData.**appendData(data)** - 将 data 添加到节点的末尾

```ts
data.appendData(data: DOMString): void
```

▎ CharacterData.**insertData(offset, data)** - 在 offset 指定的位置插入 data

```ts
data.insertData(offset: unsigned long, data: DOMString): void
```

▎ CharacterData.**deleteData(offset, count)** - 从 offset 指定的位置开始删除 count 个字符

```ts
data.deleteData(offset: unsigned long, count: unsigned long): void
```

▎ CharacterData.**replaceData(offset, count, data)** - 用 data 替换从 offset 指定的位置开始到 offset+count 为止处的文本

```ts
data.replaceData(
  offset: unsigned long,
  count: unsigned long,
  data: DOMString
): void
```
