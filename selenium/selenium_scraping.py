from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from config import Config
from constants import Constant

website_link = "https://www.htmlelements.com/demos/button/overview/"
chr_options = Options()
chr_options.add_experimental_option("detach", True)
chr_options.add_argument("--ignore-certificate-errors")
chr_options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome_driver_path = Constant.LINUX_CHROME_DRIVER_PATH.value
if Config.os_type == Constant.WINDOWS_OS.value:
    chrome_driver_path = Constant.WINDOWS_CHROME_DRIVER_PATH.value

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chr_options)
driver.get(website_link)

try:
    delay = int(Constant.DELAY_IN_SECONDS.value)
    device_bar = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@class="device"]')))
    portrait_button = driver.find_element("xpath", '//button[@title="Phone Portrait"]')
    portrait_button.click()
except TimeoutException:
    print("Loading took too much time!")
