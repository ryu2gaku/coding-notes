## ArrayBuffer 对象

**ArrayBuffer** 对象代表一个存储固定长度的二进制数据的缓存区。不能直接存取 **ArrayBuffer** 缓存区中的内容，只能通过视图（**TypedArray** 和 **DataView**）来存取。

**ArrayBuffer** 对象作为内存区域，可以存放多种类型的数据。同一段内存，不同数据有不同的解读方式，这就叫作“视图”。**ArrayBuffer** 有两种视图：一种是 **TypedArray** 视图，另一种是 **DataView** 视图。前者的数组成员都是同一个数据类型，后者的数组成员可以是不同的数据类型。

**ArrayBuffer**

```js
// 构造器
ArrayBuffer(number length);
// 单位为字节

// ArrayBuffer ⬇︎
// -----------
bool isView(ArrayBuffer arg);
// 参数是否为 ArrayBuffer 的视图实例

// ArrayBuffer.prototype ⬇︎
// ---------------------
number byteLength; //（只读）
// 返回所分配的内存区域的字节长度
ArrayBuffer slice(number begin, number? end);
// 将内存区域的一部分，拷贝生成一个新的 ArrayBuffer 对象
```

## TypedArray 视图

**TypedArray** 视图一共包括 9 种类型，每一种视图都是一种构造器

- `Int8Array`
- `Uint8Array`
- `Uint8ClampedArray`
- `Int16Array`
- `Uint16Array`
- `Int32Array`
- `Uint32Array`
- `Float32Array`
- `Float64Array`

**TypedArray** 数组只是一层视图，本身不储存数据，它的数据都储存在底层的 **ArrayBuffer** 对象之中，要获取底层对象必须使用 buffer 属性。

```js
new TypedArray(buffer [, byteOffset [, length]]);  😂

// 📌
// 创建一个 8 字节的 ArrayBuffer
var b = new ArrayBuffer(8);
// 创建一个指向 b 的 Int32 视图，开始于字节 0，直到缓冲区的末尾
var v1 = new Int32Array(b);
// 创建一个指向 b 的 Uint8 视图，开始于字节 2，直到缓冲区的末尾
var v2 = new Uint8Array(b, 2);
// 创建一个指向 b 的 Int16 视图，开始于字节 2，长度为 2
var v3 = new Int16Array(b, 2, 2);
// 上面代码在一段长度为 8 个字节的内存之上，
// 生成了三个视图：v1、v2 和 v3。
// 因此 v1、v2 和 v3 是重叠的，
// 只要任何一个视图对内存有所修改，就会在另外两个视图上反应出来

new TypedArray(length);
new TypedArray(typedArray);
new TypedArray(object);

// TypedArray.prototype ⬇︎
// --------------------
// 只读属性
ArrayBuffer buffer; // TypedArray 对象所引用的 ArrayBuffer 缓存区
number byteLength;
number byteOffset;
number length;
```

## DataView 视图

```js
new DataView(ArrayBuffer buffer, number? byteOffset, number? byteLength)

// DataView.prototype ⬇︎
// ------------------
ArrayBuffer buffer;
number byteLength;
number byteOffset;

// Read
number getInt8(number byteOffset);
number getUint8(number byteOffset);
number getInt16(number byteOffset, bool? littleEndian);
// littleEndian 用于判断该整数数值的字节序
// 为 true 时，表示以 little-endian 方式读取该整数数值（低地址存放最低有效字节）
// 为 false 或 undefined 时表示以 big-endian 方式读取该整数数值（低地址存放最高有效字节）
// ----------------------
// 以整数值 0x12345678 为例
// big-endian 方式存储数据
// 低地址 -----------------> 高地址
//        12  34  56  78
// little-endian 方式存储数据
// 低地址 ----------------> 高地址
//        78  56  34  12
number getUint16(number byteOffset, bool? littleEndian);
number getInt32(number byteOffset, bool? littleEndian);
number getUint32(number byteOffset, bool? littleEndian);
number getFloat32(number byteOffset, bool? littleEndian);
number getFloat64(number byteOffset, bool? littleEndian);
// Write
void setInt8(number byteOffset, number value);
void setUint8(number byteOffset, number value);
void setInt16(number byteOffset, number value, bool? littleEndian);
void setUint16(number byteOffset, number value, bool? littleEndian);
void setInt32(number byteOffset, number value, bool? littleEndian);
void setUint32(number byteOffset, number value, bool? littleEndian);
void setFloat32(number byteOffset, number value, bool? littleEndian);
void setFloat64(number byteOffset, number value, bool? littleEndian);
```

## 附录

- [ArrayBuffer - ECMAScript 6 入门](http://es6.ruanyifeng.com/#docs/arraybuffer)