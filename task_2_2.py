i = int(input('сколько элементов будет в списке?'))
my_list = []

while i > 0:
    my_list.append(int(input('введите число')))
    i -= 1

for j in range(len(my_list)):
    if j % 2 == 0:
        continue
    else:
        my_list[j - 1], my_list[j] = my_list[j], my_list[j - 1]

print(my_list)
