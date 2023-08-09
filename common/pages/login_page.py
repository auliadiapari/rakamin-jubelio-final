from selenium import webdriver
from selenium.webdriver.common.by import By
from common.pages.base_page import BasePageUsers, BasePageLocators

# Initiate browser, verify page title, login with valid credentials, click login, redirect to homepage

class LoginPage(BasePageUsers, BasePageLocators):
    def on_login_page(self):

        # Initiate browser
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BasePageUsers.URL)

        # Verify login page
        pageTitle = self.driver.title
        try:
            assert 'Jubelio' == pageTitle
            print('Successfull loaded to login page')
        except:
            assert 'Jubelio' != pageTitle
            print('Unsuccessfull loaded to login page')

    def input_email_and_password(self, email, password):
        
        # Login with valid credentials
        self.driver.find_element(By.NAME, BasePageLocators.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(By.NAME, BasePageLocators.PASSWORD_FIELD).send_keys(password)

    def click_login(self):

        # Click login
        clicklogin = self.driver.find_element(By.CLASS_NAME, BasePageLocators.LOGIN_BUTTON)
        clicklogin.click()

    def redirected_to_homepage(self):
        
        # Redirect to homepage
        self.driver.find_element(By.CSS_SELECTOR,
                             ".metismenu-container:nth-child(1) > .metismenu-item:nth-child(1) span").click()
        pageheader = self.driver.find_element(By.CSS_SELECTOR,
                                           '#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div >'
                                           'div > div.col-xs-10 > h1').text
        self.driver.implicitly_wait(5)
        try:
            assert 'Dashboard' == pageheader
            print('Assertion is passed')
        except:
            assert 'Dashboard' != pageheader
            print('Assertion is failed')

        self.driver.implicitly_wait(3)
        self.driver.close()



    


        

        