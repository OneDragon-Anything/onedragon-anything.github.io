---
lang: zh-CN
title: 基础-00-Yaml格式
---

本文只会介绍自动战斗中可能用到的内容，其他可以看[完整教程](https://www.runoob.com/w3cnote/yaml-intro.html)

如果中途有疑问，可以找 [通义千问](https://tongyi.aliyun.com/qianwen/)

## 1.对象

通常，我们把多个属性的合集，称为一个对象。

我们先来看一个简单的yml文件

```yaml
name: "DoctorReid"
github_homepage: "https://github.com/DoctorReid"
level: 60
```

这里面表示了一个人物的对象，名称(name)是DoctorReid，主页(github_homepage)是后面的地址。

也就是，我们通过 `属性: 值` 的方式取描述一个对象，一个对象中可以包含任意个属性，属性之间没有要求顺序。

### 1.1.值类型

通常，我们只需要关注两种类型

- 文本(字符串) - 就是上述用双引号中包含的内容，`"DoctorReid"` 表示这是一个字符串，值是 `DoctorReid`。
- 数值 - 你可以先简单认为，没有双引号包含的，只有数字的内容，就是数值，例如上述的 `60`。

## 2.数组

那如果有多个人物，又要怎么表示呢，我们看下面的例子

```yaml
- name: "DoctorReid"
  github_homepage: "https://github.com/DoctorReid"
  level: 60
- name: "小巡夜"
  github_homepage: "https://github.com/yokuminto"
  level: 60
```

你可以使用 [本网站](https://yaml.cn/)，把上面的内容复制进入，看右方显示，可以更清晰地看到有2块内容。

这说明，我们当前有2个人物，他们分别都有3个属性。

### 2.1.数组元素表示方式

通过上述例子可以看到，我们是使用 横线+1个空格 `- ` 来表示数组里每个对象的开始的。

对象的第一个属性，前方会有 横线+1个空格 `- `；后续属性，前方会有 2个空格 `  `。

这样排列后，同一个对象中的所有属性，它的起始字母，在每行的位置是一样的。

这个也叫做 缩进对齐，也就是依赖 `空格符号` 来对齐属性的位置，来表示这几个属性是属于同一个对象的。

这时候再回去看 `1.对象` 的例子，它刚好是属性都从每行最左边开始，缩进是相同的，所以是在描述同一个对象里的属性。

## 3.复杂的对象属性

我们继续拓展上述例子，一个对象的属性，可以是一个数组，也可以是另一个嵌套的对象。

以下例子你都可以复制到 [这里](https://yaml.cn/) 观察。

```yaml
org_name: "一条龙"
members:
  - name: "DoctorReid"
    github_homepage: "https://github.com/DoctorReid"
    level: 60
  - name: "小巡夜"
    github_homepage: "https://github.com/yokuminto"
    level: 60
keywords: [ "脚本", "自动化" ]
other_info:
  homepage: "https://one-dragon.com/"
  create_date: "2024-09-01"
```

现在我们描述的是一个对象，可以理解成一个组织，里面有以下的属性：

- 组织名称(org_name) : 它的值是一个字符串，等于 `一条龙`
- 组织成员(members) : 它的值是一个数组，数组里是多个成员对象，每个成员对象包含多个属性
- 关键词(keywords) : 它的值是一个数组，数组里是多个字符串
- 其它信息(other_info) : 它的值是一个对象，里面再包含多个属性: 主页(homepage)，创建时间(create_date)

### 3.1.缩进对齐

观察上述例子，缩进(每行前的空格)会在以下情况下出现

- 属性的值是一个数组或者是另一个对象，我们会先加入 2个空格 `  `，再开始描述这个数组或者另一个对象
- 描述一个数组时，数组中的每一个元素，第一个属性，我们会加入 横线+1个空格 `- `，其它属性，我们会加入 2个空格 `  `


### 3.2.数组的另一种表示方式

```yaml
keywords: [ "脚本", "自动化" ]
```

我们可以看到 keywords 这行，当我们的数组里的元素，都是字符串或者数值时，我们可用 `中括号` 来包围这些值，来表示一个数组。

当然，你也可以使用原来的结构来表示

```yaml
keywords:
  - "脚本"
  - "自动化"
```

## 4.复杂嵌套

一个属性的值，可以是一个对象2；对象2里的属性，依然可以是另一个对象3，这就可以不断嵌套来表示很复杂的关系。

```yaml
org_name: "一条龙"
members:
  - name: "DoctorReid"
    github_homepage: "https://github.com/DoctorReid"
    level: 60
    friends:
      - name: "a"
        github_homepage: "https://github.com/a"
      - name: "b"
        github_homepage: "https://github.com/b"
  - name: "小巡夜"
    github_homepage: "https://github.com/yokuminto"
    level: 60
keywords: [ "脚本", "自动化" ]
other_info:
  homepage: "https://one-dragon.com/"
  create_date: "2024-09-01"
```

这个例子中，我们给一条龙的成员DoctorReid添加了一个 朋友(friends) 的属性，里面因为有 `横线(-)`，说明是一个数组，数组里的每个元素又再包含2个属性。

你可以复制出来观察，复杂的嵌套下，无非就是继续增加 `缩进(2个空格)`。

所以，yaml文件的格式，本质上就是管理好缩进，让内容外观好看的同时，结构化地表达内容。