import numpy as np
import pandas as pd
import re


def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else None

def modify(s):
	return ''.join([i for i in s if not i.isdigit()])

def year(s):

    return int(s[:4])

def read():
    df = pd.read_csv('uc_all.csv')
    df = df.drop('gpa', 1)
    race = df["ethcat"].unique()
    #print(race) #['Asian' 'Hispanic/ Latino' 'Domestic Unknown' 'White' 'American Indian' 'All' 'African American' 'Inter- national']
    df = df.loc[df['ethcat'].isin(['Asian','Hispanic/ Latino','White','American Indian','African American'])]
    df = df[~df["campus"].isin(['Universitywide'])]
    df = df[~df["fullname"].isnull()]

    id = df["fullname"].tolist()
    school_id = []
    for i in range(len(id)):
        num = get_trailing_number(id[i])
        school_id.append(num)

    df['school_id'] = np.array(school_id)
    df['fullname'] = df['fullname'].apply(modify)
    df['fall_term'] = df['fall_term'].apply(year)
    df = df.loc[~df['measure_name'].isin(['enr'])]
    df = df[~df["total_number"].isnull()]
    frosh = df[~df["status"].isin(['transfer'])]

    groups = frosh.groupby(['school_id','campus','fall_term','ethcat'])['measure_name'].apply(list)
    tojoin = groups.reset_index(name='listvalues')
    tojoin = tojoin.loc[~tojoin['listvalues'].isin([['adm'], ['app']])]




    new_df = pd.merge(tojoin, frosh, how='left', left_on=['school_id', 'campus', 'fall_term', 'ethcat'], right_on=['school_id', 'campus', 'fall_term', 'ethcat'])

    groups0 = new_df.groupby(['school_id', 'campus','fall_term', 'ethcat', 'measure_name'])['total_number'].agg('sum')
    tojoin0 = groups0.reset_index(name='total')

    app0 = tojoin0.loc[tojoin0['measure_name'] == 'app']
    adm0 = tojoin0.loc[tojoin0['measure_name'] == 'adm']
    new_df1 = pd.merge(app0, adm0, how='left', left_on=['school_id', 'campus', 'ethcat','fall_term'],
                       right_on=['school_id', 'campus', 'ethcat','fall_term'])
    new_df1['Result'] = new_df1['total_y'] / new_df1['total_x']
    new_df1 = new_df1.rename(columns={'total_y': 'adm', 'total_x': 'app'})
    new_df1 = new_df1.drop(['measure_name_x', 'measure_name_y'], 1)
    new_df1 = new_df1.drop_duplicates()
    #print(new_df1) #by year
    new_df1.to_csv('year_uc_all.csv', sep=',',  encoding='utf-8')




    groups1 = new_df.groupby(['school_id', 'campus', 'ethcat','measure_name'])['total_number'].agg('sum')
    tojoin1 = groups1.reset_index(name='total')
    app = tojoin1.loc[tojoin1['measure_name'] == 'app']
    adm = tojoin1.loc[tojoin1['measure_name'] == 'adm']
    new_df0 = pd.merge(app, adm, how='left', left_on=['school_id', 'campus', 'ethcat'],
                      right_on=['school_id', 'campus', 'ethcat'])
    new_df0['Result'] = new_df0['total_y'] / new_df0['total_x']
    new_df0 = new_df0.rename(columns={'total_y': 'adm', 'total_x': 'app'})
    new_df0 = new_df0.drop(['measure_name_x', 'measure_name_y'], 1)
    new_df0.to_csv('total_uc_all.csv', sep=',', encoding='utf-8')
    #print(new_df0) #total




    """
    print(len(frosh["fall_term"].unique()))
    groups = frosh.groupby('school_id')['fall_term'].apply(list)
    allyears = []
    years = groups.reset_index(name ='listvalues')
    for i in range(len(years)):
        l = years.loc[i, "listvalues"]
        unique = list(set(l))
        if len(unique) == 23:
            allyears.append(years.loc[i, "school_id"])
    print(allyears)
    """
    #transfer = df[~df["status"].isin(['frosh'])]
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   read()


