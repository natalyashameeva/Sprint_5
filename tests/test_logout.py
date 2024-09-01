from locators import Locators
from selenium.webdriver.common.by import By

class TestLogout:

    def test_logout(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # Ввод логина и пароля
        email_input = driver.find_element(*Locators.EMAIL_AUTO)
        email_input.send_keys("surovtseva_n@ya.ru")

        password_input = driver.find_element(*Locators.PASSWORD_FIELD)
        password_input.send_keys("qazwsx")

        # Нажатие на кнопку "Войти"
        submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
        submit_button.click()

        # Переход с главной в личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        # Выход из личного кабинета
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        assert driver.find_element(By.XPATH, '//main/div/h2').text == 'Вход'
