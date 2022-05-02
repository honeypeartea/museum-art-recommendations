import pandas as pd
import numpy as np



def read():
    df = pd.read_csv('FR_GPA_by_Inst_data.csv')

    df = df[~df['Measure Values'].isnull()]
    df = df[~df['Calculation1'].isnull()]
    df = df[~df['Measure Names'].isin(['Enrl GPA'])]

    l = df['Calculation1'].tolist()
    name = []
    school_id = []
    for i in range(len(l)):
        a = l[i][:-6]
        b =l[i][-6:]
        name.append(a)
        school_id.append(int(b))
    df['name'] = name
    df['school_id'] = school_id
    df = df.drop('Calculation1', 1)
    gk = df.groupby(['Fall Term', 'Campus'])['Measure Values'].mean()
    gk.to_csv("gpa.csv", sep=',', encoding='utf-8')
    return gk




if __name__ == '__main__':
    print(read())