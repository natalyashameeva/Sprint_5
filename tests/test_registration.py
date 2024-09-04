import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:
    @pytest.mark.parametrize("email, password", [
        ("surovtseva_000013@yandex.ru", "validpassword"),
        ("surovtseva_0013@yandex.ru", "short")
    ])
    def test_registration(self, driver, email, password):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Ввод имени
        name_input = driver.find_element(*Locators.NAME_FIELD)
        name_input.send_keys("Test User")

        # Ввод email
        email_input = driver.find_element(*Locators.EMAIL_FIELD)
        email_input.send_keys(email)

        # Ввод пароля
        password_input = driver.find_element(*Locators.PASSWORD_FIELD)
        password_input.send_keys(password)

        # Нажатие на кнопку регистрации
        submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)
        submit_button.click()


        if len(password) < 6:
            error_message = driver.find_element(*Locators.ERROR_MESSAGE)
            assert error_message.is_displayed()
        else:
            WebDriverWait(driver, 10).until(
                EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
            )
            assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
