# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

x_1, y_1 = float(input(f'Введите координаты х и y первой точки.\nх = ')), float(input('y = '))
x_2, y_2 = float(input('Введите координаты х и y второй точки. \nx = ')), float(input('y = '))
k = (y_1 - y_2)/(x_1 - x_2)
b = y_2 - k*x_2
print(f'\nУравнение прямой y = {k}*x+{b}')

