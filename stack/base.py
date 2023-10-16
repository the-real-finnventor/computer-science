class StackError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))


class Stack:
    max_len = 100

    def __init__(self) -> None:
        self.stack = [None]*Stack.max_len
        self.curr_len = 0

    def push(self, data) -> None:
        if self.curr_len == Stack.max_len:
            raise StackError("Reached max length")
        self.stack[self.curr_len] = data
        self.curr_len += 1

    def pop(self) -> object:
        if self.curr_len == 0:
            raise StackError("No items in list")
        rv = self.stack[self.curr_len - 1]
        self.stack[self.curr_len - 1] = None
        self.curr_len -= 1
        return rv

    def peek(self) -> object:
        if self.curr_len == 0:
            raise StackError("No items in list")
        return self.stack[self.curr_len - 1]
