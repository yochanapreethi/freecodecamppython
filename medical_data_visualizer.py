import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

df['overweight'] = (df['weight']/((df['height']/100)**2) > 25).astype(int)

df[['gluc','cholesterol']] = (df[['gluc','cholesterol']] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    fig = sns.catplot(data = df_cat, kind='count',  x='variable', hue='value', col='cardio').set(ylabel = 'total').fig

    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[ 
        ( df['ap_lo'] <= df['ap_hi'] ) & 
        ( df['height'] >= df['height'].quantile(0.025) ) & 
        ( df['height'] <= df['height'].quantile(0.975) ) & 
        ( df['weight'] >= df['weight'].quantile(0.025) ) & 
        ( df['weight'] <= df['weight'].quantile(0.975) ) 
    ]

    corr = df_heat.corr()

    mask = np.triu(corr)

    fig, ax =  plt.subplots()
    
    ax = sns.heatmap(corr, mask=mask, annot=True, fmt='0.1f', square=True)

    fig.savefig('heatmap.png')
    return fig