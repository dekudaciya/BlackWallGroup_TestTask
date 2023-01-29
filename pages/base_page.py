from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # переход на страницу авторизации
    def go_to_login_page(self):
        button = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        button.click()

    # открытие страницы
    def open(self):
        self.browser.get(self.url)

    # поиск элемента на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # проверка кнопки выйти
    def should_be_logout_button(self):
        assert self.is_element_present_wait(*BasePageLocators.LOGOUT_LINK), "Logout button is not presented "

    # поиск элемента, что он не появится в течении заданного времени
    def is_element_present_wait(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # показ меню еще
    def show_menu_more(self):
        button = self.browser.find_element(*BasePageLocators.MENU_MORE)
        button.click()

    # переход на страницу контакты
    def go_to_contacts_page(self):
        button = self.browser.find_element(*BasePageLocators.CONTACTS_LINK)
        button.click()
