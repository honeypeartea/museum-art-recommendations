
import logging
import re
import sys
from bs4 import BeautifulSoup
from queue import Queue
from urllib import parse, request
import pandas as pd
from csv import writer

if __name__ == '__main__':
    #url = "https://www.rijksmuseum.nl/nl/collectie/SK-A-4877"
    file = "/home/xmh/Desktop/courses/cs666/with_rec/rijks_with_rec.csv"
    df = pd.read_csv(file,sep=',')
    result = []
    with open('out.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        for ind in df.index:
            url = df['url'][ind]
            try:
                req = request.urlopen(url)
            except:
                print(url)
                continue
            html = req.read()
            links = re.findall("\"og:image\" content=[\"\'](.*?)[\"\']", str(html))
            if len(links) != 1:
                print("too many:",url)
            else:
                list_data = [ind, df['id'][ind], links[0]]
                print(list_data)
                writer_object.writerow(list_data)

                # result.append((ind, df['id'][ind], links[0]))
            if ind %10 ==0:
                print(ind)
        f_object.close()


    # data = pd.DataFrame(result, columns=['id', 'img_real_url'])
    # data.to_csv('out.csv')
    print("done")