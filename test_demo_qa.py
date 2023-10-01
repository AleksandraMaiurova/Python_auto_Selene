from selene import browser, have, command
import os


def test_demoqa_form(size):
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Aleksandra')
    browser.element('#lastName').type('Maiurova')
    browser.element('#userEmail').type('asmaiurova@itmo.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('1234567899')
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__month-select").click().element('option[value="6"]').click()
    browser.element(".react-datepicker__year-select").click().element('[value="1993"]').click()
    browser.element(".react-datepicker__day--013").click()
    browser.element('#subjectsInput').type('english').press_enter()
    browser.element('[id="react-select-3-input"]').perform(command.js.scroll_into_view)
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('vbUrzS0RtIg.jpg'))
    browser.element('#currentAddress').type('This is my address where I can cry if I wanna')
    browser.element('[id="react-select-3-input"]').type('Uttar Pradesh').press_enter()
    browser.element('[id="react-select-4-input"]').type('Agra').press_enter()
    browser.element('#close-fixedban').click()
    browser.element('[id="submit"]').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

