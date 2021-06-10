import time

from selenium.webdriver.support.select import Select


class AddCustomer:

    #Add customer Page
    lnkCustomers_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkCustomers_menu_item_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddnew_xpath="/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_xpath="//*[@id='Email']"
    txtPassword_xpath="//*[@id='Password']"
    txtFirstName_xpath = "//*[@id='FirstName']"
    txtLastName_xpath = "//*[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//*[@id='DateOfBirth']"
    txtCompanyName_xpath = "//*[@id='Company']"
    txtCustomerRole_xpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitemAdministrators_xpath="//*[@id='SelectedCustomerRoleIds_taglist']/li[4]/span[1]"
    lstitemRegistered_xpath="//*[@id='SelectedCustomerRoleIds_taglist']/li[1]/span[1]"
    lstitemGustes_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstitemVendors_xpath="//*[@id='SelectedCustomerRoleIds_taglist']/li[3]/span[1]"
    drpmgrOfVendor_xpath="//*[@id='VendorId']"
    txtAdminContent_xpath="//*[@id='AdminComment']"
    btnSave_xpath="/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self,driver):
        self.driver=driver
    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_item_xpath).click()
    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)


    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRole_xpath).click()


        time.sleep(3)
        if role=='Registered':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif  role=='Administrators':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role=='Gustes':
            # Here user can be Registered(or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]/span").click()
            self.listitem=self.driver.find_element_by_xpath(self.lstitemGustes_xpath)
        elif role=="Registered":
            self.listitem=self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role=="Vendors":
            self.listitem=self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem=self.driver.find_element_by_xpath(self.lstitemGustes_xpath)
        time.sleep(3)
        self.listitem.click();
        """this statement will execute java script internally and perform the click action on the element"""
        self.driver.execute_script("arguments[0].click()",self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)
    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender=="Female":
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)
    def setLasttName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)
    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)
    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def setDob(self,dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()