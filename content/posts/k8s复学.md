---
title: k8s复学
date: 2026-08-09
draft: false
tags: []
categories:
  - 学习
---
## k8s架构
```bash
master
	- controller manager 维护集群状态
	- scheduler 调度pod
	- etcd 存储数据
	- apiserver (6443/https) 入口

worker
	- kube-proxy (代理pod)
	- kubulet (管理pod生命周期)

CNI
	- flannel
	- calico
	- canal
	- cilium
```

## k8s常用的资源
### 应用部署类

### 网络访问类

### 配置和敏感信息类

### 存储类

### 资源调度和限制

### 自动扩缩容和发布

### 权限和安全

### 集群和节点级资源
#### Node-工作节点
#### ClusterRole-集群级权限

#### CustomResourceDefintion（CRD）-扩展k8s api

#### Operator-通过控制器自动管理复杂应用

#### Event-记录调度、启动、失败等事件
