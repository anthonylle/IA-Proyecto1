from Node import Node

class DecisionTree:
    def __init__(self):
        self.root = None

    def set_root(self, root_attribute, root_avg):
        self.root = Node(root_attribute, root_avg)
    
