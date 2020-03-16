#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/16 下午4:24
#@Author: guangliang
#@File  : Remove_endth_node.py
"""
Given a linked list, remove the n-th node from the end of list and return its head.
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 1
        cur = p = head
        while cur.next:
            size += 1
            cur = cur.next
            if size > n + 1:
                p = p.next
        if size == n:
            return head.next
        else:
            p.next = p.next.next
            return head

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        """
        1、把每个节点按照顺序存储在字典里 2、找到需要删掉的元素在哪个位置 3、需要注意删掉的元素是head 和最后一个元素的情况
        :param head:
        :param n:
        :return:
        """
        d = {}
        p = head
        i = 1
        d[i] = p
        while p.next:
            i += 1
            p = p.next
            d[i] = p
        i -= n
        if i == 0:
            return head.next
        if d[i + 1].next:
            d[i].next = d[i + 1].next
        else:
            d[i].next = None
        return head