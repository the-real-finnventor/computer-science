import unittest
import sys
import os

sys.path.insert(1, os.path.dirname(os.path.dirname(__file__)))
from heap import MinHeap


class HeapTests(unittest.TestCase):
    def test_push(self):
        heap = MinHeap()
        heap.push(5)
        heap.push(6)
        heap.push(4)
        self.assertEqual(heap.value, [4, 6, 5])

    def test_peek(self):
        heap = MinHeap()
        heap.push(8)
        heap.push(4)
        heap.push(10)
        heap.push(13)
        heap.push(-7)
        self.assertEqual(heap.peek(), -7)

    def test_empty_peek(self):
        heap = MinHeap()
        self.assertEqual(heap.peek(), None)

    def test_pop(self):
        heap = MinHeap()
        heap.push(8)
        heap.push(4)
        heap.push(10)
        heap.push(13)
        heap.push(-7)
        self.assertEqual(heap.pop(), -7)
        self.assertEqual(heap.peek(), 4)

    def test_empty_pop(self):
        heap = MinHeap()
        self.assertEqual(heap.pop(), None)


if __name__ == "__main__":
    unittest.main()
