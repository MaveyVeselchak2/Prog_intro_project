import parse as par
import correlation as cor
from predict import predict
from top_analytics import calculate_top_analytics
import patterns as pat


if __name__ == '__main__':
    df = par.parse_pipeline("Data/student_success_factors.csv")
    print("\nЗапуск анализа топ-20 студентов: \n")
    calculate_top_analytics(df, 20)
    print("\nПостроение графиков зависимостей: \n")
    cor.plot_correlations(df)
    print("\nПоиск паттернов: \n")
    pat.patterns(df)

    print("\nПоиск коэффициентов для предсказания: \n")
    predict(df)


