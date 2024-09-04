from locators import Locators

class TestConstructorSections:

    def test_constructor_sections(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        # Переход в раздел "Соусы"
        sauces_section = driver.find_element(*Locators.SAUCES_SECTION)
        sauces_section.click()
        assert Locators.CURRENT_TAB in sauces_section.get_attribute("class")


        # Переход в раздел "Начинки"
        fillings_section = driver.find_element(*Locators.FILLINGS_SECTION)
        fillings_section.click()
        assert Locators.CURRENT_TAB in fillings_section.get_attribute("class")


        # Переход в раздел "Булки"
        buns_section = driver.find_element(*Locators.BUNS_SECTION)
        buns_section.click()
        assert Locators.CURRENT_TAB in buns_section.get_attribute("class")