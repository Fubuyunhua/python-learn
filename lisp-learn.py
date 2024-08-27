def average(x, y):
    return (x + y) / 2.0


def square_guess(g, x):
    guess = average(g, x / g)
    return guess


def Squart_x(inputValue, guess):
    if inputValue < 0:
        print('error')
        return -1
    elif abs(guess - inputValue / guess) < 0.001:
        return guess
    else:
        return Squart_x(inputValue, square_guess(guess, inputValue))


list_test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in list_test:
    print(f'{x}的平方根为{Squart_x(x, 1)}', end='\t')
    print('%2d的三位精度平方根为%6.4f' %(x, Squart_x(x, 1)))




