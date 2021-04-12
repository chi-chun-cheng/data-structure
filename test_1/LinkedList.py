#Create the Node class of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Create Linked list and operations
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = newNode

def mergeLists(headA, headB):

    #dummy node is used to store the result 
    dummyNode = Node(0)

    tail = dummyNode
    while True:

        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
        
        tail = tail.next

    return dummyNode.next

def mergeLists_rec(headA, headB):

    temp = None

    if headA is None:
        return headB
    if headB is None:
        return headA

    if headA.data <= headB.data:
        temp = headA

        temp.next = mergeLists_rec(headA.next, headB)

    else:
        temp = headB

        temp.next = mergeLists_rec(headA, headB.next)

    return temp

if __name__ == "__main__":
    listA = LinkedList()
    listB = LinkedList()

    listA.addToList(5)
    listA.addToList(10)
    listA.addToList(15)

    listB.addToList(2)
    listB.addToList(3)
    listB.addToList(20)

    listA.head = mergeLists(listA.head, listB.head)

    print("Merged Linked List is : ", end="")
    listA.printList()
    
a = [[4, 3], [3, 2], [2, 1], [5, 4]]
def MergeKSortedSequences(sequences):
    l = []
    temp = []
    for i in range(len(a)):
    print("=")
        print(temp, a[i])
        while temp and a[i]:
            #print(l, a[i])
            if temp[-1] >= a[i][-1]:
                temp.insert(0, temp.pop())
            else:
                temp.insert(0, a[i].pop())
        
        if temp:
            temp = temp + temp
        if a[i]:
            temp = a[i] + temp
        print("temp = ", temp)
        l = temp.copy()
    return temp
print(MergeKSortedSequences(a))
#========================================================================================
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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

# alternative1
def mergeLists(head1, head2):
    dummy = SinglyLinkedListNode(None)
    head = dummy

    while head1 and head2:
        if head1.data > head2.data:
            head1, head2 = head2, head1
        
        head.next = head1
        head1 = head1.next
        head = head.next
    
    if head1 != None:
        head.next = head1
    else:
        head.next = head2

    
    return dummy.next

# alternative 2
def mergeLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        head = head1
        curr1 = head1.next
        curr2 = head2
    else:
        head = head2
        curr1 = head1
        curr2 = head2.next

    curr = head
        
    while True:
        if curr1 is None:
            curr.next = curr2
            break
        elif curr2 is None:
            curr.next = curr1
            break

        if curr1.data <= curr2.data:
            curr.next = curr1
            curr1 = curr1.next
        else:
            curr.next = curr2
            curr2 = curr2.next
        
        curr = curr.next

    return head