import time

from appium.webdriver.webdriver import WebDriver


class Locators:
    main_page_profile = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.ImageView"
    profile_page_ext = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout'
    ext_yes = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.Button'


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def tap_element(self, locator: tuple) -> None:
        """Нажать элемент"""
        self.waiting_element_id(locator, 5)
        self.driver.find_element_by_id(locator).click()

    def send_element(self, locator: tuple, text: str):
        """Ввести текст в поле"""
        self.waiting_element_id(locator, 5)
        self.driver.find_element(locator).send_keys(text)

    def send_element_in_element(self, locator1: tuple, locator2: tuple, text: str):
        """Ввести текст в поле"""
        self.waiting_element_id(locator1, 5)
        element = self.driver.find_element_by_id(locator1)
        element = element.find_element_by_id(locator2).send_keys(text)

    def exist_element(self, locator: tuple):
        """Проверка на существование элемента"""

        if len(self.driver.find_elements(locator)) > 0:
            print('Есть элемент на экране')
            return True
        else:
            print('Нет элемента на экране')
            return False

    def kostil(self):
        # Не смог избавиться от автоматического логина при входе, сделал костыль
        time.sleep(3)
        if len(self.driver.find_elements_by_xpath(Locators.main_page_profile)) > 0:
            print('Пользователь залогинен')
            self.driver.find_element_by_xpath(Locators.main_page_profile).click()
            time.sleep(1)
            self.driver.find_element_by_xpath(Locators.profile_page_ext).click()
            time.sleep(1)
            self.driver.find_element_by_xpath(Locators.ext_yes).click()

    # Необходимо поправить
    def waiting_element_id(self, id, time):
        """Грубое ожидание элемента"""

        spent_time = 0
        while not self.exist_element(id):
            print(spent_time)
            time.sleep(0.5)
            spent_time += 0.5
            if spent_time > time:
                break
