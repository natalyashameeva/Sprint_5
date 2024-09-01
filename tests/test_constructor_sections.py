from locators import Locators
from selenium.webdriver.common.by import By

class TestConstructorSections:

    def test_constructor_sections(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        # Переход в раздел "Соусы"
        sauces_section = driver.find_element(*Locators.SAUCES_SECTION)
        sauces_section.click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, "//span[text()='Соусы']/parent::div").get_attribute("class")


        # Переход в раздел "Начинки"
        fillings_section = driver.find_element(*Locators.FILLINGS_SECTION)
        fillings_section.click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, "//span[text()='Начинки']/parent::div").get_attribute("class")


        # Переход в раздел "Булки"
        buns_section = driver.find_element(*Locators.BUNS_SECTION)
        buns_section.click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, "//span[text()='Булки']/parent::div").get_attribute("class")