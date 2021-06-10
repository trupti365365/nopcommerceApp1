import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig #from utilities package, readproperties module import Loginpage class
from Utilities.customLogger import LogGen #by using this LogGen class i can directly access LogGen method

class Test_001_Login:
    """baseURL="https://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com"
    password="admin" without calling any method we can give values like this"""
    baseURL=ReadConfig.getApplicationURL()#utilities file get data from .ini file and give to us
    #username =ReadConfig.getUseremail()  # replace hard coded values in Login test case
    #password=ReadConfig.getPassword()

    logger=LogGen.loggen()#this logger variable will be used to send the messages to the log files

    @pytest.mark.regression
    def test_homePageTitle(self,setup):      # home page title test
        #self.driver=webdriver.Chrome()initiating driver
        self.logger.info("*********************Test_001_Login**************************")
        self.logger.info("*********************Verifying Home Page Title**************************")
        self.driver = setup
        self.driver.get(self.baseURL)  # launching application
        act_title=self.driver.title  #getting title
        #self.driver.close()
        if act_title=="Your store. Login": #comparision
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            assert True
            self.driver.close()
            self.logger.info("*********************Home Page Title Test is passed**************************")
        else:
            self.driver.close()
            self.logger.error("*********************Home Page Title Test is failed**************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        #self.driver=webdriver.Chrome()
        self.logger.info("*********************Verifying Login Test**************************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)     #crerating object of Loginpage class(constructer will automatically invoked)
        #self.lp.setUserName(self.username)
        #self.lp.SetPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        #self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*********************Login Test is passed**************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")# . represents the current project directory
            self.driver.close()
            self.logger.error("*********************Login Test is failed**************************")
            assert False

