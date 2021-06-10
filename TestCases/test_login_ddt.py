import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig #from utilities package, readproperties module import Loginpage class
from Utilities.customLogger import LogGen #by using this LogGen class i can directly access LogGen method
from Utilities import XLUtils24

class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURL()#utilities file get data from .ini file and give to us
    PATH=".//TestData/LoginData.xlsx"
    logger=LogGen.loggen()#this logger variable will be used to send the messages to the log files

    @pytest.mark.regression
    def test_login_ddt(self,setup):

        self.logger.info("*********************Test_002_DDT_Login**************************")
        self.logger.info("*********************Verifying Login DDT Test**************************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)     #crerating object of Loginpage class(constructer will automatically invoked)

        self.rows=XLUtils24.getRowCount(self.path,'Sheet1')
        print("number of rows in Excel: ",self.rows)

        for r in range(2,self.rows+1):
            self.user=XLUtils24.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils24.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils24.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            lst_status=[]

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("*****passed*********")
                    self.lp.clickLogout();
                    lst_status.append("Pass")

                elif self.exp=="Fail":
                    self.logger.info("*****failed*********")
                    self.lp.clickLogout();
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("*****failed*********")
                    self.lp.clickLogout();
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("*****passed*********")
                    self.lp.clickLogout();
                    lst_status.append("Pass")

            if "Fail" not in lst_status:
                self.logger.info("********Login DDT test passed******")
                self.driver.close()
                assert True

            else:
                self.logger.info("********Login DDT test failed******")
                self.driver.close()
                assert False
            self.logger.info("********End of Login DDT Test******")
            self.logger.info("********completed TC_LoginDDT_002******")






