import softest
import logging
import inspect
import csv


class Utils(softest.TestCase):

    PATH = r"testdata\tdata.csv"

    def assertListItemText(self, list_of_elements, value):
        for stop in list_of_elements:
            print("The text is: ", stop.text)
            # if stop.text == '1 Stop':
            # assert stop.text == value
            self.soft_assert(self.assertEqual, stop.text, value)
            if stop.text == value:
                print("test pass")
            else:
                print("test failed")
        self.assert_all()

    def custom_logger(logLevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        fh = logging.FileHandler('automation.log')
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s  : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    def read_data_from_csv(path):
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            data = [row for row in csv_reader]
            print(data)
            return data

