from .base_page import BasePage
from .locators import RegistrationPageLocators


class RegistrationPage(BasePage):

    # проверка доступности полей для регистрации
    def should_be_registration_fields(self):
        self.should_be_registration_button()
        self.should_be_email_input()
        self.should_be_password_input()
        self.should_be_password_repeat_input()

    # проверка, что есть кнопка зарегистрироваться
    def should_be_registration_button(self):
        assert self.is_element_present(*RegistrationPageLocators.REGISTER_FORM_BUTTON), "Registration button is not " \
                                                                                        "presented "

    # проверка, что есть поле для ввода email
    def should_be_email_input(self):
        assert self.is_element_present(*RegistrationPageLocators.REGISTER_FORM_EMAIL), "Field 'Email' is not " \
                                                                                       "presented "

    # проверка, что есть поле для ввода пароля
    def should_be_password_input(self):
        assert self.is_element_present(*RegistrationPageLocators.REGISTER_FORM_PASSWORD), "Field 'Password' is not " \
                                                                                          "presented "

    # проверка, что есть поле для ввода подтверждения пароля
    def should_be_password_repeat_input(self):
        assert self.is_element_present(*RegistrationPageLocators.REGISTER_FORM_PASSWORD_REPEAT), "Field 'Repeat " \
                                                                                                 "password' is not " \
                                                                                                 "presented "

    # проверка, что рамка поменялась на красный цвет у поля повтор пароля
    def should_be_password_repeat_error_bold(self):
        assert self.is_element_present_wait(*RegistrationPageLocators.REGISTER_FORM_PASSWORD_REPEAT_BOLD_ERROR), "Bold error of 'Repeat " \
                                                                                                 "password' is not " \
                                                                                                 "presented "

    # Отправляем заполненную форму
    def click_registration_button(self):
        button = self.browser.find_element(*RegistrationPageLocators.REGISTER_FORM_BUTTON)
        button.click()

    # регистрация пользователя
    def registration_user_data_entry(self, email, password, repeat_password):
        # заполняем поле email
        input_email = self.browser.find_element(*RegistrationPageLocators.REGISTER_FORM_EMAIL)
        input_email.send_keys(email)
        # заполняем поле пароль
        input_password = self.browser.find_element(*RegistrationPageLocators.REGISTER_FORM_PASSWORD)
        input_password.send_keys(password)
        # заполняем поле повтор пароля
        input_repeat_password = self.browser.find_element(*RegistrationPageLocators.REGISTER_FORM_PASSWORD_REPEAT)
        input_repeat_password.send_keys(repeat_password)
