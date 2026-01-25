# 一条龙主页

本项目为一条龙的官方网站提供支持，基于 [VuePress](https://vuepress.vuejs.org/zh/) 框架。

## 🚀 快速开始

### 如果需要修改文档内容，可直接定位到对应的 Markdown 文件，修改后保存即可。

### 1️⃣ 前置准备

确保你的机器上安装了 [Node.js v20.17.0](https://nodejs.org/dist/v20.17.0/node-v20.17.0-win-x64.zip)，然后运行以下命令安装并激活 pnpm：

```powershell
winget install OpenJS.NodeJS.LTS; corepack enable; corepack prepare pnpm@latest --activate
```

> 执行完后**必须关闭并重新打开 PowerShell 窗口**

### 2️⃣ 安装依赖

```powershell
# 设置淘宝源（可选，加快下载速度）
npm config set registry https://registry.npmmirror.com

# 安装依赖
pnpm install
```

### 3️⃣ 本地运行

```powershell
pnpm docs:dev
```

你会在控制台看到如下内容：

```
✔ Initializing and preparing data - done in 1.09s

  vite v6.3.5 dev server running at:

  ➜  Local:   http://localhost:8080/
  ➜  Network: http://172.23.224.1:8080/
  ➜  Network: http://192.168.2.6:8080/
```

你可以 Ctrl+鼠标左键点击上述地址来预览文档，也可以直接访问 `http://localhost:8080/`

### 4️⃣ 生成静态文件

```powershell
pnpm docs:build
```

静态文件将生成到 `src/.vuepress/dist/` 目录。

### 5️⃣ 预览构建结果

```powershell
pnpm docs:preview
```

### 其他命令

```powershell
# 更新版本
pnpm docs:update-package
```

## 🤝 贡献指南

欢迎贡献你的改进！

1. Fork 本仓库
2. 创建分支：`git checkout -b feature/your-feature`
3. 提交修改：`git commit -m "feat: 添加新功能"`
4. 推送分支：`git push origin feature/your-feature`
5. 创建 Pull Request

## 🎨 资源链接

- [图标库 - FontAwesome](https://fontawesome.com/search?o=r&m=free)
- [VuePress 官方文档](https://vuepress.vuejs.org/zh/)
