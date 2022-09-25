#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:34:31 2021

@author: andrew (kinda)
"""

import numpy as np
import pandas as pd
import pylab as plt
from sampleclim import samplepico,samplesurf

# The number of allowable model runs
n_samples = 500

post_loc = 'config/X_posterior_v2.csv.gz'
#post_loc = '/import/c1/ICESHEET/ICESHEET/uaf-antarctica/X_posterior_v2.csv.gz'

X_posterior = pd.read_csv(post_loc)

# Names of all the variables that do not appear in X
keys = list(X_posterior.keys()[1:])


mc_indices = np.random.choice(range(X_posterior.shape[0]), n_samples)
X_sample = X_posterior.to_numpy()[mc_indices, 1:]

#%%

keys = keys[0:6]
X_sample = X_sample[0:n_samples,0:6]

appendkeys = ['pico_g','pico_c','surf_anom']
for k in appendkeys:
    # print(k)
    keys.append(k)

X_sample = np.concatenate((X_sample,np.zeros((n_samples,len(appendkeys)))),axis=1)
for n in range(n_samples):
    X_sample[n,6],X_sample[n,7] = samplepico()
    X_sample[n,8] = samplesurf()

csn=150
checkset = X_sample[:csn]
print(f'Surf model 0: {np.sum(checkset[:,8]==0)}')
print(f'Surf model 1: {np.sum(checkset[:,8]==1)}')
print(f'Surf model 2: {np.sum(checkset[:,8]==2)}')
print(f'Pico model >1: {np.sum(checkset[:,7]>1.)}')

#%%

# Convert to Pandas dataframe, append column headers, output as csv
df = pd.DataFrame(X_sample)
df.to_csv("config/random_posterior_samples.csv", header=keys, index=True)

#%%

fig, axs = plt.subplots(len(keys[0:6]), 1)
fig.set_size_inches(6, 8)
fig.subplots_adjust(hspace=0.45)
for i, key in enumerate(keys[0:6]):
    axs[i].hist(X_sample[:, i], 20, density=True, histtype="step")
    axs[i].set_ylabel(key)
fig.savefig("parameter_histograms.pdf", bbox_inches="tight")

X_sample_small = X_sample[:150]

fig, axs = plt.subplots(len(keys[0:6]), 1)
fig.set_size_inches(6, 8)
fig.subplots_adjust(hspace=0.45)
for i, key in enumerate(keys[0:6]):
    axs[i].hist(X_sample[:, i], 20, density=True, histtype="step")
    axs[i].set_ylabel(key)
fig.savefig("parameter_histograms_100.pdf", bbox_inches="tight")