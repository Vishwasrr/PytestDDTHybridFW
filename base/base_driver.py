from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert


class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        # pageLength = self.driver.execute_script(
        #     "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        # while True:
        #     last_count = pageLength
        #     sleep(3)
        #     pageLength = self.driver.execute_script(
        #         "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        #     if last_count == pageLength:
        #         break
        self.driver.find_element(By.XPATH, "//body").send_keys(Keys.ENTER)

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.presence_of_all_elements_located((locator_type, locator)))
    
    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.element_to_be_clickable((locator_type, locator)))

    def dismiss_alerts(self):
        alert = Alert(self.driver)
        alert.dismiss()

    def refresh_browser(self):
        self.driver.refresh()
