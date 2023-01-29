from pages.main_page import MainPage
from pages.login_page import LoginPage
from data_for_tets import LINK, RightUser
import pytest


@pytest.mark.skip
@pytest.mark.login_user
class TestUserLoginFromLoginPage:

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
