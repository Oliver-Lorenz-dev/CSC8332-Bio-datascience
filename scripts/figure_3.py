#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn

processed_data = pd.read_pickle('/home/c0059478/Documents/8332/data/patients_processed.pkl.gz')

seaborn.set_style("whitegrid")
seaborn.set_context("paper")
seaborn.set_palette("deep", color_codes=True)

# make figure for subplots
fig3 = plt.figure(figsize=(10,5))
ax1 = fig3.add_subplot(121)
ax2 = fig3.add_subplot(122)
ax1.set_title('Tobacco consumption and BMI')
ax2.set_title('Alcohol consumption and BMI')
# plot histograms
seaborn.histplot(x="BMI",hue = 'SMOKING' , multiple="stack", data=processed_data, ax=ax1)
seaborn.histplot(x="BMI",hue = 'ALCOHOL' , multiple="stack", data=processed_data, ax=ax2)

# save figure
fig3.savefig("./results/figure3.png", dpi=200)
