#целью этой программы является прогназирование оценки студента изходя из его посещаемости и количество потраченых
# на учебу часов, тк в резултате анализа таблицы была выявлена кореляция между этими показателями и итоговой оценкой
# Работу выполнил Немировский Матвей


#вычисляем среднее влияние фактора на оценку
def mid_impact(df, column_name):
    res = 0.0
    count = 0

    for i in range(len(df)):
        try:
            column_value = df[column_name].iloc[i]
            exam_score = df['exam_score'].iloc[i]

            if column_value != 0:
                res += float(exam_score) / column_value
                count += 1
        except:
            continue

    return res / count if count > 0 else 0.0


def predict(df):
    #считаем базовые влияния
    impact_hours_studied = mid_impact(df, 'hours_studied')
    impact_attendance = mid_impact(df, 'attendance')

    print(f"  Влияние hours_studied: {impact_hours_studied:.4f}")
    print(f"  Влияние attendance: {impact_attendance:.4f}")



    # создаем массив для хранения ошибок для разных коэффициентов [i, j, error]
    # Коэффициенты: i для hours (1-10), j для attendance (1-10) => 100 вариантов

    inaccuracies = [0,0, 100.0]
    lust_inaccuracies = [0,0, 0.0]

    total_students = len(df)

    # Перебираем все комбинации коэффициентов
    for i in range(1, 100):  # Коэффициент для attendance (1-10)
        lust_inaccuracies = inaccuracies.copy()
        # Сохраняем коэффициенты
        inaccuracies[0] = i
        inaccuracies[1] = 100 - i
        total_error = 0.0

        # для каждого студента вычисляем ошибку прогноза
        for student_idx in range(total_students):

            hours = df['hours_studied'].iloc[student_idx]
            attendance = df['attendance'].iloc[student_idx]
            actual_score = df['exam_score'].iloc[student_idx]

            # прогнозируем оценку
            pred = ((hours * impact_hours_studied * i / 100) +
                    (attendance * impact_attendance * (100 - i)/100))

            # вычисляем ошибку по модулю
            error = abs(pred - actual_score)
            total_error += error

        # Сохраняем среднюю ошибку
        inaccuracies[2] = total_error / total_students

        #тк функция среднеей ошибки очевидно имеет один экстренум, то как только предыдущее значение меньше, оно оптимально
        if lust_inaccuracies[2] < inaccuracies[2]:
            break



    # пишем результаты
    best_hs, best_att, best_error = lust_inaccuracies

    print(f"  Коэффициент для hours_studied: {best_hs/100}")
    print(f"  Коэффициент для attendance: {best_att/100}")
    print(f"  Средняя ошибка: {best_error:.2f} баллов")

    print(f"\n4. ФОРМУЛА ПРОГНОЗА:")
    print(
        f"   Оценка = (часы × {impact_hours_studied:.2f} × {best_hs/100} + посещаемость × {impact_attendance:.3f} × {best_att/100}))")
