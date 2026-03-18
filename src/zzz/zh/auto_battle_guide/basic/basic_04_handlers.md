---
lang: zh-CN
title: 基础-04-处理方法
---

处理方法(handlers)，是一个数组，定义了“在什么条件下执行什么操作”，是场景内的决策逻辑。
```yaml
handlers:
  - states: "[前台-击破]"
    operations:
      - op_name: "按键-普通攻击"
```
## 1.处理方法属性

| 属性 | 说明 |
|---|---|
| `states` | 状态表达式，为真时执行该处理方法 |
| `operations` | 操作指令 |
| `sub_handlers` | 子处理方法，用于进一步细分判断 |
| `state_template` | 引用状态处理模板（出现时 states/operations/sub_handlers 无效） |
| `interrupt_states` | 打断表达式，匹配时中断当前操作。子处理方法继承父级（OR 合并） |
| `debug_name` | 调试日志中显示的名称，方便排查 |

## 2.状态表达式

戳 [这里](basic_05_states.md) 了解

## 3.操作指令数组

戳 [这里](basic_06_operations.md) 了解

## 4.执行逻辑

脚本按顺序遍历 `handlers` 数组：

1. 判断当前处理方法的 `states` 是否为真
2. 如果为真：
   - 有 `operations` → 执行操作
   - 有 `sub_handlers` → 递归进入子级继续判断
3. 如果为假 → 继续下一个处理方法

**等价于一个 IF-ELIF-ELSE 链**：

```yaml
handlers:
  - states: "[条件A]"                    # IF 条件A
    operations: ...
  - states: "[条件B]"                    # ELIF 条件B
    operations: ...
  - states: ""                           # ELSE（空字符串 = 永远为真）
    operations: ...
```

## 5.子处理方法 (sub_handlers)

当需要在某个条件下进一步细分时，使用 `sub_handlers` 代替 `operations`：

```yaml
handlers:
  - states: "[前台-安比]"
    sub_handlers:
      - states: "[按键可用-终结技]"          # IF 安比在前台 且 终结技可用
        operations:
          - op_name: "按键-终结技"
      - states: "[安比-特殊技可用]"          # ELIF 安比在前台 且 特殊技可用
        operations:
          - op_name: "按键-特殊攻击"
      - states: ""                           # ELSE 安比在前台 → 默认普攻
        operations:
          - op_name: "按键-普通攻击"
```

这等价于把 `[前台-安比]` 提到外面，省去每个子级重复写，逻辑上更直观。

## 6.interrupt_states

`interrupt_states` 用于定义一个“紧急中断”条件。当处理方法正在执行 `operations` 时，如果 `interrupt_states` 匹配，操作会被立即中断。

```yaml
handlers:
  - states: "[前台-安比]"
    interrupt_states: "[闪避识别-红光]"    # 执行到一半遇到红光就中断
    operations:
      - op_name: "按键-普通攻击"
        repeat: 10
```

子处理方法会**继承**父级的 `interrupt_states`（以 OR 逻辑合并）。
