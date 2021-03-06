#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

processed_data = pd.read_pickle('/home/c0059478/Documents/8332/data/patients_processed.pkl.gz')

# plot histogram
processed_data.hist(figsize = (20,15))

# save figure
plt.savefig("./results/figure2.png", dpi=200)
