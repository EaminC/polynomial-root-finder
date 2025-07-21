# 部署到 Vercel 指南

## 概述

本指南将帮助您将多项式求根应用部署到 Vercel 平台。

## 前置要求

1. 拥有 GitHub 账户
2. 拥有 Vercel 账户（可以免费注册）
3. 代码已推送到 GitHub 仓库

## 部署步骤

### 1. 准备代码

确保您的代码包含以下文件：

- `app.py` - Flask 主应用
- `templates/index.html` - 前端模板
- `requirements.txt` - Python 依赖
- `vercel.json` - Vercel 配置

### 2. 连接到 Vercel

1. 访问 [vercel.com](https://vercel.com)
2. 使用 GitHub 账户登录
3. 点击 "New Project"

### 3. 导入 GitHub 仓库

1. 在 Vercel 仪表板中，选择 "Import Git Repository"
2. 找到并选择您的 `polynomial-root-finder` 仓库
3. 点击 "Import"

### 4. 配置项目

1. **Framework Preset**: 选择 "Other"
2. **Root Directory**: 保持默认（./）
3. **Build Command**: 留空（Vercel 会自动检测）
4. **Output Directory**: 留空
5. **Install Command**: 留空

### 5. 环境变量（可选）

如果需要，可以设置以下环境变量：

- `FLASK_ENV`: `production`
- `FLASK_DEBUG`: `false`

### 6. 部署

1. 点击 "Deploy"
2. 等待构建完成（通常需要 1-2 分钟）

## 部署后配置

### 自定义域名（可选）

1. 在项目仪表板中，点击 "Settings"
2. 选择 "Domains"
3. 添加您的自定义域名

### 环境变量管理

1. 在项目仪表板中，点击 "Settings"
2. 选择 "Environment Variables"
3. 添加或修改环境变量

## 故障排除

### 常见问题

#### 1. 构建失败

- 检查 `requirements.txt` 是否包含所有依赖
- 确保 `vercel.json` 配置正确
- 查看构建日志获取详细错误信息

#### 2. 应用无法访问

- 检查路由配置是否正确
- 确保 Flask 应用正确导出

#### 3. 静态文件问题

- 确保模板文件路径正确
- 检查文件权限

### 调试技巧

1. 查看 Vercel 构建日志
2. 使用 Vercel CLI 进行本地测试
3. 检查网络请求和响应

## 性能优化

### 1. 缓存策略

- 启用静态文件缓存
- 配置适当的缓存头

### 2. 代码优化

- 压缩静态资源
- 优化 Python 代码

### 3. 监控

- 使用 Vercel Analytics 监控性能
- 设置错误告警

## 更新部署

每次推送到 GitHub 主分支时，Vercel 会自动重新部署。

## 支持

如果遇到问题，可以：

1. 查看 Vercel 文档
2. 检查 GitHub Issues
3. 联系 Vercel 支持

## 相关链接

- [Vercel 文档](https://vercel.com/docs)
- [Flask 部署指南](https://flask.palletsprojects.com/en/2.0.x/deploying/)
- [项目 GitHub 仓库](https://github.com/EaminC/polynomial-root-finder)
