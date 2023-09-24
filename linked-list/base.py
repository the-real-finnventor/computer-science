class LinkedListError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))


class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class LinkedList:
    def __init__(self):
        self.head = None

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

    def insert_at(self, data, pos: int) -> None:
        """
        Places a new node with given data, 
        at the position given. If the position given 
        is past the end of the list, will return error.
        """
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        if pos == 0:
            newNode.nextNode = self.head
            self.head = newNode
            return
        curr_pos = 0
        current = self.head
        last_node = self.head
        while current:
            if curr_pos == pos:
                newNode.nextNode = current
                last_node.nextNode = newNode
                break
            last_node = current
            current = current.nextNode
            curr_pos += 1
            if pos == self.len() and not current:
                last_node.nextNode = newNode
            elif not current:
                raise LinkedListError("Index out of range")

    def insert_front(self, data) -> None:
        self.insert_at(data, 0)

    def insert_end(self, data) -> None:
        self.insert_at(data, self.len())

    def getLL(self):
        current = self.head
        linked_list = []
        while current:
            linked_list.append(current.data)
            current = current.nextNode
        return linked_list

    @staticmethod
    def insertItems(items=[], ll=None):
        if not ll:
            ll = LinkedList()
        for item in items:
            ll.insert_end(item)
        return ll
