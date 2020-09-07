revenue = int(input('введите выручку'))
cost = int(input('введите издержки'))

if revenue > cost:
    print("ваша фирма работает в прибыль\n"
          f"ваша рентабельность выручки составляет {(revenue - cost)/revenue}")
    worker_amount = int(input("сколько работников в вашей фирме?"))
    print(f"прибыль фирмы в расчете на одного сотрудника составляет {(revenue - cost)/worker_amount}")

else:
    print('ваша фирма работает в убыток')