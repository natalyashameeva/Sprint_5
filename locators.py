from selenium.webdriver.common.by import By

class Locators:

    # Поля для регистрации
    NAME_FIELD = (By.XPATH, '//label[text()="Имя"]/parent::div/input')
    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/parent::div/input')
    PASSWORD_FIELD = (By.NAME, 'Пароль')


    # Сообщение об ошибке некорректного пароля
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")


    # Кнопка «Войти в аккаунт» на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')

    # Поле для ввода почты на странице авторизации
    EMAIL_AUTO = (By.XPATH, '//input[@name="name"]')

    # Кнопка «Личный кабинет»
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[contains(text(), "Личный Кабинет")]')

    # Кнопка для входа в форме регистрации
    LOGIN_BUTTON_REGISTRATION = (By.XPATH, '//a[contains(@class, "Auth")]')

    # Кнопка в форме восстановления пароля для входа
    LOGIN_BUTTON_FORGOT_PASSWORD = (By.XPATH, '//a[contains(text(), "Войти")]')

    # Кнопка "Войти"/"Зарегистрироваться" на экране авторизации
    SUBMIT_BUTTON = (By.XPATH,'//form[contains(@class, "Auth")]/button[contains(@class, "button")]')

    # Кнопка «Конструктор»
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(text(), "Конструктор")]')

    # Логотип Stellar Burgers
    LOGO = (By.XPATH, '//*[name()="svg"][@fill="none"]')

    # Кнопка «Выход» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(@class, "Account")]')

    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, '//span[text()="Соусы"]/parent::div')
    SAUCES_SECTION = (By.XPATH, '//span[text()="Начинки"]/parent::div')
    FILLINGS_SECTION = (By.XPATH, '//span[text()="Булки"]/parent::div')

    # Элемент для проверки переключения разделов
    CURRENT_TAB = "tab_tab_type_current__2BEPc"

    # Кнопка "Оформить заказ"
    ORDER_BUTTON = (By.XPATH, '//button[contains(text(), "Оформить заказ")]')

    # Заголовок "Вход" на экране авторизации
    LOGIN_PAGE_HEADER = (By.XPATH, '//h2[contains(text(), "Вход")]')

    # Заголовок в конструкторе
    CONSTRUCTOR_HEADER = (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')