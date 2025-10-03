"""
Page Object para a página principal do DemoQA (foco em Elements)
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.elements_config import MAIN_PAGE_SELECTORS


class ElementsMainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.elements_card_locator = (By.XPATH, MAIN_PAGE_SELECTORS["elements_card"])
        self.web_tables_menu_locator = (By.XPATH, MAIN_PAGE_SELECTORS["web_tables_menu"])
    
    def click_elements_card(self):
        """Clica no card 'Elements'"""
        import time
        time.sleep(1)
        
        selectors = [
            (By.XPATH, "//div[contains(@class, 'card')]//h5[text()='Elements']"),
            (By.XPATH, "//div[contains(@class, 'card') and contains(., 'Elements')]"),
            (By.XPATH, "//h5[text()='Elements']/ancestor::div[contains(@class, 'card')]")
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
            if "Elements" in card.text:
                card.click()
                time.sleep(1)
                return
        
        raise Exception("Não foi possível encontrar o card Elements")
    
    def click_web_tables_menu(self):
        """Clica no menu 'Web Tables'"""
        import time
        time.sleep(1)
        
        try:
            self.click_element(self.web_tables_menu_locator)
            time.sleep(0.5)
        except:
            web_tables_fallback = (By.XPATH, "//li[@id='item-3']//span[contains(text(), 'Web Tables')]")
            self.click_element(web_tables_fallback)
            time.sleep(0.5)
