#!/usr/bin/env python3

import pandas as pd

data1 = pd.read_csv("/opt/data/report_psoriasis/data.csv")
data2 = pd.read_excel("/opt/data/report_psoriasis/pasi_scores.xlsx")

# set to categorical variables
data1.ALCOHOL = data1.ALCOHOL.astype("category")
data1.SEASONAL_FLARE = data1.SEASONAL_FLARE.astype("category")
data1.SEX = data1.SEX.astype("category")
data1.SKIN_TYPE = data1.SKIN_TYPE.astype("category")
data1.SMOKING = data1.SMOKING.astype("category")

# fill NaN with mean values as data is continuous
data1.BMI = data1.BMI.fillna(data1.BMI.mean())
data1.BASELINE_CRP = data1.BASELINE_CRP.fillna(data1.BASELINE_CRP.mean())
data1.BASELINE_ZINC = data1.BASELINE_ZINC.fillna(data1.BASELINE_ZINC.mean())
data1.BASELINE_CALCIUM = data1.BASELINE_CALCIUM.fillna(data1.BASELINE_CALCIUM.mean())
data1.BASELINE_ADJ_CALCIUM = data1.BASELINE_ADJ_CALCIUM.fillna(data1.BASELINE_ADJ_CALCIUM.mean())
data1.BASELINE_MAGNESIUM = data1.BASELINE_MAGNESIUM.fillna(data1.BASELINE_MAGNESIUM.mean())
data1.BASELINE_ALBUMIN = data1.BASELINE_ALBUMIN.fillna(data1.BASELINE_ALBUMIN.mean())
data1.BASELINE_SELENIUM = data1.BASELINE_SELENIUM.fillna(data1.BASELINE_SELENIUM.mean())
data1.BASELINE_VIT_D = data1.BASELINE_VIT_D.fillna(data1.BASELINE_VIT_D.mean())

data1.set_index('ID', inplace = True)

# drop NaN on row 11
data2 = data2.dropna(how="all", axis=1)

# fill missing data via interpolation
data2 = data2.T.interpolate(limit_direction="forward", limit_area="inside")

# reorient data
data2 = data2.T

data2.set_index('ID', inplace = True)

# normalise data
data2 = data2.subtract(data2.min(axis = 1), axis = 0)
data2 = data2.div((data2.max(axis = 1) - data2.min(axis = 1)), axis = 0)

# merge on index
final_df = data1.merge(data2, left_index= True, right_index= True)

