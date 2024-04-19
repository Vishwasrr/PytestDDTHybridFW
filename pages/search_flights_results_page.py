from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from time import sleep
from utilities.utils import Utils
import logging


class SearchFlightResults(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    # changed grey to gray
    FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    SEARCH_FLIGHT_RESULTS = "//span[contains(text(), '1 Stop') or contains(text(), '2 Stop') or contains(text(), 'Non Stop')]"

    def get_filter_by_one_stop_icon(self):
        # sleep(2)
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_by_two_stop_icon(self):
        # sleep(2)
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_filter_by_non_stop_icon(self):
        # sleep(2)
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULTS)

    def filter_flights_by_stop(self, by_stop):
        if by_stop == '1 Stop':
            self.get_filter_by_one_stop_icon().click()
            # sleep(2)
        elif by_stop == '2 Stop':
            self.get_filter_by_two_stop_icon().click()
            # sleep(2)
        else:
            self.get_filter_by_non_stop_icon().click()
            # sleep(2)
        self.log.warning(f'Selecting {by_stop.split()[0]} stop flights')

    # def filter_flights(self):
    #     # self.driver.find_element(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
    #     filter = self.wait_until_element_is_clickable(
    #         By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']")
    #     filter.click()
    #     sleep(4)
        # all_stops = self.wait_for_presence_of_all_elements(
        #     By.XPATH, "//span[contains(text(), '1 Stop')]")
        # self.log.warning(len(all_stops))
