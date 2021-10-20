import time

import pytest

from page.AuturizationPage import Autorization


@pytest.mark.parametrize("login, password", [
    ("78808437", '0')
])
def test_auth_positiv(driver, login, password):
    """Кейс позитивный"""
    main_auth_page = Autorization(driver)
    main_auth_page.lol()
    main_auth_page.send_login(login)
    main_auth_page.click_enter()
    time.sleep(5)


