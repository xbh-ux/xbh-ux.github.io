---
title: Ceph学习
date: 2026-08-17
draft: false
tags:
  - 学习
categories: []
---
ceph是一个集群式分布式存储管理器，可以将ceph视为一个用于存储数据并利用网络确保数据有备份副本的计算机程序

# ceph组件
## ceph-mon
集群的大脑，负责维护整个集群的状态地图
## ceph-mgr
集群的管家，复制跟踪集群的运行时指标
## ceph-osd
集群的执行者，这是最核心的存储服务进程，负责实际存储所有用户数据
## ceph-mds
cephFS的目录管理员，存储和管理ceph文件系统的元数据
## ceph-radosgw
对象存储网关。
