from selenium.webdriver.common.by import By

from page.BasePage import BasePage


class Locators:
    auth_voiti = "ru.beeline.services:id/enter_button"
    # auth_edit_text = (By.ID, "ru.beeline.services:id/edit_text")
    # auth_login_edit_text = (By.ID, 'ru.beeline.services:id/login_edit_text')
    auth_edit_text = "ru.beeline.services:id/edit_text"
    auth_login_edit_text = "ru.beeline.services:id/login_edit_text"
    auth_password_edit_text = (By.ID, "ru.beeline.services:id/edit_text")
    # auth_voiti = (By.ID, "ru.beeline.services:id/enter_button")


class Autorization(BasePage):
    def lol(self):
        self.kostil()

    def click_enter(self):
        return self.tap_element(Locators.auth_voiti)

    def send_login(self, text: str):
        """Ввод номера телефона"""
        return self.send_element_in_element(Locators.auth_login_edit_text, Locators.auth_edit_text, text)
