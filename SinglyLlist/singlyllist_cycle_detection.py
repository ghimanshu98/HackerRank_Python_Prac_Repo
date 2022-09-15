#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            pass

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    # using python id() to obtain the address of variable
    id_lst = []
    flag = 0
    temp = head
    if head !=None:
        while(temp.next != None):
            if id(temp) not in id_lst:
                id_lst.append(id(temp))
                temp = temp.next
            else:
                flag = 1
                break
        return flag
    return flag

def has_cycle2(head):
    # using concept - working
    flag = 0
    if head.next != None:
        i, j = head, head
        while(i!= None and j!= None):
            if i.next== None:
                break
            else:
                i=i.next
            if j.next == None:
                break
            else:
                j=j.next.next
            if i==j:
                flag = 1
                return flag
        return flag
    return flag



if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1);
        temp = llist.head;

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count-1:
                temp = temp.next

        temp.next = extra

        result = has_cycle2(llist.head)

        print(str(int(result)) + '\n')

    print()