import subprocess
import time
import pytest

from appium import webdriver as AppiumDriver
from config.main_conf import uuid_list
from config.main_conf import port

from config.сapabilities import CapsDevice
from support_tools.tools import get_adb_devices


def init_driver(caps: CapsDevice) -> object:
    """Создает драйвер апиума, запускает приложение """
    driver = AppiumDriver.Remote(caps.get_address(), desired_capabilities=caps.get_caps())
    return driver


def appium_start(uuid: str, my_caps: classmethod) -> None:
    """Старт аппиум сервера"""
    return subprocess.run(f"appium -U {uuid} -p {my_caps.appium_port} -a {my_caps.appium_id}", shell=True,
                          stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


@pytest.fixture(scope="module")
def start_driver():
    if uuid_list is None: uuid_list = get_adb_devices()

    for uuid in uuid_list:
        caps = CapsDevice(uuid=uuid, port=port)
        appium_start(uuid, caps)
        time.sleep(1)
        driver = init_driver(caps)

    yield driver
    driver.quit()
    # app_serv.kill()
