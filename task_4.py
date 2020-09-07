a = int(input('введите ваше число'))
max_dig = 0

while a > 0:
    dig = a % 10
    a //= 10
    if max_dig < dig:
        max_dig = dig

print(f'{max_dig} самая большая цифра в числе')
