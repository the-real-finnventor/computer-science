import unittest
import base


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = base.Stack()
        self.empty_stack_list = [None]*base.Stack.max_len

    def testPush(self):
        self.stack.push(8)
        self.empty_stack_list[0] = 8
        self.assertEqual(self.stack.stack, self.empty_stack_list)

    def testOverPush(self):
        for _ in range(base.Stack.max_len):
            self.stack.push(1)
        with self.assertRaises(base.StackError):
            self.stack.push(2)

    def testPop(self):
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.stack, self.empty_stack_list)

    def testEmptyPop(self):
        with self.assertRaises(base.StackError):
            self.stack.pop()

    def testPeek(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.empty_stack_list[0] = 1
        self.assertEqual(self.stack.stack, self.empty_stack_list)

    def testEmptyPeek(self):
        with self.assertRaises(base.StackError):
            self.stack.peek()


if __name__ == "__main__":
    unittest.main()
