from typing import Optional

class Node:
    def __init__(self, value: int):
        self.data = value
        self.next = None

def oddEvenList(head: Optional[Node]) -> Optional[Node]:
    # Write your code here.
    # Approach1:
    # t.c: O(N), S.c: O(1)
    if head is None or head.next is None:
        return head

    oddNode = head
    evenNode = evenHeadNode = head.next   
    while evenNode and evenNode.next:
        oddNode.next = oddNode.next.next
        evenNode.next = evenNode.next.next
        oddNode = oddNode.next
        evenNode = evenNode.next    

    oddNode.next = evenHeadNode
    return head