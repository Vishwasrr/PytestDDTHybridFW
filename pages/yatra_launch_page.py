from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from pages.search_flights_results_page import SearchFlightResults
from time import sleep
from utilities.utils import Utils
import logging
from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):

    log = Utils.custom_logger(logLevel=logging.INFO)
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div//div//li//div//p[@class='ac_cityname']"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_FLIGHT_BUTTON = "//input[@value='Search Flights']"

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getDepartureDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDatesField(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ALL_DATES)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_FLIGHT_BUTTON)

    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)

    # def depart(self, depart_location):
    #     depart_from = self.wait_until_element_is_clickable(
    #         By.XPATH, "//input[@id='BE_flight_origin_city']")
    #     depart_from.send_keys(depart_location)
    #     depart_from.send_keys(Keys.ENTER)

    def enterGoingToLocation(self, goingtolocation):
        going_to = self.getGoingToField()
        going_to.click()
        sleep(2)
        going_to.send_keys(goingtolocation)
        sleep(2)
        # self.getGoingToField().send_keys(Keys.ENTER)
        search_results = self.getGoingToResults()
        for results in search_results:
            if goingtolocation in results.text:
                results.click()
                break
        # self.log.info(search_results)

    def enterDepartureDate(self, departuredate):
        try:
            self.getDepartureDateField().click()
            all_dates = self.getAllDatesField()
            for date in all_dates:
                if date.get_attribute("data-date") == departuredate:
                    self.log.info(date.get_attribute("data-date"))
                    date.click()
                    break
        except StaleElementReferenceException:
            self.getDepartureDateField().click()
            all_dates = self.getAllDatesField()
            for date in all_dates:
                if date.get_attribute("data-date") == departuredate:
                    self.log.info(date.get_attribute("data-date"))
                    date.click()
                    break

    def clickSearchFlightsButton(self):
        self.getSearchButton().click()
        sleep(4)

    def searchFlights(self, departlocation, goingtolocation, departuredate):
        self.enterDepartFromLocation(departlocation)
        sleep(3)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepartureDate(departuredate)
        sleep(3)
        self.clickSearchFlightsButton()
        search_flight_result = SearchFlightResults(self.driver)
        return search_flight_result

    # def selectdate(self, depaturedate):
    #     date = self.wait_until_element_is_clickable(
    #         By.XPATH, self.ALL_DATES)
    #     date.click()
    #     all_dates = self.wait_for_presence_of_all_elements(
    #         By.XPATH, self.ALL_DATES)

    #     for date in all_dates:
    #         if date.get_attribute("data-date") == depaturedate:
    #             date.click()
    #             break

        # sleep(4)
