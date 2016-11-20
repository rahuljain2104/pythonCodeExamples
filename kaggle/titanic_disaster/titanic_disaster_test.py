import pandas as pd


def rstr(df): return df.shape, df.apply(lambda x: [x.unique()])


df = pd.read_csv("D:\codes\datasets\kaggle\Titanic\\train.csv")

print(rstr(df))

lst_Pclass_survived = [0] * 6
survived = df['Survived']
pclass = df['Pclass']

for i in range(len(survived)):
    lst_Pclass_survived[survived[i] * 3 + pclass[i] - 1] += 1

print lst_Pclass_survived
