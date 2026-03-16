# AIO Server 前端（Frontend）

本目录是 **AIO Server** 的 Web 前端项目，负责为后端提供的各类功能（博客、账本、币种对比、账号系统、自行车管理、图库等）提供统一的网页界面。

- **对应后端能力**（参考仓库根目录 `README` 中的功能）：
  - **Blogs**：博客列表展示、详情查看，后续支持登录后的私有编辑与评论。
  - **Ledger**：账单上传、解析结果展示、规则配置结果可视化。
  - **Bank Currency Comparing**：多银行汇率对比页面、历史数据图表展示。
  - **Account Management System**：注册登录、2FA、Passkey 登录等相关界面。
  - **Bike Management System**：自行车保养记录、骑行记录的录入和统计展示。
  - **Gallery**：动漫图片展示页面。

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

## 目录结构（简要）

- `src/`
  - `main.js`：应用入口。
  - `router/`：前端路由配置（后续可在此新增各功能模块的页面）。
  - `stores/`：Pinia 全局状态（如用户信息、账本数据等）。
  - `views/`：页面级组件（首页、关于页等，将来可扩展为 Blogs / Ledger / Gallery 等页面）。
  - `components/`：通用组件与 UI 组件。
- `public/`：静态资源（如 `favicon.ico`）。

后续可以根据根项目的模块划分，在 `views/` 下增加：

- `views/blogs/*`
- `views/ledger/*`
- `views/currency/*`
- `views/account/*`
- `views/bike/*`
- `views/gallery/*`

---

## 本地开发

在 `Frontend` 目录下执行以下命令。

### 安装依赖

```sh
npm install
```

### 启动开发服务器（带热更新）

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

## 测试与质量检查

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

## 与整个 AIO Server 的关系

- 本前端项目是 **AIO Server** 的 UI 层，建议与后端共同部署在同一域名下（例如 `api.example.com` 提供接口，`www.example.com` 提供前端页面，或通过 Nginx 反向代理统一入口）。
- 根仓库 `README` 中出现的各个业务模块（Blogs / Ledger / Bank Currency / Account / Bike / Gallery 等），都应对应到前端的页面路由与交互逻辑中。
- 后续在实现具体模块时，可以在本 README 中继续补充：
  - 接口约定（与后端的 API 路径、请求 / 响应格式）。
  - 页面截图或交互流程说明。
  - 权限控制（哪些页面需要登录、哪些功能需要 2FA / Passkey 等）。
