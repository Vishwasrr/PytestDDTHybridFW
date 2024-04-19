from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from pages.yatra_launch_page import LaunchPage
from pages.search_flights_results_page import SearchFlightResults
from utilities.utils import Utils
import pytest
import softest
import logging
from ddt import data, ddt, unpack, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):

    log = Utils.custom_logger(logLevel=logging.INFO)
    PATH = r"testdata\tdata.csv"

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.launch_page = LaunchPage(self.driver)
        self.utils = Utils()


    print(*Utils.read_data_from_csv(PATH))
    @data(*Utils.read_data_from_csv(PATH))
    @unpack
    def test_search_flight_1_stop(self, goingfrom, goingto, departuredate, stops):
        sleep(2)
        # search_flight_results = self.launch_page.searchFlights(
        #     "New Delhi", "BOM", "19/04/2024")
        
        search_flight_results = self.launch_page.searchFlights(
            goingfrom, goingto, departuredate)
        

        self.launch_page.page_scroll()
        # search_flight_results.filter_flights_by_stop("1 Stop")
        search_flight_results.filter_flights_by_stop(stops)
        all_stops = search_flight_results.get_search_flight_results()
        self.log.info(len(all_stops))

        # ut = Utils()
        # self.utils.assertListItemText(all_stops, "1 Stop")
        self.utils.assertListItemText(all_stops, stops)

    # def test_search_flight_2_stop(self):
    #     sleep(2)
    #     search_flight_results = self.launch_page.searchFlights(
    #         "New Delhi ", "New York", "14/04/2024")
    #     self.launch_page.page_scroll()
    #     search_flight_results.filter_flights_by_stop('2 Stop')
    #     all_stops = search_flight_results.get_search_flight_results()
    #     self.log.info(len(all_stops))

    #     # ut = Utils()
    #     self.utils.assertListItemText(all_stops, '1 Stop')

# lp.enterDepartFromLocation("New Delhi ")
# sleep(3)
# lp.enterGoingToLocation("New York")
# lp.enterDepartureDate("14/04/2024")
# sleep(5)
# lp.clickSearchFlightsButton()
