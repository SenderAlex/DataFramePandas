import pandas as pd

data = {
    'student name': [f'student {student + 1}' for student in range(10)],
    'mathematics': [10, 4, 7, 8, 9, 6, 9, 4, 5, 10],
    'physics': [8, 6, 9, 7, 5, 4, 10, 3, 2, 8],
    'chemistry': [6, 2, 5, 7, 3, 9, 8, 6, 8, 4],
    'english': [5, 6, 8, 7, 8, 9, 4, 3, 7, 5],
    'geography': [9, 9, 8, 6, 4, 10, 7, 7, 10, 5]
}

# Создание DataFrame
data_df = pd.DataFrame(data)
print(data_df)
print('')

# средние оценки по каждому предмету
print(f'Средняя оценка по математике равна {data_df['mathematics'].mean()}')
print(f'Средняя оценка по физике равна {data_df['physics'].mean()}')
print(f'Средняя оценка по химии равна {data_df['chemistry'].mean()}')
print(f'Средняя оценка по английскому равна {data_df['english'].mean()}')
print(f'Средняя оценка по географии равна {data_df['geography'].mean()}')
print('')

# медианные оценки по каждому предмету
print(f'Медианная оценка по математике равна {data_df['mathematics'].median()}')
print(f'Медианная оценка по физике равна {data_df['physics'].median()}')
print(f'Медианная оценка по химии равна {data_df['chemistry'].median()}')
print(f'Медианная оценка по английскому равна {data_df['english'].median()}')
print(f'Медианная оценка по географии равна {data_df['geography'].median()}')
print('')

# Q1 и Q3 для оценок по математике
Q1_math = data_df['mathematics'].quantile(0.25)
print(f'Первый квантиль оценок по математике равен {Q1_math}')

Q3_math = data_df['mathematics'].quantile(0.75)
print(f'Третий квантиль оценок по математике равен {Q3_math}')

# IQR по математике
IQR_math = Q3_math - Q1_math
print(f'IQR по математике равен {IQR_math}')
print('')

# стандартное отклонение по предметам
print(f'Стандартное отклонение по математике равно {data_df['mathematics'].std()}')
print(f'Стандартное отклонение по физике равно {data_df['physics'].std()}')
print(f'Стандартное отклонение по химии равно {data_df['chemistry'].std()}')
print(f'Стандартное отклонение по английскому равно {data_df['english'].std()}')
print(f'Стандартное отклонение по географии равно {data_df['geography'].std()}')