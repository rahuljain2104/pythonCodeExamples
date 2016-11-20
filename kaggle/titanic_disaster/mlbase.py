import configparser as cp
import pandas as pd


class MLBase():
    def __init__(self, params_file=""):
        self.params_file = params_file

    def get_data(self, params_file=""):
        pass

    # read the csv data defined in the params file and return the same
    def read_csv_data(self):
        config = cp.ConfigParser()
        config.read(self.params_file)
        csv_file_path = config['mandatory']['csv_file_path']
        return pd.read_csv(csv_file_path)

    def process_data(self, params_file=""):
        pass
