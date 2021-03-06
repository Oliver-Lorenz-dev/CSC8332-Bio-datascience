#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

processed_data = pd.read_pickle('/home/c0059478/Documents/8332/data/patients_processed.pkl.gz')

original_data = pd.read_csv("/opt/data/report_psoriasis/data.csv")

# number of missing values per attribute
value_counts = original_data.isna().sum(axis=0)

value_list = []
cat_list = ['ID','ENTRY_DATE','SEX','BMI','SKIN_TYPE','SEASONAL_FLARE','SMOKING','ALCOHOL','BASELINE_CRP',
            'BASELINE_ZINC','BASELINE_CALCIUM','BASELINE_ADJ_CALCIUM','BASELINE_MAGNESIUM',
           'BASELINE_ALBUMIN', 'BASELINE_SELENIUM','BASELINE_VIT_D']

# get percentage of missing values
for value in value_counts:
    value = ((value/96)*100)
    value_list.append(value)

# convert lists back to series
percentage_series = pd.Series(value_list, index = cat_list) 
percentage_series

# plot new series
#fig, p = plt.subplots()

percentage_series.plot(kind = 'barh')
plt.xlabel("Percentage of values missing")
plt.ylabel("Attribute")
plt.title("Figure 1")

# save figure
plt.savefig("./results/figure1.png", dpi=200)
