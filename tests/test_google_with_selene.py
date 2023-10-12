import pytest
from selene.support.shared import browser
from selene import be, have


def test_google(size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('Tom Hardy').press_enter()
    browser.element('[id="search"]').should(have.text('Edward Thomas "Tom" Hardy'))


def test_google_no_result(size):
    text = 'aregeiorjb[EIJRG[BPjrbJDFPOBKobkf'
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type(text).press_enter()
    browser.element('[class="card-section"]').should(have.text(f'По запросу {text} ничего не найдено'))
    print(f'Искомый текст {text} - не найден')