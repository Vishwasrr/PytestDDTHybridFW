class WebUtils:

    def clickButton(self, driver, element):
        loc_type, loc_value = element
        driver.find_element(loc_type, loc_value)

    def sendKeys(self, driver, text, element):
        loc_type, loc_value = element
        driver.find_element(loc_type, loc_value).send_keys(text)