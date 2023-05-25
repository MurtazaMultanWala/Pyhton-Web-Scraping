from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

website_link = "https://www.htmlelements.com/demos/button/overview/"
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome("selenium/chromedriver", options=chr_options)

driver.get(website_link)

delay = 15 # seconds
try:
    device_bar = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@class="device"]')))
    portrait_button = driver.find_element("xpath", '//button[@title="Phone Portrait"]')
    portrait_button.click()
except TimeoutException:
    print ("Loading took too much time!")