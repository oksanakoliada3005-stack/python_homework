import random

def get_numbers_ticket(min, max, quantity):

    #перевірка параметрів
    if min < 1 or max > 1000 or min > max:
        return []
    
    if quantity > (max - min + 1) or quantity <= 0:
        return []

    #генерація унікальних чисел
    numbers = random.sample(range(min, max + 1), quantity)

    #повертаємо відсортований список
    return sorted(numbers)

# приклад 
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
