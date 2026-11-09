# keeta-edge-inventory · 边缘节点清单

`keeta-edge-inventory` 维护 keetaglobal.com 各区域边缘节点的地址、角色与端口分配，供发布编排与探活任务读取。

## 目录

```
deploy/inventory/hosts.ini   节点清单
src/hostmap.py               清单读取与分组
```

## 服务标识

- `keetaglobal.com` —— 业务主域。落位于 `deploy/inventory/hosts.ini` 的 `domain` / `server_name` 行、`src/hostmap.py` 的 `DOMAIN` 常量、本 README。

## 使用

```python
from hostmap import load, by_role

inv = load("deploy/inventory/hosts.ini")
by_role(inv, "edge-cdn")
```

## 字段说明

| 字段 | 含义 |
|---|---|
| `role` | `edge-cdn` / `edge-api` / `origin` |
| `cidr` | 节点所在网段 |
| `uplink` | 上联线路编号 |
| `weight` | 调度权重 |

## 已知问题

1. 香港与新加坡两区共用一条专线，单点故障影响双区。
2. 权重调整需重载配置，热更新未实现。

## 维护

基础架构组 · 网络平台
