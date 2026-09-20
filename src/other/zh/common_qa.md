---
lang: zh-CN
title: 安装运行常见问题
---

## 1.安装时出错

### 1.1.安装依赖失败

#### 场景1: 日志中出现 `CSIDL_COMMON_APPDATA` 和 `FileNotFoundError: [WinError 2]`

原因：你的系统曾经安装过其它的python环境，可能是python或者anaconda，导致冲突了。

解决方案: (2选1)

- 到windows系统设置的应用中，将旧的python都删掉，然后再安装。
- 参考安装指南，使用自己的anaconda创建环境安装

## 2.运行时出错

### 2.1.动态链接库(DLL)初始化例程失败

安装最新版的 [Microsoft Visual C++](https://aka.ms/vs/17/release/vc_redist.x64.exe)