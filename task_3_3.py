def my_func(a, b, c):
    d = list(sorted([a, b, c]))
    return d[-1] + d[-2]


print(my_func(100, 34, 15))
