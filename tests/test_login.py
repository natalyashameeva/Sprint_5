import pytest
from locators import Locators
from selenium.webdriver.common.by import By


class TestLogin:
    @pytest.mark.parametrize("login_button, url", [
        (Locators.LOGIN_BUTTON_MAIN, "https://stellarburgers.nomoreparties.site"),
        (Locators.PERSONAL_ACCOUNT_BUTTON, "https://stellarburgers.nomoreparties.site"),
        (Locators.LOGIN_BUTTON_REGISTRATION, "https://stellarburgers.nomoreparties.site/register"),
        (Locators.LOGIN_BUTTON_FORGOT_PASSWORD, "https://stellarburgers.nomoreparties.site/forgot-password")
    ])
    def test_login(self, driver, login_button, url):
        driver.get(url)

        # Нажатие на кнопку входа
        login_btn = driver.find_element(*login_button)
        login_btn.click()

        # Ввод логина и пароля
        email_input = driver.find_element(*Locators.EMAIL_AUTO)
        email_input.send_keys("surovtseva_n@ya.ru")

        password_input = driver.find_element(*Locators.PASSWORD_FIELD)
        password_input.send_keys("qazwsx")

        # Нажатие на кнопку "Войти"
        submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
        submit_button.click()


        # Проверка, что появилась кнопка "Оформить заказ"
        assert driver.find_element(By.XPATH, '//section[2]/div/button').text == 'Оформить заказ'

