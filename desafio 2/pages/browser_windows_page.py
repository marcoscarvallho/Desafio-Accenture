"""
Page Object para a página Browser Windows
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.AFW_config import BROWSER_WINDOWS_SELECTORS, TEST_DATA


class BrowserWindowsPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.new_window_button_locator = (By.ID, BROWSER_WINDOWS_SELECTORS["new_window_button"])
        self.sample_heading_locator = (By.ID, BROWSER_WINDOWS_SELECTORS["sample_heading"])
    
    def click_new_window(self):
        """Clica no botão 'New Window'"""
        self.click_element(self.new_window_button_locator)
    
    def switch_to_new_window(self):
        """Muda para a nova janela aberta"""
        # Espera pela nova janela
        import time
        time.sleep(1)
        
        # Guarda a janela original
        original_window = self.driver.current_window_handle
        
        # Pega todas as janelas
        all_windows = self.driver.window_handles
        
        # Muda para a nova janela (última aberta)
        for window in all_windows:
            if window != original_window:
                self.driver.switch_to.window(window)
                break
        
        return original_window
    
    def get_sample_message(self):
        """Obtém a mensagem de exemplo na nova janela"""
        return self.get_element_text(self.sample_heading_locator)
    
    def close_current_window(self):
        """Fecha a janela atual"""
        self.driver.close()
    
    def switch_to_window(self, window_handle):
        """Muda para uma janela específica"""
        self.driver.switch_to.window(window_handle)
    
    def get_window_count(self):
        """Retorna o número de janelas abertas"""
        return len(self.driver.window_handles)
