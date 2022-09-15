"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

 would have it's logo with the letters .

Input Format

A single line of input containing the string .

Constraints

 has at least  distinct characters
Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde
Sample Output 0

b 3
a 2
c 2
Explanation 0


Here, b occurs  times. It is printed first.
Both a and c occur  times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string  has at least  distinct characters.

"""
## Solution

class Node:
    def __init__(self, ch = None, position = None, value = None):
        self.ch = ch
        self.position = position
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    # def insert(self, ch, value):
    #     # Create Node
    #     newnode = Node(ch = ch, value = value)
    #     # Inserting first node:
    #     if self.head.next == None:
    #         self.head.next = newnode
    #     else:
    #         temp = self.head
    #         while(temp.next != None):
    #             temp = temp.next
    #         temp.next = newnode

    def sorted_inserted(self, ch, position, value):
        #Create Node
        newnode = Node(ch = ch, position=position, value = value)
        # Inserting first node, i.e LnkedList is empty:
        if self.head.next == None:
            self.head.next = newnode
        else:
            temp = self.head
            while(temp.next!=None):
                # comparing value and inserting
                if newnode.value > temp.next.value:
                    newnode.next = temp.next
                    temp.next = newnode
                    break
                elif newnode.value == temp.next.value :  # if value is same then checking position
                    if temp.next.position > newnode.position:
                        newnode.next = temp.next
                        temp.next = newnode
                        break
                    elif temp.next.position < newnode.position:
                        if temp.next.next == None:
                            newnode.next = temp.next.next
                            temp.next.next = newnode 
                            break
                        elif temp.next.next !=None and temp.next.next.position > newnode.position:
                            newnode.next = temp.next.next
                            temp.next.next = newnode 
                            break
                        elif temp.next.next !=None and temp.next.next.position < newnode.position:
                            temp =temp.next
                            continue
                    else:
                        temp = temp.next
                elif newnode.value < temp.next.value:
                    if temp.next.next == None:
                        newnode.next = temp.next.next
                        temp.next.next = newnode
                        break
                    else:
                        temp = temp.next
                        continue

    # def view(self):
    #     if self.head.next == None:
    #         print("Empty LinkedList..")
    #     else:
    #         temp = self.head
    #         while(temp.next!=None):
    #             print('{} {}'.format(temp.next.ch, temp.next.value))
    #             temp = temp.next

    def view_top_3(self):
        temp = self.head
        for i in range(3):
            print('{} {}'.format(temp.next.ch, temp.next.value))
            temp = temp.next



position = "abcdefghijklmnopqrstuvwxyz"

string = 'aabbbccde'
    # function(s
dic = {ch : string.count(ch) for ch in string}

print(dic)

ll_obj = LinkedList()

for key in dic.keys():
    value = dic.get(key)
    ll_obj.sorted_inserted(ch = key,position = position.find(key), value = value)


ll_obj.view_top_3()
