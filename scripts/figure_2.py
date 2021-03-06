#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

processed_data = pd.read_pickle('/home/c0059478/Documents/8332/data/patients_processed.pkl.gz')

# plot histogram
processed_data.hist(figsize = (20,15))

# save figure
plt.savefig("./results/figure2.1.png", dpi=200)

# value counts for categorical data
smoking_counts = processed_data.SMOKING.value_counts()
seasonal_flare_counts = processed_data.SEASONAL_FLARE.value_counts()
alcohol_counts = processed_data.ALCOHOL.value_counts()
skin_type_counts = processed_data.SKIN_TYPE.value_counts()

# plot bar charts for non numeric data

# smoking and alcohol
fig = plt.figure(figsize=(10,9))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.set_title('Tobacco consumption')
ax1.set_xlabel('Smoking status')
ax1.set_ylabel('Count')
ax2.set_title('Alcohol consumption')
ax2.set_xlabel('Alcohol consumption')
ax2.set_ylabel('Count')
smoking_counts.plot(kind='bar',ax=ax1)
alcohol_counts.plot(kind='bar', ax=ax2)
fig.savefig("./results/figure2.2.png", dpi=200)

# skin and seasons
fig2 = plt.figure(figsize=(10,9))
ax1 = fig2.add_subplot(121)
ax2 = fig2.add_subplot(122)
ax1.set_title('Skin types')
ax1.set_xlabel('Skin type')
ax1.set_ylabel('Count')
ax2.set_title('Seasonal flare')
ax2.set_xlabel('Seasonal flare')
ax2.set_ylabel('Count')
skin_type_counts.plot(kind='bar',ax=ax1)
seasonal_flare_counts.plot(kind='bar', ax=ax2)
fig2.savefig("./results/figure2.3.png", dpi=200)
