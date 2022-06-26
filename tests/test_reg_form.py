from selene import have
from selene.support.shared import browser


def test_fill_form():
    browser.open("/automation-practice-form")
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
    browser.element('#uploadPicture').type("C:/Users/Ash/PycharmProjects/selene_test_box/159627.png")
    browser.element("#currentAddress").type("Moscow")
    browser.element("#react-select-3-input").type("NCR").press_tab()
    browser.element("#react-select-4-input").type("Delhi").press_tab()
    browser.execute_script("document.querySelector('#app > footer').style.display='none'")
    browser.element("#submit").click()
