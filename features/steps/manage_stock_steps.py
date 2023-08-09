from behave import *
from common.pages.manage_stock_page import ManageStock


class ManageStockSteps:

    @given('User is Already logged in and navigated')
    def user_logged_and_navigated(self):
        ManageStock(self.driver).user_logged_in_and_navigated()


    @when('User search item by SKU code with "{SKU}"')
    def user_search_item(self):
        ManageStock(self.driver).search_item()


    @when('User will edit and enter value for managing stock')
    def user_edit_enter_value(self):
        ManageStock(self.driver).managing_stock


    @then('User will be notify after save the value')
    def user_get_notified(self):
        ManageStock(self.driver).verify_notif()
