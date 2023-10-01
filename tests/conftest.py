import pytest
from selene.support.shared import browser


@pytest.fixture (scope="function")
def size():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 4.0
    browser.config.window_height = 800
    browser.config.window_width = 400
    yield
    browser.quit()
