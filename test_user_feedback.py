from pages.contacts_page import ContactsPage
from pages.main_page import MainPage
from data_for_tets import LINK, Message
import pytest


@pytest.mark.user_feedback
class TestUserRegistrationFromRegistrationPage:

    def test_user_send_feedback_on_site(self, browser):
        # Разворачиваем на полный экран
        browser.maximize_window()

        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, LINK)

        # открываем страницу
        page.open()

        # раскрываем меню ЕЩЕ
        page.show_menu_more()

        # переходим на страницу контакты
        page.go_to_contacts_page()

        contacts_page = ContactsPage(browser, browser.current_url)

        # ожидаем загрузку формы обратной связи
        contacts_page.should_be_feedback_form()

        # проверяем доступность полей формы обратная связь
        contacts_page.should_be_feedback_fields()

        # вводим данные сообщения
        contacts_page.feedback_user_data_entry(Message.name, Message.email, Message.message)

        # нажимаем кнопку отправить
        contacts_page.click_send_button()

        # проверяем, что кнопка заблокировалась для отправки
        contacts_page.shold_be_disabled_send_button()
