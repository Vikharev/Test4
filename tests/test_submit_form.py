import allure

from allure_commons.types import Severity
from model.registration_page import RegistrationPage


@allure.tag("testing Jenkins")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Somebody")
@allure.feature("QA-2025")
@allure.story("GURU-10")
@allure.link("https://github.com", name="Test demoqa")
@allure.title('Проверка регистрации')
def test_submit_form_success(browser_settings):
    with allure.step('Открыть форму для заполнения'):
        registration_page = RegistrationPage()
        registration_page.open()
        registration_page.remove_banners()
    with allure.step('Заполнить форму регистрации'):
        registration_page.fill_first_name("Иван")
        registration_page.fill_last_name("Иванов")
        registration_page.fill_email("ivanov@yandex.ru")
        registration_page.select_gender("Male")
        registration_page.fill_mobile_number("1234567890")
        registration_page.fill_date_of_birth(1989, 11, 11)
        registration_page.fill_subject("Maths")
        registration_page.select_hobbies("Sports")
        registration_page.upload_photo("20241021_190523.jpg")
        registration_page.fill_current_address(
            "Москва, ул.Ленина, д.1, кв.100"
        )
        registration_page.fill_state("NCR")
        registration_page.fill_city("Delhi")
    with allure.step('Нажать кнопку Submit'):
        registration_page.click_submit_button()
        registration_page.should_have_registered(
            full_name="Иван Иванов",
            email="ivanov@yandex.ru",
            gender="Male",
            phone="1234567890",
            date_of_birth="11 November,1989",
            subjects="Maths",
            hobbies="Sports",
            file_name="20241021_190523.jpg",
            address="Москва, ул.Ленина, д.1, кв.100",
            state="NCR",
            city="Delhi",
        )
