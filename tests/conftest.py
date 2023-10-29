import pytest
from selene.support.shared import browser
import shutil
import os



@pytest.fixture (scope="function")
def size():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 4.0
    browser.config.window_height = 1000
    browser.config.window_width = 800
    yield
    browser.quit()


