import pytest
import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "asmaiurova")
@allure.feature("Поиск issue")
@allure.story("Можно найти issue")
@allure.link("https://github.com", name="Testing")
def test_name_issue_clean():
    browser.open("https://github.com")
    s(".header-search-button").click()
    s("#query-builder-test").send_keys("meefik/ITMOproctor")
    s("#query-builder-test").submit()
    s(by.link_text("meefik/ITMOproctor")).click()
    s("#issues-tab").click()
    s(by.partial_text("#55")).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "asmaiurova")
@allure.feature("Поиск issue")
@allure.story("Можно найти issue с шагами allure")
@allure.link("https://github.com", name="Testing")
def test_name_issue_steps():
    with allure.step("Open browser"):
        browser.open("https://github.com")
    with allure.step("Work with search"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("meefik/ITMOproctor")
        s("#query-builder-test").submit()
    with allure.step("Find repo"):
        s(by.link_text("meefik/ITMOproctor")).click()
    with allure.step("Open issues"):
        s("#issues-tab").click()
    with allure.step("Find issue 55"):
        s(by.partial_text("#55")).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "asmaiurova")
@allure.feature("Поиск issue")
@allure.story("Можно найти issue с декоратором allure")
@allure.link("https://github.com", name="Testing")
def test_name_issue_decorator():
    repo = "meefik/ITMOproctor"
    open_browser()
    work_with_search(repo)
    find_repo(repo)
    open_issues()
    find_issue(55)


@allure.step("Open browser")
def open_browser():
    browser.open("https://github.com")


@allure.step("Work with search")
def work_with_search(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()


@allure.step("Find repo")
def find_repo(repo):
    s(by.link_text(repo)).click()


@allure.step("Open issues")
def open_issues():
    s("#issues-tab").click()


@allure.step("Find issue")
def find_issue(issue):
    s(by.partial_text(f"#{issue}")).should(be.visible)
