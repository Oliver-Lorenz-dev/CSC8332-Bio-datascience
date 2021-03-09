#!/usr/bin/env python3

import pandas as pd
import seaborn
import matplotlib.pyplot as plt

processed_data = pd.read_pickle('/home/c0059478/Documents/8332/data/patients_processed.pkl.gz')

seaborn.set_style("whitegrid")
seaborn.set_context("paper")
seaborn.set_palette("deep", color_codes=True)

# plot heatmap
fig5 = plt.figure(figsize=(15,15))
heatmap = seaborn.heatmap(processed_data.corr(),cmap='Blues')
heatmap.set_title('Figure 5 - Heatmap of Psoriasis data', fontsize = 30)
# fix labels overlapping
plt.xticks(rotation=90)
plt.yticks(rotation=45)
fig5.savefig("./results/figure5.png", dpi=200)


