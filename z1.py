#  Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число: '))

summ = number // 100 + (number % 100) // 10 + number % 10

print(f'Сумма чисел числа {number} равна {summ}')