from helpers.commons import RegistrationPage
import allure

reg_page = RegistrationPage()


@allure.story('Registration form')
@allure.title('Filling registration form')
@allure.tag('UI')
def test_qa_form():
    with allure.step('Opening browser page'):
        reg_page.open_page()

    with allure.step('Filling registration form'):
        reg_page.first_name('Aleksandra')
        reg_page.last_name('Maiurova')
        reg_page.email('asmaiurova@itmo.ru')
        reg_page.gender('Female')
        reg_page.phone_number('1234567899')
        reg_page.birthdate(year=1993, month=6, day=13)
        reg_page.subjects('English', 'Physics')
        reg_page.hobbies(sports='sports', reading='reading')
        reg_page.upload_photo(photo='vbUrzS0RtIg.jpg')
        reg_page.current_address('This is my address where I can cry if I wanna')
        reg_page.state('Uttar Pradesh')
        reg_page.city('Agra')
        reg_page.submit()

    with allure.step('Check result'):
        reg_page.should_have_inside('Aleksandra Maiurova',
                                    'asmaiurova@itmo.ru',
                                    'Female',
                                    '1234567899',
                                    'English, Physics',
                                    '13 July,1993',
                                    'vbUrzS0RtIg.jpg',
                                    'This is my address where I can cry if I wanna',
                                    'Uttar Pradesh Agra',
                                    'Sports, Reading')
