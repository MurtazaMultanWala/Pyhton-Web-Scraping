from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from constants import Constant
from bootstrap import get_chrome_driver

website_link = "https://www.htmlelements.com/demos/button/overview/"
driver = get_chrome_driver()
driver.get(website_link)

try:
    delay = int(Constant.DELAY_IN_SECONDS.value)
    device_bar = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@class="device"]')))
    portrait_button = driver.find_element("xpath", '//button[@title="Phone Portrait"]')
    portrait_button.click()
except TimeoutException:
    print("Loading took too much time!")

driver.quit()
