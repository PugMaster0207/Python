num = int(input('введите ваше число '))
multi = 1
or_num = num
i = 0

while num > 0:
    num //= 10
    multi *= 10

print(or_num * (3 + 2 * multi + multi ** 2))