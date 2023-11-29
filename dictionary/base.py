from linked_list import LinkedList


class Dictionary:
    max_items = 392

    def __init__(self):
        self.buckets = [None]*Dictionary.max_items

    def add(self, key, value) -> None:
        bucket_num = hash(key) % Dictionary.max_items
        if type(self.buckets[bucket_num]) != LinkedList:
            self.buckets[bucket_num] = LinkedList()
        if key in self.keys():
            raise KeyError("Key already exists")

        self.buckets[bucket_num].insert_end((key, value))

    def lookup(self, key):
        bucket_num = hash(key) % Dictionary.max_items
        if type(self.buckets[bucket_num]) != LinkedList:
            raise KeyError("Key not found")
        if self.buckets[bucket_num].find_by_key(key, None) == None and self.buckets[bucket_num].find_by_key(key, False) == False:
            raise KeyError("Key not found")

        return self.buckets[bucket_num].find_by_key(key, None)[1]

    def keys(self):
        for bucket in self.buckets:
            if bucket:
                curr = bucket.head
                while curr:
                    yield curr.data[0]
                    curr = curr.nextNode

    def values(self):
        for bucket in self.buckets:
            if bucket:
                curr = bucket.head
                while curr:
                    yield curr.data[1]
                    curr = curr.nextNode

    def keys_and_values(self):
        for bucket in self.buckets:
            if bucket:
                curr = bucket.head
                while curr:
                    yield curr.data
                    curr = curr.nextNode

    def __iter__(self):
        kav = list(self.keys_and_values())
        self.len = len(kav)
        if self.len != 0:
            self.current = list(self.keys_and_values())[0]
        else:
            self.current = None
        self.curr_index = 0
        return self

    def __next__(self):
        if self.curr_index == self.len:
            raise StopIteration
        rv = self.current
        self.current = list(self.keys_and_values())[self.curr_index]
        self.curr_index += 1
        return rv
