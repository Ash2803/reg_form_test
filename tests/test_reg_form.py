from selene import have, command
from selene.support.shared import browser
import os
from registration_tests.controls import select


def student_reg_form_opened():
    browser.open('https://demoqa.com/automation-practice-form')


def test_fill_reg_form():
    student_reg_form_opened()
    browser.element('.main-header').should(have.exact_text('Practice Form'))
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
    browser.element('#subjectsInput').type("Math").press_tab()
    browser.element('#subjectsInput').type("History").press_tab()
    browser.element("[for='hobbies-checkbox-1']").click()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../159627.png'))
    browser.element("#currentAddress").type("Moscow")
    select.select(browser.element('#state'), option='NCR')
    select.select(browser.element('#city'), option='Delhi')
    browser.element('#submit').perform(command.js.click)

    # Assert
    browser.elements('.modal-title').should(have.text("Thanks for submitting the form"))
    browser.elements("table tr").element(1).should(have.text("Name LastName"))
    browser.elements("table tr").element(2).should(have.text("name@name.com"))
    browser.elements("table tr").element(3).should(have.text("Male"))
    browser.elements("table tr").element(4).should(have.text("8999555336"))
    browser.elements("table tr").element(5).should(have.text("28 March,1993"))
    browser.elements("table tr").element(6).should(have.text("Maths, History"))
    browser.elements("table tr").element(7).should(have.text("Sports, Music"))
    browser.elements("table tr").element(8).should(have.text("159627.png"))
    browser.elements("table tr").element(9).should(have.text("Moscow"))
    browser.elements("table tr").element(10).should(have.text("NCR Delhi"))


