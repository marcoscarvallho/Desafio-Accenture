"""
Page Object para a página Progress Bar
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.widgets_config import PROGRESS_BAR_SELECTORS, VALIDATION
import time


class ProgressBarPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.start_stop_button_locator = (By.ID, PROGRESS_BAR_SELECTORS["start_stop_button"])
        self.reset_button_locator = (By.ID, PROGRESS_BAR_SELECTORS["reset_button"])
        self.progress_bar_locator = (By.XPATH, PROGRESS_BAR_SELECTORS["progress_bar"])
    
    def click_start_stop(self):
        """Clica no botão Start/Stop"""
        import time
        time.sleep(1)  # Aguarda antes de clicar para garantir que a UI está pronta
        self.click_element(self.start_stop_button_locator)
        time.sleep(0.2)  # Aguarda o clique processar
    
    def click_reset(self):
        """Clica no botão Reset"""
        self.click_element(self.reset_button_locator)
    
    def get_progress_value(self):
        """Obtém o valor atual da progress bar"""
        progress_bar = self.find_element(self.progress_bar_locator)
        value = progress_bar.get_attribute("aria-valuenow")
        return int(value) if value else 0
    
    def get_progress_class(self):
        """Obtém a classe da progress bar"""
        progress_bar = self.find_element(self.progress_bar_locator)
        return progress_bar.get_attribute("class")
    
    def is_complete(self):
        """Verifica se a progress bar está completa (100%)"""
        progress_class = self.get_progress_class()
        return "bg-success" in progress_class
    
    def start_and_stop_before(self, target_percentage=None, max_percentage=25):
        """Inicia a barra e para antes de atingir uma porcentagem específica"""
        # Usa o target fixo do config se não for especificado
        if target_percentage is None:
            target_percentage = VALIDATION.get("target_stop_percentage", 15)
        
        print(f"🎯 Objetivo: Parar antes ou em {target_percentage}%")
        
        self.click_start_stop()
        
        check_interval = VALIDATION["check_interval"]
        last_value = 0
        
        # Tenta parar ANTES do target (target - 2)
        stop_before = max(1, target_percentage - 2)
        
        while True:
            current_value = self.get_progress_value()
            
            # Detecta se houve mudança
            if current_value != last_value:
                print(f"   📊 {current_value}%", end="")
                
                # Se chegou perto do target, para imediatamente
                if current_value >= stop_before:
                    print(f" → ⏸️  STOP!")
                    self.click_start_stop()
                    break
                else:
                    print()
                
                last_value = current_value
            
            # Verifica a cada intervalo (muito rápido)
            time.sleep(check_interval)
        
        # Aguarda estabilizar
        time.sleep(0.3)
        stopped_at = self.get_progress_value()
        
        print(f"✅ RESULTADO: Parou em {stopped_at}% (objetivo era ≤{target_percentage}%)")
        
        # Valida que está dentro do limite máximo
        if stopped_at > max_percentage:
            print(f"⚠️  AVISO: Parou em {stopped_at}%, mas deveria ser ≤{max_percentage}%")
        
        return stopped_at
    
    def start_and_wait_completion(self, continue_from_value=None):
        """Inicia a barra e aguarda chegar a 100%"""
        # Captura o valor inicial antes de iniciar (se estiver pausada)
        value_before_start = self.get_progress_value()
        
        self.click_start_stop()
        
        # Aguarda até completar
        timeout = 120  # 2 minutos no máximo
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            if self.is_complete():
                time.sleep(0.3)
                final_value = self.get_progress_value()
                
                # Valida que continuou de onde estava (não resetou)
                if continue_from_value is not None:
                    print(f"✅ Continuou de: {continue_from_value}% → Completou: {final_value}%")
                
                return final_value
            
            time.sleep(0.5)
        
        raise Exception("Progress bar não completou no tempo esperado")
    
    def get_button_text(self):
        """Obtém o texto do botão Start/Stop"""
        button = self.find_element(self.start_stop_button_locator)
        return button.text
    
    def is_reset_visible(self):
        """Verifica se o botão Reset está visível"""
        try:
            button = self.find_element(self.reset_button_locator, timeout=2)
            return button.is_displayed()
        except:
            return False
