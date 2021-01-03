class Node:

    def __init__(self,name,children=None):

        self.name = name
        self.childen = [Node(child) for child in children]