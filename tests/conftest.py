import subprocess
import time
import pytest

from appium import webdriver as AppiumDriver
from config.main_conf import uuid_list
from config.main_conf import port

from config.сapabilities import CapsDevice
from support_tools.tools import get_adb_devices


# def init_driver(caps: CapsDevice) -> object:
#     """Создает драйвер апиума, запускает приложение """
#     driver = AppiumDriver.Remote(caps.get_address(), desired_capabilities=caps.get_caps())
#     return driver


def appium_start(uuid: str, my_caps: classmethod) -> None:
    """Старт аппиум сервера"""
    return subprocess.run(f"appium -U {uuid} -p {my_caps.appium_port} -a {my_caps.appium_id}", shell=True,
                          stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


@pytest.fixture(scope="session")
def driver():
    uuid_list = get_adb_devices()
    uuid = uuid_list[-1]
    # for uuid in uuid_list:
    caps = CapsDevice(uuid=uuid)

    # Магия в том что не работает запуск апиума, хотя строка из рабочего проекта
    # Необходимо сначала запустить его в консольке - appium -p 5906 -a 127.0.0.1

    # appium_server = subprocess.Popen(f"appium -U {uuid} -p {caps.appium_port} -a {caps.appium_id}",
    #                                shell=True,
    #                               stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    time.sleep(1)
    driver = AppiumDriver.Remote(caps.get_address(), desired_capabilities=caps.get_caps())

    yield driver
    driver.quit()
    # appium_server.kill()
