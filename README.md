# hm-insurance（安心保）

保险领域 AI Agent 项目，包含后端 Agent 服务、前端商城界面和本地基础设施编排。

## 项目结构

```
hm-insurance/
├── agent-service/          # 后端：FastAPI + LangChain/LangGraph
│   ├── app/
│   │   ├── main.py         # 应用入口
│   │   ├── core/           # 配置、日志
│   │   └── infra/          # 数据库等基础设施连接
│   ├── notebooks/          # 学习与实验笔记
│   ├── pyproject.toml      # 依赖（uv 管理）
│   └── .env.example        # 环境变量模板
├── frontend/               # 前端：React + Vite + TypeScript + Ant Design
├── deploy/                 # docker-compose 编排
│   ├── postgres/           # 初始化脚本
│   └── milvus/             # Milvus 配置
└── .gitignore
```

## 技术栈

| 部分 | 技术 |
| --- | --- |
| 后端 | Python 3.14 / FastAPI / Uvicorn / SQLAlchemy + asyncpg / structlog |
| Agent | LangChain / LangGraph / DeepSeek / Milvus（向量检索） |
| 前端 | React 18 / Vite 6 / TypeScript / Ant Design 5 |
| 基础设施 | PostgreSQL 16 / Milvus 3.0（etcd + MinIO）/ Attu |

## 快速开始

### 1. 启动基础设施

```bash
cd deploy
docker compose up -d
```

启动后可用：

- PostgreSQL：`localhost:5432`（默认库/用户/密码均为 `insurance`）
- Milvus：`localhost:19530`
- Attu（Milvus 可视化）：<http://localhost:3000>

### 2. 后端

```bash
cd agent-service
cp .env.example .env      # 填入自己的数据库密码和 DEEPSEEK_API_KEY
uv sync
uv run uvicorn app.main:app --reload --port 8001
```

### 3. 前端

```bash
cd frontend
npm install
npm run dev
```

## 环境变量

`agent-service/.env` 包含密钥，**不入库**。参考 `.env.example`：

| 变量 | 说明 |
| --- | --- |
| `APP_HOST` / `APP_PORT` | 服务监听地址与端口 |
| `DB_HOST` / `DB_PORT` / `DB_NAME` / `DB_USER` / `DB_PASSWORD` | PostgreSQL 连接信息 |
| `DEEPSEEK_API_KEY` | 大模型 API Key |
| `CHAT_MODEL` | 对话模型名 |
