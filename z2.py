# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

Summ = int(input('Введите общее количество журавликов: '))
P = Summ / 6
S = Summ / 6
K = (P + S) * 2

print(f'Петя сделал - {P}')
print(f'Катя сделала - {K}')
print(f'Сережа сделал - {S}')