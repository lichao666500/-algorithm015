第一周学习笔记

Array

是有限个相同类型的变量所组成的有序集合

内存地址连续
随机访问快O(1) prepend/append/lookup
insert O(n)、delete O(n)
Python中没有数组，通过列表List和元组tuple实现

Link List

物理上非连续、非顺序的数据结构，由若干节点node组成

insert O(1)、delete O(1)
look up O(n)
单向链表、双向链表、循环链表

Skip List

元素有序且添加了索引的链表，

插入/删除/搜索 O(log n)
原理简单
容易实现
方便扩展
只用于元素有序的情况

Stack

先入后出
添加删除O(1)

Queue

先入先出FIFO
添加删除O(1)

Double-End Queue

两端可进出的Queue
添加删除O(1)

Priority Queue

插入操作O(1)
取出操作O(log n)



