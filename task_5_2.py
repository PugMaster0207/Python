list_of_red_int = [9, 6, 6, 5, 3, 1]
new_int = int(input('введите натуральное число '))
for i in range(len(list_of_red_int)):
    if new_int <= list_of_red_int[i]:
        continue
    else:
        list_of_red_int.insert(i, new_int)
        break
print(list_of_red_int)