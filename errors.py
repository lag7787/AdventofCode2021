class Error(Exception):
    """Base class for exceptions in this module."""

class SizeError(Error):

    def __init__(self,capacity,size):
        self.capacity = capacity
        self.size = size

    def __str__(self):

        return "SizeError"
