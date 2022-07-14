from selene import have
from selene.support.shared import browser


class SubjectsInput:
    physics = 'Physics'
    english = 'English'

    def __init__(self, physics, english):
        self.physics = physics
        self.english = english

    @staticmethod
    def autocomplete(selector, option):
        browser.element(selector).type(option)
        browser.all('.subjects-auto-complete__option').element_by(have.text(option)).click()

    # def autocomplete(self, from_: str, /, *, autocomplete: Optional[str] = None):
    #     browser.element(selector).type(from_).press_enter()
    #     browser.all('.subjects-auto-complete__option').element_by(have.exact_text(from_))
