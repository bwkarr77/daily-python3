## CREATE 2 LINKED LISTS

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

## ^^ CREATED 2 LINKED LISTS ^^
#####
## vv FIND WHERE LINKED LISTS INTERSECT vv

def compareLists(list1, length1, list2, length2):
    # set the smaller list to iterate through first
    if length1 <= length2:
        firstIterate = list1
        secondIterate = list2
    else:
        firstIterate = list2
        secondIterate = list1
    
    # input the smaller list into a set for comparison to
    visitedNodes = set()
    temp1 = firstIterate.head
    while(temp1):
        visitedNodes.add(temp1.value)
        temp1 = temp1.next

    # iterate through the larger list to find the first matching pair
    temp2 = secondIterate.head
    while (temp2):
        if temp2.value in visitedNodes:
            return temp2.value
        temp2 = temp2.next

print(compareLists(listA, lengthA, listB, lengthB))
