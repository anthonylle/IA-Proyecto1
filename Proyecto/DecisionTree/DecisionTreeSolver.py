import pandas as pd
from Proyecto.DataSet.DataFrame import DataFrame
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
        
    def information_gain(self, dataset, attribute):
        column = 0
        for attrib in dataset.get_columns_names():
            if attribute == attrib:
                break
            column += 1
            
        avgValue = 0
        for row in dataset.get_all_values():
            avgValue += row[column]
        avgValue /= dataset.size()

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





