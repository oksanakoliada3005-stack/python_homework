from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        #перетворюємо рядок у дату
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        #день народження в цьому році
        birthday_this_year = birthday.replace(year=today.year)

        #якщо вже був то беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_diff = (birthday_this_year - today).days

        #якщо день народження у найближчі 7 днів
        if 0 <= days_diff <= 7:
            congratulation_date = birthday_this_year

            #переносимо якщо вихідний
            if congratulation_date.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result


if __name__ == "__main__":
    # приклад
    users = [
        {"name": "Оксана", "birthday": "1998.11.02"},
        {"name": "Іван", "birthday": "1992.02.12"},
        {"name": "Марія", "birthday": "1990.02.18"}
    ]

    print(get_upcoming_birthdays(users))
