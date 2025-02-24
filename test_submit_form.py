from selene import browser, be, have, by, command
import os


def test_submit_form_success(practice_form):
    browser.element('#firstName').type('Иван')
    browser.element('#lastName').type('Иванов')
    browser.element('#userEmail').type('Ivanov@mail.ru')
    browser.element('#genterWrapper').element(by.text('Male')).click()
    browser.element('#userNumber').type('1234567890')
    browser.element('.react-datepicker-wrapper').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('May')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1990')).click()
    browser.element('.react-datepicker__day--010').click()
    browser.element('#subjectsInput').type('m')
    browser.element('.subjects-auto-complete__menu-list').element(by.text('Maths')).click()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').type(os.path.abspath('src/20241021_190523.jpg'))
    browser.element('#currentAddress').type('Москва, ул.Ленина, д.1, кв.100')
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#state').click().element('#react-select-3-option-0').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()
    browser.element('#submit').click()
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-content').element('tbody').all('tr').all('td').even.should(
        have.exact_texts(
            (
            'Иван Иванов',
            'Ivanov@mail.ru',
            'Male',
            '1234567890',
            '10 May,1990',
            'Maths',
            'Sports, Reading',
            '20241021_190523.jpg',
            'Москва, ул.Ленина, д.1, кв.100',
            'NCR Delhi'
            )
        )
    )
    browser.element('#closeLargeModal').should(be.clickable)


def test_submit_form_empty(practice_form):
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#submit').click()
    browser.element('#firstName').should(have.css_property('validity[valid]', False))
    browser.element('#lastName').should(have.css_property('validity[valid]', False))
    browser.element('#userNumber').should(have.css_property('validity[valid]', False))