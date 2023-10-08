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

    def has_cycle(self) -> bool:
        """
        Checks if this list has a cycle.
        """
        # Time: O(n)
        # Space: O(1)
        slow = self.head  # slow pointer moves one at a time
        fast = self.head  # fast pointer moves 2x faster than slow
        if fast and fast.nextNode:
            fast = fast.nextNode
        while fast:
            if slow == fast:
                return True
            slow = slow.nextNode
            if fast and fast.nextNode:
                fast = fast.nextNode.nextNode
        return False

    def has_duplicate(self) -> bool:
        """
        Checks if this list has duplicate values.
        """
        # Time: O(n)
        # Space: O(n)
        seen = set()
        current = self.head
        while current:
            if current.data in seen:
                return True
            seen.add(current.data)
            current = current.nextNode
        return False

    def find_most_duplicate(self):
        """
        Finds the most duplicate value in this list. 
        If multible, returns the first one.
        If no duplicate, returns None.
        """
        # Time: O(n)
        # Space: O(n)
        seen = {}
        current = self.head
        while current:
            if current.data in seen:
                seen[current.data] += 1
            else:
                seen[current.data] = 1
            current = current.nextNode
        max_val = max(seen.values())
        for key, value in seen.items():
            if value != 1:
                if value == max_val:
                    return key
        return None
