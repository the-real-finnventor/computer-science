class StackError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))


class Stack:
    max_len = 100

    def __init__(self):
        self.stack = [None]*Stack.max_len
        self.curr_len = 0

    def push(self, data, no_error=False) -> None:
        if self.curr_len == Stack.max_len:
            if not no_error:
                raise StackError("Reached max length")
            return None
        self.stack[self.curr_len] = data
        self.curr_len += 1

    def pop(self, no_error=False) -> object:
        if self.curr_len == 0:
            if not no_error:
                raise StackError("No items in list")
            return None
        rv = self.stack[self.curr_len - 1]
        self.stack[self.curr_len - 1] = None
        self.curr_len -= 1
        return rv

    def peek(self, no_error=False, no_error_return=None) -> object:
        if self.curr_len == 0:
            if not no_error:
                raise StackError("No items in list")
            return no_error_return
        return self.stack[self.curr_len - 1]

    def __str__(self) -> str:
        return str(self.stack[:self.curr_len])

    def __repr__(self) -> str:
        return self.__str__()
