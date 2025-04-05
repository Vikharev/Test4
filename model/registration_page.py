import allure
import os

from selene import browser, be, have, command

import tests


class RegistrationPage:
    @allure.step('Открытие страницы /automation-practice-form')
    def open(self):
        browser.open("/automation-practice-form")

    @allure.step('Удаление мешающих банеров')
    def remove_banners(self):
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.element('footer').execute_script('element.remove()')

    @allure.step('Заполнение имени значением: {value}')
    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    @allure.step('Заполнение фамилии значением: {value}')
    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    @allure.step('Заполнение E-MAIL значением: {value}')
    def fill_email(self, value):
        browser.element("#userEmail").type(value)

    @allure.step('Выбор пола: {value}')
    def select_gender(self, value=None):
        browser.all("label").element_by(have.exact_text(value)).click()

    @allure.step('Заполнение телефона значением: {value}')
    def fill_mobile_number(self, value):
        browser.element("#userNumber").type(value)

    @allure.step('Заполнение даты рождения значением: {day}.{month}.{year}')
    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").perform(command.js.scroll_into_view).click()
        browser.element("#dateOfBirthInput").click()
        (browser.element(".react-datepicker__year-select").click().
         element(f'[value="{year}"]').click())
        (browser.element(".react-datepicker__month-select").click().
         element(f'[value="{month - 1}"]').click())
        browser.element(f'.react-datepicker__day--0{day}').click()

    @allure.step('Выбор предмета: {value}')
    def fill_subject(self, value):
        browser.element('#subjectsInput').perform(command.js.scroll_into_view).click()
        browser.element('#subjectsInput').type(value).press_enter()

    @allure.step('Выбор хобби: {hobbies}')
    def select_hobbies(self, *hobbies):
        for hobby in hobbies:
            element = browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby))
            element.should(be.clickable).click()

    @allure.step('Загрузка изображения: {value}')
    def upload_photo(self, value):
        browser.element("#uploadPicture").type(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(tests.__file__), f'src/{value}')
            )
        )

    @allure.step('Заполнение адреса: {value}')
    def fill_current_address(self, value):
        browser.element("#currentAddress").type(value)

    @allure.step('Выбор штата: {value}')
    def fill_state(self, value):
        browser.element('#state').click().all("#state div").element_by(have.exact_text(value)).click()

    @allure.step('Выбор города: {value}')
    def fill_city(self, value):
        browser.element('#city').click().all("#city div").element_by(have.exact_text(value)).click()

    @allure.step('Нажатие на кнопку отправки формы')
    def click_submit_button(self):
        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#submit').should(be.visible).click()

    @staticmethod
    @allure.step('Проверка корректной регистрации')
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

    @allure.step('Нажатие на кнопку закрытия окна')
    def click_close_button(self):
        browser.element('#closeLargeModal').should(be.visible).click()