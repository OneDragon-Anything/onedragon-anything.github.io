---
lang: zh-CN
title: 绝区零 一条龙 快速开始
---

::: important

请确保你使用的是最新版本安装包，过时的安装包版本可能产生的问题开发组不予解决

:::

## 环境准备

基于绝区零[官方公告](https://zzz.mihoyo.com/news/124528?category=279), 公测要求支持配置最低为

```bash
PC端：第七代英特尔酷睿i5，8G内存，英伟达GeForce GTX970及以上
```

且本脚本需要额外的算力以支持OCR/推理, 因此本项目运行基本配置为

- 台式机
  - 第八代英特尔酷睿i5及以上
  - 8G内存及以上
  - 英伟达GeForce GTX1060及以上
- 笔记本
  - 第十二代英特尔酷睿i5及以上
  - 8G内存及以上
  - 英伟达GeForce GTX1060及以上

 E3等更低的配置 算力不够/缺少指令集 无法保证逻辑流畅运行,请优先考虑升级硬件. AMD请参考各家天梯图等效换算.

## 安装

脚本请存放在 <span style="color:red"><strong>全英文的路径</strong></span> 下

- ### 下载安装包

你可以在以下位置免费下载到一条龙最新的安装包
> - [github 的 Release 页面](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon/releases) 
> - [Mirror酱](https://mirrorchyan.com/zh/projects?rid=ZZZ-OneDragon&source=zzzgh-release) 需要 Mirror CDK
> - 我们的官方 QQ 群(861603314)

推荐下载带有 `-Full-Environment` 的完整包来避免网络环境导致的安装失败  
Mirror源默认下载的就是这个包

---

- ### 使用安装器安装（推荐）
> 此处教程以 2.1.1版本的 `Full-Environment` 的完整包为基准
> <font color="red">不要放在非英文字符路径下！！不要包含空格！！</font><br>
> <font color="red">不要放在非英文字符路径下！！不要包含空格！！</font><br>
> <font color="red">不要放在非英文字符路径下！！不要包含空格！！</font><br>

- 选择要安装的位置并将文件解压

选择一个安装位置，比如 **D盘的ZZZ-OneDragon文件夹**  
将下载的压缩包内文件解压进去

- 运行安装器

1. 点击浏览选择路径，默认选择当前解压的文件夹
2. 选择合适的下载源，`Full-Environment` 包默认已经包含了需要下载的工具，仅需要下载代码
3. 默认预设了三个配置好的源，如果开加速器/代理软件，请选择海外源并参考下文[代理说明](#代理说明)进行配置
4. 点击一键安装或自定义安装，按步骤点击下一步，等待配置完成

::: tip

UV和Python环境安装这一步文件较多较大，可能需要一定时间下载，请耐心等待下载

:::
- 清理安装残留（可选）

`.install` 文件夹内的三个压缩包，在安装成功后可以删除

- 启动一条龙

安装完成后使用 `OneDragon-Launcher.exe` 即可启动  
> 启动失败的话请参考[常见问题](faq.md) [热门问题文档](https://www.kdocs.cn/l/cbSJUUNotJ3Z)  
> 安装完成后，请参照[必要设置](./docs/config.md)进行游戏和脚本的基础配置  
> 高级启动参数请参考[启动参数](#高级启动参数)  

---

- ### 手动安装步骤（高级）
<details>

咕咕咕咕

</details>

---

## 脚本如何更新

目前版本一条龙默认启用**自动更新**功能，在你启动 `OneDragon-Launcher.exe` 时会尝试一次自动更新  
启动器右上角会显示当前代码版本的哈希值  
可在启动器左下角点击 `代码同步` 功能进行代码的手动更新，或关闭自动更新  
**一条龙是基于图像识别，所以及时更新识别模型非常重要**  
可以通过 `设置-资源下载` 进行模型的选择和更新，模型后面的数字为日期，一般来说越新越好  

---

### 代理说明

#### 代理类型分为 **Github免费代理 个人代理 无**
- Github 免费代理可以加速所有 Github 下载相关步骤（代码同步，环境下载，Python下载）可以在网络上找到很多免费提供加速的服务商  
- 个人代理适用于拥有自己代理软件的用户，请填写代理软件对应的监听地址
> 比如某代理软件默认监听地址为 http://127.0.0.1:7890
- 无 一般不推荐使用，代理软件使用了 pac 模式 代理软件运行在上级路由器 海外 的用户可以直接使用此项

::: tip
  tip：如果使用了个人代理或在其他设备上运行了代理软件，使用镜像站可能会被站点拉黑，此时请切换下载源为官方源<br>
  tip2：免费的github代理地址推荐<br>
  > https://github.moeyy.xyz/<br>
  > https://ghfast.top/<br>
  > https://ghfile.geekertao.top/
::: 

## 高级启动参数
<details>

你可以使用纯命令行来启动`OneDragon-Launcher.exe`并添加参数以获取一些更加便捷的功能

```shell
usage: OneDragon-Launcher.exe [-h] [-v] [-o] [-c] [-s [SHUTDOWN]] [-i INSTANCE] [-a APP]

绝区零 一条龙 启动器

options:
  -h, --help            显示帮助信息
  -v, --version         显示版本号
  -o, --onedragon       一条龙运行
  -c, --close-game      运行后关闭游戏
  -s [SHUTDOWN], --shutdown [SHUTDOWN]
                        运行后关机，可指定延迟秒数，默认60秒
  -i INSTANCE, --instance INSTANCE
                        指定运行的账号实例，多个用英文逗号分隔，如：1,2
  -a APP, --app APP     指定运行的应用，多个用英文逗号分隔
```

</details>