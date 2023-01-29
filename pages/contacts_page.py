from .base_page import BasePage
from .locators import ContactsPageLocators, BasePageLocators


class ContactsPage(BasePage):

    # проверка доступности полей для обратной связи
    def should_be_feedback_fields(self):
        self.should_be_name_input()
        self.should_be_email_input()
        self.should_be_message_input()
        self.should_be_send_button()

    # проверка, что есть поле для ввода имени
    def should_be_name_input(self):
        assert self.is_element_present(*ContactsPageLocators.FEEDBACK_FORM_NAME), "Field 'Name' is not " \
                                                                                  "presented "

    # проверка, что есть поле для ввода email
    def should_be_email_input(self):
        assert self.is_element_present(*ContactsPageLocators.FEEDBACK_FORM_EMAIL), "Field 'Email' is not " \
                                                                                   "presented "

    # проверка, что есть поле для ввода сообщения
    def should_be_message_input(self):
        assert self.is_element_present(*ContactsPageLocators.FEEDBACK_FORM_MESSAGE), "Field 'Message' is not " \
                                                                                     "presented "

    # проверка, что есть кнопка отправить сообщение
    def should_be_send_button(self):
        assert self.is_element_present(*ContactsPageLocators.FEEDBACK_FORM_BUTTON), "Send button is not " \
                                                                                    "presented "

    # нажатие кнопки отправить
    def click_send_button(self):
        # закрываем окно по поводу кук
        button_cookie = self.browser.find_element(*BasePageLocators.BOTTON_COOKIE)
        button_cookie.click()

        # закрываем окно вопросов online
        button_support = self.browser.find_element(*BasePageLocators.BOTTON_SUPPORT)
        button_support.click()

        # нажимаем кнопку отправить сообщение
        button = self.browser.find_element(*ContactsPageLocators.FEEDBACK_FORM_BUTTON)
        button.click()

    # Заполнение полей данными отбратной связи
    def feedback_user_data_entry(self, name, email, message):
        # заполняем поле имя
        input_name = self.browser.find_element(*ContactsPageLocators.FEEDBACK_FORM_NAME)
        input_name.send_keys(name)
        # заполняем поле email
        input_email = self.browser.find_element(*ContactsPageLocators.FEEDBACK_FORM_EMAIL)
        input_email.send_keys(email)
        # заполняем поле сообщение
        textarea_message = self.browser.find_element(*ContactsPageLocators.FEEDBACK_FORM_MESSAGE)
        textarea_message.send_keys(message)

    # проверка, что кнопка отправить заблокирована
    def shold_be_disabled_send_button(self):
        assert self.is_element_present(*ContactsPageLocators.FEEDBACK_FORM_DISABLED_BUTTON), "Send button is not " \
                                                                                             "disabled "

    # скролинг до формы
    # def scroll_to_feedback_form(self):
    #     self.browser.execute_script("window.scrollTo(0, document.body.form);")

    # ождание показа формы обратной связи
    def should_be_feedback_form(self):
        assert self.is_element_present_wait(*ContactsPageLocators.FEEDBACK_FORM), "Form FEEDBACK is not presented "
