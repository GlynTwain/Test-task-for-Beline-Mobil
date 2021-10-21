import time

import pytest

from page.AuturizationPage import Autorization
from support_tools.tools import get_sms_for_login

"""

 На данный момент есть несколько проблем:
 1. Не запускается апиум сервер, на скорую руку не получается быстро решить 
 2. Нет ожидания элементов у шагов/ методов, пока используются обычные слипы
 3. Нет паралельности у тестов, так как задачи не стоит. Но +- части некоторые готовы
 
 """


@pytest.mark.parametrize("login", [
    "9880843702"
])
def test_auth_login_sms(driver, login):
    """Авторизация через логин и смс"""
    main_auth_page = Autorization(driver)
    main_auth_page.lol()
    main_auth_page.send_login(login)
    main_auth_page.click_enter()
    time.sleep(2)
    main_auth_page.click_authorization_type_sms()

    # sms_code = get_sms_for_login(login) # Логика обработки кода из смс
    # main_auth_page.send_sms(sms_code)

    time.sleep(500)


@pytest.mark.parametrize("login, password", [
    ("9880843702", '0')
])
def test_auth_login_passw(driver, login, password):
    """Кейс позитивный"""
    main_auth_page = Autorization(driver)
    main_auth_page.lol()
    time.sleep(5)
    main_auth_page.send_login(login)
    main_auth_page.click_enter()
    time.sleep(500)


@pytest.mark.parametrize("login, password", [
    ("78808437", '0'), ('test', 'ps')
])
def test_auth_main_page(driver, login, password):
    pass
