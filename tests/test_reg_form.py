import os

from selene import have, command
from selene.support.shared import browser


class Hobbies:
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


class Subjects:
    physics = 'Physics'
    english = 'English'


class City:
    state = 'NCR'
    city = 'Delhi'


def student_reg_form_opened():
    browser.open('https://demoqa.com/automation-practice-form')


def test_fill_reg_form():
    student_reg_form_opened()
    # Act
    browser.element("#firstName").type('Name')
    browser.element("#lastName").type('LastName')
    browser.element("#userEmail").type('name@name.com')

    browser.element('[for="gender-radio-1"]').click()

    browser.element("#userNumber").type('89995553366')

    browser.element("#dateOfBirthInput").scroll_to().click()
    browser.element(".react-datepicker__month-select")
    browser.element('[value="1993"]').click()
    browser.element('[value="2"]').click()
    browser.element('div[aria-label="Choose Sunday, March 28th, 1993"]').click()

    browser.element('#subjectsInput').type(Subjects.physics).press_enter()
    browser.element('#subjectsInput').type(Subjects.english).press_enter()

    browser.all('.custom-checkbox').element_by(have.exact_text(Hobbies.music)).click()
    browser.all('.custom-checkbox').element_by(have.exact_text(Hobbies.sports)).click()
    browser.all('.custom-checkbox').element_by(have.exact_text(Hobbies.reading)).click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../159627.png'))

    browser.element("#currentAddress").type("Moscow")

    browser.element('#state').element('input').type(City.state).press_enter()
    browser.element('#city').element('input').type(City.city).press_enter()

    browser.element('#submit').perform(command.js.click)

    # Assert
    browser.elements('.modal-title').should(have.text("Thanks for submitting the form"))
    browser.elements("table tr").element(1).should(have.text("Name LastName"))
    browser.elements("table tr").element(2).should(have.text("name@name.com"))
    browser.elements("table tr").element(3).should(have.text("Male"))
    browser.elements("table tr").element(4).should(have.text("8999555336"))
    browser.elements("table tr").element(5).should(have.text("28 March,1993"))
    browser.elements("table tr").element(6).should(have.text('Physics, English'))
    browser.elements("table tr").element(7).should(have.text("Music, Sports, Reading"))
    browser.elements("table tr").element(8).should(have.text("159627.png"))
    browser.elements("table tr").element(9).should(have.text("Moscow"))
    browser.elements("table tr").element(10).should(have.text("NCR Delhi"))
