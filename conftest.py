import pytest
from selenium import webdriver

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Chrome/Firefox"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="E:\\Browsers\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="E:\\Browsers\\geckodriver.exe")

    driver.maximize_window()
    driver.get("https://testing.d3eymc78cqte40.amplifyapp.com/login")

    request.cls.driver = driver

    yield
    driver.quit()


@pytest.fixture()
def Dataload_orderPlacement():
    return ["123435", "Rahul", "9876543210", "9976544200", "rahooman@yahoo.com", "JP nagar", "Starbucks", "560166", "Bengaluru", "Karnataka", "Dr. Raghu", "C:\\Users\\devmishr\\Desktop\\Test.docx"]

@pytest.fixture()
def Dataload_medDetails():
    return ["Horlicks", "Augmentin", "Sporidex", "Codifab"]

@pytest.fixture()
def Dataload_login():
    return ["TestUser123", "123456"]

@pytest.fixture()
def Dataload_existingOrderActions():
    return ["123435"]


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

