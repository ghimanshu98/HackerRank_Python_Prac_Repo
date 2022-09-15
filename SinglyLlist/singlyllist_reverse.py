#!/bin/python3

import math
import os
import random
import re
import sys

from requests import head

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
        print(str(node.data), end = ' ')

        node = node.next

        if node:
            pass

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(head):
    # Write your code here
    temp_llist = SinglyLinkedList()

    temp = head
    while(temp.next != None):
        node = SinglyLinkedListNode(temp.data)
        if temp_llist.head == None:
            temp_llist.head = node
        else:
            node.next = temp_llist.head
            temp_llist.head = node
        temp = temp.next
    node = SinglyLinkedListNode(temp.data)
    node.next = temp_llist.head
    temp_llist.head = node
    return temp_llist.head

if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1)
        


