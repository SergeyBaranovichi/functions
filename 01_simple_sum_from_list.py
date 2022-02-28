# Создайте функцию, которая будет считать сумму чисел в случано сгенерированном массиве длиной 10
# и выводить результат в консоль
import random

def sum_list_of_numbers(lst: list) -> int:
    sum = 0
    for number in lst:
        sum += number
    return(sum)

numbers = [random.randint(-10, 20) for _ in range(10)]
print(numbers)
print(sum_list_of_numbers(numbers))