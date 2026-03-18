---
lang: zh-CN
title: 基础-00-自动战斗简介
---

## 1.原理

自动战斗的逻辑与玩家手动操作一致：观察画面 → 判断状态 → 执行操作。

- **识别线程**：程序持续截图、监听声音，识别游戏当前状态（如闪光、角色、连携提示等）。
- **操作线程**：根据配置文件中定义的规则，在不同状态下执行对应的按键操作。

操作线程会区分 **常规循环操作** 和 **特殊事件触发操作**。没有特殊事件时执行常规循环；发生特殊事件时，打断当前操作并执行事件对应的操作。

## 2.配置文件

自动战斗使用三层配置文件，分别存放于：

| 文件类型 | 路径 | 职责 |
|---|---|---|
| 战斗配置 | `config/auto_battle/*.yml` | 顶层策略，定义场景、优先级 |
| 状态模板 | `config/auto_battle_state_handler/*.yml` | 中层决策，角色决策树 |
| 操作模板 | `config/auto_battle_operation/*.yml` | 底层执行，具体连招 |

> 脚本自带的配置以 `.sample.yml` 结尾，更新时会被覆盖，**不要修改**。需要自定义请复制后改名。

## 3.学习路线

建议按以下顺序阅读：

1. [YAML 格式](basic_01_yaml.md) — 了解配置文件的书写格式
2. [场景](basic_02_scenes.md) — 了解场景的整体结构
   - [触发条件](basic_03_triggers.md) — 了解 triggers / priority / 打断机制
   - [处理方法](basic_04_handlers.md) — 了解 handlers / sub_handlers / interrupt_states
     - [状态表达式](basic_05_states.md) — 了解如何编写条件判断
     - [操作指令](basic_06_operations.md) — 了解 `op_name` 和各种参数
3. [模板系统](basic_07_templates.md) — 了解三层模板体系与复用

掌握基础后：

- [参考手册](../reference/states_enum.md) — 写配置时随时查阅状态枚举
- [实战教程](../tutorial/zhu_yuan_01.md) — 想边学边做？跳到朱鸢配队教程跟着实操
