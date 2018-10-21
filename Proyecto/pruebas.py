from Proyecto.Normalizer.Normalizer import Normalizer
from Proyecto.DataSet.DataFrame import DataFrame
from Proyecto.KFoldCrossValidation.KFoldCrossValidation import KFoldCrossValidation
from Proyecto.NeuralNetwork.NeuralNetwork import NeuralNetwork
def prueba():
    
    # create data_frame to input
    data = DataFrame()
    # create data_frame to output
    output = DataFrame()
    # create normalizer 
    normalizer = Normalizer()
    data.load_data_set("breast-cancer-wisconsin-data.csv")

    data.drop_columns_by_name(["id"])

    output.data_set = data.cut_column('diagnosis')

    data = data.data_set
    data.data_set = normalizer.normalize_data(data)

    data.join_data(output.data_set)

    rn = NeuralNetwork()
    kwargs = {"units": 2, "layers": 5, "activation": "sigmoid"}
    rn.create_model(kwargs)

    cv = KFoldCrossValidation(10, "diagnosis")
    cv.k_fold_validation(data, model=rn)
    cv.view_report()


def prueba2():
    # create data_frame to input
    input = DataFrame()
    # create data_frame to output
    output = DataFrame()
    # create normalizer
    normalizer = Normalizer()
    cv = CategoricalValues()
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
    cv.view_report()

prueba()
