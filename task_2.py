user_time = int(input("введте время в секундах"))
hours = 0
minutes = 0
seconds = 0

while True:
    if user_time > 3600:
        hours += 1
        user_time -= 3600
        continue
    elif user_time > 60:
        minutes += 1
        user_time -= 60
        continue
    else:
        seconds = user_time
        break

print("{:0>2}:{:0>2}:{:0>2}".format(hours, minutes, seconds))
