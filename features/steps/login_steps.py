from behave import *
from common.pages.login_page import LoginPage


class LoginSteps(LoginPage):

    @given('User is on Jubelio login page')
    def user_on_login_page(self):
        LoginPage.on_login_page
    
    @when('User input  Email with "{email}" and Password with "{password}"')
    def user_input_credentials(self):
        LoginPage.input_email_and_password()
    
    @when('User Click on Login')
    def user_click_login(self):
        LoginPage.click_login()
    
    @then('User will be redirected to homepage')
    def user_redirected_homepage(self):
        LoginPage.redirected_to_homepage()


LoginSteps()
    


    
    


    





