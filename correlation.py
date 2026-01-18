import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


def plot_correlations(df: pd.DataFrame) -> None:
    """
    Строит графики зависимости экзаменационного балла от факторов.
    Сохраняет графики в файлы.
    """

    # Создаем папку для графиков
    os.makedirs("plots", exist_ok=True)

    # Графики с настройками
    plot_configs = [
        ("hours_studied", "scatter"),
        ("attendance", "scatter"),
        ("sleep_hours", "box"),
        ("motivation", "box"),
        ("tutoring_sessions", "box"),
        ("family_income", "box")
    ]

    # Строим и сохраняем
    for col, plot_type in plot_configs:
        plt.figure(figsize=(6, 4))

        if plot_type == "scatter":
            sns.scatterplot(data=df, x=col, y="exam_score")
        else:
            sns.boxplot(data=df, x=col, y="exam_score")

        plt.title(f"Exam Score vs {col}")
        plt.xlabel(col)
        plt.ylabel("exam_score")
        plt.tight_layout()

        # Сохраняем вместо показа
        plt.savefig(f"plots/exam_vs_{col}.png", dpi=100)
        plt.close()

    print("графики построены и находятся в папке plots")