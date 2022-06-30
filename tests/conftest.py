from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.browser_name = 'chrome'
    yield
    browser.quit()


