import configparser as cp
import pandas as pd
from scipy.stats import mode
import scipy as sp
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
entropy = importr('entropy')


# todo 1. create function to read configuration
# default value is "params.ini"
def get_config_file(config_file_path="params.ini"):
    config = cp.ConfigParser()
    config.read(config_file_path)
    return config


# todo : Read CSV files and return the data frame
def read_csv_file(csv_file_path):
    return pd.read_csv(csv_file_path)


# todo : read labels and features
# the default values are defined in the arguments, can be changed dynamically
def get_labels_and_features(config, section='mandatory', label='labels', features='features'):
    label = config[section][label]
    features = config[section][features]
    features = features.split(",")
    return label, features


# todo 2. Methods to deal with different type of data types
# here we need to care about factors, NAs : need to convert them to appropriate values
# should give the output processed values
# right now implemented for two columns who can take sertain values and the data frame needs to be displayed accordingly
# need to test this code, dont know who this will react
def filter_columns_on_values(data, col_val_pair_list):
    items = col_val_pair_list.items()
    return data.loc[(data[items[0][0]] == items[0][1]) & (data[items[1][0]] == items[1][1]), data]


# used to find number of NAs in columns and Rows
def num_missing(x):
    return sum(x.isnull())


# replaces NA with mode : value with the maximum frequency
def replace_na_by_mode(data, col):
    data[col].fillna(mode(data[col]).mode[0], inplace=True)
    return data


# Determine pivot table : dont know how to use
def pivot_table(data, col_list):
    impute_groups = data.pivot_table(values=[col_list[0]], index=[col_list[1], col_list[2], col_list[3]],
                                     aggfunc=sp.mean)
    print impute_groups
    return impute_groups


#
def percent_convert(ser):
    return ser / float(ser[-1])


# used to quickly analyze the two columns and there dependencies
def cross_tab(data, col1, col2):
    return pd.crosstab(data[col1], data[col2], margins=True).apply(percent_convert, axis=1)


# used to sort data frame based on two columns
def sort_data_frame(df, col1, col2):
    data_sorted = df.sort_values([col1, col2], ascending=False)
    data_sorted[[col1, col2]].head(10)
    return data_sorted


# Define a generic function using Pandas replace function
def coding(col, code_dict):
    col_coded = pd.Series(col, copy=True)
    for key, value in code_dict.items():
        col_coded.replace(key, value, inplace=True)
    return col_coded


def data_frame_dtype(data):
    return data.dtype


# storing column factors to the features configuration file
def store_col_factors(data, params_file="params.ini"):
    cols = data_frame_dtype(data)
    for col in cols:
        print col[0], col[1]


def get_levels(col, data, conf):
    ro.r('setwd("' + conf["mandatory"]["working_directory"] + '")')
    ro.r('train <- read.csv("train.csv")')
    levels = ro.r('levels(train$' + col + ')')
    length = ro.r('length(levels(train$' + col + '))')
    return levels, length


def fillna_by_value(df, value):
    df = df.fillna(value)
    return df


# fill column by median
def fillna_by_median(df, col):
    median_age = df[col].dropna().median()
    if len(df.col[df.col.isnull()]) > 0:
        df.loc[(df.col.isnull()), col] = median_age


def rstr(df):
    return df.shape, df.apply(lambda x: [x.unique()])


# remove all data containing nulls(rows)
def remove_null(df):
    return df.dropna(how='any')


def df_info(df):
    return df.info()


# to save all col feature to to features.ini file
def store_features_as_dict(conf, feature_dict_file="features.ini", section_name="features"):
    # get all the features
    features = conf['mandatory']['features'].split(',')
    df = read_csv_file(csv_file_path=conf['mandatory']['train_csv_file_path'])
    con = cp.ConfigParser()
    con.add_section(section_name)
    # here we are dealing with missing values, filling with zero(assumption : no effect of missing values)

    for feature in features:

        # get all the levels
        feature_levels, length = get_levels(feature, df, conf)
        if length[0] is not 0:
            # make dictionary of all the features with numeric values
            ls = list(feature_levels)
            dict = {item: index + 1 for index, item in enumerate(ls)}
            # and store the feature in the features.ini

            # add the settings to the structure of the file

            con.set(section_name, str(feature), str(dict))

    with open(feature_dict_file, "wb") as config_file:
        con.write(config_file)


        # conf = get_config_file()
        # train = read_csv_file(csv_file_path=conf['mandatory']['train_csv_file_path'])
        # rstr(train)
        # store_features_as_dict(conf)
        #
        # conf_features = get_config_file("features.ini")
        # print conf_features

        # train = train.dropna(how='any')
        # rstr(train)


# read data frame from csv file
        # train = read_csv_file(csv_file_path=conf['mandatory']['train_csv_file_path'])
        # store_features_as_dict(conf, "feat.ini", "feat")

        #
        # def calc_bin_entropy():
        #     ro.r('setwd("D:/codes/datasets/kaggle/Titanic")')
        #     ro.r('train <- read.csv("train.csv")')
        #     survived = ro.r('x = train$Survived')
        #     pclass = ro.r('z = train$Pclass')
        #     sex = ro.r('s = as.integer(train$Sex)')
        #     # calculating entropy between Survived and Pclass
        #     binclassification = ro.r('y2 = entropy::discretize2d(x,z,2,3,r1=range(x),r2=range(z))')
        #     ent = ro.r('entropy(y2)')
        #     return binclassification
        #     print ent
        #
        #     # todo : All R functions should also come here
        #
        # # will be very useful for analysis
