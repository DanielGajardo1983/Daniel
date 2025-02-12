import pandas as pd

def calculate_demographic_data(print_data=True):
    # Leer los datos desde el archivo 'adult.data'
    df = pd.read_csv('adult.data.csv', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ])

    # ¿Cuántas personas de cada raza están representadas en este conjunto de datos? Esto debe ser una serie de Pandas con los nombres de las razas como etiquetas de índice.
    race_count = df['race'].value_counts()

    # ¿Cuál es la edad promedio de los hombres?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # ¿Cuál es el porcentaje de personas que tienen un título de licenciatura?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # ¿Qué porcentaje de personas con educación avanzada (`Bachelors`, `Masters`, o `Doctorate`) ganan más de 50K?
    # ¿Qué porcentaje de personas sin educación avanzada ganan más de 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Porcentaje con salario >50K
    higher_education_rich = (higher_education['salary'] == '>50K').mean() * 100
    lower_education_rich = (lower_education['salary'] == '>50K').mean() * 100

    # ¿Cuál es el número mínimo de horas que una persona trabaja por semana (característica horas-por-semana)?
    min_work_hours = df['hours-per-week'].min()

    # ¿Qué porcentaje de las personas que trabajan el número mínimo de horas por semana tienen un salario mayor a 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

    # ¿Qué país tiene el mayor porcentaje de personas que ganan más de 50K?
    country_salary_group = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)
    country_salary_group['>50K'] = country_salary_group['>50K'] * 100
    highest_earning_country = country_salary_group['>50K'].idxmax()
    highest_earning_country_percentage = country_salary_group['>50K'].max()

    # Identificar la ocupación más popular para aquellos que ganan >50K en India.
    india_high_salary = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_salary['occupation'].value_counts().idxmax()

    # NO MODIFICAR POR DEBAJO DE ESTA LÍNEA

    if print_data:
        print("Número de personas de cada raza:\n", race_count) 
        print("Edad promedio de los hombres:", round(average_age_men, 1))
        print(f"Porcentaje con título de licenciatura: {round(percentage_bachelors, 1)}%")
        print(f"Porcentaje con educación avanzada que ganan >50K: {round(higher_education_rich, 1)}%")
        print(f"Porcentaje sin educación avanzada que ganan >50K: {round(lower_education_rich, 1)}%")
        print(f"Tiempo mínimo de trabajo: {min_work_hours} horas/semana")
        print(f"Porcentaje de ricos entre los que trabajan menos horas: {round(rich_percentage, 1)}%")
        print("País con el mayor porcentaje de ricos:", highest_earning_country)
        print(f"Mayor porcentaje de ricos en un país: {round(highest_earning_country_percentage, 1)}%")
        print("Ocupaciones más populares en India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }
