from selene import be, have
from selene.support.shared import browser
from pathlib import Path
from helpers.users.users import User


def path_name(photo):
    return str(Path(__file__).parent.joinpath(f'photo/{photo}'))


class RegistrationPage:

    def open_page(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def registration_form(self, user: User):
        browser.element('#firstName').should(be.blank).type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('.custom-radio').element_by(have.text(user.gender)).click()
        browser.element('#userNumber').type(user.phone)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element(f'option[value="{user.year_birth}"]').click()
        browser.element('.react-datepicker__month-select').click().element(f'option[value="{user.month_birth}"]').click()
        browser.element(f'.react-datepicker__day--0{user.day_birth}').click()
        browser.element('#subjectsInput').type(f'{user.first_subject}').press_enter().type(f'{user.second_subject}').press_enter()
        browser.element('label[for="hobbies-checkbox-1"]').click()
        browser.element('label[for="hobbies-checkbox-2"]').click()
        browser.element('#uploadPicture').set_value(path_name(user.photo))
        browser.element('#currentAddress').type(user.current_address).press_enter()
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        browser.element('#submit').press_enter()

    def should_be(self, user: User):
        (browser.element('tbody').all('tr td:nth-child(2)')
         .should(have.texts(f'{user.first_name} {user.last_name}',
                            user.email,
                            user.gender,
                            user.phone,
                            f"{user.day_birth.replace('0', '')} " f"{user.month_birth.replace('6', 'July')},{user.year_birth}",
                            f'{user.first_subject}, {user.second_subject}',
                            user.hobbies,
                            user.photo,
                            user.current_address,
                            f'{user.state} {user.city}')))
