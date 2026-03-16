## ✨ 项目简介

本目录是 **AIO Server** 的 Web 前端项目，负责为后端提供的各类功能（博客、账本、币种对比、账号系统、自行车管理、图库等）提供统一的网页界面。

一些你可以在这个前端里实现 / 看到的东西：

- **Blogs**：清爽的博客列表、文章阅读页，将来支持登录后的私有编辑 + 评论区。
- **Ledger**：上传账单文件，一键解析成可视化流水表和统计图，适合「记账系」创作者。
- **Bank Currency Comparing**：多银行汇率对比 & 历史曲线，一眼看出哪家更「良心」。
- **Account Management System**：注册 / 登录 / 2FA / Passkey 登录等与安全相关的交互页。
- **Bike Management System**：记录每一次骑行和保养，更适合「骑车也要写前端」的你。
- **Gallery**：展示你的动漫插画、截图或摄影作品，做一个属于自己的「小画廊」。

---

## 🧩 技术栈

本前端使用以下主要技术构建：

- **Vue 3**：渐进式前端框架。
- **Vite 7**：开发构建工具，提供快速热更新。
- **Vue Router 5**：前端路由管理。
- **Pinia 3**：状态管理。
- **Vitest + @vue/test-utils**：单元测试。
- **Playwright**：端到端（E2E）测试。
- **ESLint + Oxlint + Prettier**：代码质量与格式化工具。

Node 版本要求（来自 `package.json`）：

```txt
node: ^20.19.0 || >=22.12.0
```

建议使用 **Node 20 LTS** 或更新版本。

---

## 技术栈

本前端使用以下主要技术构建：

- **Vue 3**：渐进式前端框架。
- **Vite 7**：开发构建工具，提供快速热更新。
- **Vue Router 5**：前端路由管理。
- **Pinia 3**：状态管理。
- **Vitest + @vue/test-utils**：单元测试。
- **Playwright**：端到端（E2E）测试。
- **ESLint + Oxlint + Prettier**：代码质量与格式化工具。

Node 版本要求（来自 `package.json`）：

```txt
node: ^20.19.0 || >=22.12.0
```

建议使用 **Node 20 LTS** 或更新版本。

---

## 📁 目录结构（简要）

```txt
Frontend/
  ├─ src/
  │  ├─ main.js          # 应用入口
  │  ├─ router/          # 路由配置（Blogs / Ledger / Gallery 等页面的入口）
  │  ├─ stores/          # Pinia 全局状态（用户、账本数据等）
  │  ├─ views/           # 页面级组件（首页 / 功能页）
  │  └─ components/      # 通用组件 & UI 组件
  ├─ public/
  │  ├─ favicon.ico
  │  └─ preview-banner.png  # README 顶部展示图（可自定义二次元插画）
  └─ vite.config.js
```

根据根项目的模块划分，推荐在 `views/` 下增加：

- `views/blogs/*`：博客主页、文章详情、编辑器。
- `views/ledger/*`：账单上传页、解析结果页、统计图表页。
- `views/currency/*`：汇率对比页、历史曲线页。
- `views/account/*`：登录、注册、2FA / Passkey 相关设置页。
- `views/bike/*`：保养记录、骑行记录、统计页。
- `views/gallery/*`：插画 / 图片瀑布流、详情大图页。

---

## 🛠 本地开发

在 `Frontend` 目录下执行以下命令。

### 安装依赖

```sh
npm install
```

### 启动开发服务器（带热更新 🔥）

```sh
npm run dev
```

默认会在本机启动一个 Vite 开发服务器（通常是 `http://localhost:5173`），用于本地开发调试。  
当后端服务启动后，可以在 `.env` 或配置文件中设置后端 API 地址，实现前后端联调（根据后续实现补充）。

### 生产构建

```sh
npm run build
```

构建完成后会生成静态资源（默认在 `dist/` 目录），可由后端或任意静态服务器托管。

### 预览生产构建

```sh
npm run preview
```

---

## ✅ 测试与质量检查

### 单元测试（Vitest）

```sh
npm run test:unit
```

### 端到端测试（Playwright）

```sh
# 第一次运行需要安装浏览器
npx playwright install

# 构建后运行 E2E 测试
npm run build
npm run test:e2e
```

你也可以像官方模板那样指定浏览器或某个测试文件，例如：

```sh
npm run test:e2e -- --project=chromium
npm run test:e2e -- tests/example.spec.ts
```

### 代码检查与修复

```sh
# 运行 ESLint + Oxlint 自动修复
npm run lint

# 仅运行 Oxlint
npm run lint:oxlint

# 仅运行 ESLint
npm run lint:eslint

# 使用 Prettier 格式化 src 下的代码
npm run format
```

---

## 🌌 与整个 AIO Server 的关系

- 本前端项目是 **AIO Server** 的 UI 层，建议与后端共同部署在同一域名下（例如 `api.example.com` 提供接口，`www.example.com` 提供前端页面，或通过 Nginx 反向代理统一入口）。
- 根仓库 `README` 中出现的各个业务模块（Blogs / Ledger / Bank Currency / Account / Bike / Gallery 等），都应对应到前端的页面路由与交互逻辑中。
- 如果你是二次元创作者 / 独立开发者，可以在这里做的事情包括：
  - 把自己的 **博客 / 插画 / 账本** 都做成一个完整的「个人数字生活面板」。
  - 结合后端 API，自定义页面风格（例如：主题色、暗色模式、卡片 UI、玻璃拟态等）。
  - 在 `README` 中继续补充：
    - 接口约定（与后端的 API 路径、请求 / 响应格式）。
    - 页面截图或交互流程说明。
    - 权限控制（哪些页面需要登录、哪些功能需要 2FA / Passkey 等）。
