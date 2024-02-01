class MinHeap:
    def __init__(self):
        self.value = []

    def peek(self) -> int | None:
        if self.value == []:
            return None
        return self.value[0]

    def push(self, value: int) -> None:
        self.value.append(value)
        if len(self.value) <= 1:
            return
        curr_index = len(self.value) - 1
        while value < self.value[(curr_index - 1) // 2]:
            self.value[curr_index] = self.value[(curr_index - 1) // 2]
            self.value[(curr_index - 1) // 2] = value
            curr_index = (curr_index - 1) // 2
            if (curr_index - 1) // 2 < 0:
                return

    def pop(self) -> int | None:
        if self.value == []:
            return None
        rv = self.value[0]
        if len(self.value) == 0:
            return rv
        self.value[0] = self.value.pop()
        curr_index = 0
        while len(self.value) > (curr_index * 2) + 1 and (self.value[curr_index] > self.value[(curr_index * 2) + 1] or (len(self.value) > (curr_index * 2) + 2 and self.value[curr_index] > self.value[(curr_index * 2) + 2])):
            if not (len(self.value) <= (curr_index * 2) + 2) or self.value[(curr_index * 2) + 1] < self.value[(curr_index * 2) + 2]:
                value = self.value[curr_index]
                self.value[curr_index] = self.value[(curr_index * 2) + 1]
                self.value[(curr_index * 2) + 1] = value
                curr_index = (curr_index * 2) + 1
            else:
                self.value[curr_index] = self.value[(curr_index * 2) + 2]
                self.value[(curr_index * 2) + 2] = self.value[curr_index]
                curr_index = (curr_index * 2) + 2
        return rv
