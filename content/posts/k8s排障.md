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
NAME      STATUS   ROLES           AGE   VERSION    LABELS
master    Ready    control-plane   20d   v1.32.13   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=master,kubernetes.io/os=linux,node-role.kubernetes.io/control-plane=,node.kubernetes.io/exclude-from-external-load-balancers=
worker1   Ready    <none>          20d   v1.32.13   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=worker1,kubernetes.io/os=linux
worker2   Ready    <none>          20d   v1.32.13   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=worker2,kubernetes.io/os=linux

并没有这个disktype这个标签，所有3个节点都无法创建pod
```

## 2.DNS解析失败
```bash
1.查看节点状态
kubectl get node -o wide

2.查看pod详细信息
kubectl describe pods

3.报错信息
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  100s  default-scheduler  Successfully assigned default/dns-failure-pod to worker1
  Normal  Pulling    100s  kubelet            Pulling image "busybox"
  Normal  Pulled     99s   kubelet            Successfully pulled image "busybox" in 776ms (776ms including waiting). Image size: 2236931 bytes.
  Normal  Created    99s   kubelet            Created container: dns-test
  Normal  Started    99s   kubelet            Started container dns-test


```
