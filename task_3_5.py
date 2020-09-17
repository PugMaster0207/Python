def sum_str():
    sum = 0
    z = 0
    while True:
        print(f'вы желаете ввести еще числа? если нет то напечатайте q\n ваша текущяя сумма - {sum}')
        str = input()
        str = str.split()
        for i in range(len(str)):
            if str[i] == 'q':
                z = 1
            else:
                try:
                    sum += int(str[i])
                except ValueError:
                    print('ERROR!')
        if z == 1:
            return sum


print(sum_str())
