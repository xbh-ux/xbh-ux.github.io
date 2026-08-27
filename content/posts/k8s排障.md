---
title: k8s排障
date: 2026-08-27
draft: false
tags:
  - 学习
categories:
  - k8s
---
# k8s故障场景
## 1.亲和性规则冲突
```bash
1.排查问题
kubectl describe pods 

2.查看evtens字段
Events:
  Type     Reason            Age   From               Message
  ----     ------            ----  ----               -------
  Warning  FailedScheduling  103s  default-scheduler  0/3 nodes are available: 1 node(s) had untolerated taint {node-role.kubernetes.io/control-plane: }, 2 node(s) didn't match Pod's node affinity/selector. preemption: 0/3 nodes are available: 3 Preemption is not helpful for scheduling.
  
  警告  调度失败  103秒前  默认调度器 3个节点均不可用：
  - 一个节点无法容忍的五点（污点键：node-role.kubernetes.io/control-plane)
  - 2个节点不匹配pod的亲和性/选择器
    
抢占调度：0/3个节点可用，抢占对当前调度无帮助

3.查看pod的资源清单
kubectl get pod <pod-name> -o yaml |grep -A 10 "affinity\|nodeSelector"
```

![](../assets/images/Pasted%20image%2020260827212223.png)
```bash
4.查看node节点是否存在disktype这个节点
kubectl get nodes --show-labels
```