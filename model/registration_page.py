import os

from selene import browser, be, have, command


class RegistrationPage:
    def open(self):
        browser.open("/automation-practice-form")

    def remove_banners(self):
        browser.element('footer').execute_script('element.remove()')

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def fill_email(self, value):
        browser.element("#userEmail").type(value)

    def select_gender(self, value=None):
        browser.all("label").element_by(have.exact_text(value)).click()

    def fill_mobile_number(self, value):
        browser.element("#userNumber").type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        (browser.element(".react-datepicker__year-select").click().
         element(f'[value="{year}"]').click())
        (browser.element(".react-datepicker__month-select").click().
         element(f'[value="{month - 1}"]').click())
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def select_hobbies(self, *hobbies):
        for hobby in hobbies:
            element = browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby))
            element.should(be.clickable).click()

    def upload_photo(self, value):
        browser.element("#uploadPicture").type(os.path.abspath(value))

    def fill_current_address(self, value):
        browser.element("#currentAddress").type(value)

    def fill_state(self, value):
        browser.element('#state').click().all("#state div").element_by(have.exact_text(value)).click()

    def fill_city(self, value):
        browser.element('#city').click().all("#city div").element_by(have.exact_text(value)).click()

    def click_submit_button(self):
        browser.element('#submit').should(be.visible).click()

    @staticmethod
    def should_have_registered(
        full_name,
        email,
        gender,
        phone,
        date_of_birth,
        subjects,
        hobbies,
        file_name,
        address,
        state,
        city,
    ):
        browser.element(".table").all("td").even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date_of_birth,
                subjects,
                hobbies,
                file_name,
                address,
                f"{state} {city}",
            )
        )

    def click_close_button(self):
        browser.element('#closeLargeModal').should(be.visible).click()