from Normalizer.Normalizer import Normalizer
from DataSet.DataFrame import DataFrame

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
    
    # take column from idenpendents_vars
    objective_var.data_set = idenpendents_vars.cut_column("Exited")
    
    #normalizer data
    data =idenpendents_vars.data_set
    idenpendents_vars.data_set = normalizer.normalizer_data(data)
    
    data = objective_var.data_set
    objective_var.data_set = normalizer.normalizer_data(data)
    
    idenpendents_vars.to_excel("independents.xlsx")
    
    objective_var.to_excel("objective.xlsx")
    

    