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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    temp_list = SinglyLinkedList()
    # temp = temp_list.head
    i,j = head1,head2
    while(i!= None and j!= None):
        if i.data <= j.data:
            node = SinglyLinkedListNode(i.data)
            if temp_list.head == None:
                temp_list.head = node
                # temp_list.tail= node
                # temp = temp.next
            else:
                temp_list.tail.next = node
                # temp_list = temp
                # temp = temp.next
            temp_list.tail = node
            i = i.next
        elif i.data > j.data:
            node = SinglyLinkedListNode(j.data)
            if temp_list.head == None:
                temp_list.head = node
                # temp = temp.next
            else:
                temp_list.tail.next = node
                # temp_list = temp
            temp_list.tail = node
            j = j.next

    if i != None:
        temp_list.tail.next = i
        # temp_list = temp

    if j != None:
        temp_list.tail.next = j
        # temp_list = temp

    return temp_list.head


if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        print()

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3)
        print('\n')


