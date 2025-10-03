"""
Page Object para a página principal do DemoQA (foco em Interactions)
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.interactions_config import MAIN_PAGE_SELECTORS


class InteractionsMainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.interactions_card_locator = (By.XPATH, MAIN_PAGE_SELECTORS["interactions_card"])
        self.sortable_menu_locator = (By.XPATH, MAIN_PAGE_SELECTORS["sortable_menu"])
    
    def click_interactions_card(self):
        """Clica no card 'Interactions'"""
        import time
        time.sleep(1)
        
        selectors = [
            (By.XPATH, "//div[contains(@class, 'card')]//h5[text()='Interactions']"),
            (By.XPATH, "//div[contains(@class, 'card') and contains(., 'Interactions')]"),
            (By.XPATH, "//h5[text()='Interactions']/ancestor::div[contains(@class, 'card')]")
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
            if "Interactions" in card.text:
                card.click()
                time.sleep(1)
                return
        
        raise Exception("Não foi possível encontrar o card Interactions")
    
    def click_sortable_menu(self):
        """Clica no menu 'Sortable'"""
        import time
        time.sleep(1)
        
        try:
            self.click_element(self.sortable_menu_locator)
            time.sleep(0.5)
        except:
            sortable_fallback = (By.XPATH, "//li[@id='item-0']//span[contains(text(), 'Sortable')]")
            self.click_element(sortable_fallback)
            time.sleep(0.5)
