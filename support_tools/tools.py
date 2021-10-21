import subprocess


def get_adb_devices() -> list:
    """Создание списка доступных устройств по adb"""
    skip = ['List of devices attached', '', 'device']  # Список исключений
    adb_response = subprocess.check_output('adb devices', shell=True).decode('utf-8')
    adb_response = adb_response.split("\n")  # Разделить по строкам
    raw_list = []
    for v in adb_response:
        if not v in skip:
            raw_list.append(v.split("\t"))  # Разделение по tab-ам

    adb_dev = []
    for this_list in raw_list:
        for this_str in this_list:
            if not this_str in skip:
                adb_dev.append(this_str)

    print(f"Подготовлен список устройств : {adb_dev}")
    return adb_dev


def get_sms_for_login(login: str) -> str:
    """Получить код смс для авторизации, по логину"""
    # Логика работы с API и возможно парсинг
    pass
