"""
Page Object para a página principal do DemoQA
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage
from config.config import MAIN_PAGE_SELECTORS


class MainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.forms_card_locator = (By.XPATH, MAIN_PAGE_SELECTORS["forms_card"])
    
    def click_forms_card(self):
        """Clica no card 'Forms'"""
        import time
        time.sleep(2)
        
        selectors = [
            (By.XPATH, "//div[contains(@class, 'card')]//h5[text()='Forms']"),
            (By.XPATH, "//div[contains(@class, 'card') and contains(., 'Forms')]"),
            (By.XPATH, "//div[@class='card mt-4 top-card']//h5[text()='Forms']"),
            (By.XPATH, "//h5[text()='Forms']/ancestor::div[contains(@class, 'card')]")
        ]
        
        for selector in selectors:
            try:
                self.click_element(selector)
                time.sleep(2)
                return
            except:
                continue
        
        cards = self.driver.find_elements(By.CLASS_NAME, "card")
        for card in cards:
            if "Forms" in card.text:
                card.click()
                time.sleep(2)
                return
        
        raise Exception("Não foi possível encontrar o card Forms")
    
    def click_practice_form_menu(self):
        """Clica no menu 'Practice Form'"""
        import time
        time.sleep(2)
        
        try:
            practice_form_locator = (By.XPATH, MAIN_PAGE_SELECTORS["practice_form_menu"])
            self.click_element(practice_form_locator)
            time.sleep(2)
        except:
            practice_form_fallback = (By.XPATH, "//li[@id='item-0']//span[contains(text(), 'Practice Form')]")
            self.click_element(practice_form_fallback)
            time.sleep(2)
