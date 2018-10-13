"""
class Node:
    children = []
    def __init__(self, value):
        self.value = value

class NodoCondicion:
    hijos = []
    def __init__(self, parametro, tipo):
        self.parametro = parametro
        self.tipo = tipo        

class Tree:
    def __init__(self, root):
        self.root = Node(root)
"""
    
import math
import csv

dataset = []

def openCSV():
    global dataset
    dataset = []
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=" ", quotechar="|")
        rowNum = 0
        for row in reader:
            newRow = row[0].split(",")
            colNum = 0
            for value in newRow:
                if colNum != 1 or rowNum == 0:
                    newRow[colNum] = eval(value)
                colNum += 1
            dataset += [newRow]
            rowNum += 1
#    for row in dataset:
#        print(row, "\n")
    
def entropy(prob):
    if prob == 0 or prob == 1:
        return 0
    else:
        result = prob*math.log(prob, 2)
        result += (1-prob)*math.log((1-prob), 2)
        result *= -1
        return result
        
def informationGain(attribute):
    global dataset
    dataLength = len(dataset)-1
    column = 0
    for attrib in dataset[0]:
        if attribute == attrib:
            break
        column += 1
    avgValue = 0
    for row in dataset[1:]:
        avgValue += row[column]
    avgValue /= dataLength

    numBenign = 0
    for row in dataset[1:]:
        if row[1] == 'B':
            numBenign += 1
    prob = numBenign/dataLength
    dataEntropy = entropy(prob)

    probGT = 0
    totalRowsGT = 0
    for row in dataset[1:]:
        if row[column] > avgValue:
            totalRowsGT += 1
            if row[1] == 'B':
                probGT += 1
    probLT = (numBenign - probGT)/(dataLength-totalRowsGT)
    probGT /= totalRowsGT

    entropyGT = entropy(probGT)
    entropyLT = entropy(probLT)

    IG = dataEntropy - (totalRowsGT/dataLength * entropyGT) - ((dataLength-totalRowsGT)/dataLength * entropyLT)
    return IG

def selectAttribute():
    global dataset

    highestIG = ""
    highestIGVal = 0
    for attribute in dataset[0][2:]:
        IG = informationGain(attribute)
        if IG > highestIGVal:
            highestIGVal = IG
            highestIG = attribute
        else:
            continue
    return highestIG
        
    
    








