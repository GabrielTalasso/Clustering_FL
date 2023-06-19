import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as spc
from scipy.cluster.hierarchy import dendrogram, linkage

sns.set()

file_path = './clustering_fl/data/ckas.pickle'

with open(file_path, "rb") as f:
  ckas = pickle.load(f)

pdist = spc.distance.pdist(ckas)
linkage = spc.linkage(pdist, method='ward')
idx = spc.fcluster(linkage, 1.2, 'distance' )

dendrogram(linkage, color_threshold=1.2)
plt.show()
