from selene import be, have
from selene.support.shared import browser
from pathlib import Path


def path_name(photo):
    return str(Path(__file__).parent.joinpath(f'photo/{photo}'))


class RegistrationPage:

    def open_page(self):
        return browser.open('https://demoqa.com/automation-practice-form')

    def first_name(self, name):
        return browser.element('#firstName').should(be.blank).type(f'{name}')

    def last_name(self, lastname):
        return browser.element('#lastName').type(f'{lastname}')

    def email(self, email):
        return browser.element('#userEmail').type(f'{email}')

    def gender(self, gender):
        return browser.element('[for="gender-radio-2"]').should(have.text(f'{gender}')).click()

    def phone_number(self, phone_number):
        return browser.element('#userNumber').type(f'{phone_number}')

    def birthdate(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element(f'option[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').click().element(f'option[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def subjects(self, first_subj, second_subj):
        return browser.element('#subjectsInput').type(f'{first_subj}').press_enter().type(
            f'{second_subj}').press_enter()

    def hobbies(self, sports, music=None, reading=None):
        if sports == 'sports':
            browser.element('label[for="hobbies-checkbox-1"]').click()
        if music == 'music':
            browser.element('label[for="hobbies-checkbox-3"]').click()
        if reading == 'reading':
            browser.element('label[for="hobbies-checkbox-2"]').click()

    def upload_photo(self, photo):
        browser.element('#uploadPicture').set_value(path_name(photo))

    def current_address(self, address):
        browser.element('#currentAddress').type(f'{address}').press_enter()

    def state(self, state):
        browser.element('#react-select-3-input').type(f'{state}').press_enter()

    def city(self, city):
        browser.element('#react-select-4-input').type(f'{city}').press_enter()

    def submit(self):
        browser.element('#submit').press_enter()

    def should_have_inside(self, full_name, email, gender, phone, subjects, birth_date, file_name, address, state_city,
                          hobbies):
        (browser.element('tbody').all('tr td:nth-child(2)')
         .should(have.texts(full_name, email,
                            gender, phone, birth_date,
                            subjects,
                            hobbies,
                            file_name,
                            address,
                            state_city)))
