from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2


if __name__ == '__main__':
    while True:
        try:
            numbers_list = input('Для решения квадратного уравнения\n'
                                 'вида a*x^2 + b*x + c = 0\n'
                                 'введите коэффициенты a, b, c '
                                 'через запятую:\n').split(',')
            a, b, c = [float(number.strip()) for number in numbers_list]
            break
        except:
            print('Некорректные значения!\n'
                  'Попробуйте еще раз!')

    print('Корни уравнения:')
    print(get_roots(a, b, c))
