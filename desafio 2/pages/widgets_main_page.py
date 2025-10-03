"""
Page Object para a página principal do DemoQA (foco em Widgets)
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.widgets_config import MAIN_PAGE_SELECTORS


class WidgetsMainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.widgets_card_locator = (By.XPATH, MAIN_PAGE_SELECTORS["widgets_card"])
        self.progress_bar_menu_locator = (By.XPATH, MAIN_PAGE_SELECTORS["progress_bar_menu"])
    
    def click_widgets_card(self):
        """Clica no card 'Widgets'"""
        import time
        time.sleep(1)
        
        selectors = [
            (By.XPATH, "//div[contains(@class, 'card')]//h5[text()='Widgets']"),
            (By.XPATH, "//div[contains(@class, 'card') and contains(., 'Widgets')]"),
            (By.XPATH, "//h5[text()='Widgets']/ancestor::div[contains(@class, 'card')]")
        ]
        
        for selector in selectors:
            try:
                self.click_element(selector)
                time.sleep(1)
                return
            except:
                continue
        
        cards = self.driver.find_elements(By.CLASS_NAME, "card")
        for card in cards:
            if "Widgets" in card.text:
                card.click()
                time.sleep(1)
                return
        
        raise Exception("Não foi possível encontrar o card Widgets")
    
    def click_progress_bar_menu(self):
        """Clica no menu 'Progress Bar'"""
        import time
        time.sleep(1)
        
        try:
            self.click_element(self.progress_bar_menu_locator)
            time.sleep(0.5)
        except:
            progress_bar_fallback = (By.XPATH, "//li[@id='item-4']//span[contains(text(), 'Progress Bar')]")
            self.click_element(progress_bar_fallback)
            time.sleep(0.5)
