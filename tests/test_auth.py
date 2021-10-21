import time

import pytest

from page.AuturizationPage import Autorization, AutorizationSMS
from support_tools.tools import get_sms_for_login

"""

 На данный момент есть несколько проблем:
 1. Не запускается апиум сервер, на скорую руку не получается быстро решить 
 2. Нет ожидания элементов у шагов/ методов, пока используются обычные слипы
 3. Нет паралельности у тестов, так как задачи не стоит. Но +- части некоторые готовы
 4. Есть повторяющийся код, это очень не хорошо и необходимо обернуть.
 5. Есть немного другая логика при клике на поле и она не покрыта, но экраны используются одни
 
 """


@pytest.mark.parametrize("login", [
    "9880843702", "glyntwain"
])
def test_auth_login_sms_p(driver, login):
    """Авторизация через логин и смс - ПОЗИТИВ"""
    main_auth_page = Autorization(driver)
    main_auth_page.lol()
    main_auth_page.send_login(login)
    main_auth_page.click_enter()
    time.sleep(2)
    main_auth_page.click_authorization_type_sms()

    # sms_code = get_sms_for_login(login) # Логика обработки кода из смс
    # main_auth_page.send_sms(sms_code)

    time.sleep(2)
    assert True


# Набросан грубо
@pytest.mark.parametrize('login', ['9880843702'])
@pytest.mark.parametrize("code", [
    '4444',
    '44445',
    '66666666',
    'tests',
    ' ',
    '!"?*;%'

])
def test_auth_login_sms_n(driver, login, code):
    """Авторизация через логин и смс - НЕГАТИВ"""
    main_auth_page = Autorization(driver)
    main_auth_page.lol()
    main_auth_page.send_login(login)
    main_auth_page.click_enter()
    time.sleep(2)
    main_auth_page.click_authorization_type_sms()
    time.sleep(4)

    auth_sms_page = AutorizationSMS(driver)
    auth_sms_page.send_code_sms(code)

    time.sleep(10)
    assert False


@pytest.mark.parametrize("login, password", [
    ("78808437", 'test_password'), ("glyntwain", 'test_password')
])
def test_auth_login_password_p(driver, login, password):
    """Авторизация через логин и пароль - ПОЗИТИВ"""
    main_auth_page = Autorization(driver)
    main_auth_page.lol()
    main_auth_page.send_login(login)
    main_auth_page.click_enter()
    time.sleep(2)
    main_auth_page.click_authorization_type_password(password)


@pytest.mark.parametrize('login', ['glyntwain'])
@pytest.mark.parametrize("password",
                         ["test_password",
                          "test_password",
                          "#№!;$%:^&?*(@»)+=*/",
                          "  tes",
                          "",
                          "TESTTESTTEST"
                          ])
def test_auth_login_password_n(driver, login, password):
    """Авторизация через логин и пароль - НЕГАТИВ"""
    main_auth_page = Autorization(driver)
    main_auth_page.lol()
    main_auth_page.send_login(login)
    main_auth_page.click_enter()
    time.sleep(2)
    main_auth_page.click_authorization_type_password(password)
    pass
