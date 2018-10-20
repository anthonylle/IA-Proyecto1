import math as m
import pandas as pd

class NumberValues():

    #  --------------Z score-----------------------------------
    # -----------------------------------------------------------
    # input: int: media , list of x values
    # function: sum all square of  x- media
    # output: int: sum
    def square_sum(self, media, Xs):
        sum = 0
        for i in range(len(Xs)):
            sub = Xs[i][0] - media
            temp = pow(sub, 2)
            sum = sum + temp
        return sum

    # -----------------------------------------------------------
    # input: int: n, int: media, list of x values
    # function: calculate standar desviation
    # output: number with the standar desviation
    def stand_deviation(self, n, media, Xs):

        square_sum = self.square_sum(media, Xs)
        sq_div_n = square_sum / n
        sqrt = m.sqrt(sq_div_n)

        return sqrt

    # -----------------------------------------------------------
    # input: list of x values, int: media, int: standar desviation
    # function: do z score formula
    # output: list with the scores
    def z_score_formula(self, Xs, media, stand_desviation):

        scores = []

        for i in range(len(Xs)):
            result = (Xs[i][0] - media) / stand_desviation
            scores += [[result]]
        return scores

    # -----------------------------------------------------------
    # input: list of scores, string: name of column
    # function: create a dataframe column
    # output: pandas dataframe
    def zs_column(self, data, name):

        df = pd.DataFrame(data, columns=[name])
        return df

    # -----------------------------------------------------------
    # input: a pandas series
    # function: convert a pandas series in a int
    # output: a number
    def series_toInt(self, pd_series):
        ltemp = pd_series.tolist()
        return ltemp[0]

    # -----------------------------------------------------------
    # input: pandas dataframes, string: column name
    # function: do the calculate of s-score
    # output: pandas dataframe
    def z_score(self, data_set, column_name):
        sum = self.series_toInt(data_set.sum())
        n = data_set.shape[0]
        media = sum / n
        Xs = data_set.iloc[:, :].values
        # nparray to list
        Xs = Xs.tolist()
        stand_desviation = self.stand_deviation(n, media, Xs)
        data = self.z_score_formula(Xs, media, stand_desviation)
        df = self.zs_column(data, column_name)
        return df
