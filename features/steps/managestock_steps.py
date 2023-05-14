from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import common.login_creds as LoginCreds
import common.constants as Constants


@given('User is Already logged in')
def user_login(self):
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
    time.sleep(2)
    self.driver.find_element(By.NAME, Constants.txt_password).send_keys('Jubelio123!')
    time.sleep(2)
    clickLogin = self.driver.find_element(By.CLASS_NAME, Constants.btn_login)
    clickLogin.click()
    time.sleep(2)


@when('User Click on "Barang", Select "Katalog" and "In Review" Menu')
def click_menu(self):
    self.driver.find_element(By.CSS_SELECTOR, Constants.MTSMENU_BARANG).click()
    self.driver.find_element(By.CSS_SELECTOR, Constants.MTSMENU_KATALOG).click()
    self.driver.find_element(By.CSS_SELECTOR, Constants.MTSMENU_IN_REVIEW).click()
    REVIEW_PAGE_TITLE = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div/div/div[1]/h1').txt
    assert 'In Review' in REVIEW_PAGE_TITLE


@when('User Enter SKU Code with "HJUEID" in Search')
def enter_sku_code(self):
    # ENTER_SKU = self.driver.find_element(By.CSS_SELECTOR, Constants.INREVIEW_SEARCHBAR).send_keys('HJUEID')
    # ENTER_SKU.send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, Constants.INREVIEW_SEARCHBAR).send_keys('HJUEID')
    self.driver.find_element(By.CSS_SELECTOR, Constants.INREVIEW_SEARCHBAR_ICON).click()
    time.sleep(4)
    self.driver.find_element(By.CSS_SELECTOR, Constants.INREVIEW_FILTERED_ITEM_RESULT).click()
    DESIRED_SKU = self.driver.find_element(By.CSS_SELECTOR, 'item-box').text
    assert "HJUEID" in DESIRED_SKU


@then('User Will Edit and Enter the desired Value in "Batas Stok Menipis" Field')
def edit_stock(self):
    self.driver.find_element(By.CSS_SELECTOR, ".b-t:nth-child(3) .form-control").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".b-t:nth-child(3) .form-control").send_keys("25")
    time.sleep(1)


@then('User will Click on "Simpan" and Will be notify with "Data Berhasil Disimpan"')
def verify_update(self):
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .ladda-label").click()
    SUCCESS_ALERT = self.driver.find_element(By.CSS_SELECTOR, ".app-alert > li").text
    assert "Data berhasil disimpan." in SUCCESS_ALERT
