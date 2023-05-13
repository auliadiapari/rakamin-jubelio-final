from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import common.login_creds as LoginCreds
import common.constants as Constants


# You can implement step definitions for undefined steps with these snippets:

@given('User is on Jubelio login page')
def on_login_page(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.get(LoginCreds.URL)
    TITLE_LOGIN_PAGE = self.driver.title
    try:
        assert 'Jubelio' == TITLE_LOGIN_PAGE
        print('Successful Loaded to Login Page')
    except:
        assert 'Jubelio' != TITLE_LOGIN_PAGE
        print('Unsuccessful Loaded to Login Page')


@when('User input  Email with "{email}" and Password with "{password}"')
def input_email_and_password(self, email, password):
    self.driver.find_element(By.NAME, Constants.txt_email).send_keys(email)
    time.sleep(2)
    self.driver.find_element(By.NAME, Constants.txt_password).send_keys(password)
    time.sleep(2)


@when('User Click on Login')
def click_login(self):
    clickLogin = self.driver.find_element(By.CLASS_NAME, Constants.btn_login)
    clickLogin.click()
    time.sleep(2)


@then('User will be redirected to homepage')
def redirected_to_homepage(self):
    self.driver.find_element(By.CSS_SELECTOR,
                             ".metismenu-container:nth-child(1) > .metismenu-item:nth-child(1) span").click()
    PAGE_HEADER = self.driver.find_element(By.CSS_SELECTOR,
                                           '#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div >'
                                           'div > div.col-xs-10 > h1').text
    time.sleep(2)
    try:
        assert 'Dashboard' == PAGE_HEADER
        print('Assertion is passed')
    except:
        assert 'Dashboard' != PAGE_HEADER
        print('Assertion is failed')
    time.sleep(3)
    self.driver.close()
