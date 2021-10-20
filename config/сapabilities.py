class CapsDevice:
    def __init__(self, uuid: str):
        self.desired_capabilities = {
            "udid": str(uuid),  #
            "platformName": "Android",
            "app": '/home/glyntwain/Документы/Test-task-for-Beline-Mobil/builds/beline.apk',  # можно сделать парсер
            "noReset": "true",
            "unicodeKeyboard": "true",
            "useNewWDA": "false",
            "usePrebuiltWDA": "true",
            "automationName": "UiAutomator2",
            "uiautomator2ServerLaunchTimeout": 900000,
            "uiautomator2ServerInstallTimeout": 800000,
            'adbExecTimeout': 100000,
            'maxDuration': 10800,
            'newCommandTimeout': 1000,
            'autoGrantPermissions': 'true',
            'resetKeyboard': 'true',
        }
        self.appium_port = '5906'
        self.appium_id = '127.0.0.1'

    def get_caps(self) -> dict:
        """получить Капабили под данное устройство"""
        return self.desired_capabilities

    def get_address(self) -> str:
        """Адрес общения для данного устройства"""
        return f'http://{self.appium_id}:{self.appium_port}/wd/hub'

    def get_uuid(self) -> str:
        """Получить Юид данного устройства"""
        return self.desired_capabilities['udid']
