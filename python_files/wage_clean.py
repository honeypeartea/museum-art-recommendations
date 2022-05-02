import pandas as pd
import numpy as np



def read():
    df = pd.read_csv('free-zipcode-database.csv')
    df = df[['Zipcode', 'EstimatedPopulation','TotalWages']]
    df = df[~df['EstimatedPopulation'].isnull()]
    df = df[~df['TotalWages'].isnull()]
    df = df.groupby(['Zipcode'])['EstimatedPopulation','TotalWages'].sum()
    df['Result'] = df['TotalWages'] / df['EstimatedPopulation']

    df.to_csv("wage.csv", sep=',', encoding='utf-8')




    return df




if __name__ == '__main__':
    print(read())