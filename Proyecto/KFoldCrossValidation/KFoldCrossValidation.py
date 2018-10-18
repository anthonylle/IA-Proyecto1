from Proyecto.Folds.Folds import Folds
from Proyecto.DataSet.DataFrame import DataFrame


class KFoldCrossValidation():

    def __init__(self, k, output_column):
        self.folds = Folds(k, output_column)

    # input: object of DataFrame class
    # function: genered the folds
    # output: none
    def genered_folds(self, data_frame):
        self.folds.created_folds(data_frame)

    """ 
    aqui verifica que las varas esten bien  
    """

    def validated_folds(self):
        self.folds.check_classes();
        pass

    # input: object of DataFrame class
    # function: cross validation function
    # output: none
    def k_fold_validation(self, data_frame):
        self.genered_folds(data_frame)
        for i in range(self.folds.size()):
            test = self.folds.get_test(i)
            train_list = self.folds.get_train(i)
            # no se que carajos sigue