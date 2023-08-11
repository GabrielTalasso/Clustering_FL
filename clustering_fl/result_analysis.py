import pandas as pd
import pickle
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = 'MotionSense'
n_rounds = 15
n_clients = 24
n_clusters = [1,2, 5,8, 'Affinity']
n_clusters = [ 5, 10, 15]
n_clusters = [1, 2, 5, 10, 'POC', 'Affinity', '5RCS', '5KCENTER', '5KCENTER_random']

path = './experiments/MNIST/noniid'
#path = './experiments/MNIST/noniid'
path = './experiments/MotionSense'

for c in n_clusters:
    acc =  pd.read_csv(f'{path}/acc_{dataset}_{n_clients}clients_{c}clusters.csv',
                       names=['_', 'client', 'acc', 'loss'])
    if c==1:
        label_clusters = 'FedAvg'
    else:
        label_clusters = f'{c} clusters'

    rounds = np.ones(n_clients)
    for r in range(2,n_rounds+1):
        rounds = np.concatenate((rounds, np.ones(n_clients)*r), axis = None)

    if c == 'POC' or c == '5RCS' or c == '5KCENTER_random':
        rounds = acc['_']

    acc['round'] = rounds


    sns.lineplot(acc.groupby('round').mean(), y = 'acc', x = 'round', legend='brief', label=label_clusters)
plt.ylim(0.7, 0.82)
plt.show()

## comparing with random clusters:
#c = 10
#for i in range(1,4):
#    acc_random = pd.read_csv(f'{path}/random_clusters/acc{i}_{dataset}_{n_clients}clients_{c}clusters.csv',
#                       names=['_', 'client', 'acc', 'loss']).drop('_', axis = 1)
#    acc_random['round'] = rounds
#
#    sns.lineplot(acc_random.groupby('round').mean(), y = 'acc', x = 'round', legend='brief', label=f'random{i}')
#
#acc =  pd.read_csv(f'{path}/acc_{dataset}_{n_clients}clients_{c}clusters.csv',
#                       names=['_', 'client', 'acc', 'loss']).drop('_', axis = 1)
#acc['round'] = rounds
#sns.lineplot(acc.groupby('round').mean(), y = 'acc', x = 'round', legend='brief', label='cka_clusters')
#
#acc =  pd.read_csv(f'results/acc_MNIST_10clients_5clusters.csv',
#                       names=['_', 'client', 'acc', 'loss']).drop('_', axis = 1)
#acc['round'] = rounds
#
#sns.lineplot(acc.groupby('round').mean(), y = 'acc', x = 'round', legend='brief', label='cka_clusters_noise')
#
#plt.show()
#
#
### comparing with clustering with weights
#c = 10
#acc_w = pd.read_csv(f'{path}/w_clustering/acc1_{dataset}_{n_clients}clients_{c}clusters.csv',
#                       names=['_', 'client', 'acc', 'loss']).drop('_', axis = 1)
#acc_w['round'] = rounds
#
#sns.lineplot(acc_w.groupby('round').mean(), y = 'acc', x = 'round', legend='brief', label=f'w/weights')
#
#acc_random = pd.read_csv(f'{path}/random_clusters/acc{3}_{dataset}_{n_clients}clients_{c}clusters.csv',
#                       names=['_', 'client', 'acc', 'loss']).drop('_', axis = 1)
#acc_random['round'] = rounds
#
#sns.lineplot(acc_random.groupby('round').mean(), y = 'acc', x = 'round', legend='brief', label=f'random{1}')
#
#acc =  pd.read_csv(f'{path}/acc_{dataset}_{n_clients}clients_{c}clusters.csv',
#                       names=['_', 'client', 'acc', 'loss']).drop('_', axis = 1)
#acc['round'] = rounds
#
#sns.lineplot(acc.groupby('round').mean(), y = 'acc', x = 'round', legend='brief', label='cka_clusters')
#
#acc =  pd.read_csv(f'{path}/acc_{dataset}_{n_clients}clients_{c}clusters.csv',
#                       names=['_', 'client', 'acc', 'loss']).drop('_', axis = 1)
#acc['round'] = rounds
#
#sns.lineplot(acc.groupby('round').mean(), y = 'acc', x = 'round', legend='brief', label='cka_clusters')
#
#
#plt.show()
#