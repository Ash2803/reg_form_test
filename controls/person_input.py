from faker import Faker
from selene.support.shared import browser


class Person:
    fake = Faker()
    name = fake.first_name_male()
    last_name = fake.last_name_male()
    email = fake.email()
    phone_number = '8999658121'
    current_address = fake.street_address()

    @staticmethod
    def fill_person_info(selector, value):
        browser.element(selector).type(value)
