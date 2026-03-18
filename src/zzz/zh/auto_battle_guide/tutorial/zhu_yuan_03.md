---
lang: zh-CN
title: 03-连携与快速支援-朱鸢
---

## 0.前置说明

本章节的目的，是让角色打出连携后，按想要的顺序进行连携换人，最后通过快速支援切换到主C输出。

打开编辑你的`朱鸢教程.yml`，进入训练场，敌人选择狂乱暴徒，开启怪物的无敌，关闭移动，开启失衡，然后开始本章节的内容。

## 1.基础逻辑

由于脚本无法识别当前失衡可以触发多少次连携，所以我们策略固定为先切强攻，再切支援，然后取消，最后按快速支援切出主C。

试试以下配置，在训练场运行一段时间看看效果吧。

<details>
<summary>示例</summary>

```yaml
scenes:
  - triggers: [ "按键可用-连携技" ]
    interval: 1
    handlers:
      - states: "[连携技-1-强攻]"
        operations:
          - op_name: "按键-连携技-左"
            post_delay: 1
      - states: "[连携技-2-强攻]"
        operations:
          - op_name: "按键-连携技-右"
            post_delay: 1
      - states: "[连携技-1-支援]"
        operations:
          - op_name: "按键-连携技-左"
            post_delay: 1
      - states: "[连携技-2-支援]"
        operations:
          - op_name: "按键-连携技-右"
            post_delay: 1
      - states: ""
        operations:
          - op_name: "按键-连携技-取消"
            way: "按下"
            press: 0.02
            post_delay: 0.01

  - triggers: [ "按键可用-快速支援" ]
    interval: 1
    handlers:
      - states: "[按键可用-快速支援]"
        operations:
          - op_name: "按键-快速支援"
            post_delay: 1

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

## 2.配置讲解

开始前，学习 [触发条件](../basic/basic_03_triggers.md)

上述例子中，我们也是沿用了 连携 和 快速支援 部分的触发条件，然后在里面判断具体要切换到哪个角色。

`处理方法(handlers)` 是按顺序判断里面的 `状态表达式(states)` 是否满足，我们就是用这个来做连携的顺序。

而快速支援，目前由于只有安妮会触发，就无脑按切到强攻就行。

## 3.失衡爆发

上述例子中，强攻切换出来后打一两下就换下场了，这是因为我们的无触发场景中，依然要求保持击破站场。

怪物失衡期间，我们是希望强攻站场输出的，于是脚本可以改善为这样。

<details>
<summary>示例</summary>

```yaml

scenes:
  - triggers: [ "按键可用-连携技" ]
    interval: 1
    handlers:
      - states: "[连携技-1-强攻]"
        operations:
          - op_name: "按键-连携技-左"
            post_delay: 1
      - states: "[连携技-2-强攻]"
        operations:
          - op_name: "按键-连携技-右"
            post_delay: 1
      - states: "[连携技-1-支援]"
        operations:
          - op_name: "按键-连携技-左"
            post_delay: 1
      - states: "[连携技-2-支援]"
        operations:
          - op_name: "按键-连携技-右"
            post_delay: 1
      - states: ""
        operations:
          - op_name: "按键-连携技-取消"
            way: "按下"
            press: 0.02
            post_delay: 0.01

  - triggers: [ "按键可用-快速支援" ]
    interval: 1
    handlers:
      - states: "[按键可用-快速支援]"
        operations:
          - op_name: "按键-快速支援"
            post_delay: 1

  - triggers: [ ]
    interval: 0.02
    handlers:
      # 连携按键后 由强攻站场
      - states: "[按键-连携技-左, 0, 12] | [按键-连携技-右, 0, 12]"
        sub_handlers:
          - states: "[前台-强攻]"
            sub_handlers:
              - states: "[按键可用-终结技]"
                operations:
                  - op_name: "按键-终结技"
                    post_delay: 5
              - states: "[按键可用-特殊攻击]"
                operations:
                  - op_name: "按键-特殊攻击"
                    post_delay: 1
              - states: ""
                operations:
                  - op_name: "按键-普通攻击"
                    post_delay: 0.05
          - states: "[后台-2-强攻]"
            operations:
              - op_name: "按键-切换角色-上一个"
                post_delay: 0.1
          - states: "[后台-1-强攻]"
            operations:
              - op_name: "按键-切换角色-下一个"
                post_delay: 0.1

      # 普通情况下 由击破站场
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

由于脚本无法识别怪物是否处于失衡状态，我们改用了判断是否在按连携键的12秒内，作为失衡期的替代判断。

```yaml
- states: "[按键-连携技-左, 0, 12] | [按键-连携技-右, 0, 12]"
```

状态的时间判断，可以在 [状态表达式](../basic/basic_05_states.md) 的 `状态识别时间` 学习。

判断符合失衡期后，里面的逻辑基本就跟由击破站场一致，只需要将里面的连招替换成对应的主C连招即可。

## 4.章节作业

1. 加入场景，使用闪避识别作为触发条件，里面的闪避切人逻辑自由发挥即可。
2. 为强攻角色站场添加对应的连招，也是自由发挥。一个简单的思路是，以朱鸢为例，有子弹的时候就长按普攻，没有子弹的时候就普攻或者使用强化特殊技补充子弹。

开始前，你需要学习如何在状态表达式中判断子弹数，见 [状态表达式](../basic/basic_05_states.md) 的 `状态值判断` 。

<details>
<summary>最终成果</summary>

未有

</details>


## 5.阶段完成

在本章节后，你应该就能完成任何一个队伍的基本战斗逻辑了。

后续章节，会补充一些实战中会遇到的奇奇怪怪场景，同时再介绍其它较少使用的用法。

你可以先按照自己的配队编写，到实战中看看效果，然后再继续看后续内容，可能会感受理解更深一点。

也可以看看脚本中自带的专属配队写法，由于这些配队不是脚本作者编写，里面有一些写法并不是作者推荐，但实际效果也挺不错，就让大家自由发挥了。不过还是建议按本教程讲述的逻辑进行编写。
