# Создайте функцию вычисляющую среднее арифметическое элементов массива.
# Массив должен состоять из случайных чисел, длинной 10 элементов.
import random

def average_list_of_numbers(lst: list) -> int:
    sum = 0
    for number in lst:
        sum += number
    return(sum / len(lst))

numbers = [random.randint(-10, 20) for _ in range(10)]
print(numbers)
print(average_list_of_numbers(numbers))