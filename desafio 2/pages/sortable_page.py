"""
Page Object para a página Sortable
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from config.interactions_config import SORTABLE_SELECTORS, EXPECTED_ORDER


class SortablePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.list_items_locator = (By.XPATH, SORTABLE_SELECTORS["list_items"])
    
    def get_current_order(self):
        """Obtém a ordem atual dos elementos"""
        items = self.driver.find_elements(*self.list_items_locator)
        return [item.text.strip() for item in items]
    
    def get_item_by_text(self, text):
        """Obtém um elemento específico pelo texto"""
        items = self.driver.find_elements(*self.list_items_locator)
        for item in items:
            if item.text.strip() == text:
                return item
        return None
    
    def drag_and_drop_to_position(self, source_text, target_position):
        """Arrasta um elemento para uma posição específica"""
        import time
        
        # Encontra o elemento source
        source = self.get_item_by_text(source_text)
        if not source:
            raise Exception(f"Elemento '{source_text}' não encontrado")
        
        # Encontra todos os elementos
        items = self.driver.find_elements(*self.list_items_locator)
        
        # Elemento target é o que está na posição desejada
        if target_position >= len(items):
            target_position = len(items) - 1
        
        target = items[target_position]
        
        # Executa o drag and drop
        actions = ActionChains(self.driver)
        actions.click_and_hold(source)
        actions.pause(0.2)
        actions.move_to_element(target)
        actions.pause(0.2)
        actions.release()
        actions.perform()
        
        time.sleep(0.3)
    
    def sort_to_descending_order(self):
        """Ordena os elementos em ordem decrescente (Six, Five, Four, Three, Two, One)"""
        import time
        
        # Scroll down para evitar anúncios no topo
        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(0.5)
        
        print("\n🔄 Iniciando ordenação decrescente...")
        
        max_attempts = 20  # Limite de tentativas para evitar loop infinito
        attempt = 0
        
        while attempt < max_attempts:
            current_order = self.get_current_order()
            print(f"   📊 Ordem atual: {', '.join(current_order)}")
            
            # Verifica se já está na ordem correta
            if current_order == EXPECTED_ORDER:
                print("✅ Elementos já estão na ordem correta!")
                return True
            
            # Encontra o primeiro elemento fora de ordem
            for i, expected in enumerate(EXPECTED_ORDER):
                if current_order[i] != expected:
                    # Encontra onde está o elemento esperado
                    current_position = current_order.index(expected)
                    
                    print(f"   🔀 Movendo '{expected}' da posição {current_position} para {i}")
                    
                    # Move o elemento para a posição correta
                    self.drag_and_drop_to_position(expected, i)
                    
                    break
            
            attempt += 1
        
        # Verifica se conseguiu ordenar
        final_order = self.get_current_order()
        if final_order == EXPECTED_ORDER:
            print("✅ Ordenação concluída com sucesso!")
            return True
        else:
            print(f"⚠️  Não conseguiu ordenar completamente. Ordem final: {', '.join(final_order)}")
            return False
    
    def verify_order(self, expected_order):
        """Verifica se os elementos estão na ordem esperada"""
        current_order = self.get_current_order()
        return current_order == expected_order
