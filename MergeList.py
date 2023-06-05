class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # Criando um nó predefinido
        head = Node()
        current = head
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Anexando o restante dos nós da lista que ainda contém nós
        current.next = l1 if l1 is not None else l2
        return head.next