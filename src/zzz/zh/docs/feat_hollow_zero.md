---
lang: zh-CN
title: 功能-零号空洞-枯萎之都
---

## 0.前置须知

### 事件无响应

遇到卡死时可以使用脚本的F11截图反馈到群里，截图应该包含具体的选项，截图保存在 `.debug/images` 文件夹中。

### 运行后不进入空洞

通常是完成了每周基础次数，而且没有设置额外刷取任务。

也有可能是脚本识别错误，任务2层出现了灰色的业绩点（已领取完的状态），如果是这种，可以点击重置记录，然后在你下一次进入时在2层使用F11截图上传反馈。

### 继续运行

脚本拥有继续运行的能力，在空洞中卡死，自行调整后，可按F9启动继续运行，无需退出。

### 棋盘加速

游戏内「设置」-「其他」-「记录棋盘加速设置」选择「开启」，第一次进入空洞后手动选择一次加速。可以让后续刷空洞稍微快一点。


## 1.配置

### 1.1.功能性配置

- 每周基础次数 - 就是需要完整通关多少次，用于完成委托任务。每周重置。完成后需要配置刷业绩点才会继续挑战。
- 额外刷取 - 在完成指定通关次数后，可继续进行刷取，获取完整奖励。<span style="color:red"><strong>不配置时，完成基础次数后不再进入空洞！！！</strong></span>
- 额外刷取方式 - 根据自身练度，配合速通寻路方式，决定在那一层后退出，自行找一种刷取最快的方式。
- 每天进入次数 - <span style="color:red"><strong>必须要大于0；</strong></span>如果你想一次性刷完，可以设置99；如果你想在将空洞运行均摊到每日运行，可以设置5或者10。

### 1.2.挑战配置

挑战空洞前，需要配置，配置文件存放在 `config/hollow_zero_challenge`。

脚本的默认配置无法修改，你可以复制后自行修改。

#### 1.2.1.配置名称

就是文件名称，用于显示，无特殊作用。

#### 1.2.2.目标配队

由于自动战斗的配置文件可能对组队的位置有要求，这里请按照你使用的自动战斗配置所需选择。

选择后，游戏中进入空洞时的角色选择可以大于3个（只要你的自动战斗配置能支持你选择的角色），从而获取代理人离队的鸣徽奖励。

请注意，角色位置是可以顺移的，即 `鲨鱼+狼+苍角` `狼+苍角+鲨鱼` `苍角+鲨鱼+狼` 都是等价的。

#### 1.2.3.自动战斗

空洞内，自动战斗使用的配置文件。具体见 [功能-战斗助手](feat_battle_assistant.md)

#### 1.2.4.寻路方式

空洞内，走格子的方式。

|配置名称|一步可达时前往|优先途经点|避免途经点|
|---|---|---|---|
|默认|大部分非战斗的有奖励的节点都会前往|呼叫增援, 业绩考察点, 零号银行, 邦布商人, 诡雾|战斗节点|
|速通|无|呼叫增援, 业绩考察点|战斗节点|

支持自定义，可以根据自身练度和需求填写。填写内容为每行一个格子类型，格子类型可以参考 [米游社](https://baike.mihoyo.com/zzz/wiki/channel/map/6/8) 或者游戏内的 __事件图鉴__

说明
- 一步可达时前往 - 就是点一下就能去到的位置，每次寻路时，优先考虑这些节点，适合去一些奖励节点。例如 `齿轮硬币箱`, `安全区`, `休息区` 等。
- 优先途经点 - 一步可达的没有匹配时，看地图上有没有优先途经点，有的话，会先以最短路径的方式前往，适合填一些认为必须要去的节点。例如 `呼叫增援`, `业绩考察点`, `零号银行` 等。
- 避免途经点 - 在寻路时，都会先考虑避免这些类型的格子去找路径，适合填一些不想经过的点。例如 `危机`, `双重危机`, `限时战斗` 等。由于空洞内战斗是有可能出现寻路失败，建议是把战斗节点都写上。这有可能导致绕路，自行权衡决定。
- 脚本默认会朝最终目标点走，此部分不需要配置。

#### 1.2.5.奖励优先级

鸣徽、邦布等都写在这，运行过程中会按顺序选择。如果游戏中的选项没有命中优先级的，那么按等级 SABC 来选取。

优先级每行填写一个，填写方式有两种：

- 填写分类，例如 `以太`, `冻结`。这个说明优先选择这个分类，多个选项属于同个分类时，按等级 SABC 来选取。
- 填写具体内容，以 `分类` + `空格` + `名称` 表述。例如 `邦布 以太布`。
