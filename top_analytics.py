# Импортируем функцию load_and_prepare_data из файла parse.py
import pandas as pd

# Создаем функцию с параметром filename
def calculate_top_analytics(df: pd.DataFrame, num_top):

    # Сортируем таблицу студентов по столбцу "exam_score" 
    sorted_df = df.sort_values(by="exam_score", ascending=False)
    
    # Берем первые n строк из отсортированной таблицы
    top = sorted_df.head(20)

    print(
        f"аналитика для топ{num_top} студентов:")

    #берем все столбцы кроме экзамена
    columns_to_analyze = [col for col in top.columns if col != 'exam_score']
    # для каждого столбца начинаем аналитику
    for column_name in columns_to_analyze:
        analytics(df, column_name)
    return None
    


def analytics(top, column_name):
    max_val = top[column_name].max()
    min_val = top[column_name].min()
    avg_val = top[column_name].mean()
    mid_val = top[column_name].median()
    print(f"аналитика столбца {column_name}: "
          f"значения от {min_val} до {max_val}, медианное значение {mid_val}, среднее {avg_val}")



