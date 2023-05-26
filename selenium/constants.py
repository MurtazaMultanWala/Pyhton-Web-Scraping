import enum


class Constant(enum.Enum):
    WINDOWS_OS = "Windows"
    LINUX_OS = "Linux"
    DELAY_IN_SECONDS = 15
    LINUX_CHROME_DRIVER_PATH = "selenium/linux_driver/chromedriver"
    WINDOWS_CHROME_DRIVER_PATH = "selenium/windows_driver/chromedriver"
