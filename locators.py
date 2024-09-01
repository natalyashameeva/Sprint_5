from selenium.webdriver.common.by import By

class Locators:

    # Поля для регистрации
    NAME_FIELD = (By.XPATH, '//fieldset[1]/div/div/input')
    EMAIL_FIELD = (By.XPATH, '//fieldset[2]/div/div/input')
    PASSWORD_FIELD = (By.NAME, 'Пароль')


    # Сообщение об ошибке некорректного пароля
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")


    # Кнопка «Войти в аккаунт» на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, '//section[2]/div/button')

    # Поле для ввода почты на странице авторизации
    EMAIL_AUTO = (By.XPATH, '//fieldset[1]/div/div/input')

    # Кнопка «Личный кабинет»
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//header/nav/a/p')

    # Кнопка для входа в форме регистрации
    LOGIN_BUTTON_REGISTRATION = (By.XPATH, '//main/div/div/p/a')

    # Кнопка в форме восстановления пароля для входа
    LOGIN_BUTTON_FORGOT_PASSWORD = (By.XPATH, '//main/div/div/p/a')

    # Кнопка "Войти"/"Зарегистрироваться" на экране авторизации
    SUBMIT_BUTTON = (By.XPATH,'/html/body/div/div/main/div/form/button')

    # Кнопка «Конструктор»
    CONSTRUCTOR_BUTTON = (By.XPATH, '//header/nav/ul/li[1]/a/p')

    # Логотип Stellar Burgers
    LOGO = (By.XPATH, '//header/nav/div/a')

    # Кнопка «Выйти» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, '//nav/ul/li[3]/button')

    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, '//span[text()="Булки"]')
    SAUCES_SECTION = (By.XPATH, '//span[text()="Соусы"]')
    FILLINGS_SECTION = (By.XPATH, '//span[text()="Начинки"]')
