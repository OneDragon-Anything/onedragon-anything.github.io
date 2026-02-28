---
lang: zh-CN
title: 绝区零 一条龙 快速开始
---

::: important

请确保你使用的是最新版本安装包，否则可能出现兼容性问题。
- [点此确认安装包最新版本](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon/releases)
- [点此确认代码最新版本](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon/commits/main/)

:::

## 1.环境检查/准备

### 1.1.硬件

建议使用较新的电脑，我们的软件基于AI运行，依赖较新的硬件支持。

<details>

基于绝区零[官方公告](https://zzz.mihoyo.com/news/124528?category=279)，正式开服的机型推荐配置为：

```text
PC端：第十代英特尔酷睿i5，8G内存，英伟达GeForce GTX1660及以上
```

AMD请参考各家天梯图等效换算。

且本脚本需要额外的算力以支持OCR/推理。

E3等更低的配置 算力不够/缺少指令集 无法保证逻辑流畅运行，请优先考虑升级硬件。

有社区案例表明可以在插入VR眼镜后的 [运行windows系统的Steam Deck](https://pd.qq.com/s/1figjk5c9?b=2) 上运行。

~~但是请注意，Steam Deck 并非完美支持，可能存在一些兼容性问题。~~

如果你发现了新的兼容硬件不在上述清单中，欢迎前往[官方频道](https://pd.qq.com/g/onedrag00n?subc=716388285)分享。
</details>

### 1.2.系统

使用较新的Windows 10 64位及以上操作系统。

### 1.3.网络

运行失败的时候，可通过下方详情中链接确认连通性。
> 如果下载最新的 `Full-Environment` 超完整包，其实可以离线安装避免网络环境导致的安装失败。

<details>

每个大类至少要有一个联通，如果都不通，尝试使用手机热点或其他方式。

- 代码源
  - [Github](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon)
  - [Gitee](https://gitee.com/OneDragon-Anything/ZenlessZoneZero-OneDragon)
- PIP源
  - [官方pip源](https://pypi.org/project/pip/)
  - [清华pip镜像源](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)
  - [阿里云pip镜像源](https://mirrors.aliyun.com/pypi/)

</details>

## 2.下载安装/运行

<a id="download-package"></a>
### **使用安装器安装/运行（推荐）**

::: tip

你可以在以下位置下载到一条龙最新的安装包：
- [GitHub 的 Release 页面](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon/releases)（对网络有一定的特殊要求）
- [Mirror酱](https://mirrorchyan.com/zh/projects?rid=ZZZ-OneDragon&source=zzzgh-release) 需要 Mirror CDK（不免费但是可以支持开发者的开发）
- [官方频道](https://pd.qq.com/g/onedrag00n)获取安装包（网盘下载）

:::

- 下载：推荐下载最新的 `-Full-Environment` 的超完整包来避免网络环境导致的安装失败。

> 请使用最新的安装包，此处教程仅以 `2.1.1-beta1` 版本的 `Full-Environment` 的完整包做示范。

![download_zip](quickstart/download_zip.gif)

- 解压：在某个**固态磁盘**的根目录创建一个全英文的空文件夹，并解压缩安装包到刚才创建的路径，例如：

```
D:\ZZZ-OD
```

<details>

1. 不要放在非英文字符路径下。
   - 例如 "C:\用户\你的名字\..." 这种路径会导致python环境无法创建。
   - 或者 "D:\英文\one-dragon\..."，也不可以。
2. 不要包含空格。
   - 可能会导致路径解析错误。
3. 不要使用过长的路径名。
   - 例如"C:\THISPATHISWAYTOOOOOOOOOOOOOOOOOOOOOOOOOOOOLONG\..." 会导致路径解析错误。
4. 一定要使用固态硬盘。
   - 用机械硬盘不是不能用，但是凹深渊总是少几千分的话...
5. 如果你没有D盘，那你就用C盘吧。

还有一些其他的奇怪情况，无法穷举，请务必按照上述要求创建路径。
</details>

  ![folder_overview](./quickstart/folder_overview.png)

- 准备安装：**以管理员身份运行安装器**，等待安装器界面打开。

   ![open_installer](quickstart/open_installer.gif)

- 开始安装：
  - 点击浏览选择路径，默认选择当前解压的文件夹。
  - 选择合适的下载源，`Full-Environment` 包默认已经包含了需要下载的工具，仅需要下载代码。
  - 默认预设了三个配置好的源，如果开加速器/代理软件，请选择海外源并参考下文[代理说明](#代理说明)进行配置。
  - 点击一键安装或自定义安装，按步骤点击下一步，等待配置完成。

   ![use_installer](quickstart/use_installer.gif)

::: tip

UV和Python环境安装这一步文件较多较大，可能需要一定时间下载，请耐心等待下载。

:::

- 清理安装残留（可选）。

`.install` 文件夹内的三个压缩包，在安装成功后可以删除。

- 启动！

安装完成后使用 `OneDragon-Launcher.exe` 即可启动。
> 启动失败请参考：[常见问题](faq.md) 或 [热门问题文档](https://docs.qq.com/doc/p/7add96a4600d363b75d2df83bb2635a7c6a969b5)
> 安装完成后，请参照[必要设置](./config.md)进行游戏和脚本的基础配置。
> 高级启动参数请参考[启动参数](#高级启动参数)。

### **使用源码运行（可选）**

高级玩家可以查看详情使用源码运行 ~~我觉得没必要~~

<details>

1. 安装 uv（如果你有 uv 可以跳过此步骤）

   ```powershell
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. 创建并进入指定目录（以 C:\ 为示例）

   ```powershell
   $targetDir = "C:\"; if (!(Test-Path $targetDir)) { New-Item -ItemType Directory -Path $targetDir -Force }; cd $targetDir
   ```

3. 在该目录下克隆仓库

   ```powershell
   git clone https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon.git
   ```

4. 进入项目文件夹

   ```powershell
   cd ZenlessZoneZero-OneDragon
   ```

5. 同步环境（uv 会自动处理 Python 版本和依赖库）

   ```powershell
   uv sync
   ```

6. 设置临时路径变量

   ```powershell
   $env:PYTHONPATH=".\src"
   ```

7. 启动程序

   ```powershell
   uv run python .\src\zzz_od\gui\app.py
   ```

::: tip

如果第一步运行后提示找不到 uv，请重启 PowerShell 窗口，然后从第 2 步重新开始。

:::

</details>

<a id="代理说明"></a>
## 3. 代理说明

- Github 免费代理，可以加速所有 Github 下载相关步骤（代码同步，环境下载，Python下载）可以在网络上找到很多免费提供加速的服务商。

- 个人代理，适用于拥有自己代理软件的用户，请填写代理软件对应的监听地址。
  > 比如某代理软件默认监听地址为 http://127.0.0.1:7890

- 无，一般不推荐使用，代理软件使用了 pac 模式、代理软件运行在上级路由器和海外的用户可以直接使用此项。

::: tip
  tip：如果使用了个人代理或在其他设备上运行了代理软件，使用镜像站可能会被站点拉黑，此时请切换下载源为官方源。<br>
  tip2：免费的github代理地址推荐。<br>
  > https://github.moeyy.xyz/<br>
  > https://ghfast.top/<br>
  > https://ghfile.geekertao.top/
  > https://gh.dpik.top/
:::

<a id="update-package"></a>
## 4.脚本如何更新

目前版本一条龙默认启用**自动更新**功能，启动器右上角会显示当前代码版本的哈希值。

一条龙包含三个主要部分：

1. 安装器
   - 用于安装一条龙
   - 安装成功后可以删除

2. 运行代码
   - 一条龙的核心部分
   - 会频繁更新
   - 更新方式：
     - <font color="red">每次启动脚本时自动尝试更新</font>
     - <font color="red">点击左下角 `代码同步` 可手动更新</font>

3. 模型文件
   - **一条龙基于图像识别，及时更新识别模型非常重要**
   - 更新方式：
     - 通过 `设置-资源下载` 进行模型选择和更新
     - 模型后的数字表示日期，通常越新越好

## 5.高级启动参数

<a id="高级启动参数"></a>

你可以使用纯命令行来启动`OneDragon-Launcher.exe`并添加参数以获取一些更加便捷的功能。

<details>

- OneDragon 不支持自动启动运行，启动参数可完成 OneDragon 启动后自动运行。
- OneDragon 自带拉起对应游戏的功能，请特别注意在 OneDragon 本体内选择好对应游戏的路径，否则无法拉起对应游戏启动。
- OneDragon 参数也可自行在任务计划程序等填写善用，意图完成 OneDragon 自动启动运行。

```shell
usage: OneDragon-Launcher.exe [-h] [-v] [-o] [-c] [-s [SHUTDOWN]] [-i INSTANCE]

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
```

</details>

启动参数推荐示例（一条龙运行+运行完关游戏）：

```shell
OneDragon-Launcher.exe -o -c
```

![properties_demonstration](quickstart/properties_demonstration.png)