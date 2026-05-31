---
lang: zh-CN
title: 千机链
date: 2026-05-31
---

## 0.简介

[千机链](https://github.com/OneDragon-Anything/OneDragon-ScriptChainer) 是一个脚本链式调用工具，用来把多个自动化脚本按顺序编排到同一个脚本链中运行。

千机链负责启动脚本、等待指定的完成条件、按需清理进程，并可推送开始/结束通知和运行日志。脚本自身仍需要能完成自己的日常流程，例如唤起游戏、执行任务、在结束时关闭游戏或退出脚本。

## 1.安装方式

从 [GitHub](https://github.com/OneDragon-Anything/OneDragon-ScriptChainer/releases) 下载最新的 `OneDragon-ScriptChainer-vX.Y.Z.zip`，解压到任意目录即可使用。

[点击此处查看访问GitHub和下载加速的帮助](../../other/zh/visit_github.md)

压缩包内主要有两个入口：

- `OneDragon ScriptChainer.exe` - 统一入口。双击打开配置界面；加上 `-o` 或 `--onedragon` 参数后直接运行脚本链。
- `OneDragon ScriptChainer Runner.exe` - 独立运行器，不打开配置界面，适合快捷方式或 Windows 任务计划程序调用。

程序需要管理员权限运行；如果弹出 UAC 确认窗口，请选择允许。

## 2.配置编辑

1. 运行 `OneDragon ScriptChainer.exe`。
2. 在 `脚本链` 页面新建、重命名、删除脚本链。新建时默认按 `01`、`02` 递增命名；重命名后，运行参数中的 `--chain` 需要填写新的完整名称。
3. 点击 `新增脚本`，选择 `外部程序`、`新建 Python 脚本` 或 `选择已有 Python 脚本`。
4. 在列表中拖拽脚本卡片可以调整运行顺序；卡片右侧开关可以临时禁用脚本；播放按钮可以调试运行当前脚本或当前脚本链。

### 2.1.脚本类型

- 外部程序 - 运行已有的 exe、bat 或其他可执行入口，并通过进程状态判断是否完成。
- Python 脚本 - 由千机链直接执行 `.py` 文件，可作为独立步骤，也可挂靠到相邻外部程序前后运行。

### 2.2.外部程序配置说明

- 脚本路径 - 选择需要启动的 exe、bat 或其他可执行文件。
- 脚本进程名称 - 需要监听脚本是否关闭，或需要结束后关闭脚本进程时填写。可以选择预设，也可以手动输入进程名。
- 游戏进程名称 - 需要监听游戏是否关闭，或需要结束后关闭游戏进程时填写。可以选择预设，也可以手动输入进程名。
- 运行超时(秒) - 为避免脚本异常卡死，必须设置为大于 0 的秒数。超时后千机链会进入清理和下一步。
- 检查完成方式 - 可选择 `游戏被关闭`、`脚本被关闭`、`游戏或脚本被关闭`。
- 结束后关闭脚本进程 - 关闭千机链本次启动并追踪到的脚本进程及其子进程。
- 结束后关闭游戏进程 - 按游戏进程名称尝试关闭游戏进程。
- 脚本启动参数 - 启动脚本时传入的命令行参数，多个参数用空格分隔。
- 脚本开始/结束通知 - 运行到该脚本时按配置发送通知。
- 定时推送运行日志 - 按设定间隔把命令行输出合并推送。间隔单位为分钟。

> 如何查看进程名称？
>
> 任务管理器 -> 进程 -> 选择目标进程右键（部分程序需要展开后选择子进程右键）-> 转到详细信息 -> 右键属性复制名称。

### 2.3.Python 脚本配置说明

- `新建 Python 脚本` 会创建一个由千机链管理的 `.py` 文件，并可在内置编辑器中修改。
- `选择已有 Python 脚本` 会引用外部 `.py` 文件，编辑时会调用系统外部编辑器。
- Python 脚本在千机链运行器进程内执行，命令行输出会显示在运行窗口中，并可被宿主脚本的日志推送收集。
- 点击 Python 脚本卡片上的向上箭头，会将它挂靠到上方脚本，作为上方脚本的后置脚本。
- 点击 Python 脚本卡片上的向下箭头，会将它挂靠到下方脚本，作为下方脚本的前置脚本。

### 2.4.运行逻辑说明

1. 千机链按脚本列表顺序运行启用的脚本；被禁用的脚本会跳过。
2. 挂靠到外部程序的 Python 脚本会与宿主脚本组成运行组：前置 Python 脚本先运行，宿主脚本再运行，后置 Python 脚本最后运行。
3. 外部程序启动后，千机链会等待所选的完成条件成立。只有目标进程曾经出现过并随后关闭，才会被视为完成。
4. 单个运行组完成后，千机链会按配置清理脚本进程和游戏进程，再等待 10 秒进入下一个运行组。
5. 全部运行结束后，如果运行参数包含关机选项，则按指定延迟执行关机。

## 3.常见脚本配置

### 3.1.内置预设清单

千机链当前在下拉框中内置了下列常见工具和游戏进程，点击名称可跳转到对应配置示例。内置预设只代表进程名可以直接选择，脚本路径和启动参数仍以对应工具自身安装目录及文档为准。

| 脚本进程名称 | 脚本实际进程名 | 游戏进程名称 | 游戏实际进程名 |
| --- | --- | --- | --- |
| [一条龙](#script-chainer-zzz-od) / [一条龙-集成](#script-chainer-zzz-od) | `python.exe` / `OneDragon-RuntimeLauncher.exe` | [绝区零](#script-chainer-zzz-od) | `ZenlessZoneZero.exe` |
| [BetterGI](#script-chainer-bettergi) | `BetterGI.exe` | [原神](#script-chainer-bettergi) / [原神 · 国际服](#script-chainer-bettergi) | `YuanShen.exe` / `GenshinImpact.exe` |
| [三月七小助手](#script-chainer-march7th) | `March7th Assistant.exe` | [崩坏：星穹铁道](#script-chainer-march7th) | `StarRail.exe` |
| [StarRailAssistant](#script-chainer-sra) | `SRA.exe` | [崩坏：星穹铁道](#script-chainer-sra) | `StarRail.exe` |
| [识宝小助手](#script-chainer-bh3) | `MFAAvalonia.exe` | [崩坏3](#script-chainer-bh3) | `BH3.exe` |
| [MaaEnd](#script-chainer-maaend) | `MaaEnd.exe` | [终末地](#script-chainer-maaend) | `Endfield.exe` |
| [MaaGF2Exilium](#script-chainer-maagf2) | `MaaGF2Exilium.exe` | [MUMU模拟器](#script-chainer-maagf2) | `MuMuNxDevice.exe` |

> 表中的实际进程名是千机链用于监听完成条件和清理进程的目标，不一定等同于 `脚本路径` 选择的启动文件。

<a id="script-chainer-zzz-od"></a>

### 3.2.绝区零 | 一条龙

普通启动器：

- 脚本路径 - 选择 `OneDragon-Launcher.exe`。
- 脚本进程名称 - 选择 `一条龙`。
- 游戏进程名称 - 选择 `绝区零`。
- 脚本启动参数 - 填入 `-o -c`，表示直接运行一条龙并在结束后关闭游戏。

这里的 `一条龙` 下拉项对应 `python.exe`，是为了监听普通启动器拉起的一条龙运行进程；`脚本路径` 仍然选择 `OneDragon-Launcher.exe`。

集成启动器：

- 脚本路径 - 选择 `OneDragon-RuntimeLauncher.exe`。
- 脚本进程名称 - 选择 `一条龙-集成`。
- 游戏进程名称、脚本启动参数同上。

<a id="script-chainer-march7th"></a>

### 3.3.崩坏：星穹铁道 | 三月七小助手

- 脚本路径 - 选择 `March7th Assistant.exe`。
- 脚本进程名称 - 选择 `三月七小助手`。
- 游戏进程名称 - 选择 `崩坏：星穹铁道`。
- 脚本启动参数 - 按三月七小助手自身需要填写；不需要时留空。

<a id="script-chainer-sra"></a>

### 3.4.崩坏：星穹铁道 | StarRailAssistant

- 使用前先运行 `SRA.exe` 完成 SRA 自身的任务配置。
- 脚本路径 - 选择 SRA 解压目录中的 `SRA.exe`。
- 脚本进程名称 - 选择 `StarRailAssistant`。
- 游戏进程名称 - 选择 `崩坏：星穹铁道`。
- 脚本启动参数 - 填入 `-e run Default + exit`，把 `Default` 换成实际配置名。`run` 会阻塞运行指定配置，完成后执行 `exit` 退出 SRA。

<a id="script-chainer-bettergi"></a>

### 3.5.原神 | BetterGI

- 脚本路径 - 选择 `BetterGI.exe`。
- 脚本进程名称 - 选择 `BetterGI`。
- 游戏进程名称 - 按服务器选择 `原神` 或 `原神 · 国际服`。
- 脚本启动参数 - 填入 `startOneDragon`。

<a id="script-chainer-bh3"></a>

### 3.6.崩坏3 | 识宝小助手

- 脚本路径 - 选择 `MFAAvalonia.exe`。
- 脚本进程名称 - 选择 `识宝小助手`。
- 游戏进程名称 - 选择 `崩坏3`。
- 脚本启动参数 - 按识宝小助手自身需要填写；不需要时留空。

<a id="script-chainer-maaend"></a>

### 3.7.终末地 | MaaEnd

- 脚本路径 - 选择 `MaaEnd.exe`。
- 脚本进程名称 - 选择 `MaaEnd`。
- 游戏进程名称 - 选择 `终末地`。
- 脚本启动参数 - 填入 `--autostart -q`，让 MaaEnd 启动后自动执行，并在结束后自动关闭自身。

<a id="script-chainer-maagf2"></a>

### 3.8.少女前线2：追放 | MaaGF2Exilium

- 脚本路径 - 选择 `MaaGF2Exilium.exe`。
- 脚本进程名称 - 选择 `MaaGF2Exilium`。
- 游戏进程名称 - 如果通过 MuMu 模拟器运行，选择 `MUMU模拟器`；使用其他环境时可手动填写实际游戏或模拟器进程名。
- 脚本启动参数 - 按 MaaGF2Exilium 自身需要填写；不需要时留空。

## 4.运行

### 4.1.在配置界面运行

- 点击脚本链右侧的 `运行全部`，会在终端中启动当前脚本链。
- 点击单个脚本卡片上的播放按钮，会调试运行该脚本。

### 4.2.手动触发

推荐使用统一入口：

1. 右键 `OneDragon ScriptChainer.exe` -> 发送到 -> 桌面快捷方式。
2. 右键桌面快捷方式 -> 属性 -> 目标，在末尾追加参数：` -o --chain 01`。
3. 如果脚本链已经重命名，把 `01` 换成实际脚本链名称。
4. 双击快捷方式运行。

也可以使用独立运行器：

1. 右键 `OneDragon ScriptChainer Runner.exe` -> 发送到 -> 桌面快捷方式。
2. 右键桌面快捷方式 -> 属性 -> 目标，在末尾追加参数：` --chain 01`。
3. 双击快捷方式运行。

### 4.3.定时运行

[参考](../../other/zh/windows_plan.md) 设置 Windows 任务计划程序。

推荐填写方式：

- 程序或脚本 - 选择 `OneDragon ScriptChainer.exe`。
- 添加参数 - 填写 `-o --chain 01`。
- 起始于 - 填写千机链解压目录。

如果使用 `OneDragon ScriptChainer Runner.exe`，则 `添加参数` 填写 `--chain 01`，同样建议填写 `起始于` 为千机链解压目录。

### 4.4.运行参数

`OneDragon ScriptChainer.exe` 是统一入口，无参数时打开配置界面；带 `-o` / `--onedragon` 时直接运行脚本链。

| 参数 | 说明 |
| --- | --- |
| `-o, --onedragon` | 跳过配置界面，直接运行脚本链 |
| `--chain <名称>` | 指定脚本链名称，默认 `01`；仅运行模式使用 |
| `--debug-index <下标>` | 仅调试指定下标脚本，并按挂靠关系一并编排；普通运行不需要填写 |
| `-s, --shutdown [秒数]` | 运行后关机；不填秒数时默认 60 秒；仅运行模式使用 |
| `-v, --version` | 显示版本号 |

`OneDragon ScriptChainer Runner.exe` 是独立运行器，直接运行脚本链，支持：

| 参数 | 说明 |
| --- | --- |
| `--chain <名称>` | 指定脚本链名称，默认 `01` |
| `--debug-index <下标>` | 仅调试指定下标脚本，并按挂靠关系一并编排；普通运行不需要填写 |
| `-s, --shutdown [秒数]` | 运行后关机；不填秒数时默认 60 秒 |

示例：

```shell
"OneDragon ScriptChainer.exe" -o --chain 01
"OneDragon ScriptChainer.exe" -o --chain 01 -s 120
"OneDragon ScriptChainer Runner.exe" --chain 01
"OneDragon ScriptChainer Runner.exe" --chain 01 -s 120
```

## 5.更多

问题反馈请到 [GitHub Issue](https://github.com/OneDragon-Anything/OneDragon-ScriptChainer/issues)。

欢迎提供更多常用脚本的配置方式加入到默认选项中。
