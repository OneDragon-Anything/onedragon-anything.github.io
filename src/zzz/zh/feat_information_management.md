# 前言
此系统旨在为一条龙应用提供标准化接口，为仓库扫描系统的开发提供数据决策支持
## 代理人信息管理
<img width="1337" height="946" alt="image (1)" src="https://github.com/user-attachments/assets/24610f69-6f72-498c-8dd9-76a676ae23a9" />

- 优先级自动分配
用户通过在优先级表格中选择对应的词条后点击一键生成权重,系统将会自动针对权重进行分配到右侧权重配置表格中

- 最优音擎管理
此功能目前还未得到开发,后续会根据仓库扫描的开发情况进行添加

- 角色基础信息
可根据需要对角色的名称,类型,属性,稀有度,code进行修改

## 驱动盘信息管理
<img width="1336" height="947" alt="image (3)" src="https://github.com/user-attachments/assets/fe15ed53-6b55-4664-a3a1-877772cf143c" />
定义了驱动盘的基础信息,可根据需要自行修改

## 音擎信息管理
<img width="1334" height="948" alt="image (4)" src="https://github.com/user-attachments/assets/c212ed5e-c31f-4f7a-8fea-9fcc59fd85b9" />

定义了音擎的基础信息,可根据需要自行修改

## 数据交互方式

### 方式1:通过信息管理GUI界面修改(推荐)
根据上述介绍,开发者可根据需要对信息进行维护和开发

### 方式2:直接修改配置文件

> 角色配置路径:assets\game_data\agent

> 驱动盘配置路径:assets\game_data\drive_disk

> 音擎配置路径:assets\game_data\engine_weapon

访问对应的路径后,即可对其中定义的yml文件进行直接修改

稀有度映射:
```python
class RareTypeEnum(Enum):
    S = 'S'
    A = 'A'
    B = 'B'
    UNKNOWN = '未知'
```
角色
```yml
agent_name: 爱芮 #代理人名称
agent_type: ANOMALY #代理人类型
dmg_type: ETHER #伤害类型
rare_type: S #稀有度
code: aria #代码最好为英文
weight: #权重配置
  生命值: 0.0 #权重值的范围为0-1
  攻击力: 0.75
  防御力: 0.0
  穿透率: 0.75
  冲击力: 0.0
  暴击率: 0.0
  暴击伤害: 0.0
  物理伤害加成: 0.0
  以太伤害加成: 1.0
  火属性伤害加成: 0.0
  冰属性伤害加成: 0.0
  电属性伤害加成: 0.0
  异常掌控: 1.0
  异常精通: 1.0
  能量自动回复: 0.0
  小攻击: 0.25
  小生命: 0.0
  小防御: 0.0
  穿透值: 0.25
```

其中代理人类型映射(src\zzz_od\game_data\agent.py):
```python
class AgentTypeEnum(Enum):

    ATTACK = '强攻'
    STUN = '击破'
    SUPPORT = '支援'
    DEFENSE = '防护'
    ANOMALY = '异常'
    RUPTURE = '命破'
    UNKNOWN = '未知'
```

其中代理人伤害类型映射(src\zzz_od\game_data\agent.py):
```python
class DmgTypeEnum(Enum):

    ELECTRIC = '电属性'
    ETHER = '以太'
    PHYSICAL = '物理'
    FIRE = '火属性'
    ICE = '冰属性'
    UNKNOWN = '未知'
```

驱动盘
```yml
set_name: "沧浪行歌" #驱动盘名称
mission_type_name: "诡步与重壁" #任务类型名称
code: canglang_song #驱动盘代码
```
音擎
```yml
weapon_name: 「灰烬」-钴蓝 #音擎名称
rarity: B #音擎稀有度
code: "[Cinder] Cobalt" #音擎代码
```

>注:在编辑时如果遇到了yml解析的问题,可使用""包裹


## 关于运维
可通过python爬虫脚本来实现






