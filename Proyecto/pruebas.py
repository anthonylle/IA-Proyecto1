from Proyecto.Normalizer.Normalizer import Normalizer
from Proyecto.DataSet.DataFrame import DataFrame
from Proyecto.Folds.Folds import Folds
from Proyecto.CrossValidation.CrossValidation import CrossValidation
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
    
    #normalizer data
    data =idenpendents_vars.data_set
    idenpendents_vars.data_set = normalizer.normalizer_data(data)
    
    data = objective_var.data_set
    objective_var.data_set = normalizer.normalizer_data(data)


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
    idenpendents_vars.data_set = normalizer.normalizer_data(data)
    
    idenpendents_vars.join_data(objective_var.data_set)
    
    cv = CrossValidation( 10, "Exited")
    
    cv.genered_folds(idenpendents_vars)
    cv.k_fold_validation()    
    
pruebaFolds()    
    
    