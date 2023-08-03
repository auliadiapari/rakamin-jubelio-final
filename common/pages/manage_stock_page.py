from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support.expected_conditions import e
import common.login_creds as LoginCreds
import common.constants as Constants

# Initiate browser, Verify page title, loggin with valid credentials, click login, redirected to homepage
# User already logged in and navigated to SKU/Product Search, Search item by SKU, Edit and managing stock, save after edit and verfy save success


class ManageStock:
    def user_logged_in_and_navigated(self):

        # Valid Credentials
        validUsername = 'qa.rakamin.jubelio@gmail.com'
        validPasswrod = 'Jubelio123!'

        # User already logged in and navigated to Product Search Page
            # Initiate browser
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LoginCreds.URL)

            # Verify login page
        pagetitle = self.driver.title
        try:
            assert 'Jubelio' == pagetitle
            print('Successfull loaded to login page')
        except:
            assert 'Jubelio' != pagetitle
            print('Unsuccessfull loaded to login page')

            # Login with valid credentials
        self.driver.find_element(By.NAME, Constants.txt_email).send_keys(validUsername)
        self.driver.find_element(By.NAME, Constants.txt_password).send_keys(validPasswrod)
        clickLogin = self.driver.find_element(By.CLASS_NAME, Constants.btn_login)
        clickLogin.click()
        
            # navigate to Product Search Page via Menu
        self.driver.find_element(By.CSS_SELECTOR, Constants.MTSMENU_BARANG).click()
        self.driver.find_element(By.CSS_SELECTOR, Constants.MTSMENU_KATALOG).click()
        self.driver.find_element(By.CSS_SELECTOR, Constants.MTSMENU_IN_REVIEW).click()
    
    def search_item(self, SKU):
        
        # User enter SKU id in search bar
        searchSKU = self.driver.find_element(By.CLASS_NAME, Constants.INREVIEW_SEARCHBAR)
        searchSKU.send_keys('HJUEID')
        searchSKU.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(1)

        # Verify the item and SKU, then clicking on the filtered item
        selectedSKU = self.driver.find_element(By.CLASS_NAME, 'item-box').text
        assert "HJUEID" in selectedSKU
        print('The item shown is right')
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CLASS_NAME, Constants.INREVIEW_FILTERED_ITEM_RESULT).click()
    
    def managing_stock(self):

        # User is on item details page, editing the stock

            # Verify user is on the In Review item page
        pageTitle = self.driver.find_element(By.CLASS_NAME, 'col-xs-10').text
        assert "In Review" in pageTitle
        print('The shown Page Title is correct')
        self.driver.implicitly_wait(2)
        
            # Editing the stock by entering the stock value
        self.driver.find_element(By.CSS_SELECTOR, ".b-t:nth-child(3) .form-control").click()
        self.driver.find_element(By.CSS_SELECTOR, ".b-t:nth-child(3) .form-control").send_keys("25")
    
    def verify_notif(self):

        # After click save, user redirected to product page and get success save value notification
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .ladda-label").click()
        self.driver.implicitly_wait(1)

            # Verify notif
        successNotif = self.driver.find_element(By.CSS_SELECTOR, ".app-alert > li").text
        assert "Data berhasil disimpan." in successNotif
        print('Verifying Success notif is done')
        self.driver.implicitly_wait(1)
        self.driver.close()








    
        
        
        


