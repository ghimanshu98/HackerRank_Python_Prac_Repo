#!/bin/python3

import math
import os
from pydoc import tempfilepager
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            pass

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

# The below code is working , but myself only not able to understand the logic clearly and we need to optimize the logic for sorting the llist before inserting the new node

def sortedInsert(head, data):
    head = sort(head)
    newnode = DoublyLinkedListNode(data)
    if head==None:
        head = newnode
    else:
        temp = head
        while(temp != None):
            if newnode.data <= temp.data:
                newnode.next = temp
                temp.prev = newnode
                head = newnode
                break
            elif newnode.data>=temp.data and temp.next == None:
                temp.next = newnode
                newnode.prev = temp
                break
            elif newnode.data >= temp.data:
                if newnode.data <= temp.next.data:
                    newnode.next = temp.next
                    newnode.prev = temp
                    newnode.next.prev = newnode
                    newnode.prev.next = newnode
                    break
                elif newnode.data >temp.next.data:
                    temp=temp.next
    return head

# first we need to sort the passed list and then insert the new data

def sort(llist):
    i = llist
    if i.next == None:
        return i
    else:
        while(i.next!=None):
            j = i.next
            while(j != None):
                if i.data > j.data:
                    i.data, j.data = j.data, i.data
                    j = j.next
                    continue
                elif i.data <= j.data:
                    j = j.next
                    continue
            i = i.next
        return llist






if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1)
        print('\n')
    print()
