import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Importar los datos
    data = pd.read_csv('epa-sea-level.csv')

    # Crear un gráfico de dispersión
    fig, ax = plt.subplots()
    ax.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Primer ajuste lineal (todos los datos)
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)  # Años hasta 2050
    ax.plot(years_extended, [slope * year + intercept for year in years_extended], label='Best fit line')

    # Segundo ajuste lineal (desde el año 2000 en adelante)
    data_recent = data[data['Year'] >= 2000]  # Solo los datos de 2000 en adelante
    slope_recent, intercept_recent, _, _, _ = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])

    # Modificar para calcular la línea de ajuste solo para los años desde 2000
    years_recent = range(2000, 2051)  # Años de 2000 en adelante
    ax.plot(years_recent, [slope_recent * year + intercept_recent for year in years_recent], label='Fit line (2000+)')

    # Etiquetas y título
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Mostrar leyenda
    ax.legend()

    # Guardar la figura
    plt.savefig('sea_level_plot.png')

    return ax
