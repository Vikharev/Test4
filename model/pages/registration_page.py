import os

from selene import browser, be, have

import tests
from model.data.users import User


class RegistrationPage:
    def open(self):
        browser.open("/automation-practice-form")
        return self

    def remove_banners(self):
        browser.element('footer').execute_script('element.remove()')
        return self

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def select_gender(self, value=None):
        browser.all("label").element_by(have.exact_text(value)).click()
        return self

    def fill_mobile_number(self, value):
        browser.element("#userNumber").type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        (browser.element(".react-datepicker__year-select").click().
         element(f'[value="{year}"]').click())
        (browser.element(".react-datepicker__month-select").click().
         type(month))
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def select_hobbies(self, hobbies):
        for hobby in hobbies:
            element = browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby))
            element.should(be.clickable).click()
        return self

    def upload_photo(self, value):
        browser.element("#uploadPicture").type(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(tests.__file__), f'src/{value}')
            )
        )
        return self

    def fill_current_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def fill_state(self, value):
        browser.element('#state').click().all("#state div").element_by(have.exact_text(value)).click()
        return self

    def fill_city(self, value):
        browser.element('#city').click().all("#city div").element_by(have.exact_text(value)).click()
        return self

    def click_submit_button(self):
        browser.element('#submit').should(be.visible).click()
        return self

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_mobile_number(user.phone_number)
        self.fill_date_of_birth(user.year_of_birth,
                                user.month_of_birth,
                                user.day_of_birth)
        self.fill_subject(user.subject)
        self.select_hobbies(user.hobbies)
        self.upload_photo(user.picture)
        self.fill_current_address(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.click_submit_button()
        return self

    def should_have_registered(self, user: User):
        browser.element('.table').all('td:nth-child(2)').should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
            user.subject,
            ", ".join(user.hobbies),
            user.picture,
            user.address,
            f'{user.state} {user.city}'.strip()))
        return self

    def click_close_button(self):
        browser.element('#closeLargeModal').should(be.visible).click()
        return self
