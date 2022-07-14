from selene import have, command
from selene.support.shared import browser

from controls.city_selector import City, select_by_choosing
from controls.hobbies_input import Hobbies
from controls.image_input import resource
from controls.person_input import Person
from controls.subjects_input import SubjectsInput


def student_reg_form_opened():
    browser.open('/automation-practice-form')


def test_fill_reg_form():
    # Open registration form
    student_reg_form_opened()

    # Filling Person information
    Person().fill_person_info('#firstName', Person.name)
    Person().fill_person_info('#lastName', Person.last_name)
    Person().fill_person_info('#userEmail', Person.email)
    Person().fill_person_info('#userNumber', Person.phone_number)
    Person().fill_person_info('#currentAddress', Person.current_address)

    gender = browser.element('#genterWrapper')
    gender.all('.custom-radio').element_by(have.exact_text('Male')).click()

    browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
    browser.element('.react-datepicker__year-select').element('[value="1993"]').click()
    browser.element('.react-datepicker__month-select').element('[value="3"]').click()
    browser.element('.react-datepicker__day--028').click()

    subjects_input = SubjectsInput
    subjects_input.autocomplete('#subjectsInput', SubjectsInput.physics)
    subjects_input.autocomplete('#subjectsInput', SubjectsInput.english)

    browser.all('.custom-checkbox').element_by(have.exact_text(Hobbies.music)).click()
    browser.all('.custom-checkbox').element_by(have.exact_text(Hobbies.sports)).click()
    browser.all('.custom-checkbox').element_by(have.exact_text(Hobbies.reading)).click()

    browser.element('#uploadPicture').send_keys(resource('159627.png'))
    # browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/159627.png'))

    select_by_choosing(browser.element('#state'), option=City.state)
    select_by_choosing(browser.element('#city'), option=City.city)

    browser.element('#submit').perform(command.js.click)

    # Assert
    browser.elements('.modal-title').should(have.text("Thanks for submitting the form"))
    browser.elements("table tr").element(1).should(have.text(f'{Person.name} {Person.last_name}'))
    browser.elements("table tr").element(2).should(have.text(f'{Person.email}'))
    browser.elements("table tr").element(3).should(have.text("Male"))
    browser.elements("table tr").element(4).should(have.text(f'{Person.phone_number}'))
    browser.elements("table tr").element(5).should(have.text("28 March,1993"))
    browser.elements("table tr").element(6).should(have.text('Physics, English'))
    browser.elements("table tr").element(7).should(have.text("Music, Sports, Reading"))
    browser.elements("table tr").element(8).should(have.text("159627.png"))
    browser.elements("table tr").element(9).should(have.text(f'{Person.current_address}'))
    browser.elements("table tr").element(10).should(have.text("NCR Delhi"))
