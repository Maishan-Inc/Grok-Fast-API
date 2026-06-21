# Grok Fast API

OpenAI / Anthropic compatible Grok API gateway with Admin panel and WebUI.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FMaishan-Inc%2FGrok-Fast-API)

[前往 Aiven 申请 PostgreSQL 数据库](https://aiven.io/)

## Vercel 部署

1. 点击上方 **Deploy with Vercel**。
2. 前往 Aiven 创建 PostgreSQL 数据库。
3. 在 Aiven 控制台复制 PostgreSQL Service URI。
4. 下载 Aiven 的 `ca.pem` 证书。
5. 在 Vercel 项目环境变量中填写下面两个变量。
6. 部署完成后访问 `/admin/login`。

默认 Admin 密码：

```text
grok2api
```

## 环境变量

| 变量名 | 说明 |
| :-- | :-- |
| `ACCOUNT_STORAGE` | 存储后端，默认 `postgresql` |
| `ACCOUNT_POSTGRESQL_URL` | Aiven PostgreSQL 连接串，建议包含 `sslmode=verify-full` |
| `AIVEN_CA_CERT` | Aiven `ca.pem` 完整内容 |
| `GROK_APP_APP_KEY` |后台密码 如果出现修改密码后无法登录 请使用此环境变量强制修改密码 |
| `GROK_APP_API_KEY` | API密钥 如果出现修改密钥无法使用 请使用此环境变量强制修改密钥 |


示例：

```env
ACCOUNT_STORAGE=postgresql
ACCOUNT_POSTGRESQL_URL=postgresql://avnadmin:password@host.aivencloud.com:12345/defaultdb?sslmode=verify-full
AIVEN_CA_CERT=-----BEGIN CERTIFICATE-----
...
-----END CERTIFICATE-----
```

<<<<<<< HEAD
后台配置会写入 PostgreSQL 的 `config_store` 表；`GROK_*` 环境变量仍然拥有最高优先级，例如 `GROK_APP_APP_KEY` 会强制覆盖后台密码。

不要把真实数据库密码或证书提交到 Git 仓库。
=======
[linux do](https://linux.do)
>>>>>>> d7d38aff6f3b8f270dee9d3a2826fc19cb16dccf
