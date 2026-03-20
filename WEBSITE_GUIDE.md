# Hugo Blowfish 个人网站修改指南

本指南将帮助你如何自定义你的个人网站。

---

## 目录
1. [修改主题颜色和样式](#1-修改主题颜色和样式)
2. [添加更多内容页面](#2-添加更多内容页面)
3. [部署更新](#3-部署更新)

---

## 1. 修改主题颜色和样式

### 1.1 修改颜色方案

打开文件 `config/params.toml`，找到以下行：

```toml
colorScheme = "blowfish"
```

可用的颜色方案：
- `blowfish` - 默认蓝色
- `fire` - 火焰红
- `ocean` - 海洋蓝
- `forest` - 森林绿
- `avocado` - 牛油果绿
- `serenade` - 浅色柔和
- `twilight` - 黄昏紫

示例：
```toml
colorScheme = "ocean"
```

### 1.2 修改默认外观（亮色/暗色）

```toml
defaultAppearance = "light"   # 改为 "dark" 就是暗色主题
autoSwitchAppearance = true   # 允许用户切换明暗
```

### 1.3 修改首页布局

在 `config/params.toml` 中找到：

```toml
[homepage]
  layout = "profile"  # 可选: page, profile, hero, card, background, custom
```

可选布局说明：
- `profile` - 个人资料卡片（当前使用）
- `hero` - 大图英雄区域
- `card` - 卡片式布局
- `page` - 普通页面
- `background` - 背景图

### 1.4 修改头部样式

```toml
[header]
  layout = "basic"  # 可选: basic, fixed, fixed-fill, fixed-gradient, fixed-fill-blur
```

---

## 2. 添加更多内容页面

### 2.1 创建新页面

在 `content` 文件夹中创建新文件夹，例如：

```
content/
  posts/           # 博客文章
    first-post.md  # 第一篇博客
  projects/        # 项目展示
    my-project.md  # 项目页面
  about.md         # 关于页面
```

### 2.2 页面文件格式

创建一个简单的页面 `content/about.md`：

```markdown
---
title: "关于我"
description: "这是关于我的页面"
---

# 关于我

你好！我叫 Hongnan，是一名软件工程师。

## 我的经历

- 2020年：开始学习编程
- 2024年：毕业于某某大学
- 现在：从事软件开发

## 联系我

如果你想联系我，可以发送邮件到 myemail@example.com
```

### 2.3 创建博客文章

创建 `content/posts/my-first-post.md`：

```markdown
---
title: "我的第一篇博客"
date: 2024-01-01
description: "这是我博客的第一篇文章"
tags: ["个人", "你好世界"]
categories: ["随笔"]
draft: false
---

# 我的第一篇博客

这是博客的正文内容...

## 小标题

更多内容...
```

### 2.4 添加图片

1. 将图片放入 `static/images/` 文件夹
2. 在 Markdown 中引用：

```markdown
![图片描述](/images/my-photo.jpg)
```

---

## 3. 部署更新

每次修改完配置或内容后，需要重新部署到 GitHub：

### 步骤 1：推送源代码到 main 分支

```powershell
cd C:\Users\ASUS\Hongnan
git add .
git commit -m "更新网站内容"
git push origin main
```

### 步骤 2：构建并部署到 gh-pages

```powershell
# 构建网站
hugo

# 进入 public 目录
cd public

# 提交并推送
git add .
git commit -m "Deploy updated site"
git push origin gh-pages --force
```

### 步骤 3：等待部署

约 1-2 分钟后，访问 https://chndaz.github.io/PersonalWebsite/ 查看更新

---

## 常用配置参考

### 修改个人信息

编辑 `config/languages.en.toml`：

```toml
[params.author]
  name = "你的名字"
  email = "your@email.com"
  headline = "职业头衔"
  bio = "个人简介"

  # 添加社交链接
  links = [
    { github = "https://github.com/你的用户名" },
    { linkedin = "https://linkedin.com/in/你的用户名" },
    { twitter = "https://twitter.com/你的用户名" }
  ]
```

### 修改网站标题

在 `config/languages.en.toml` 中修改：

```toml
title = "你的网站标题"
```

### 添加菜单链接

编辑 `config/menus.en.toml`：

```toml
[[main]]
  name = "博客"
  pageRef = "posts"
  weight = 1

[[main]]
  name = "关于"
  pageRef = "about"
  weight = 2

[[main]]
  name = "项目"
  pageRef = "projects"
  weight = 3
```

---

## 常见问题

### Q: 如何本地预览修改？
A: 运行 `hugo server -D`，然后访问 http://localhost:1313

### Q: 如何查看所有可用的配置选项？
A: 访问 https://blowfish.page/docs/configuration/

### Q: 为什么修改后网站没有变化？
A: 确保你执行了 `git push origin gh-pages --force` 强制推送到 gh-pages 分支

---

## 相关链接

- Hugo 官网: https://gohugo.io
- Blowfish 主题文档: https://blowfish.page
- GitHub: https://github.com/chndaz/PersonalWebsite

---

*最后更新: 2024年3月20*
