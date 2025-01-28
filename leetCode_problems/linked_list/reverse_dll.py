class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def reverseDLL(head):
    # Write your code here
    if head is None:
        return None
    if head.next is None:
        return head
    temp = head
    while temp:
        # print(temp.data)
        prevConn = temp.prev
        temp.prev = temp.next
        temp.next = prevConn
        head = temp
        temp = temp.prev
    return head
