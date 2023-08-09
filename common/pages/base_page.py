"""Constant variables used throughout the framework."""


class BasePageUsers:

    # Valid Credetials
    VALID_EMAIL = "qa.rakamin.jubelio@gmail.com"
    VALID_PASSWORD = "Jubelio123!"
    URL = "https://app.jubelio.com/login"

class BasePageLocators:

    # UI Selectors/Locators
        # Login Page

    EMAIL_FIELD = "email"
    PASSWORD_FIELD = "password"
    LOGIN_BUTTON = "ladda-label"

    ERR_MSG_EMAIL = "Email harus diisi."
    ERR_MSG_PASSWORD = "Password harus diisi."

    # Homepage
        # CSS
    MTSMENU_BARANG = ".metismenu-container:nth-child(1) > .metismenu-item:nth-child(2) > .metismenu-link " \
                    ".metismenu-state-icon"
    MTSMENU_KATALOG = ".visible .metismenu-state-icon"
    MTSMENU_IN_REVIEW = ".metismenu-item:nth-child(1) > .visible > .metismenu-item:nth-child(1) span"

        # Class name
    INREVIEW_SEARCHBAR = "form-control"
    INREVIEW_SEARCHBAR_ICON = "glyphicon glyphicon-search"
    INREVIEW_FILTERED_ITEM_RESULT = "item-image"



