class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def createLinkedListFronArray(arr):
    head = currHead = Node(arr[0])
    for i in range(1, len(arr)):
        newNode = Node(arr[i])
        currHead.next = newNode
        currHead = newNode
    return head

def linkedListLength(linkedList: Node):
    index = 0
    head = linkedList
    while head:
        head = head.next
        index += 1
    return index

def searchInLinkedList(linkedList: Node, val: int):
    head = linkedList
    while head:
        if head.val == val:
            return 1
        head = head.next
    return 0

def deleteKthElement(linkedList: Node, k: int) -> Node:
    head = linkedList
    # first always write the most basic edge cases that is head == Null or k = 1
    if head is None:
        return None
    if k==1:
        return head.next

    prevNode = temp = head
    temp = temp.next
    index = 2
    while temp:
        print(f"check: {index, temp.val, prevNode.val}")
        if index == k:
            prevNode.next = temp.next
            break
        prevNode = temp
        temp = temp.next
        index += 1
    return head

def insertElementAtKthPosition(linkedList: Node, element: int, k: int) -> Node:
    temp = linkedList
    # Edge cases: check for Empty linkedList, linkedList having 1 element, k is greater than len of LL
    if linkedList is None:
        newNode = Node(element)
        return newNode
    if linkedListLength(temp) < k:
        print(f"not a valid K!!!")
        return None
    if k == 1:
        newNode = Node(element)
        newNode.next = temp
        return newNode
    index = 2
    prevNode = temp
    while temp:
        temp = temp.next
        if index == k:
            # print(f"check {index, temp.val}")
            newNode = Node(element)
            newNode.next = temp
            prevNode.next = newNode
            break
        index += 1
        prevNode = temp
        temp = temp.next
    return linkedList

def reverseLL(head: Node) -> Node:
    temp = head 
    if head is None or head.next is None:
        return head
    prevNode = temp
    temp = temp.next
    # print(temp)
    prevNode.next = None
    while(temp):
        # print("csds",temp.val)
        front = temp.next
        temp.next = prevNode
        prevNode = temp
        temp = front
    return prevNode



def printLinkedList(linkedList: Node):
    head = linkedList
    while head:
        print(head.val)
        head = head.next 


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    linkedList = None
    if len(arr) > 1:
        linkedList = createLinkedListFronArray(arr)
    
    # #print linked list
    # printLinkedList(linkedList)
    
    # # find linked list length
    # print(f"Linked list length {linkedListLength(linkedList)} ")
    # element = 4
    # #searching in a linkedList
    # if searchInLinkedList(linkedList, element):
    #     print(f"{element} available!!!")
    # else:
    #     print(f"{element} is not available!!!")
    
    # #delete kth element
    # k=3
    # head = deleteKthElement(linkedList, k)
    # printLinkedList(head)

    # # Insertion element at some position
    # k=4
    # element = 23
    # head = insertElementAtKthPosition(linkedList, element, k)
    # printLinkedList(head)

    #reverse a linked list
    printLinkedList(linkedList)
    head = reverseLL(linkedList)
    printLinkedList(head)