# Integers
"""
num1 = 7  # num1  - is a number
num2 = 10 # num2  - is a number
num3 = num1 + num2 # num3  - is a number

print(num3)
"""
# the operations are: +, -, *, /

"""
a = 3
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
"""

# Order as at Math

"""
num1 = 2 + 3 * 4
num2 = (2 + 3) * 4

print(num1)
print(num2)
"""
# Type transformation
"""
# if there is a string

string1 = "2024"
year = int(string1)
print(year)
"""
# if it's necessary to work with integers
"""
num1 = int(input())
num2 = int(input())
print(num1 + num2)
"""
# integer to string
"""
num = 17
string2 = str(num)

"""

"""
#ex1
a = int(input())
b = a + 1
c = b + 1

print(a)
print(b)
print(c)

"""

# ex2
"""
a = int(input())
b = int(input())
c = int(input())

print(a + b + c)
"""

# ex3
"""
one_side = int(input())
volume = one_side * one_side * one_side
area = 6 * (one_side * one_side)
print("Объем =", volume)
print("Площадь полной поверхности =", area)
"""

# ex4
"""
a = int(input())
b = int(input())
c = (a + b) * (a + b) * (a + b)

f = (3 * c) + (275 * (b * b)) - (127 * a) - 41
print(f)
"""

# ex5
"""
a = int(input())
before_a = a - 1
after_a = a + 1

print("Следующее за числом", a, "число:", after_a)
print("Для числа", a, "предыдущее число:", before_a)
"""
# ex6
"""
monitor_price = int(input())
system_unit_price = int(input())
keyboard_price = int(input())
mouse_price = int(input())

sum_of_one = monitor_price + system_unit_price + keyboard_price + mouse_price
result = sum_of_one * 3
print(result)
"""

# ex7
"""
a = int(input())
b = int(input())

sum1 = a + b
sub = a - b
div = a * b

print(str(a), "+", str(b), "=", sum1)
print(str(a), "-", str(b), "=", sub)
print(str(a), "*", str(b), "=", div)
"""

# ex8
"""

first_num = int(input())
difference = int(input())
quantity = int(input())

result = first_num + difference * (quantity - 1)
print(result)
"""

# ex9
"""
n = int(input())
print(n, 2 * n, 3 * n, 4 * n, 5 * n, sep="---")
"""

# a = 15 // 2
# print(a)
# a = 82 // 3**2 % 7
# print(a)

# ex10 geometr
"""
first_numb = int(input())
quantity = int(input())
n = int(input())

result = first_numb * quantity ** (n - 1)
print(result)
"""

# ex11
"""
cm_length = int(input())
m_length = cm_length // 100
print(m_length)
"""

# ex12
"""
n = int(input())
k = int(input())

a = k // n
b = k % n
print(a)
print(b)
"""

# ex13
"""
population = int(input())
div_to_two = population // 2
what_is_left = population % 2

result = div_to_two + what_is_left


print(result)
"""

# ex14 time
"""
given_minutes = int(input())
minutes_to_hours = given_minutes // 60
minutes_left = given_minutes % 60

print(
    str(given_minutes),
    " мин - это",
    str(minutes_to_hours),
    "час",
    str(minutes_left),
    "минут.",
)
"""

# ex15 train

seat_number = int(input())

a = seat_number // 4

if seat_number % 4 == 0:
    print(a)
else:
    print(a + 1)
