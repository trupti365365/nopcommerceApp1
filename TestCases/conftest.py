from selenium import webdriver
import pytest
"""@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver #fixture method can return the driver insted of creating driver multiple times ..i created one fixture
 when i call this fixture it will return the driver for us
we are doing this to avoid duplication  """
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver=webdriver.Edge
        print("Launching internet explorer browser")

    return driver

def pytest_addoption(parser): #this will get the value from CLI\hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):        # this will return the browser value to set option
    return request.config.getoption("--browser")

################## pyTest HTML Reports  ############################
# it is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Trupti'

# it is hook for delete/Modify Enviroment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins",None)
