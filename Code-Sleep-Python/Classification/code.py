import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.decomposition
from matplotlib.colors import ListedColormap
#  More accuracy
from sklearn.neighbors import KNeighborsClassifier


def accuracy(predictions, outcomes):
    # Enter your code here!
    occur = 0
    v = np.array(predictions) == np.array(outcomes)
    occur = np.sum(v)
    return occur


data = pd.read_csv('https://s3.amazonaws.com/demo-datasets/wine.csv')

df2 = data.drop('color', axis=1)  # color is redundant

numeric_data = df2.values

numeric_data = (numeric_data - np.mean(numeric_data)) / (np.std(numeric_data))


pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit(numeric_data).transform(numeric_data)

observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:, 0]
y = principal_components[:, 1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha=0.2,
            c=data['high_quality'], cmap=observation_colormap,
            edgecolors='none')
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

x = np.array([1, 2, 3])
y = np.array([1, 2, 4])

print(accuracy(x, y))

print(accuracy([], data["high_quality"]))

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(numeric_data, data['high_quality'])
# Enter your code here!

library_predictions = knn.predict(numeric_data)

print(accuracy(library_predictions, data['high_quality']))

n_rows = data.shape[0]

print()
random.seed(123)
selection = random.sample(range(n_rows), 10)

predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])

my_predictions = [
    knn.predict(predictors[training_indices, :]) for p in
    predictors[selection]]
percentage = accuracy(my_predictions, outcomes)

print(percentage)
