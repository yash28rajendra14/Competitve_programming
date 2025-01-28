class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    
def createDoublyLL(arr: list) -> Node:
    if len(arr) ==0: 
        return None
    prevNode = None
    head = Node(arr[0])
    head.prev = prevNode
    prevNode = head
    newNode = None
    for i in range(1, len(arr)):
        newNode = Node(arr[i])
        prevNode.next = newNode
        newNode.prev = prevNode
        prevNode = newNode
    return head, newNode

def printForwardDLL(head: Node)->None:
    print("forward print")
    tempHead = head
    while(tempHead):
        print(tempHead.val)
        tempHead = tempHead.next
    return None

def printBackwardDLL(tail: Node)->None:
    print("backward print")
    tempHead = tail
    while(tempHead):
        print(tempHead.val)
        tempHead = tempHead.prev
    return None

def findDllLength(head: Node) -> int:
    temp = head
    index = 0
    while temp:
        index+=1
        temp = temp.next
    print(f"length of DLL: {index}")
    return index

def deleteDLLAtKth(head: Node, k: int) -> Node:
    temp = head
    if k > findDllLength(temp):
        print("invalid deletion!!!")
        return
    if k==1:
        return temp.next
    index = 2
    prevNode = temp
    temp = temp.next
    while temp:
        if index == k:
            prevNode.next = temp.next
            if temp.next is not None:
                temp.next.prev = prevNode
                break
        index += 1
        prevNode = temp
        temp = temp.next
    return head

def insertionDllAtKth(head: Node, element: int, k: int) -> Node:
    if findDllLength(head) < k:
        print("invlaid insertion!!!")
        return None
    if head == None:
        return Node(element)
    if k == 1:
        newNode = Node(element)
        newNode.next = head
        return newNode
    temp = head
    prevNode = temp
    temp = temp.next 
    index = 2
    newNode = None
    while temp:
        if index == k:
            newNode = Node(element)
            newNode.next = prevNode.next
            prevNode.next = newNode
            newNode.prev = prevNode
            if newNode.next:
                newNode.next.prev = newNode
            break
        prevNode = temp 
        temp = temp.next
        index += 1

    return newNode if head ==1 else head
        




if __name__ == "__main__":
    arr = [1, 2, 3 ,4, 5, 6]

    #create Doubly Linked list
    head, tail = createDoublyLL(arr)
    # printForwardDLL(head)
    # printBackwardDLL(tail)

    # # find the length of the DLL
    # len_dl = findDllLength(head)

    # #delete node in doubly LL at Kth
    # k=1
    # head = deleteDLLAtKth(head, k)
    # printForwardDLL(head)

    k = 1
    element = 34
    head = insertionDllAtKth(head, element, k)
    printForwardDLL(head)
