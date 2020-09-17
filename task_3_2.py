def person_info(name, surname, birth_date, city, email, phone):
    print(f"{name} {surname} {birth_date} {city} {email} {phone}")


person_info(name=input(f'введите имя, '),
            surname=input('фамилию, '),
            birth_date=input('год рождения, '),
            city=input('город проживания, '),
            email=input('email '),
            phone=input('и номер телефона'))
