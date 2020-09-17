def ext_func(string):
    string = string.split()
    for i in range(len(string)):
        print(int_func(string[i]))


def int_func(word):
    count = 0
    for i in range(len(word)):
        if ord(word[i]) < 97 or ord(word[i]) > 122:
            count += 1
    if count == len(word):
        return 'я же просил только маленькие латинские символы =('
    else:
        return word.title()


ext_func(input('введите предложение маленькими латинскими символами - '))
