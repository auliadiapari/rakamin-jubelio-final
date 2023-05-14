from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import common.login_creds as LoginCreds
import common.constants as Constants


# You can implement step definitions for undefined steps with these snippets:


@given('User is Already logged in and navigated')
def user_login_navigated(self):
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
    self.driver.find_element(By.NAME, Constants.txt_email).send_keys('qa.rakamin.jubelio@gmail.com')
    time.sleep(1)
    self.driver.find_element(By.NAME, Constants.txt_password).send_keys('Jubelio123!')
    time.sleep(1)
    clickLogin = self.driver.find_element(By.CLASS_NAME, Constants.btn_login)
    clickLogin.click()
    time.sleep(3)
    # navigated
    self.driver.find_element(By.CSS_SELECTOR, Constants.MTSMENU_BARANG).click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, Constants.MTSMENU_KATALOG).click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, Constants.MTSMENU_IN_REVIEW).click()
    time.sleep(1)


@when('User search item by SKU code with "{SKU}"')
def search_item(self, SKU):
    ENTER_SKU = self.driver.find_element(By.CLASS_NAME, Constants.INREVIEW_SEARCHBAR)
    time.sleep(1)
    ENTER_SKU.send_keys('HJUEID')
    time.sleep(1)
    ENTER_SKU.send_keys(Keys.ENTER)
    time.sleep(2)
    DESIRED_SKU = self.driver.find_element(By.CLASS_NAME, 'item-box').text
    assert "HJUEID" in DESIRED_SKU
    print('The item shown is right')
    time.sleep(1)
    self.driver.find_element(By.CLASS_NAME, Constants.INREVIEW_FILTERED_ITEM_RESULT).click()
    time.sleep(1)


@when('User will edit and enter value for managing stock')
def manage_stock(self):
    PAGE_TITLE = self.driver.find_element(By.CLASS_NAME, 'col-xs-10').text
    assert "In Review" in PAGE_TITLE
    print('The shown Page title is correct')
    self.driver.find_element(By.CSS_SELECTOR, ".b-t:nth-child(3) .form-control").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".b-t:nth-child(3) .form-control").send_keys("25")
    time.sleep(1)


@then('User will be notify after save the value')
def verify_notif(self):
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .ladda-label").click()
    time.sleep(1)
    SUCCESS_ALERT = self.driver.find_element(By.CSS_SELECTOR, ".app-alert > li").text
    assert "Data berhasil disimpan." in SUCCESS_ALERT
    print('Verifying Success notif is done')
    time.sleep(3)
    self.driver.close()

