
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos
df = pd.read_csv("medical_examination.csv")

# Agregar columna 'overweight'
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (df['BMI'] > 25).astype(int)
df.drop(columns=['BMI'], inplace=True)

# Normalizar las columnas 'cholesterol' y 'gluc'
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Función para dibujar el gráfico categórico
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name='total')
    
    g = sns.catplot(x="variable", y="total", hue="value", col="cardio", kind="bar", data=df_cat)
    fig = g.fig
    return fig

# Función para dibujar el heatmap
def draw_heat_map():
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]
    
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap="coolwarm", center=0)

    # 16
    fig.savefig('heatmap.png')
    return fig
