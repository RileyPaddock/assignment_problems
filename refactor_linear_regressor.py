from matrix import Matrix
from dataframe import DataFrame

class LinearRegressor:
    def __init__(self,data_class, prediction_column):
        self.data = data_class
        self.prediction_column = prediction_column
        self.coefficients = self.solve_coefficients()

    def solve_coefficients(self):
        coefficients = {}

        Inputs = Matrix(self.data.remove_columns([self.prediction_column]).to_array())
        Results = Matrix(self.data.remove_columns([key for key in self.data.data_dict if key != self.prediction_column]).to_array())
        x_transpose = Inputs.transpose()

        coefficients = ((x_transpose @ Inputs).inverse() @ (x_transpose @ Results)).elements

        coefficient_index = 0
        for key in self.data.remove_columns([self.prediction_column]).data_dict:
            coefficients[key] = round(coefficients[coefficient_index][0], 8)
            coefficient_index+=1
        return coefficients

    def gather_all_inputs(self,input_set):
        inputs = {}

        if len(input_set)+2< len(self.data.columns):
            for key in input_set:
                inputs[key] = input_set[key]

            for key1 in input_set:
                for key2 in input_set:
                    if key1 != key2 and (key1 + "_" + key2) not in inputs and (key2 + "_" + key1) not in inputs:
                        inputs[key1 + "_" + key2] = input_set[key1]*input_set[key2]

            inputs['constant'] = 1

        elif len(input_set)+2 == len(self.data.columns):
            inputs = {column:self.coefficients[column]*input_set[column] for column in input_set}
            inputs['constant'] = 1

        return inputs

    
    def predict(self, input_set):
        inputs = self.gather_all_inputs(input_set)
        result = sum([inputs[key]*self.coefficients[key] for key in inputs])
        return result

