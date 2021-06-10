import pytest
import time


from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from PageObjects.SearchCustomerPage import SearchCustomer

class Test_SearchCustomerByName:
    baseURL=ReadConfig.getApplicationURL()
    #username=ReadConfig.getuseremail()
    #password=ReadConfig.getPassword()
    logger=LogGen.loggen() #Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("*************SearchCustomerByName_005**************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        # self.lp.setUserName(self.username) #we are reusing the other pageobject class(we no need to create element and write method again and again
        # self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********Login successful**********")

        self.logger.info("**********starting search customer By Name*******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("**********searching customer by Name***********")
        searchcust=SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchcustomerByName("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("***************TC_SearchCustomerByName_005 Finished************")

        self.driver.close()