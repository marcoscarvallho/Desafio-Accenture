"""
Page Object para a página principal do DemoQA (foco em AFW)
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.AFW_config import MAIN_PAGE_SELECTORS


class AFWMainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.afw_card_locator = (By.XPATH, MAIN_PAGE_SELECTORS["afw_card"])
        self.browser_windows_menu_locator = (By.XPATH, MAIN_PAGE_SELECTORS["browser_windows_menu"])
    
    def click_afw_card(self):
        """Clica no card 'Alerts, Frame & Windows'"""
        self.click_element(self.afw_card_locator)
    
    def click_browser_windows_menu(self):
        """Clica no menu 'Browser Windows'"""
        self.click_element(self.browser_windows_menu_locator)
