from selene import command, have
from selene.core.entity import Element
from selene.support.shared import browser


class City:
    state = 'NCR'
    city = 'Delhi'


def select_by_autocomplete(selector, value):
    browser.element(selector).type(value).press_enter()


def select_by_choosing(element: Element, /, *, option: str):
    element.perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select-]').element_by(have.exact_text(option)).click()



