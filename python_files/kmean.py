from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read():
    wage = pd.read_csv('wage.csv')

    unemployment = pd.read_csv("unemployment.csv").drop('index', 1)
    education = pd.read_csv("education.csv").drop('index', 1)
    df = pd.merge(wage, unemployment, left_on='Zipcode', right_on='FIPS_Code', how='inner').drop('FIPS_Code', axis=1)
    df = pd.merge(df, education, left_on='Zipcode', right_on='FIPS Code', how='inner').drop('FIPS Code', axis=1)
    return df

def call():
    from sklearn.datasets import load_digits
    from sklearn.decomposition import PCA
    from sklearn.cluster import KMeans
    import numpy as np

    # Load Data
    data = load_digits().data
    pca = PCA(2)

    # Transform the data
    df = pca.fit_transform(data)

    # Import KMeans module
    from sklearn.cluster import KMeans

    # Initialize the class object
    kmeans = KMeans(n_clusters=9)

    # predict the labels of clusters.
    label = kmeans.fit_predict(df)

    # Getting unique labels
    u_labels = np.unique(label)

    # plotting the results:
    for i in u_labels:
        plt.scatter(df[label == i, 0], df[label == i, 1], label=i)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    '''
    df = read()
    X = df[["Result", "unemp_percent", "edu_percent"]].to_numpy()
    kmeans = KMeans(n_clusters=9, random_state=0).fit(X)
    label = kmeans.labels_
    filtered_label2 = df[label == 2]

    filtered_label8 = df[label == 8]

    # Plotting the results
    plt.scatter(filtered_label2[:, 0], filtered_label2[:, 1], color='red')
    plt.scatter(filtered_label8[:, 0], filtered_label8[:, 1], color='black')
    plt.show()
    print(kmeans.labels_)
    '''
    call()