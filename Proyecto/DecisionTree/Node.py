class Node:
    children = []
    def __init__(self, attribute, avg_value):
        self.attribute = attribute
        self.avg_value = avg_value

    def set_node(self, attribute, avg_value):
        self.attribute = attribute
        self.avg_value = avg_value
