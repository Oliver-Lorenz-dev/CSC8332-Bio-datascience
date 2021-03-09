#!/usr/bin/env python3

import pandas as pd
import seaborn

processed_data = pd.read_pickle('/home/c0059478/Documents/8332/data/patients_processed.pkl.gz')

seaborn.set_style("whitegrid")
seaborn.set_context("paper")
seaborn.set_palette("deep", color_codes=True)

# pairplot
pair_plot = seaborn.pairplot(processed_data,vars=['PASI_WEEK_0','PASI_WEEK_2','PASI_WEEK_5'])

# save plot
pair_plot.savefig("./results/figure4.png", dpi=200)
