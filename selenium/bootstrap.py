from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from config import Config
from constants import Constant


def get_chrome_driver(is_headless_mode=False):
    chrome_driver_path = Constant.LINUX_CHROME_DRIVER_PATH.value
    if Config.os_type == Constant.WINDOWS_OS.value:
        chrome_driver_path = Constant.WINDOWS_CHROME_DRIVER_PATH.value
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=get_chrome_driver_options(is_headless_mode))
    return driver


def get_chrome_driver_options(is_headless_mode=False):
    chr_options = Options()
    chr_options.headless = is_headless_mode
    chr_options.add_experimental_option("detach", True)
    chr_options.add_argument("--ignore-certificate-errors")
    chr_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return chr_options
