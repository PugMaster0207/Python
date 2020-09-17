def div(a, b):
    try:
        a = int(a)
        b = int(b)
        return a / b
    except (ZeroDivisionError, TypeError, ValueError):
        return 'error!'


print(div(input('введите делимое - '), input('введите делитель - ')))
