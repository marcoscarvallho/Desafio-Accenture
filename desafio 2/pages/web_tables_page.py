"""
Page Object para a página Web Tables
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.elements_config import WEB_TABLES_SELECTORS


class WebTablesPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.add_button_locator = (By.ID, WEB_TABLES_SELECTORS["add_button"])
        self.first_name_locator = (By.ID, WEB_TABLES_SELECTORS["first_name"])
        self.last_name_locator = (By.ID, WEB_TABLES_SELECTORS["last_name"])
        self.email_locator = (By.ID, WEB_TABLES_SELECTORS["email"])
        self.age_locator = (By.ID, WEB_TABLES_SELECTORS["age"])
        self.salary_locator = (By.ID, WEB_TABLES_SELECTORS["salary"])
        self.department_locator = (By.ID, WEB_TABLES_SELECTORS["department"])
        self.submit_button_locator = (By.ID, WEB_TABLES_SELECTORS["submit_button"])
        self.search_box_locator = (By.ID, WEB_TABLES_SELECTORS["search_box"])
    
    def click_add_button(self):
        """Clica no botão Add"""
        self.click_element(self.add_button_locator)
    
    def fill_registration_form(self, first_name, last_name, email, age, salary, department):
        """Preenche o formulário de registro"""
        self.send_keys(self.first_name_locator, first_name)
        self.send_keys(self.last_name_locator, last_name)
        self.send_keys(self.email_locator, email)
        self.send_keys(self.age_locator, str(age))
        self.send_keys(self.salary_locator, str(salary))
        self.send_keys(self.department_locator, department)
    
    def click_submit(self):
        """Clica no botão Submit"""
        self.click_element(self.submit_button_locator)
    
    def create_record(self, record_data):
        """Cria um novo registro completo"""
        self.click_add_button()
        import time
        time.sleep(0.2)
        
        self.fill_registration_form(
            record_data["first_name"],
            record_data["last_name"],
            record_data["email"],
            record_data["age"],
            record_data["salary"],
            record_data["department"]
        )
        
        self.click_submit()
        time.sleep(0.2)
    
    def search_record(self, search_term):
        """Busca um registro na tabela"""
        search_box = self.find_element(self.search_box_locator)
        search_box.clear()
        self.send_keys(self.search_box_locator, search_term)
        import time
        time.sleep(0.2)
    
    def is_record_visible(self, email):
        """Verifica se um registro está visível na tabela"""
        try:
            self.search_record(email)
            row_locator = (By.XPATH, f"//div[@class='rt-tbody']//div[contains(text(), '{email}')]")
            element = self.find_element(row_locator, timeout=2)
            return element is not None
        except:
            return False
    
    def get_record_row(self, email):
        """Obtém a linha da tabela que contém o email especificado"""
        self.search_record(email)
        import time
        time.sleep(0.5)
        
        row_locator = (By.XPATH, f"//div[@class='rt-tbody']//div[contains(@class, 'rt-tr-group') and .//div[contains(text(), '{email}')]]")
        return self.find_element(row_locator)
    
    def edit_record(self, email, new_data):
        """Edita um registro existente"""
        import time
        
        # Buscar e clicar no botão de editar
        self.search_record(email)
        time.sleep(0.5)
        
        edit_button_locator = (By.XPATH, f"//div[contains(text(), '{email}')]/ancestor::div[@class='rt-tr-group']//span[@title='Edit']")
        self.click_element(edit_button_locator)
        time.sleep(0.5)
        
        # Limpar e preencher com novos dados
        first_name_field = self.find_element(self.first_name_locator)
        first_name_field.clear()
        
        last_name_field = self.find_element(self.last_name_locator)
        last_name_field.clear()
        
        email_field = self.find_element(self.email_locator)
        email_field.clear()
        
        age_field = self.find_element(self.age_locator)
        age_field.clear()
        
        salary_field = self.find_element(self.salary_locator)
        salary_field.clear()
        
        department_field = self.find_element(self.department_locator)
        department_field.clear()
        
        # Preencher com novos dados
        self.fill_registration_form(
            new_data["first_name"],
            new_data["last_name"],
            new_data["email"],
            new_data["age"],
            new_data["salary"],
            new_data["department"]
        )
        
        self.click_submit()
        time.sleep(0.5)
    
    def delete_record(self, email):
        """Deleta um registro específico"""
        import time
        
        # Buscar o registro
        self.search_record(email)
        time.sleep(0.15)
        
        # Clicar no botão de deletar
        delete_button_locator = (By.XPATH, f"//div[contains(text(), '{email}')]/ancestor::div[@class='rt-tr-group']//span[@title='Delete']")
        self.click_element(delete_button_locator)
        time.sleep(0.15)
        
        # Limpar busca
        search_box = self.find_element(self.search_box_locator)
        search_box.clear()
        time.sleep(0.1)
    
    def get_all_table_rows(self):
        """Retorna todas as linhas visíveis da tabela"""
        rows_locator = (By.XPATH, WEB_TABLES_SELECTORS["table_rows"])
        rows = self.driver.find_elements(*rows_locator)
        
        # Filtrar apenas linhas com conteúdo
        non_empty_rows = []
        for row in rows:
            if row.text.strip() and row.text.strip() != " ":
                non_empty_rows.append(row)
        
        return non_empty_rows
    
    def clear_search(self):
        """Limpa o campo de busca"""
        search_box = self.find_element(self.search_box_locator)
        search_box.clear()
        import time
        time.sleep(0.1)
