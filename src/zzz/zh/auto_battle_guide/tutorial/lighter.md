---
lang: zh-CN
title: 角色连招示例-莱特
---

## 清空士气切换角色

以下逻辑主要作用是识别出莱特通过打拳消耗完士气，然后下场切换角色

```yaml
scenes:
  - triggers: [ ]
    interval: 0.02
    handlers:
      - states: "[前台-莱特]"
        sub_handlers:
          - states: "[莱特-士气]{80, 100} & ![自定义-莱特-士气, 0, 999]{1}"
            operations:
              - op_name: "设置状态"
                state: "自定义-莱特-士气"
                value: 1
          - states: "[莱特-士气]{0, 10} & [自定义-莱特-士气, 0, 999]{1}"
            operations:
              - op_name: "清除状态"
                state: "自定义-莱特-士气"
              - op_name: "按键-切换角色-下一个"
                post_delay: 0.05
          - states: ""
            operations:
              - op_name: "按键-普通攻击"
                post_delay: 0.05
```

逻辑讲解

- 在士气足够的时候，进入一个自定义状态，代表后续打拳开始消耗士气了
- 拥有自定义状态的情况下，士气消耗完毕，这轮速切结束，就可以切换角色了
