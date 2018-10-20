from Proyecto.Normalizer.Normalizer import Normalizer
from Proyecto.DataSet.DataFrame import DataFrame
from Proyecto.KFoldCrossValidation.KFoldCrossValidation import KFoldCrossValidation

def prueba():
    
    # create data_frame to input
    input = DataFrame()
    # create data_frame to output
    output = DataFrame()
    # create normalizer 
    normalizer = Normalizer()

    input.load_data_set("breast-cancer-wisconsin-data.csv")
    # drop innecesary columns in the input
    #input.view()
    input.drop_columns_by_name(["id"])
    #input.view()
    output.data_set = input.cut_column('diagnosis')
    #input.view()
    # normalizer data
    data = input.data_set
    input.data_set = normalizer.normalize_data(data)

    input.join_data(output.data_set)

    #input.view()
    cv = KFoldCrossValidation(10, "diagnosis")
    cv.k_fold_validation(input)


def prueba2():
    # create data_frame to input
    input = DataFrame()
    # create data_frame to output
    output = DataFrame()
    # create normalizer
    normalizer = Normalizer()

    input.load_data_set("Churn_Modelling.csv")
    # drop innecesary columns in the input

    input.drop_columns_by_name(["RowNumber", "CustomerId", "Surname"])

    output.data_set = input.cut_column('Exited')

    # normalizer data
    data = input.data_set
    input.data_set = normalizer.normalize_data(data)
    input.join_data(output.data_set)

    cv = KFoldCrossValidation(10, "Exited")
    cv.k_fold_validation(input)

prueba()
