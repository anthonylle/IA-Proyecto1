import pandas as pd
from DataFrame import DataFrame
from DecisionTree import DecisionTree 
#from Proyecto.DataSet.DataFrame import DataFrame
import random
import math
import csv


class DecisionTreeSolver:

    def entropy(self, prob):
        if prob == 0 or prob == 1:
            return 0
        else:
            result = prob*math.log(prob, 2)
            result += (1-prob)*math.log((1-prob), 2)
            result *= -1
            return result

    def avg_attribute(self, dataset, attribute):
        avgValue = 0
        for row in dataset.get_all_values():
            avgValue += row[column]
        avgValue /= dataset.size()
        return avgValue

        
    def information_gain(self, dataset, attribute):
        column = 0
        for attrib in dataset.get_columns_names():
            if attribute == attrib:
                break
            column += 1
            
        avgValue = self.avg_attribute(dataset, attribute)

        numBenign = 0
        for row in dataset.get_all_values():
            if row[1] == 'B':
                numBenign += 1
        prob = numBenign/dataset.size()
        dataEntropy = self.entropy(prob)

        probGT = 0
        totalRowsGT = 0
        for row in dataset.get_all_values():
            if row[column] > avgValue:
                totalRowsGT += 1
                if row[1] == 'B':
                    probGT += 1
        probLT = (numBenign - probGT)/(dataset.size()-totalRowsGT)
        probGT /= totalRowsGT

        entropyGT = self.entropy(probGT)
        entropyLT = self.entropy(probLT)

        IG = dataEntropy - (totalRowsGT/dataset.size() * entropyGT) - ((dataset.size()-totalRowsGT)/dataset.size() * entropyLT)
        return IG

    def select_attribute(self, dataset):
        highestIG = ""
        highestIGVal = 0
        for attribute in dataset.get_columns_names()[2:len(dataset.get_columns_names())-1]:
            IG = self.information_gain(dataset, attribute)
            if IG > highestIGVal:
                highestIGVal = IG
                highestIG = attribute
            else:
                continue
        return highestIG

    def positive_examples(self, dataset, attribute):
        avgValue = self.avg_attribute(dataset, attribute)
        result = []
        for row in dataset.get_all_values():
            if row[1] == 'B' and row[dataset.index(attribute)] >= avgValue:
                result += [row]
        return result

    def negative_examples(self, dataset, attribute):
        avgValue = self.avg_attribute(dataset, attribute)
        result = []
        for row in dataset.get_all_values():
            if row[1] == 'M' and row[dataset.index(attribute)] < avgValue:
                result += [row]
        return result

    def build_tree(self, dataset):
        attributes = dataset.get_columns_names()[2:len(dataset.get_columns_names())-1]
        new_tree = DecisionTree()

        while attributes != []:
            selected_att = self.select_attribute(dataset)
            avg_value = self.avg_attribute(dataset, random_attrib)
            if new_tree.root == None:
                new_tree.set_root(selected_att, avg_value)
            elif new_tree.root.children == []:
                if avg_value < new_tree.root.avg_value:
                    new_dataset = self.positive_examples(dataset, selected_att)
                    new_tree.root.children[0] = Node(selected_att, avg_value)
                else:
                    new_dataset = self.negative_examples(dataset, selected_att)
                    new_tree.root.children[1] = Node(selected_att, avg_value)
            else:
                if avg_value < new_tree.root.avg_value:
                    new_dataset = self.positive_examples(dataset, selected_att)
                    if avg_value < new_tree.root.children[0].avg_value:
                        new_new_dataset = self.positive_examples(new_dataset, selected_att)
                        new_tree.root.children[0].children[0] = Node(selected_att, avg_value)
                    else:
                        new_new_dataset = self.negative_examples(new_dataset, selected_att)
                        new_tree.root.children[0].children[1] = Node(selected_att, avg_value)
                else:
                    new_dataset = self.negative_examples(dataset, selected_att)
                    if avg_value < new_tree.root.children[1].avg_value:
                        new_new_dataset = self.positive_examples(new_dataset, selected_att)
                        new_tree.root.children[1].children[0] = Node(selected_att, avg_value)
                    else:
                        new_new_dataset = self.negative_examples(new_dataset, selected_att)
                        new_tree.root.children[1].children[1] = Node(selected_att, avg_value)
            attributes.remove(selected_att)
        return new_tree

"""
    def significance_test(self, subsets, dataset, attribute):
        totalBenign = 0
        for row in dataset.get_all_values():
            if row[1] == 'B':
                totalBenign += 1
        totalMalign = dataset.size()-totalBenign

        avgValue = 0
        for row in dataset.get_all_values():
            avgValue += row[column]
        avgValue /= dataset.size()

        result = 0

        for s_set in subsets:
            s_set_size = s_set.size/len(dataset.get_columns_names())
            kBenign = 0
            for row in s_set.get_values():
                if row[1] == 'B':
                    kBenign += 1
            kMalign = s_set_size - kBenign
            expectedBenign = totalBenign * ((kBenign+kMalign)/dataset.size())
            expectedMalign = totalMalign * ((kBenign+kMalign)/dataset.size())

            result += ((kBenign-expectedBenign)**2/expectedBenign) + ((kMalign-expectedMalign)**2/expectedMalign)

        return result
"""







