from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from data_for_tets import LINK, RightUser
import pytest


@pytest.mark.registration_user
class TestUserRegistrationFromRegistrationPage:

    def test_positive_user_registration_on_site(self, browser):
        # идем до страницы регистрации
        registration_page = self.user_go_to_registration_page(browser)

        # вводим данные нового пользователя
        registration_page.registration_user_data_entry(RightUser.email, RightUser.password, RightUser.password)

        # нажимаем кнопку зарегистрироваться
        registration_page.click_registration_button()

        # проверяем регистрацию кнопкой "Выйти"
        registration_page.should_be_logout_button()

    def test_negative_user_registration_on_site_other_repeat_password(self, browser):
        # идем до страницы регистрации
        registration_page = self.user_go_to_registration_page(browser)

        # зарегистрировать нового пользователя
        registration_page.registration_user_data_entry(RightUser.email, RightUser.password, RightUser.password[::-1])

        # проверка, что вывелась рамка красная у поля подтверждение пароля
        registration_page.should_be_password_repeat_error_bold()

    def test_user_login_on_site(self, browser):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, LINK)

        # открываем страницу
        page.open()

        # переходим на страницу авторизации
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)

        # проверяем доступность полей формы авторизации
        login_page.should_be_login_fields()

        # Ввод данных для авторизации 1675008828.6463542@fakemail.org
        login_page.registration_user_data_entry(RightUser.email, RightUser.password)
        # login_page.registration_user_data_entry("1675008828.6463542@fakemail.org", RightUser.password)

        # нажимаем кнопку авторизоваться
        login_page.click_login_button()

        # проверяем регистрацию кнопкой "Выйти"
        login_page.should_be_logout_button()

    def user_go_to_registration_page(self, browser):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, LINK)

        # открываем страницу
        page.open()

        # переходим на страницу авторизации
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)

        # проверяем, что на странице авторизации по кнопке войти
        login_page.should_be_login_button()

        # проверяем ссылку на регистрацию
        login_page.should_be_registration_link()

        # переходим на страницу регистрации
        login_page.go_to_registration_page()

        registration_page = RegistrationPage(browser, browser.current_url)

        # проверяем наличие кнопок и полей для регистрации
        registration_page.should_be_registration_fields()

        return registration_page
