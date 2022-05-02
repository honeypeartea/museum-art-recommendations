import os, csv
import pprint

def csv2list(csvpath):
    with open(csvpath, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data

def main():
    college = 'Davis'
    year = 2014
    category = 'sat'

    if category == 'race':
        data = csv2list('../static/race.csv')
        dict = {
            'Asian': 0,
            'White': 0,
            'Hispanic/ Latino': 0,
            'African American': 0,
            'American Indian': 0
        }
        for row in data:
            for race in dict.keys():
                if row[2] == college and row[3] == race and row[7] == str(year):
                    dict[race] += float(row[6])
        # Round up to 100
        value_sum = sum(dict.values())
        dict['Asian'] += (100-value_sum)/2
        dict['White'] += (100-value_sum)/2
        pprint.pprint(dict)

    elif category == 'gpa':
        data = csv2list('../static/gpa.csv')
        for row in data:
            if row[0] == str(year) and row[1] == college:
                print(f' - Found it! GPA: {row[2]}')
                return row[2]

    elif category == 'sat':
        data = csv2list('../static/sat.csv')
        for row in data:
            if row[0] == college:
                print(f' - Found it! SAT: {row[1]}')
                return row[1]


if __name__ == '__main__':
    main()
