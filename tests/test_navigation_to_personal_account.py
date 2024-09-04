from locators import Locators

class TestNavigationToPersonalAccount:

    def test_navigation_to_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        personal_account_button = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

