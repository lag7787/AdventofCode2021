import itertools

class lookaheadchain():

    def __init__(self,it):
        self.it = iter(it)

    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.it)

    def peek(self,default=None,chain=itertools.chain):
        
        try:
            v = next(self.it)
            self.it = chain(v,self.it)
            return v
        except StopIteration:
            return default

    