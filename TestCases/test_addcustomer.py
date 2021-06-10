import pytest
import time

from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    #username=ReadConfig.getuseremail()
    #password=ReadConfig.getPassword()
    logger=LogGen.loggen()
    """ pytest doesnt know about this marker,this is user defined markers,,we need to create pytest.ini file
in this file we will add all this markers"""
    @pytest.mark.sanity
    def test_addcustomer(self,setup):
        self.logger.info("**************Test_003_AddCustomer***********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        #self.lp.setUserName(self.username) #we are reusing the other pageobject class(we no need to create element and write method again and again
        #self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********Login succeful**********")

        self.logger.info("*************providing customer info***************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("*********providing customer info*********")

        #self.email=random_generator() + "@gmail.com" # if email is hardcoded it will pass only one time .from second round onwords it will fail
        self.addcust.setEmail("trupti@gmail.com")
        self.addcust.setPassword("test1234")
        self.addcust.setFirstName("Panda")
        self.addcust.setLasttName("Rath")
        self.addcust.setGender("Male")
        self.addcust.setDob("6/08/2021")  # Format: D /MM / YY
        self.addcust.setCompanyName("Emids")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")



        self.addcust.setAdminContent("This is for testing.....")
        self.addcust.clickOnSave()

        self.logger.info("**********saving customer info**********")

        self.logger.info("**********add customer validation started**********")

        self.msg=self.driver.find_element_by_tag_name("card-body").text

        print(self.msg)
        if 'customer has been add sucessfully.' in self.msg:
            assert True==True
            self.logger.info("**************Add customer test passed****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_scr.png") # screenshot
            self.logger.error("**********Add customer Test Failed************")
            assert True==False

        self.driver.close()
        self.logger.info("*************Ending Test_003_AddCustomer Test**************")

        def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for x in range(size))




    """we have created pageobject class and created the test case because framework is already created
       we referred LoginPage pageobject class and Addcustomer pageobject class..this is reusability feature
       once we located the elements we can use this loginpage element in multiple test cases
    """



