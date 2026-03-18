---
lang: zh-CN
title: 架构解析 - 全配队通用
---

本文以 `全配队通用` 战斗配置为例，解析其核心的事件驱动架构与模块化设计思想。

> 阅读本文前，建议先掌握 [02-场景](../basic/basic_02_scenes.md) 和 [07-模板系统](../basic/basic_07_templates.md)。

---

## 1. 设计哲学

`全配队通用` 的核心思想是**模块化**与**事件驱动分层**。它将战斗逻辑拆分为三层：

| 层级 | 目录 | 职责 | 比喻 |
|---|---|---|---|
| 战略层 | `auto_battle/` | 监听事件，设定优先级，分派任务 | 项目经理 |
| 决策层 | `auto_battle_state_handler/` | 处理特定事件或角色的决策逻辑 | 各领域专家 |
| 动作层 | `auto_battle_operation/` | 执行具体的按键连招 | 手和脚 |

通过将 **"何时做"（战略）**、**"做什么"（决策）** 和 **"如何做"（动作）** 分离，可以适应任意角色组合，而无需为每个队伍编写独立的顶层脚本。

---

## 2. 文件结构

三层目录与引用规则详见 [07-模板系统](../basic/basic_07_templates.md)。

---

## 3. 事件调度中心

`全配队通用.yml` 定义了多个场景（`scenes`），每个场景监听不同的游戏事件。它**不直接处理**具体逻辑，而是通过 `state_template` 将任务分派给对应的"专家模板"。

### 状态引用树

```text
【全配队通用】
     │
     ├─ scene: [闪避事件] (priority: 99)
     │   ├─ "支援攻击模板-*"   → 黄光/格挡 → 支援攻击
     │   └─ "闪A模板-全角色"   → 红光/声音 → 闪避反击
     │
     ├─ scene: [连携事件] (priority: 98)
     │   └─ "连携模板-通用"    → 连携技选人
     │
     ├─ scene: [快速支援事件] (priority: 97)
     │   └─ "快速支援模板-全角色" → 快速支援
     │
     ├─ scene: [受击事件] (priority: 90)
     │   ├─ "轮换-救命-全角色" → 低血量? 切人开大!
     │   └─ "闪A模板-全角色"   → 受击闪避反击
     │
     ├─ scene: [连招结束事件] (priority: 80)
     │   └─ "轮换-合轴-全角色" → 需要补Buff? 换人!
     │
     └─ scene: [默认循环] (priority: 9)
         ├─ "站场模板-未识别角色" → 前置：角色识别检查
         ├─ "自动锁定模板"       → 前置：锁定目标
         ├─ "轮换-紧急-全角色"   → 前置：紧急换人检查
         │
         └─ "速切模板-全角色"    → 角色分派器
             ├─ "速切模板-安比"
             ├─ "速切模板-艾莲"
             └─ ...（各角色专属模板）
```

### 优先级解读

| 优先级 | 事件 | 说明 |
|---|---|---|
| 99 | 闪避 | 最高优，确保闪避不被打断 |
| 98 | 连携 | 连携技窗口稍纵即逝 |
| 97 | 快速支援 | 快速支援机会 |
| 90 | 受击 | 保命优先于输出 |
| 80 | 连招结束 | 合轴换人时机 |
| 9 | 默认循环 | 常规输出循环 |

高优先级场景会**抢占**低优先级场景正在执行的操作。例如：角色正在执行普攻连段（优先级 9），此时检测到红光反击机会（优先级 99），系统会立即中断普攻，执行闪避。

---

## 4. 关键模板解析

### 4.1 速切模板-全角色（角色分派器）

唯一职责：判断当前站场角色，将控制权交给该角色的专属"大脑"。

```yaml
handlers:
  - state_template: "速切模板-安比"    # 安比在前台时生效
  - state_template: "速切模板-艾莲"    # 艾莲在前台时生效
  - state_template: "速切模板-朱鸢"
  # ...
```

### 4.2 角色专属模板（角色的"大脑"）

定义角色在前台时的输出决策树。连招结束后通过设置状态发出"可换人"信号：

```yaml
# 速切模板-安比.yml
handlers:
  - states: "[前台-安比]"
    sub_handlers:
      # 优先检查是否有终结技
      - states: "[前台-终结技可用]"
        operations:
          - op_name: "按键-终结技"

      # 常规输出
      - states: ""
        operations:
          - operation_template: "安比-3A特殊攻击"
          - op_name: "设置状态"
            state: "自定义-合轴时间"    # 信号：我打完了，可以换人
```

### 4.3 轮换模板（团队协作）

三个轮换模板各司其职：

- **轮换-救命-全角色**：低血量触发，切人开大保命
- **轮换-合轴-全角色**：连招结束后触发（由 `自定义-合轴时间` 状态），判断是否需要补增益并换人
- **轮换-紧急-全角色**：每次主循环前检查，处理突发的换人需求

---

## 5. 设计优势

1. **添加新角色简单**：只需 4 步，无需改动顶层战略文件
2. **修改策略不影响全局**：修改闪避策略只需改闪A模板，不需要动顶层配置
3. **通用逻辑复用**：轮换、连携、支援攻击等逻辑对所有配队通用
4. **优先级清晰**：事件驱动的抢占模型确保紧急事件总能及时响应

---

## 6. 如何新增角色

得益于解耦设计，新增角色只需 4 步。以"比利"为例：

| 步骤 | 操作 | 文件位置 |
|---|---|---|
| 1. 创建操作模板 | 为角色定义所有基础连招（普攻、Buff、终结技等） | `auto_battle_operation/比利-*.yml` |
| 2. 创建角色"大脑" | 创建速切模板，定义前台时的决策逻辑。连招结束后设置 `自定义-合轴时间` 发出"可换人"信号 | `auto_battle_state_handler/速切模板-比利.yml` |
| 3. 注册到分派器 | 在分派器中添加一行引用 | `auto_battle_state_handler/速切模板-全角色.yml` |
| 4. 融入团队轮换 | 在合轴轮换和紧急轮换模板中添加比利的上场条件 | `轮换-合轴-全角色.yml` + `轮换-紧急-全角色.yml` |

## 7. 角色识别机制

在战斗画面对头像进行识别，开始时，以全角色进行匹配识别，效率较低。在连续 5 次识别成功且角色一致后，就会记录下来这批角色，后续只用这部分角色来识别。

脚本中，触发会换人的按键时，会自动计算并更新角色列表，避免在换人途中短时间内的白色头像无法识别。相关指令如下：

- 按键-切换角色-下一个
- 按键-切换角色-上一个
- 按键-连携技-左
- 按键-连携技-右
- 按键-快速支援

在更新角色的同时，会同时更新以下状态：

- `**-能量` - 跟随角色变化
- `按键可用-终结技` - 会重新判断
- `按键可用-特殊攻击` - 会置为不可用，等待下一次识别

---

## 附录：全局参数

全局参数位于战斗模板（如 `全配队通用.yml`）的顶层，控制系统的整体行为。

### 识别间隔

支持固定数字或随机区间 `[下限, 上限]`：

```yaml
check_dodge_interval: 0.02                  # 闪避识别间隔
check_agent_interval: [0.4, 0.6]            # 角色识别间隔（随机）
check_special_attack_interval: [0.4, 0.6]   # 特殊攻击就绪检测
check_ultimate_interval: [0.4, 0.6]         # 终结技就绪检测
check_chain_interval: [0.9, 1.1]            # 连携技就绪检测
check_quick_interval: [0.9, 1.1]            # 快速支援就绪检测
auto_lock_interval: 5                       # 自动锁定间隔，-1 = 不自动锁定
auto_turn_interval: 3                       # 镜头自动转向间隔
```

### 终结技限制

通过 `allow_ultimate` 限制终结技只能由特定角色使用：

```yaml
allow_ultimate:
  - agent_type: "强攻"      # 按角色类型
  - agent_name: "安比"       # 按角色名称
```

不配置时，所有角色都可以使用终结技。

### 内置默认自定义状态

内置模板定义了若干常用的自定义状态，编写配置时可以直接使用。这些是模板里进行设置，且需要在状态判断中配合使用的，不是脚本运行时自动附带的。

如果你想用，可以引用模板，或者参考模板和下述例子自己设置对应的状态。

#### 自定义-黄光切人

黄光切人时设置；不同角色格挡攻击后摇时间不同，由角色模板控制等待多长时间进行后续指令。

<details>
<summary> 设置例子 </summary>

```yaml
# 双反模板-击破.sample.yml
handlers:
  - states: "[后台-2-击破]"
    operations:
      - operation_template: "双反-上一个"
      - op_name: "设置状态"
        state: "自定义-黄光切人"
  - states: "[后台-1-击破]"
    operations:
      - operation_template: "双反-下一个"
      - op_name: "设置状态"
        state: "自定义-黄光切人"
```

</details>

<details>
<summary> 使用例子 </summary>

```yaml
# 站场模板-朱鸢.sample.yml
handlers:
  - states: "[前台-朱鸢]"
    sub_handlers:
      - states: "[自定义-黄光切人]"
        operations:
          - op_name: "按键-普通攻击"
            pre_delay: 0.2
            post_delay: 1.5
          - op_name: "清除状态"
            state: "自定义-黄光切人"
          - op_name: "设置状态"
            state: "自定义-临时站场"
```

</details>

#### 自定义-红光闪避

红光时设置；不同角色闪避攻击后摇时间不同，由角色模板控制等待多长时间进行后续指令。

<details>
<summary> 设置例子 </summary>

```yaml
# 闪A模板-通用.sample.yml
handlers:
  - states: ""
    operations:
      - op_name: "按键-闪避"
        post_delay: 0.2
      - op_name: "按键-普通攻击"
      - op_name: "设置状态"
        state: "自定义-红光闪避"
```

</details>

<details>
<summary> 使用例子 </summary>

```yaml
# 站场模板-朱鸢.sample.yml
handlers:
  - states: "[前台-朱鸢]"
    sub_handlers:
      - states: "[自定义-红光闪避]"
        operations:
          - op_name: "按键-普通攻击"
            pre_delay: 0.8
            post_delay: 1
          - op_name: "按键-普通攻击"
            post_delay: 1
            repeat: 2
          - op_name: "清除状态"
            state: "自定义-红光闪避"
```

</details>

#### 自定义-快速支援换人

快速支援换人时设置；不同角色快速支援攻击后摇时间不同，由角色模板控制等待多长时间进行后续指令。

<details>
<summary> 设置例子 </summary>

```yaml
# 击破站场-强攻速切.sample.yml
scenes:
  - triggers: [ "按键可用-快速支援" ]
    interval: 1
    handlers:
      - states: "[按键可用-快速支援]"
        operations:
          - op_name: "按键-快速支援"
          - op_name: "设置状态"
            state: "自定义-快速支援换人"
```

</details>

<details>
<summary> 使用例子 </summary>

```yaml
# 站场模板-朱鸢.sample.yml
handlers:
  - states: "[前台-朱鸢]"
    sub_handlers:
      - states: "[自定义-快速支援换人]"
        operations:
          - op_name: "等待秒数"
            seconds: 0.5
          - op_name: "清除状态"
            state: "自定义-快速支援换人"
          - op_name: "设置状态"
            state: "自定义-临时站场"
```

</details>

#### 自定义-连携换人

连携换人时设置；不同角色连携攻击后摇时间不同，由角色模板控制等待多长时间进行后续指令；同时可用于失衡判断。

<details>
<summary> 设置例子 </summary>

```yaml
# 连携模板-击破.sample.yml
handlers:
  - states: "[连携技-1-击破]"
    operations:
      - op_name: "按键-连携技-左"
      - op_name: "设置状态"
        state: "自定义-连携换人"
  - states: "[连携技-2-击破]"
    operations:
      - op_name: "按键-连携技-右"
      - op_name: "设置状态"
        state: "自定义-连携换人"
```

</details>

<details>
<summary> 使用例子 </summary>

```yaml
# 站场模板-朱鸢.sample.yml
handlers:
  - states: "[前台-朱鸢]"
    sub_handlers:
      - states: "[自定义-连携换人]"
        operations:
          - op_name: "等待秒数"
            seconds: 1.5
```

</details>

#### 自定义-临时站场

想插队站场的时候设置；例如朱鸢黄光出来的时候打几发子弹再切回击破，避免溢出。

<details>
<summary> 设置例子 </summary>

```yaml
# 站场模板-朱鸢.sample.yml
handlers:
  - states: "[前台-朱鸢]"
    sub_handlers:
      - states: "[自定义-黄光切人]"
        operations:
          - op_name: "按键-普通攻击"
            pre_delay: 0.2
            post_delay: 1.5
          - op_name: "清除状态"
            state: "自定义-黄光切人"
          - op_name: "设置状态"
            state: "自定义-临时站场"
```

</details>

<details>
<summary> 使用例子 </summary>

```yaml
# 击破站场-强攻速切.sample.yml
scenes:
  - triggers: [ ]
    interval: 0.02
    handlers:
      - state_template: "通用模板-锁定敌人"
      - state_template: "站场模板-未识别角色"
      - states: "[自定义-黄光切人, 0, 2] | [自定义-红光闪避, 0, 2] | [自定义-临时站场]"
        sub_handlers:
          - state_template: "站场模板-全角色"
```

</details>

#### 自定义-动作不打断

想指令不被触发条件打断时设置，例如青衣在打重击的时候不因为闪光打断。

<details>
<summary> 设置例子 </summary>

```yaml
# 站场模板-青衣.sample.yml
handlers:
  - states: "[前台-青衣]"
    sub_handlers:
      - states: "[青衣-电压, 0, 999]{75, 101}"
        operations:
          - op_name: "设置状态"
            state: "自定义-动作不打断"
            value: 1
          - op_name: "按键-普通攻击"
            way: "按下"
            press: 3.5
          - op_name: "清除状态"
            state: "自定义-动作不打断"
          - op_name: "清除状态"
            state: "自定义-青衣-普攻次数"
```

</details>

<details>
<summary> 使用例子 </summary>

```yaml
# 击破站场-强攻速切.sample.yml
scenes:
  - triggers: [ "闪避识别-黄光", "闪避识别-红光", "闪避识别-声音" ]
    interval: 1
    handlers:
      - states: "![自定义-动作不打断, 0, 999]{1, 1} & [闪避识别-黄光]"
        sub_handlers:
          - state_template: "双反模板-强攻"
          - state_template: "双反模板-击破"
          - state_template: "双反模板-下一个"
      - states: "![自定义-动作不打断, 0, 999]{1, 1} & ([闪避识别-红光] | [闪避识别-声音])"
        sub_handlers:
          - state_template: "闪A模板-全角色"
```

</details>
