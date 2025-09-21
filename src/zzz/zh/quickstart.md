---
lang: zh-CN
title: 绝区零 一条龙 快速开始
---

::: important

请确保你使用的是最新版本安装包, 否则可能出现兼容性问题.
- [点此确认安装包最新版本](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon/releases)
- [点此确认代码最新版本](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon/commits/main/)

:::

## 环境检查/准备

### 硬件

建议使用较新的电脑运行, 我们的软件基于AI运行,依赖较新的硬件支持.

为什么?👇
<details>

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

有社区案例表明可以在插入VR眼镜后的 运行windows系统的Steam Deck 上运行. 但是请注意，Steam Deck 并非完美支持，可能存在一些兼容性问题.

如果你发现了新的兼容硬件不在上述清单中, [欢迎分享](https://pd.qq.com/g/onedrag00n?subc=716388285)
</details>

### 操作系统

- 运行较新的Windows 10/11 64位系统.
  - 打开你的windows update, 确认升级到最新版本.


### 网络

> 你可以先跳过这个步骤, 运行失败的时候再回来看看

通过下方详情中链接确认连通性.每个大类至少要有一个联通.
如果都不通, 尝试使用手机热点或其他方式.

<details>

- 代码源
  - [Github](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon)
  - [Gitee](https://gitee.com/OneDragon-Anything/ZenlessZoneZero-OneDragon)
- PIP源
  - [官方pip源](https://pypi.org/project/pip/)
  - [清华pip镜像源](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)
  - [阿里云pip镜像源](https://mirrors.aliyun.com/pypi/)

</details>

## 下载

<a id="download-package"></a>

你可以在以下位置下载到一条龙最新的安装包
- [GitHub 的 Release 页面](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon/releases)
- [Mirror酱](https://mirrorchyan.com/zh/projects?rid=ZZZ-OneDragon&source=zzzgh-release) 需要 Mirror CDK（不免费但是可以支持开发者的开发）
- 我们的[官方频道](https://pd.qq.com/g/onedrag00n)
- 或前往[频道关联群聊](https://pd.qq.com/g/onedrag00n)

推荐下载带有 `-Full-Environment` 的超完整包来避免网络环境导致的安装失败
Mirror源默认下载的就是这个包

<details>
源码下载, 仅适用高级玩家

```bash
git clone https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon.git
```
</details>

## 安装

在某个**固态磁盘**的根目录创建一个全英文的空文件夹, 然后再开始我们的安装过程.例如

```bash
D:\ZZZ-OD
```

<details>

1. 不要放在非英文字符路径下
   1. 例如 "C:\用户\你的名字\..." 这种路径会导致python环境无法创建
   2. 或者 "D:\英文\one-dragon\...", 也不可以
2. 不要包含空格
   1. 可能会导致路径解析错误
3. 不要使用过长的路径名
   1. 例如"C:\THISPATHISWAYTOOOOOOOOOOOOOOOOOOOOOOOOOOOOLONG\..." 会导致路径解析错误
4. 一定要使用固态硬盘
   1. 用机械硬盘不是不能用, 但是凹深渊总是少几千分的话...
5. 如果你没有D盘, 那你就用C盘吧

还有一些其他的奇怪情况, 无法穷举, 请务必按照上述要求创建路径
</details>

### 使用安装器安装（推荐）

> 此处教程以 `2.1.1-beta1` 版本的 `Full-Environment` 的完整包为基准

1. 解压缩安装包到刚才创建的路径
   1. ![folder_overview](./quickstart/folder_overview.png)

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
> 启动失败请参考：[常见问题](faq.md) 或 [热门问题文档](https://docs.qq.com/doc/p/7add96a4600d363b75d2df83bb2635a7c6a969b5)
> 安装完成后，请参照[必要设置](./docs/config.md)进行游戏和脚本的基础配置
> 高级启动参数请参考[启动参数](#高级启动参数)

---

- ### 手动安装步骤（高级）

<details>

高级玩家废话少说

```bash
git clone https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon.git
cd ZenlessZoneZero-OneDragon
pip install -r requirements-prod.txt
pip install -r requirements-gamepad.txt
# 启动游戏
./onedragon-launcher.exe
```

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
  > https://gh.dpik.top/
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