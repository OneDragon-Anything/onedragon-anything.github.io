---
lang: zh-CN
title: 概念说明
---

## Context

运行上下文，用于存储各种配置、运行状态等，并提供与环境的交互能力。

## Operation

操作基类，提供完成一个操作的基本流程实现，当前为同步阻塞型，流程包含

1. 开始前的初始化
3. 完成一个动作后，可根据条件选择下一个动作
4. 失败重试
4. 暂停、继续、完成等钩子

提供基础动作

- 在指定位置匹配文本、模板，并可选点击操作
- 根据画面元素关系建模，自动前往指定页面

注解式编程

## Application

拓展Operation，是一个具体应用的基类，提供

- 运行记录
- 发送推送

## 画面元素建模

待定

## 