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

    def len(self) -> int:
        """
        Finds the length of this list.
        """
        curr_len = 0
        current = self.head
        while current:
            curr_len += 1
            current = current.nextNode
        return curr_len

    def find(self, data) -> Node:
        """
        Retrieves the first node containing the given data.
        If not found, will return None.
        """
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.nextNode

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
