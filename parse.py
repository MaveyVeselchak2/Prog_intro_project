import pandas as pd
import os


# ЗАГРУЗКА И ОТБОР ДАННЫХ

def load_data(path: str) -> pd.DataFrame:
    """
    Загружает CSV-файл и отбирает необходимые столбцы
    """
    df = pd.read_csv(path)

    columns = {
        "Hours_Studied": "hours_studied",
        "Attendance": "attendance",
        "Sleep_Hours": "sleep_hours",
        "Exam_Score": "exam_score",
        "Motivation_Level": "motivation",
        "Tutoring_Sessions": "tutoring_sessions",
        "Family_Income": "family_income"
    }

    df = df[list(columns.keys())]
    df = df.rename(columns=columns)

    return df



# ПРОВЕРКА КАЧЕСТВА ДАННЫХ

def data_quality_report(df: pd.DataFrame) -> bool:
    """
    Выводит краткую информацию о качестве данных
    """
    print("Размер датасета:", df.shape)

    #проверка на наличие пропусков
    missing = df.isnull().sum()
    if missing.any():
        print("Пропуски по столбцам:")
        print((df.isnull().mean() * 100).round(2).to_string())
        return True
    else:
        print("Пропусков нет")
        return False



# ОЧИСТКА И КОДИРОВАНИЕ

def clean_and_encode(df: pd.DataFrame, is_NA) -> pd.DataFrame:
    """
    Обрабатывает пропуски и кодирует категориальные признаки
    """
    # Кодирование категориальных признаков
    category_map = {
        "Low": 1,
        "Medium": 2,
        "High": 3
    }

    df["motivation"] = df["motivation"].map(category_map)
    df["family_income"] = df["family_income"].map(category_map)

    if is_NA:
        # Удаление строк с некорректными значениями
        df = df.dropna()

    return df



# ЭКСПОРТ ОЧИЩЕННЫХ ДАННЫХ

def export_clean_data(
    df: pd.DataFrame,
    path: str = "Data/cleaned_students.csv"
) -> None:
    """
    Сохраняет очищенный датасет в CSV
    """
    directory = os.path.dirname(path)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    df.to_csv(path, index=False)



# ГЛАВНЫЙ ПАЙПЛАЙН ПАРСИНГА

def parse_pipeline(path: str) -> pd.DataFrame:
    """
    Полный процесс подготовки данных
    """
    df = load_data(path)
    df = clean_and_encode(df,data_quality_report(df))
    export_clean_data(df)
    return df