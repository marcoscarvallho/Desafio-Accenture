"""
Classe base para todas as páginas
Implementa o padrão Page Object Model
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import os
import time


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def navigate_to(self, url, max_retries=2):
        """Navega para uma URL específica com retry em caso de timeout"""
        for attempt in range(max_retries + 1):
            try:
                self.driver.get(url)
                time.sleep(1)
                # Verifica se a página carregou minimamente
                WebDriverWait(self.driver, 10).until(
                    lambda d: d.execute_script("return document.readyState") == "complete"
                )
                return
            except TimeoutException:
                if attempt < max_retries:
                    print(f"\n⚠️ Página demorou a carregar (tentativa {attempt + 1}/{max_retries + 1})")
                    print(f"   Atualizando e tentando novamente...")
                    time.sleep(2)
                else:
                    print(f"\n❌ Página não carregou após {max_retries + 1} tentativas")
                    raise
    
    def find_element(self, locator, timeout=10):
        """Encontra um elemento com wait explícito"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def find_clickable_element(self, locator, timeout=10):
        """Encontra um elemento clicável com wait explícito"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def click_element(self, locator, timeout=10):
        """Clica em um elemento"""
        try:
            element = self.find_clickable_element(locator, timeout)
            element.click()
            return element
        except:
            # Fallback: tentar com JavaScript
            element = self.find_element(locator, timeout)
            self.driver.execute_script("arguments[0].click();", element)
            return element
    
    def click_element_js(self, locator, timeout=10):
        """Clica em um elemento usando JavaScript"""
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)
        return element
    
    def send_keys(self, locator, text, timeout=10):
        """Digita texto em um campo"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        return element
    
    def scroll_to_element(self, locator, timeout=10):
        """Faz scroll até um elemento"""
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element
    
    def scroll_to_bottom(self):
        """Faz scroll até o final da página"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    def get_element_text(self, locator, timeout=10):
        """Obtém o texto de um elemento"""
        element = self.find_element(locator, timeout)
        return element.text
    
    def upload_file(self, locator, file_path, timeout=10):
        """Faz upload de um arquivo"""
        element = self.find_element(locator, timeout)
        absolute_path = os.path.abspath(file_path)
        element.send_keys(absolute_path)
        return element
    
    def select_dropdown_option(self, dropdown_locator, option_value, timeout=10):
        """Seleciona uma opção em um dropdown"""
        dropdown = self.find_clickable_element(dropdown_locator, timeout)
        dropdown.click()
        
        option_locator = (By.XPATH, f"//option[@value='{option_value}']")
        option = self.find_clickable_element(option_locator, timeout)
        option.click()
        
        return option
    
    def select_from_autocomplete(self, input_locator, text, timeout=10):
        """Seleciona uma opção de um campo de autocomplete"""
        try:
            element = self.find_element(input_locator, timeout)
            # Tentar clique normal primeiro
            element.click()
            element.clear()
            element.send_keys(text)
            element.send_keys(Keys.RETURN)
            return element
        except:
            # Fallback com JavaScript se clique normal falhar
            element = self.find_element(input_locator, timeout)
            self.driver.execute_script("arguments[0].click();", element)
            element.clear()
            element.send_keys(text)
            element.send_keys(Keys.RETURN)
            return element
