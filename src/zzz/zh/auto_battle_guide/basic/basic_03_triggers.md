---
lang: zh-CN
title: 基础-03-触发条件
---

触发条件(triggers)，是一个字符串数组，每个元素是一个状态名。当脚本识别到数组中的任一状态时，该场景就会被尝试触发。

```yaml
# 闪避场景：三种闪光信号都触发同一个场景
- triggers: ["闪避识别-黄光", "闪避识别-红光", "闪避识别-声音"]
  handlers:
    - states: "[闪避识别-黄光, 0, 1]"    # 再用 states 细分
      operations: ...
    - states: "[闪避识别-红光, 0, 1]"
      operations: ...
```

**两种场景**：
- **有触发条件**：处理偶发的突发事件（闪避、连携、快速支援）
- **无触发条件** (`triggers: []`)：默认的常规连招循环，只能有一个

## 1.常见触发条件模板

```yaml
scenes:
  - triggers: ["闪避识别-黄光", "闪避识别-红光", "闪避识别-声音"]
    interval: 1
    priority: 99
    handlers: ...

  - triggers: ["按键可用-快速支援"]
    interval: 1
    handlers: ...

  - triggers: ["按键可用-连携技"]
    interval: 1
    handlers: ...

  - triggers: []
    interval: 0.02
    handlers: ...
```

## 2.优先级与打断

### 2.1.基本规则

- 场景正在执行时，**只有更高优先级的场景** 可以打断它
- **同优先级** 的场景互不打断
- **没有设置优先级** 的场景可被任意打断

```yaml
scenes:
  - triggers: ["闪避识别-黄光"]
    interval: 1
    priority: 99          # 最高优先级
    handlers: ...

  - triggers: ["闪避识别-红光"]
    interval: 1
    priority: 99          # 与黄光同优先级，互不打断
    handlers: ...

  - triggers: ["按键可用-连携技"]
    interval: 1
    priority: 98          # 比闪避低，闪避可以打断连携
    handlers: ...

  - triggers: []
    interval: 0.02        # 没有 priority，可被任意打断
    handlers: ...
```

### 2.2.事件驱动与抢占模型

场景实际上是 **事件驱动 + 抢占** 模型：当某个状态被识别到时，系统会唤醒所有监听该状态的场景，**只有优先级最高的**执行。场景执行期间，**更高优先级的场景可以随时打断**当前操作。

> 例如：`priority: 9` 的普攻连招执行到一半，突然出现红光 → `priority: 99` 的闪避场景立即打断 → 执行闪避 → 完成后恢复正常监听。

完整的调度机制和模板引用树详见 [架构解析](../reference/architecture.md)。

### 2.3.嵌套触发注意事项

切人动作（如连携换人）会触发 `前台-XX` 状态的变化，可能意外激活其他触发条件。编写时需注意避免场景之间的意外嵌套打断。
