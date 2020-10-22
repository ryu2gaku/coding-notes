# 事件委托

页面中的事件处理程序数量太多会导致占用大量内存，而且也会让用户感觉页面反应不够灵敏。建立在事件冒泡机制之上的事件委托技术，可以有效地减少事件处理程序的数量。

事件委托利用了事件冒泡，只指定一个事件处理程序，就可以管理某一类型的所有事件。

```html
<ul class="list">
  <li>List-1</li>
  <li>List-2</li>
  <li>List-3</li>
  <li>List-4</li>
  <li>List-5</li>
  <li>List-6</li>
</ul>
```

普通实现，需要给每个元素都添加一个事件处理程序。

```js
window.onload = function() {
  var oList = document.querySelector('.list')
  var aLi = oList.getElementsByTagName('li')

  for (var i = 0; i < aLi.length; i++) {
    aLi[i].onclick = function() {
      console.log(this.innerHTML)
    }
  }
}
```

如果在一个复杂的 Web 应用程序中，对所有可单击的元素都采用这种方式，那么结果就会有数不清的代码用于添加事件处理程序。

事件委托实现，只需在 DOM 树中尽量最高的层次添加一个事件处理程序。

```js
window.onload = function() {
  var oList = document.querySelector('.list')

  oList.onclick = function(event) {
    var event = event || window.event
    var target = event.target || event.srcElement

    if (target.nodeName.toLowerCase() == 'li') {
      console.log(target.innerHTML)
    }
  }
}
```

通过事件委托方式也会处理新增的子元素的该事件。
