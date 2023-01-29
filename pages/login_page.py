from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    # проверка, что есть кнопка войти
    def should_be_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    # проверка ссылку на регистрацию
    def should_be_registration_link(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_LINK), "Registration link is not presented"

    # переход на страницу регистрации
    def go_to_registration_page(self):
        link = self.browser.find_element(*LoginPageLocators.REGISTRATION_LINK)
        link.click()

    # проверка кнопок и полей для авторизации
    def should_be_login_fields(self):
        self.should_be_login_button()
        self.should_be_email_input()
        self.should_be_password_input()

    # проверка поля email
    def should_be_email_input(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL), "Field 'Email' is not " \
                                                                                       "presented "

    # проверка поля пароль
    def should_be_password_input(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD), "Field 'Password' is not " \
                                                                             "presented "
    # авторизация пользователя
    def registration_user_data_entry(self, email, password):
        # заполняем поле email
        input_email = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_EMAIL)
        input_email.send_keys(email)
        # заполняем поле пароль
        input_password = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_PASSWORD)
        input_password.send_keys(password)

    # Отправляем заполненную форму
    def click_login_button(self):
        button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        button.click()
