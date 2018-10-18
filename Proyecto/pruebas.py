from Proyecto.Normalizer.Normalizer import Normalizer
from Proyecto.DataSet.DataFrame import DataFrame
from Proyecto.Folds.Folds import Folds
from Proyecto.KFoldCrossValidation.KFoldCrossValidation import KFoldCrossValidation
def normalizer_data():
    
    # create data_frame to idenpendents_vars
    idenpendents_vars = DataFrame()
    # create data_frame to objective_var
    objective_var = DataFrame()
    # create normalizer 
    normalizer = Normalizer()

    idenpendents_vars.load_data_set("Churn_Modelling.csv")
    # drop innecesary columns in the idenpendents_vars
    idenpendents_vars.drop_columns_by_name(["RowNumber","CustomerId","Surname"])

    objective_var.data_set = idenpendents_vars.cut_column("Exited")
    
    # normalizer data
    data = idenpendents_vars.data_set
    idenpendents_vars.data_set = normalizer.normalize_data(data)
    
    data = objective_var.data_set
    objective_var.data_set = normalizer.normalize_data(data)


def pruebaFolds():
    idenpendents_vars = DataFrame()
    # create data_frame to objective_var
    objective_var = DataFrame()
    # create normalizer 
    normalizer = Normalizer()
    idenpendents_vars.load_data_set("Churn_Modelling.csv")
    # drop innecesary columns in the idenpendents_vars
    idenpendents_vars.drop_columns_by_name(["RowNumber","CustomerId","Surname"])
    # take column from idenpendents_vars
    objective_var.data_set = idenpendents_vars.cut_column("Exited")
    
    #normalizer data
    data =idenpendents_vars.data_set
    idenpendents_vars.data_set = normalizer.normalize_data(data)
    
    idenpendents_vars.join_data(objective_var.data_set)
    
    cv = KFoldCrossValidation(10, "Exited")
    cv.k_fold_validation(idenpendents_vars)

def pruebaZScore():
    data = DataFrame()
    # create data_frame to objective_var
    column = DataFrame()
    # create normalizer
    normalizer = Normalizer()
    data.load_data_set('Churn_Modelling.csv')

    # drop innecesary columns in the idenpendents_vars
    data.drop_columns_by_name(["RowNumber", "CustomerId", "Surname"])
    # take a number column
    column.data_set = data.cut_column("CreditScore")
    # normalizer data
    df = column.data_set
    column.data_set = normalizer.normalize_data(df)

pruebaFolds()