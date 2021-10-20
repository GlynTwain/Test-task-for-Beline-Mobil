from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def tap_element(self: WebDriver, locator: tuple) -> None:
        """Нажать элемент"""
        self.find_element(locator).click()

    def send_element(driver: WebDriver, locator: tuple, text: str):
        """Ввести текст в поле"""
        driver.find_element(locator).send_keys(text)

    def exist_element(driver, locator: tuple):
        """Проверка на существование элемента"""

        if len(driver.find_elements(locator)) > 0:
            print('Есть элемент на экране')
            return True
        else:
            print('Нет элемента на экране')
            return False