# Code review-1 🌶️🌶️

# На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке).

# Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности и их произведение. Если неотрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.

# Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.


# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print("NO")
