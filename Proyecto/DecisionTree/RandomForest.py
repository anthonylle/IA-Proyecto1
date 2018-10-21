#from Proyecto.Model.Model import Model
from DecisionTreeSolver import DecisionTreeSolver
from DecisionTree import DecisionTree
import random

class RandomForest:
    def __init__(self):
        print("")

    def load_data(self):
        pass

    def normalize_data(self):
        pass

    def build_random_tree(self, dataset, feature_number):
        split_dataset = dataset
        attributes = []
        while feature_number > 0:
            attributes += dataset.get_columns_names()[random.randint(2, len(dataset.get_columns_names()-1))]
            feature_number -= 1

        print(attributes)

        new_tree = DecisionTree()
        t_solver = DecisionTreeSolver()
        actual_node = new_tree.root

        while attributes != []:
            selected_att = t_solver.select_attribute(dataset)        
            avg_value = self.avg_attribute(dataset, selected_att)
            if actual_node == None:
                actual_node.set_node(selected_att, avg_value)
            elif actual_node.children == []:
                if avg_value < actual_node.avg_value:
                    new_dataset = self.positive_examples(dataset, selected_att)
                    actual_node = actual_node.children[0]
                    actual_node.set_node(selected_att, avg_value)
                else:
                    new_dataset = self.negative_examples(dataset, selected_att)
                    actual_node = actual_node.children[1]
                    actual_node.set_node(selected_att, avg_value)
            else:
                if avg_value < actual_node.avg_value:
                    new_dataset = self.positive_examples(dataset, selected_att)
                    actual_node = actual_node.children[0]
                    if avg_value < actual_node.avg_value:
                        new_new_dataset = self.positive_examples(new_dataset, selected_att)
                        actual_node.children[0] = Node(selected_att, avg_value)
                    else:
                        new_new_dataset = self.negative_examples(new_dataset, selected_att)
                        actual_node.children[1] = Node(selected_att, avg_value)
                else:
                    new_dataset = self.negative_examples(dataset, selected_att)
                    actual_node = actual_node.children[1]
                    if avg_value < actual_node.avg_value:
                        new_new_dataset = self.positive_examples(new_dataset, selected_att)
                        actual_node.children[0] = Node(selected_att, avg_value)
                    else:
                        new_new_dataset = self.negative_examples(new_dataset, selected_att)
                        actual_node.children[1] = Node(selected_att, avg_value)
            attributes.remove(random_att)
        return new_tree
        
    def create_model(dataset, num_trees):
        tree_list = []
        results = []
        while num_trees > 0:
            rand_tree = self.build_random_tree(dataset, random.randint(1, len(dataset.get_columns_names()-1)))
            tree_list += [rand_tree]
            num_trees -= 1
        return tree_list
            
    def train_model(self):
        pass

    def evaluate_model(self):
        pass

