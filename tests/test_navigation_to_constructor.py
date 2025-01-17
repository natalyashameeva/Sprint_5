from locators import Locators

class TestNavigationFromPersonalAccountToConstructor:

    def test_navigation_from_personal_account_to_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # Переход в конструктор
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert driver.find_element(*Locators.CONSTRUCTOR_HEADER).text == 'Соберите бургер'

        # Возврат в личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        # Переход на главную страницу через логотип
        driver.find_element(*Locators.LOGO).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"