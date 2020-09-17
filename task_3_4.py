def my_func(x, y):
    return x ** y


def my_func_2(x, y):
    a = 1
    for i in range(y, 0):
        a /= x
    return a


print(my_func(int(input('введите действительное положительное число как основание')),
              int(input('введите целое отрицательное число как мантиссу'))))

print(my_func_2(int(input('введите действительное положительное число как основание')),
              int(input('введите целое отрицательное число как мантиссу'))))