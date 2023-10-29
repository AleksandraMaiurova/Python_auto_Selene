from helpers.users.users import User
from helpers.commons import RegistrationPage
import allure


def test_qa_form():
    student = User(
        first_name='Aleksandra',
        last_name='Maiurova',
        email='asmaiurova@itmo.ru',
        gender='Female',
        phone='1234567899',
        day_birth='13',
        month_birth='6',
        year_birth='1993',
        first_subject='English',
        second_subject='Physics',
        hobbies='Sports, Reading',
        photo='vbUrzS0RtIg.jpg',
        city='Agra',
        state='Uttar Pradesh',
        current_address='This is my address where I can cry if I wanna'
    )
    regpage = RegistrationPage()

    regpage.open_page()

    regpage.registration_form(user=student)
    with allure.step('Check result'):
        regpage.should_be(user=student)

