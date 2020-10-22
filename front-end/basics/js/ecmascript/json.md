# JSON

JSON【JavaScript Object Notation】是一种轻量级的数据交换格式。其 MIME 类型为 `application/json`，文件扩展名为 `.json`。

## 语法

- `string`
- `number`
- `true` `false`
- `null`
- `object`
- `array`

注意与 JavaScript 字符串不同，**JSON 字符串必须使用双引号**。

```js
{
  "name": "Nicholas",
  "age": 29,
  "school": {
    "name": "Nerrimack College",
    "location": "North Andover, NA"
  }
}
```

## 解析与序列化

✦ **JSON.parse** ✦ 解析 JSON 字符串为 JavaScript 值

```ts
JSON.parse(text, reviver?): any

// @参数
// @text: JSON 字符串
// @reviver: callback(key, value)

// @异常
// 若传入的字符串不符合 JSON 规范，则会抛出 SyntaxError 异常
```

```js
JSON.parse("{}");              // {}
JSON.parse("true");            // true
JSON.parse('"foo"');           // "foo"
JSON.parse('[1, 5, "false"]'); // [1, 5, "false"]
JSON.parse("null");            // null
```

❐ 使用 _reviver_ 参数 ❐

如果指定了函数 _reviver_，则解析出来的值在返回前会经过转换。具体来讲，解析出来的值及其所有属性会依次调用 _reviver_ 函数（顺序从最里层属性开始往外最终到解析出来的值）。

若 _reviver_ 函数返回 `undefined` 或没有返回值，则该属性会从当前对象中删除。其他情况，当前属性值会被返回值替代。

```js
JSON.parse('{"a": 5, "b": "5"}', (key, value) =>
  typeof value === "number" ? value * 2 : value
);
// {a: 10, b: "5"}

JSON.parse('{"1": 1, "2": 2, "3": {"4": 4, "5": {"6": 6}}}', (key, value) => {
  console.log(key);
  return value;
});
// 1
// 2
// 4
// 6
// 5
// 3
// ""
```

`JSON.parse` 不容许尾部有逗号。

```js
// 以下均抛出 SyntaxError
JSON.parse("[1, 2, 3, 4, ]");
JSON.parse('{"foo" : 1, }');
```

✦ **JSON.stringify** ✦ 将 JavaScript 值转化成 JSON 字符串

```ts
JSON.stringify(value, replacer?, space?): string

// @参数
// @value: 要转换的 JavaScript 值
// @replacer:
// 1) 若为函数 callback(key, value)
// 函数返回 undefined 时，JSON 字符串中不包含该属性
// 2) 若为数组 Array<string|number>
// 只有包含在该数组中的属性名才会被序列化到 JSON 字符串中
// @space: 字符串缩进，便于阅读
// 1) 若为 number
// 返回值在每个级别缩进指定数目的空格（最多10个空格）
// 2) 若为 string
// 返回值在每个级别中缩进字符串中的字符（最多前十个字符）
```

```js
JSON.stringify({});                  // '{}'
JSON.stringify(true);                // 'true'
JSON.stringify("foo");               // '"foo"'
JSON.stringify([1, "false", false]); // '[1,"false",false]'
JSON.stringify({ x: 5 });            // '{"x":5}'
```

不可枚举的属性默认会被忽略。

```js
JSON.stringify(
  Object.create(null, {
    x: { value: "x", enumerable: false },
    y: { value: "y", enumerable: true },
  })
);
// '{"y":"y"}'
```

❐ 使用 _replacer_ 参数 ❐

```js
var foo = {
  foundation: "Mozilla",
  model: "box",
  week: 45,
  transport: "car",
  month: 7,
};

// 1) replacer 为函数
function replacer(key, value) {
  if (typeof value === "string") {
    return undefined;
  }
  return value;
}
JSON.stringify(foo, replacer);
// '{"week":45,"month":7}'

// 2) replacer 为数组
JSON.stringify(foo, ["week", "transport"]);
// '{"week":45,"transport":"car"}'
```

❐ 使用 _space_ 参数 ❐

```js
// 1) 参数为数字
JSON.stringify({ a: 2 }, null, " ");
// '{
//  "a": 2
// }'

// 2) 参数为字符串
JSON.stringify({ uno: 1, dos: 2 }, null, "\t");
// '{
// 	"uno": 1,
// 	"dos": 2
// }'
```

## 案例

结合 `localStorage` 的使用实例。

有时候想存储用户创建的一个对象，并且在浏览器被关闭后仍能恢复该对象。

```js
var session = {
  screens: [],
  state: true,
};
session.screens.push({ name: "screenA", width: 450, height: 250 });
session.screens.push({ name: "screenB", width: 650, height: 350 });
session.screens.push({ name: "screenC", width: 750, height: 120 });
session.screens.push({ name: "screenD", width: 250, height: 60 });
session.screens.push({ name: "screenE", width: 390, height: 120 });
session.screens.push({ name: "screenF", width: 1240, height: 650 });

// 使用 JSON.stringify 转换为 JSON 字符串，并使用 localStorage 保存
localStorage.setItem("session", JSON.stringify(session));

var restoredSession = JSON.parse(localStorage.getItem("session"));
console.log(restoredSession);
```

## 参考

- [介绍 JSON](http://www.json.org/json-zh.html)
- [JSON - JavaScript | MDN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON)
