# FormData

---

<p align="center">FormData</p>

---

构造器

```js
new (form?: HTMLFormElement): FormData
```

▎FormData.**append**

```ts
formData.append(
  name: USVString,
  value: USVString
): void

formData.append(
  name: USVString,
  blobValue: Blob,
  filename?: USVString
): void

// @参数 filename
// 当 Blob 或 File 作为第二个参数传递时，传给服务器的文件名称
// Blob 对象的默认文件名是 "blob"
// File 对象的默认文件名是文件的文件名

interface File
  extends Blob
```

▎FormData.**set**

```ts
formData.set(
  name: USVString,
  value: USVString
): void

formData.set(
  name: USVString,
  blobValue: Blob,
  filename?: USVString
): void
```

> `set` 和 `append` 的区别在于，若指定的 key 已存在，`set` 会使用新值覆盖已有的值，而 `append` 会把新值添加到已有值集合的后面。

▎FormData.**delete**

```ts
formData.delete(name: USVString): void
```

▎FormData.**get**

```ts
formData.get(
  name: USVString
): FormDataEntryValue | null

type FormDataEntryValue = File | USVString
```

▎FormData.**getAll**

```ts
formData.getAll(
  name: USVString
): sequence<FormDataEntryValue>
```

```js
var formData = new FormData()

formData.append('username', 'Chris')
formData.append('username', 'Bob')

formData.get('username') // 返回 "Chris"
formData.getAll('username') // 返回 ["Chris", "Bob"]
```

▎FormData.**has**

```ts
formData.has(name: USVString): boolean
```

```js
var formData = new FormData()

formData.has('username') // 返回 false
formData.append('username', 'Chris')
formData.has('username') // 返回 true
```

## 案例

FormData オブジェクトを送信する

```js
// 匿名関数を即時実行
;(function() {
  // FormData に対応していない
  if (!window.FormData) return

  // FormData オブジェクトを作成する
  var form_data = new FormData()

  // 名前と値を指定してデータを追加する
  form_data.append('aaa', 'value_a')
  form_data.append('bbb', 'value_b')
  form_data.append('ccc', 'value_c')

  // XMLHttpRequest オブジェクトを作成
  var xhr = new XMLHttpRequest()
  // 「POST メソッド」「接続先 URL」を指定
  xhr.open('POST', 'http://example.com/cgi-bin/upload.cgi')
  // 送信データに FormData を指定、XHR 通信を開始する
  xhr.send(form_data)
})()
```

フォームを指定して、FormData オブジェクトを作成する

```html
<form
  id="my_form"
  action="http://example.com/cgi-bin/upload.cgi"
  method="post"
  enctype="multipart/form-data"
>
  <textarea name="my_textarea"></textarea> <br />

  <input type="text" name="my_text" /> <br />
  <input type="hidden" name="my_hidden" /> <br />
  <input type="file" name="my_file" /> <br />

  <input type="submit" value="送信" />
</form>
```

```js
// 匿名関数を即時実行
;(function() {
  // FormData に対応していない
  if (!window.FormData) return

  // フォーム要素を取得する
  // id 属性が、"my_form" であるエレメントを取得
  var form = document.getElementById('my_form')

  // サブミット直前に実行されるイベント
  form.addEventListener('submit', function(e) {
    // デフォルトの動作をキャンセル（フォームの送信を中止）
    e.preventDefault()

    // FormData オブジェクトを作成する
    var form_data = new FormData(form)

    // XMLHttpRequest を使った通信
    // XMLHttpRequest オブジェクトを作成
    var xhr = new XMLHttpRequest()
    //「POST メソッド」「接続先 URL」を指定
    xhr.open('POST', form.action)
    // 送信データに FormData を指定、XHR 通信を開始する
    xhr.send(form_data)
  })
})()
```

## 参考

- [FormData - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/FormData)
- [Using FormData Objects | MDN](https://developer.mozilla.org/en-US/docs/Web/API/FormData/Using_FormData_Objects)
- [FormData クラスについて | JavaScript プログラミング講座](http://hakuhin.jp/js/form_data.html)
