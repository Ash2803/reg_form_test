from selene import command, have
from selene.core.entity import SeleneElement
from selene.support.shared import browser


def by_choose(element: SeleneElement, /, *, option: str):
    element.perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()


def select_by(selector: str, /, *, option: str):
    by_choose(browser.element(selector), option=option)
