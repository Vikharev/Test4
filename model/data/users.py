import dataclasses

from typing import List


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    year_of_birth: str
    month_of_birth: str
    day_of_birth: str
    subject: str
    hobbies: List[str]
    picture: str
    address: str
    state: str
    city: str


user_test = User(first_name='Иван',
                 last_name='Иванов',
                 email='ivanov@yandex.ru',
                 gender='Male',
                 phone_number='1234567890',
                 year_of_birth='1989',
                 month_of_birth='November',
                 day_of_birth='11',
                 subject='Maths',
                 hobbies=['Sports', 'Music'],
                 picture='20241021_190523.jpg',
                 address='Москва, ул.Ленина, д.1, кв.100',
                 state='NCR',
                 city='Delhi')
