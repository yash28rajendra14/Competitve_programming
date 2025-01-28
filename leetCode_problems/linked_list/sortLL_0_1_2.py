'''
Following is the structure of the Node class already defined.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        


def sortList(head):
    # Write your code here
    # # Approach 1: TC: O(2N), SC: O(1)
    # cntZero = cntOne = cntTwo = 0
    # temp = head
    # while(temp):
    #     if temp.data == 0:
    #         cntZero += 1
    #     elif temp.data == 1:
    #         cntOne += 1
    #     elif temp.data == 2:
    #         cntTwo += 1
    #     temp = temp.next
    # temp = head
    # while cntZero:
    #     temp.data = 0
    #     cntZero -= 1
    #     temp = temp.next
    # while cntOne:
    #     temp.data = 1
    #     cntOne -= 1
    #     temp = temp.next
    # while cntTwo:
    #     temp.data = 2
    #     cntTwo -= 1
    #     temp = temp.next
    
    # return head

    #Approach: TC: O(N), SC: O(1)
    if head is None or head.next is None:
        return head
    tempOne = tdOne = Node(-1)
    tempZero = tdZero = Node(-1)
    tempTwo = tdTwo = Node(-1)
    temp = head
    while(temp):

        if temp.data == 0:
            tempZero.next = temp
            tempZero = temp
        elif temp.data == 1:
            tempOne.next = temp
            tempOne = temp
        elif temp.data == 2:
            tempTwo.next = temp
            tempTwo = temp
        temp = temp.next
    #link between temps
    tempZero.next = tdOne.next if tdOne.next else tdTwo.next
    tempOne.next = tdTwo.next
    tempTwo.next = None
    return tdZero.next

    pass