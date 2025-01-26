import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")
columns = df.columns.tolist()

# 2
height = df['height'] / 100
bmi = df['weight'] / (height**2)
df['overweight'] = [1 if bmi[id] > 25 else 0 for id in df.index]


# 3
def normalise(val):
    if val <= 1:
        return 0
    return 1


for col in columns[7:9]:
    df[col] = df[col].apply(normalise)


# 4
def draw_cat_plot():
    # 5,6,7
    df_cat = pd.melt(df,
                     id_vars=['cardio'],
                     value_vars=[
                         'active', 'alco', 'cholesterol', 'gluc', 'overweight',
                         'smoke'
                     ])

    # 8
    fig = sns.catplot(data=df_cat,
                      kind='count',
                      x='variable',
                      hue='value',
                      col='cardio')
    fig.set_ylabels('total')

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    # df['ap_lo'] <= df['ap_hi'] -> diastolic pressure lower than systolic
    # df['height'] >= df['height'].quantile(0.025) -> height is more than the 2.5th percentile
    # df['height'] <= df['height'].quantile(0.975) -> height is less than the 97.5th percentile
    # df['weight'] >= df['weight'].quantile(0.025) -> weight is more than the 2.5th percentile
    # df['weight'] <= df['weight'].quantile(0.975) -> weight is less than the 97.5th percentile
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
                 & (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    ax = sns.heatmap(data=corr,
                     annot=True,
                     fmt='.1f',
                     mask=mask,
                     vmax=.3,
                     center=0,
                     square=True,
                     linewidths=.5,
                     cbar_kws={
                         'shrink': .5
                     }).figure

    # 16
    fig.savefig('heatmap.png')
    return fig
