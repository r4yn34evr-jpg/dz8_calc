print('Сложение')

try:
    num1 = float(input('Введите первое слагаемое: '))
    num2 = float(input('Введите второе слагаемое: '))

except ValueError:
    print('Ошибка: необходимо ввести число', '\n\nВычитание')

else:
    print('Сумма =', num1 + num2, '\n\nВычитание')

try:
    num1 = float(input('Введите уменьшаемое: '))
    num2 = float(input('Введите вычитаемое: '))

except ValueError:
    print('Ошибка: необходимо ввести число', '\n\nУмножение')

else:
    print('Разность =', num1 - num2, '\n\nУмножение')

try:
    num1 = float(input('Введите первый множитель: '))
    num2 = float(input('Введите второй множитель: '))

except ValueError:
    print('Ошибка: необходимо ввести число', '\n\nДеление')

else:
    print('Произведение =', num1 * num2, '\n\nДеление')

try:
    num1 = float(input('Введите делимое: '))
    num2 = float(input('Введите делитель: '))
    result = round((num1 / num2), 2)

except ValueError:
    print('Ошибка: необходимо ввести число')
except ZeroDivisionError:
    print('Ошибка: на ноль делить нельзя')

else:
    print('Частное =', result)

finally:
    print('\nКонец программы')