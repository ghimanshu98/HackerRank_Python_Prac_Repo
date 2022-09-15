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

def helper(llist, positionFromTail, fwd_cnt = 0, bwd_cnt =0):
    if llist.next != None:
        fwd_cnt = fwd_cnt +1
        returned_bwd_cnt, flag = helper(llist.next, positionFromTail, fwd_cnt, bwd_cnt)
        if flag == True:
            return returned_bwd_cnt, True
        elif flag ==  False:
            if returned_bwd_cnt ==  positionFromTail: 
                return llist.data, True
            else: 
                return returned_bwd_cnt+1, False
    else:
        if llist.next ==  None:
            if positionFromTail == 0:
                return llist.data, True
            else:
            # it means we are on tail node
                bwd_cnt = bwd_cnt + 1
                return bwd_cnt, False

def getNode(llist, positionFromTail):
    return helper(llist, positionFromTail, fwd_cnt = 0, bwd_cnt =0)[0]
   

if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)

        print(str(result) + '\n')

    
