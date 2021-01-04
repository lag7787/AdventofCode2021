import sys
from errors import SizeError

class Queue:

    def __init__(self,data = []):

        self.data = data
        self.capacity = 25
        self.size = len(data)

    def enqueue(self,value):
        """The enque method will attempt to add one item to the queue.\
            If the operation is unsuccessfull, an exception will be raised"""

        if self.size < self.capacity:

            self.data.insert(0,value)
            self.size += 1

        else:
            raise SizeError

    def dequeue(self):

        if self.size > 0:

            self.size -= 1
            return self.data.pop()

        else:
            raise SizeError

    def __str__(self):
        """The __str__ special variable returns a string"""

        return self.data.__str__()









