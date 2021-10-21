from selenium.webdriver.common.by import By

from page.BasePage import BasePage


class Locators:
    auth_voiti_button = (By.ID, "ru.beeline.services:id/enter_button")
    auth_edit_text = (By.ID, "ru.beeline.services:id/edit_text")
    auth_login_edit_text = (By.ID, 'ru.beeline.services:id/login_edit_text')
    auth_password_edit_text = (By.ID, "ru.beeline.services:id/edit_text")

    auth_password_loging_button = (By.XPATH,
                                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.Button")
    auth_sms_loging_button = (By.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.Button')

    auth_sms_edit_pin = (By.ID, 'ru.beeline.services:id/edit_pin')


class Autorization(BasePage):
    def lol(self):
        """Взываем к помощи костыля"""
        self.kostil()

    def click_enter(self):
        return self.tap_element(Locators.auth_voiti_button)

    def send_login(self, text: str):
        """Ввод номера телефона"""
        return self.send_element_in_element(Locators.auth_login_edit_text, Locators.auth_edit_text, text)

    def click_authorization_type_sms(self):
        return self.tap_element(Locators.auth_sms_loging_button)

    def click_authorization_type_password(self):
        return self.tap_element(Locators.auth_password_loging_button)


class AutorizationSMS(BasePage):

    def send_code_sms(self, sms_code: str):
        """Ввод кода из смс сообщения в соотв поле"""
        return self.send_element(Locators.auth_sms_edit_pin, sms_code)


class AutorizationPasswor(BasePage):

    def send_password(self, password: str):
        """Ввод кода из смс сообщения в соотв поле"""
        return self.send_element(Locators.auth_sms_edit_pin, password)

