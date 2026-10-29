print('Сложение')

try:
    num1 = float(input('Введите первое слагаемое: '))
    num2 = float(input('Введите второе слагаемое: '))
    print('Сумма =', num1 + num2, '\n\nВычитание')

    num1 = float(input('Введите уменьшаемое: '))
    num2 = float(input('Введите вычитаемое: '))
    print('Разность =', num1 - num2, '\n\nУмножение')

    num1 = float(input('Введите первый множитель: '))
    num2 = float(input('Введите второй множитель: '))
    print('Произведение =', num1 * num2, '\n\nДеление')

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