import pytest
from selene.support.shared import browser
import shutil
import os
import zipfile
from utils import TMP_PATH



@pytest.fixture (scope="function")
def size():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 4.0
    browser.config.window_height = 800
    browser.config.window_width = 400
    yield
    browser.quit()


@pytest.fixture(scope="function")
def archive_maker():
    if not os.path.exists(TMP_PATH):
        os.mkdir('tmp')
        yield
        shutil.rmtree(TMP_PATH)
