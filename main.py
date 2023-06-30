ODD = 'odd'
EVEN = 'even'
PRIME = 'prime'
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def power_numbers(numbers):
    return [number ** 2 for number in numbers]

def filter_numbers(numbers, filter_type):
    a = []
    if filter_type == ODD:
        for number1 in numbers:
            if number1 % 2 == 1:
                a.append(number1)
    if filter_type == EVEN:
        for number2 in numbers:
            if number2 % 2 == 0:
                a.append(number2)
    if filter_type == PRIME:
        for number3 in numbers:
            if number3 == 1:
                continue
            n = int(number3 ** 0.5)
            #print(n, '', number3)
            prost = True
            for i in range(2, n+1):
                if number3 % i == 0:
                    #print(number3 % i, '    ', i)
                    prost = False
                    break
            if prost == True:
                a.append(number3)
    return a
print('Исходный ряд', B)
print('Квадраты чисел исходного ряда ', power_numbers(B))
print('Нечетные числа исходного ряда ', filter_numbers(B, filter_type=ODD))
print('Четные числа исходного ряда ', filter_numbers(B, filter_type=EVEN))
print('Простые числа исходного ряда ', filter_numbers(B, filter_type=PRIME))
input("Для выхода нажмите любую клавишу: ")
