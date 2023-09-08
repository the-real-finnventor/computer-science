class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.nextNode:
                current = current.nextNode
            current.nextNode = newNode
        else:
            self.head = newNode

    def getLL(self):
        current = self.head
        linked_list = []
        while current:
            linked_list.append(current.data)
            current = current.nextNode
        return linked_list


def insertItems(items=[], ll=None):
    created = False
    if not ll:
        ll = LinkedList()
        created = True
    for item in items:
        ll.insert(item)
    return ll
