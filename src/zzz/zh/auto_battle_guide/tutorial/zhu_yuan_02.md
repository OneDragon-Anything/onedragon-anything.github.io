---
lang: zh-CN
title: 02-角色连招-朱鸢
---

## 0.前置说明

本章节的目的，是让一个角色可以打出对应的连招。目前来说，就是让 `安比` 能完成对应的连招。

打开编辑你的`朱鸢教程.yml`，进入训练场，开启怪物的无敌，关闭移动和失衡，然后开始本章节的内容。

## 1.基础逻辑

通常来说，一个角色在场上只需要考虑以下情况

- 有终结技时，释放终结技
- 有能量时，释放强化特殊技
- 以上都没有时，不断普通攻击过渡。

那么，我们就先按这最简单的模式来编写，在训练场运行一段时间看看效果。

<details>
<summary>配置.yml</summary>

```yaml
scenes:
  - triggers: [ ]
    interval: 0.02
    handlers:
      - states: "[前台-击破]"
        sub_handlers:
        - states: "[按键可用-终结技]"
          operations:
            - op_name: "按键-终结技"
              post_delay: 5
        - states: "[按键可用-特殊攻击]"
          operations:
            - op_name: "按键-特殊攻击"
              post_delay: 2
        - states: ""
          operations:
            - op_name: "按键-普通攻击"
              post_delay: 0.05
      - states: "[后台-2-击破]"
        operations:
          - op_name: "按键-切换角色-上一个"
            post_delay: 0.1
      - states: "[后台-1-击破]"
        operations:
          - op_name: "按键-切换角色-下一个"
            post_delay: 0.1
```

</details>

### 1.1.子处理方法(sub_handlers)

上述例子中我们使用了新的语法 `子处理方法(sub_handlers)`。

请戳这里学习 [处理方法](../basic/basic_04_handlers.md) 完成 `子处理方法` 部分学习。

## 2.节奏型连招

当然，不是所有角色都是一直普通攻击就完事的，安比就不是。为了快速打失衡，安比需要使用 3A+重击 的连招。

我们回想人工操作，基本也是不断按普通攻击，然后看到第3段攻击时候按住普通攻击打重击。

但脚本是无法知道打到第几段普通攻击的，所以我们模拟的是一段时间的普通攻击后接重击。

<details>
<summary>示例</summary>

```yaml
scenes:
  - triggers: [ ]
    interval: 0.02
    handlers:
      - states: "[前台-击破]"
        sub_handlers:
          - states: "[按键可用-终结技]"
            operations:
              - op_name: "按键-终结技"
                post_delay: 5
          - states: "[按键可用-特殊攻击]"
            operations:
              - op_name: "按键-特殊攻击"
                post_delay: 2
          - states: ""
            operations:
              - op_name: "按键-普通攻击"
                post_delay: 0.05
                repeat: 20
              - op_name: "按键-闪避"
                post_delay: 1
      - states: "[后台-2-击破]"
        operations:
          - op_name: "按键-切换角色-上一个"
            post_delay: 0.1
      - states: "[后台-1-击破]"
        operations:
          - op_name: "按键-切换角色-下一个"
            post_delay: 0.1
```

</details>

上述例子中，我们通过给 `按键-普通攻击` 添加 `重复(repeat)` 属性，来完成一段时间的不断普攻，然后接一个闪避，来进行测试验证。

尝试运行，并调整 `重复(repeat)` 次数，直到这个普攻重复次数是进行到准备重击的阶段，然后将最后的闪避指令替换成长按普攻即可。

而能打出一套3A重击后，再调整最后的指令的 `按键后等待(post_delay)`，让整套连招能循环运行。

<details>
<summary>最终成果</summary>

```yaml
scenes:
  - triggers: [ ]
    interval: 0.02
    handlers:
      - states: "[前台-击破]"
        sub_handlers:
          - states: "[按键可用-终结技]"
            operations:
              - op_name: "按键-终结技"
                post_delay: 5
          - states: "[按键可用-特殊攻击]"
            operations:
              - op_name: "按键-特殊攻击"
                post_delay: 2
          - states: ""
            operations:
              - op_name: "按键-普通攻击"
                post_delay: 0.05
                repeat: 20
              - op_name: "按键-普通攻击"
                way: "按下"
                press: 2
      - states: "[后台-2-击破]"
        operations:
          - op_name: "按键-切换角色-上一个"
            post_delay: 0.1
      - states: "[后台-1-击破]"
        operations:
          - op_name: "按键-切换角色-下一个"
            post_delay: 0.1
```

</details>

## 3.失衡判断

接下来，打开怪物的失衡，再运行上述配置试试。

你会发现，虽然打满了失衡条，但是没有触发失衡连携。

具体原因可见 [绝区零战斗冷知识](../other/battle_knowledge.md) `3.失衡判断`。

你可以尝试调整长按普攻的时间来解决这个问题，这个就作为章节作业的一部分吧。


## 4.攻击反馈

在上述连招可以流畅运行的情况下，尝试让角色移动到离敌人一段距离，或者调整敌人为10级，关闭无敌，再运行。

观察运行情况，你会发现连招有可能不流畅循环了。

具体原因可见 [绝区零战斗冷知识](../other/battle_knowledge.md) `4.攻击反馈`。

不过由于绝区零有很便利的自动索敌，大部分情况下我们的攻击都是能命中的，也就是可以忽略这个情况。

如果你想进一步改进，可以在连招的开始或者结束位置，加入一个闪避来重置当前动作。

## 5.章节作业

继续修改上述例子，在特殊技可用的情况下，让安比打出 3A+强化特殊技，普通情况依然是 3A+重击，并且两套连招都能流程循环执行，也都能触发失衡连携技。

<details>
<summary>最终成果</summary>

```yaml
scenes:
  - triggers: [ ]
    interval: 0.02
    handlers:
      - states: "[前台-击破]"
        sub_handlers:
        - states: "[按键可用-终结技]"
          operations:
            - op_name: "按键-终结技"
              post_delay: 5
        - states: "[按键可用-特殊攻击]"
          operations:
            - op_name: "按键-普通攻击"
              post_delay: 0.05
              repeat: 20
            - op_name: "按键-特殊攻击"
              post_delay: 0.05
              repeat: 30
            - op_name: "按键-普通攻击"
              post_delay: 0.05
              repeat: 30
        - states: ""
          operations:
            - op_name: "按键-普通攻击"
              post_delay: 0.05
              repeat: 20
            # 触发失衡改了这里
            - op_name: "按键-普通攻击"
              way: "按下"
              press: 1.5
              post_delay: 0.5
      - states: "[后台-2-击破]"
        operations:
          - op_name: "按键-切换角色-上一个"
            post_delay: 0.1
      - states: "[后台-1-击破]"
        operations:
          - op_name: "按键-切换角色-下一个"
            post_delay: 0.1
```

</details>
