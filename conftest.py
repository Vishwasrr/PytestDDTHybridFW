import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from utilities.utils import Utils
import time
driver = None


@pytest.fixture(autouse=True)
def setup(request, browser):
    log = Utils.custom_logger()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--disable-notifications')
    if browser == "chrome":
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome()
        # driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    # wait = WebDriverWait(driver, 10)
    driver.get("https://www.yatra.com")
    driver.maximize_window()
    request.cls.driver = driver
    # request.cls.wait = wait
    yield driver
    log.warning("\n"+"="*80)
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    # parser.addoption("--browser")


@pytest.fixture(scope='class', autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.yatra.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver = item.cls.driver
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px"'\
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))
        report.extras = extra


def pytest_html_report_title(report):
    report.title = "My Learning"
