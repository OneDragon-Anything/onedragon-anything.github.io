---
lang: zh-CN
title: 基础-07-模板系统
---

模板是实现脚本模块化和代码复用的核心机制。它将复杂的逻辑拆分为易于管理的小文件，通过引用组装起来。

## 1.三层模板体系

一条龙的配置按职责分为三层，每层存放在不同的目录：

```
config/
├── auto_battle/                # 1. 战斗模板（顶层策略）
│   └── 全配队通用.yml
├── auto_battle_state_handler/  # 2. 状态模板（中层决策）
│   ├── 速切模板-全角色.yml
│   └── 站场模板-安比.yml
└── auto_battle_operation/      # 3. 操作模板（底层动作）
    └── 安比-3A特殊攻击.yml
```

| 层级 | 路径 | 职责 | 包含内容 |
|---|---|---|---|
| 战斗模板 | `config/auto_battle/` | 顶层策略 | `scenes`、`priority`、全局参数 |
| 状态模板 | `config/auto_battle_state_handler/` | 中层决策 | 角色决策树、通用逻辑 |
| 操作模板 | `config/auto_battle_operation/` | 底层执行 | 具体的连招按键序列 |

**核心引用规则**：上层可以引用同层或下层，**底层不能引用上层**。

- ✅ 战斗模板 → 状态模板 → 操作模板
- ✅ 状态模板 → 状态模板（模板互相嵌套）
- ✅ 操作模板 → 操作模板（连招互相组装）
- ⚠️ 操作模板 → 状态模板（不推荐）

## 2.状态模板 (state_template)

在 `handlers` 中通过 `state_template` 引用外部的状态处理模板。

### 2.1. 引用方式

```yaml
handlers:
  - states: "[按键-连携技-左, 0, 12] | [按键-连携技-右, 0, 12]"
    sub_handlers:
      - states: "[前台-朱鸢]"
        operations: ...
  - state_template: "站场模板-击破站场"    # 引用外部模板
```

> 出现 `state_template` 时，`states`/`operations`/`sub_handlers` 均无效。

### 2.2. 模板文件结构

状态模板存放在 `config/auto_battle_state_handler/` 目录，结构如下：

```yaml
# 文件: 站场模板-安比.sample.yml
handlers:
  - states: "[前台-安比]"
    sub_handlers:
      - states: "[按键可用-终结技]"
        operations:
          - op_name: "按键-终结技"
      - states: ""
        operations:
          - operation_template: "安比-3A特殊攻击"
```

### 2.3. 嵌套

`sub_handlers` 和 `state_template` 可以不断嵌套。一个状态模板可以引用另一个状态模板：

```yaml
# 速切模板-全角色.yml → 分派到各角色专属模板
handlers:
  - state_template: "站场模板-安比"
  - state_template: "站场模板-艾莲"
  - state_template: "站场模板-朱鸢"
```

完整的内置状态模板列表见源码目录 [auto_battle_state_handler](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon/tree/main/config/auto_battle_state_handler)。

## 3.操作模板 (operation_template)

在 `operations` 中通过 `operation_template` 引用外部的操作模板。

### 3.1. 引用方式

```yaml
operations:
  - op_name: "设置状态"
    state: "自定义-动作不打断"
    seconds: 1
  - operation_template: "安比-3A特殊攻击"    # 引用外部模板
  - op_name: "按键-普通攻击"
```

### 3.2. 模板文件结构

操作模板存放在 `config/auto_battle_operation/` 目录：

```yaml
# 文件: 安比-3A特殊攻击.sample.yml
operations:
  - op_name: "按键-普通攻击"
    repeat: 3
    post_delay: 0.1
  - op_name: "按键-特殊攻击"
    post_delay: 0.1
```

### 3.3. 操作模板的嵌套与组装

操作模板之间可以互相引用，像"零件"一样组装成更复杂的连招：

```yaml
# 安比-普攻接特殊.yml（组装模板）
operations:
  - operation_template: "安比-三连普攻"       # 零件1
  - op_name: "等待秒数"
    seconds: 0.2
  - operation_template: "安比-特殊技收尾"     # 零件2
```

完整的内置操作模板列表见源码目录 [auto_battle_operation](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon/tree/main/config/auto_battle_operation)。

### 3.4. 操作模板示例

<details>
<summary> 安比-3A特殊攻击 </summary>

三段普攻接特殊攻击：

```yaml
operations:
  - op_name: "按键-普通攻击"
  - op_name: "等待秒数"
    seconds: 0.3
  - op_name: "按键-普通攻击"
  - op_name: "等待秒数"
    seconds: 0.5
  - op_name: "按键-普通攻击"
  - op_name: "等待秒数"
    seconds: 0.9
  - op_name: "按键-特殊攻击"
  - op_name: "等待秒数"
    seconds: 1.4
  - op_name: "按键-普通攻击"
  - op_name: "等待秒数"
    seconds: 0.2
  - op_name: "按键-普通攻击"
  - op_name: "等待秒数"
    seconds: 1.0
```
</details>

<details>
<summary> 通用-闪A </summary>

闪避后接普攻，设置 `自定义-动作不打断` 防止被打断：

```yaml
operations:
  - op_name: "设置状态"
    state: "自定义-动作不打断"
    seconds: 1
  - operation_template: "通用-闪避-左"
  - op_name: "按键-普通攻击"
    post_delay: 0.1
    repeat: 10
```
</details>
