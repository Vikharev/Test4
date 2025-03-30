from model.data.users import user_test
from model.pages.registration_page import RegistrationPage


def test_registers_user(browser_settings):
    registration_page = RegistrationPage()
    (registration_page.open()
     .remove_banners()
     .register(user_test)
     .should_have_registered(user_test))
