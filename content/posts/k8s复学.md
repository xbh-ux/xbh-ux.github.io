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
#### pod
```bash
pod其实包含三种容器类型：
	- 基础架构容器
	- 初始化容器
	- 业务容器
启动顺序依次是：基础架构容器、初始化容器、业务容器
```
##### 响应式管理pod
```bash
kubectl run
kubectl scale
kubectl delete
等这些
```
##### 声明式管理pod
```bash
kubectl apply -f 资源清单
```
#### Deployment
```bash
deployment是k8s中用于管理应用（pod）的控制器，用于部署和管理无状态应用
```
#### Replicaset
```bash
副本集，负责确保集群中始终运行指定数量的pod副本，是edployment实现滚动更新、回滚和版本管理的基础组件
```
#### Statefulset
```bash
缩写sts，管理有状态应用，为pod提供稳定的网络标识和持久化存储
```
#### Daemonset
```bash
是k8s的控制器，确保集群中等每个节点上都运行一个特定的pod
```
#### job
```bash
负责运行一次性的批处理任务，确保任务成功完成
```
#### Cronjob
```bash
基于时间调度运行job，实现周期性任务
```
#### Namespace
```bash
命名空间，在k8s集群中的虚拟隔离分区，用于将集群资源（如pod、service、deployment、pve等）划分为不同的逻辑组
```
### 网络访问类

#### Service-给pod提供稳定访问地址

#### Ingress-http/https七层路由

#### IngressClass-指定由那个Ingress Controller处理

#### networkPolicy-限制pod之间的网络访问

#### EndpointSlice-记录Service后端pod地址

### 配置和敏感信息类

#### ConfigMap-保存普通配置

#### secret-保存密码、token、证书等敏感信息

### 存储类

#### Volume-pod内挂载存储

#### PersistentVolume（PV）-集群中的实际存储资源

#### PersistentVolumeClaim（PVC）-应用申请存储

#### StorageClass-定义动态创建存储方式

#### CSI-存储插件接口

### 资源调度和限制

#### ResourceQuota-限制Namespace总资源

#### LimitRange-设置容器默认/最大资源

#### PriorityClass-设置Pod优先级

#### Resource Request-调度时预留资源

#### Resource Limit-限制最大使用量

#### NodeSelector-指定节点标签

#### Affinity/Anti-Affinity-控制pod调度关系

#### Taint/Toleration-控制节点是否允许pod调度

### 自动扩缩容和发布

#### HorizontalPodAutoscaler(HPA)-根据指标括缩Pod

#### VerticalPodAutoscale(VPA)-自动调整cpu/内存建议

#### PodDisruptionBudget（PDB）-保证维护期间最低可用副本

#### Lease-租约和选主机制

### 权限和安全
#### ServicAccount-pod使用的身份
#### Role-Namespace内权限

#### ClusterRole-集群级权限

#### RoleBinding-绑定Namespace权限

#### ClusterRoleBinding-绑定集群权限

#### PodSecurity-Pod安全控制

#### NetworkPolicy-网络隔离

### 集群和节点级资源
#### Node-工作节点
#### ClusterRole-集群级权限

#### CustomResourceDefintion（CRD）-扩展k8s api

#### Operator-通过控制器自动管理复杂应用

#### Event-记录调度、启动、失败等事件
