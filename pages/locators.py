from selenium.webdriver.common.by import By


class BasePageLocators:
    # ссылка на страницу авторизации
    LOGIN_LINK = (By.CSS_SELECTOR, "header button.secondaryButton")
    # ссылка на выход из системы
    LOGOUT_LINK = (By.CSS_SELECTOR, "header button.UI-button.logOut")
    # ссылка еще
    MENU_MORE = (By.CSS_SELECTOR, "header div.d-flex:not(.justify-content-between)  #dropdownMenuButton1")
    # ссылка на контакты
    CONTACTS_LINK = (By.CSS_SELECTOR,
                     "header div.d-flex:not(.justify-content-between) ul[aria-labelledby=dropdownMenuButton1] li:last-child a")
    # Кнопка принять куки
    BOTTON_COOKIE = (By.CSS_SELECTOR, "button.cookie-policy_btn__1sMVc")
    # кнопка закрыть поддержку
    BOTTON_SUPPORT = (By.CSS_SELECTOR, "div.support-close")


class LoginPageLocators:
    # кнопка войти
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-test-id=test-button-login]")
    # ссылка на страницу регистрации
    REGISTRATION_LINK = (By.CSS_SELECTOR, "a.ms-1.primary-link")
    # поле "Email"
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "input[data-test-id=test-input-login-email]")
    # поле "Пароль"
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "input[data-test-id=test-input-login-password]")


class RegistrationPageLocators:
    # кнопка зарегистрироваться
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, "button[data-test-id=test-button-register]")
    # поле "Email"
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "input[data-test-id=test-input-register-email]")
    # поле "Пароль"
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "input[data-test-id=test-input-register-password]")
    # поле "Подтвердить пароль"
    REGISTER_FORM_PASSWORD_REPEAT = (By.CSS_SELECTOR, "input[data-test-id=test-input-register-repeat-password]")
    # текст ошибки для "Подтвердить пароль"
    REGISTER_FORM_PASSWORD_REPEAT_BOLD_ERROR = (By.CSS_SELECTOR, "div.error input[data-test-id=test-input-register-repeat-password]")


class ContactsPageLocators:
    # поле "Имя"
    FEEDBACK_FORM_NAME = (By.CSS_SELECTOR, "form div input[name=name]")
    # поле "Email"
    FEEDBACK_FORM_EMAIL = (By.CSS_SELECTOR, "form div input[name=email]")
    # поле "Сообщение"
    FEEDBACK_FORM_MESSAGE = (By.CSS_SELECTOR, "form div textarea[name=texts]")
    # кнопка отправить
    FEEDBACK_FORM_BUTTON = (By.CSS_SELECTOR, "form button[data-test-id=test-button-undefined]")
    # кнопка отправить заблокирована
    FEEDBACK_FORM_DISABLED_BUTTON = (By.CSS_SELECTOR, "form button[data-test-id=test-button-undefined][disabled]")
    # форма обратной связи
    FEEDBACK_FORM = (By.CSS_SELECTOR, "form[action]")
