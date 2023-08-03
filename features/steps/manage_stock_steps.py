from behave import *
from common.pages.manage_stock_page import ManageStock


class ManageStockSteps(ManageStock):

    @given('User is Already logged in and navigated')
    def user_logged_and_navigated(self):
        ManageStock.user_logged_in_and_navigated()


    @when('User search item by SKU code with "{SKU}"')
    def user_search_item(self):
        ManageStock.search_item()


    @when('User will edit and enter value for managing stock')
    def user_edit_enter_value(self):
        ManageStock.managing_stock


    @then('User will be notify after save the value')
    def user_get_notified(self):
        ManageStock.verify_notif()


ManageStockSteps()

