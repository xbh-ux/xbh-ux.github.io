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

3.查看pod日志
kubectl logs dns-failure-pod

报错信息
;; connection timed out; no servers could be reached
显示无法到达任何服务器


根据报错信息得到，是容器内部的dns解析问题，进入容器内部查看解析
root@master:~# kubectl exec -it dns-failure-pod -- /bin/sh
/etc # cat /etc/resolv.conf 
nameserver 192.0.2.1

/etc # ping 192.0.2.1
PING 192.0.2.1 (192.0.2.1): 56 data bytes
^C
--- 192.0.2.1 ping statistics ---
5 packets transmitted, 0 packets received, 100% packet loss

ping指向的IP 192.0.2.1 无法ping通

4.查看pod对应的yaml文件
root@master:~# kubectl get pod dns-failure-pod -o yaml

5.根据pod名查看Pod yaml文件对应的位置
root@master:~# grep -r "name: dns-failure-pod" .
./kubernetes-like-a-pro/troubleshoot-kubernetes-like-a-pro/scenarios/dns-resolution-failure/issue.yaml:  name: dns-failure-pod

6.修改pod yaml中192.0.2.1的ip地址，将ip改为对应svc的ip
	查看对应svc的ip
	root@master:~# kubectl get svc -n kube-system |grep dns
kube-dns         ClusterIP   10.96.0.10      <none>        53/UDP,53/TCP,9153/TCP   20d

7.删除pod并新建pod后查看pod日志显示正常
kubectl delete dns-failure-pod
kubectl apply -f 查询到的yaml文件地址

```
