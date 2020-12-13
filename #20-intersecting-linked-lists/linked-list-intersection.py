class Node:
    def __init__(self, value):
        self.value = value;
        self.next = None;

class LinkedList:

    def __init__(self):
        self.head = None;
        self.length = 0

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next

def createLinkedList(listArray):
    linkedList = LinkedList()

    linkedList.head = Node(listArray.pop(0))
    length = 1
    temp = linkedList.head
    while len(listArray) > 0:
        newNode = Node(listArray.pop(0))
        temp.next = newNode
        temp = temp.next
        length += 1
    
    return linkedList, length


A = [3, 7, 8, 10]
B = [99, 1, 8, 10, 20]

listA, lengthA = createLinkedList(A)
listB, lengthB = createLinkedList(B)
# print('lengths: ', lengthA, lengthB)
#####

def compareLists(list1, length1, list2, length2):
    if length1 <= length2:
        iterable = list1
        notIterable = list2
    else:
        iterable = list2
        notIterable = list1
    
    visitedNodes = set()
    temp1 = iterable.head
    while(temp1):
        visitedNodes.add(temp1)
        temp1 = temp1.next

    temp2 = notIterable.head
    while (temp2):
        if temp2 in visitedNodes:
            return temp2
        temp2 = temp2.next

compareLists(listA, lengthA, listB, lengthB)
