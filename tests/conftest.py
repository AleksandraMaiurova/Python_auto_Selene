import pytest
from selene.support.shared import browser


@pytest.fixture (scope="function")
def size():
    browser.config.timeout = 4.0
    browser.config.window_height = 1200
    browser.config.window_width = 800
    yield
    browser.quit()


