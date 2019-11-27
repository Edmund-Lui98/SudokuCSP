"""
-------------------------------------------------------
Queue implementation
-------------------------------------------------------
Section: CP468
-------------------------------------------------------
"""
from copy import deepcopy

class Queue:

    def __init__(self):
        self._values = []
        self.length = 0

    def is_empty(self):
        return len(self._values) == 0

    def insert(self, value):
        self._values.append(value)
        self.length += 1
        return

    def remove(self):
        assert len(self._values) > 0, "Cannot remove from an empty queue"
        value = self._values.pop(len(self._values)-1)
        self.length -= 1 
        return value

    def peek(self):
        assert len(self._values) > 0, "Cannot peek at an empty queue"
        value = deepcopy(self._values[len(self._values)-1])
        return value
