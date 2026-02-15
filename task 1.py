from datetime import datetime


def get_days_from_today(date):
    """
    Повертає кількість днів від заданої дати до сьогодні.
    Формат дати: YYYY-MM-DD
    """
    try:
        # перетворюємо рядок у дату
        given_date = datetime.strptime(date, "%Y-%m-%d").date()

        # поточна дата (без часу)
        today = datetime.today().date()

        # різниця
        delta = today - given_date

        return delta.days

    except ValueError:
        print("Неправильний формат дати. Використовуйте YYYY-MM-DD")
        return None


if __name__ == "__main__":
    # приклад перевірки
    print(get_days_from_today("2020-10-09"))