user_str = input('введите предложение ')
user_str_list = user_str.split(" ")
for i in range(user_str.count(" ") + 1):
    print(user_str_list[i][:10])
