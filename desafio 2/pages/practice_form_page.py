"""
Page Object para a página de Practice Form
"""
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from config.config import FORM_SELECTORS, MODAL_SELECTORS, TEST_DATA


class PracticeFormPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self._setup_locators()
    
    def _setup_locators(self):
        """Configura todos os locators da página"""
        self.first_name_locator = (By.ID, FORM_SELECTORS["first_name"])
        self.last_name_locator = (By.ID, FORM_SELECTORS["last_name"])
        self.email_locator = (By.ID, FORM_SELECTORS["email"])
        self.mobile_locator = (By.ID, FORM_SELECTORS["mobile"])
        self.date_of_birth_locator = (By.ID, FORM_SELECTORS["date_of_birth"])
        self.subjects_input_locator = (By.ID, FORM_SELECTORS["subjects_input"])
        self.current_address_locator = (By.ID, FORM_SELECTORS["current_address"])
        self.upload_picture_locator = (By.ID, FORM_SELECTORS["upload_picture"])
        self.state_input_locator = (By.XPATH, FORM_SELECTORS["state_input"])
        self.city_input_locator = (By.XPATH, FORM_SELECTORS["city_input"])
        self.submit_button_locator = (By.ID, FORM_SELECTORS["submit_button"])
        
        # Modal locators
        self.modal_title_locator = (By.ID, MODAL_SELECTORS["modal_title"])
        self.modal_table_rows_locator = (By.XPATH, MODAL_SELECTORS["modal_table_rows"])
        self.close_button_locator = (By.ID, MODAL_SELECTORS["close_button"])
    
    def fill_first_name(self, first_name):
        """Preenche o campo First Name"""
        print(f"      📝 Preenchendo First Name: {first_name}")
        self.send_keys(self.first_name_locator, first_name)
        print(f"      ✅ First Name preenchido com sucesso!")
    
    def fill_last_name(self, last_name):
        """Preenche o campo Last Name"""
        print(f"      📝 Preenchendo Last Name: {last_name}")
        self.send_keys(self.last_name_locator, last_name)
        print(f"      ✅ Last Name preenchido com sucesso!")
    
    def fill_email(self, email):
        """Preenche o campo Email"""
        print(f"      📝 Preenchendo Email: {email}")
        self.send_keys(self.email_locator, email)
        print(f"      ✅ Email preenchido com sucesso!")
    
    def select_gender(self, gender):
        """Seleciona o gênero"""
        print(f"      📝 Selecionando gênero: {gender}")
        gender_options = {
            "male": FORM_SELECTORS["gender_male"],
            "female": FORM_SELECTORS["gender_female"],
            "other": FORM_SELECTORS["gender_other"]
        }
        
        if gender in gender_options:
            gender_locator = (By.ID, gender_options[gender])
            self.click_element_js(gender_locator)
            print(f"      ✅ Gênero '{gender}' selecionado com sucesso!")
        else:
            print(f"      ❌ Gênero '{gender}' não encontrado nas opções!")
    
    def fill_mobile(self, mobile):
        """Preenche o campo Mobile - LÓGICA ORIGINAL QUE FUNCIONAVA"""
        print(f"      Preenchendo telefone: {mobile}")
        self.send_keys(self.mobile_locator, mobile)
        print(f"         ✅ Telefone preenchido")
    
    def select_date_of_birth(self, day, month, year):
        """Seleciona a data de nascimento no calendário"""
        import time
        
        dob_input = self.find_element(self.date_of_birth_locator)
        dob_input.click()
        time.sleep(0.3)  # Aguardar calendário aparecer
        
        # Selecionar o mês
        month_dropdown = self.find_element((By.CLASS_NAME, "react-datepicker__month-select"))
        month_dropdown.click()
        month_option = self.find_element((By.XPATH, f"//option[@value='{month-1}']"))
        month_option.click()
        
        # Selecionar o ano
        year_dropdown = self.find_element((By.CLASS_NAME, "react-datepicker__year-select"))
        year_dropdown.click()
        year_option = self.find_element((By.XPATH, f"//option[@value='{year}']"))
        year_option.click()
        
        # Selecionar o dia
        day_element = self.find_element((By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']"))
        day_element.click()
    
    def select_subjects(self, subjects_list):
        """Seleciona subjects do autocomplete"""
        import time
        from selenium.webdriver.common.keys import Keys
        
        subjects_input = self.find_element(self.subjects_input_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", subjects_input)
        time.sleep(0.5)
        
        for subject in subjects_list:
            try:
                subjects_input.click()
                time.sleep(0.5)
                subjects_input.clear()
                subjects_input.send_keys(subject)
                time.sleep(1)  # Aguardar autocomplete
                subjects_input.send_keys(Keys.RETURN)
                time.sleep(0.5)
            except Exception as e:
                print(f"   Erro ao adicionar subject '{subject}': {e}")
                continue
    
    def select_hobbies(self, hobbies_list):
        """Seleciona hobbies"""
        hobbies_options = ["sports", "reading", "music"]
        
        for hobby in hobbies_list:
            if hobby in hobbies_options:
                hobby_id = f"hobbies-checkbox-{hobbies_options.index(hobby) + 1}"
                hobby_checkbox = self.find_element((By.ID, hobby_id))
                self.driver.execute_script("arguments[0].click();", hobby_checkbox)
    
    def fill_current_address(self, address):
        """Preenche o campo Current Address"""
        import time
        current_address_field = self.find_element(self.current_address_locator)
        self.driver.execute_script("arguments[0].click();", current_address_field)
        current_address_field.clear()
        current_address_field.send_keys(address)
        time.sleep(0.5)
    
    def upload_picture(self, file_name):
        """Faz upload de uma imagem"""
        import time
        import os
        upload_field = self.find_element(self.upload_picture_locator)
        file_path = os.path.abspath(file_name)
        upload_field.send_keys(file_path)
        time.sleep(0.5)
    
    def select_state(self, state_name):
        """Seleciona estado"""
        import time
        from selenium.webdriver.common.keys import Keys
        
        try:
            state_input = self.find_element(self.state_input_locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", state_input)
            time.sleep(0.5)
            self.driver.execute_script("arguments[0].click();", state_input)
            state_input.send_keys(state_name)
            state_input.send_keys(Keys.RETURN)
        except Exception:
            # Fallback
            try:
                state_container = self.find_element((By.ID, "state"))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", state_container)
                time.sleep(0.5)
                self.driver.execute_script("arguments[0].click();", state_container)
                state_container.send_keys(Keys.ARROW_DOWN)
                state_container.send_keys(Keys.RETURN)
            except Exception:
                pass
    
    def select_city(self, city_name):
        """Seleciona cidade"""
        import time
        from selenium.webdriver.common.keys import Keys
        
        try:
            city_input = self.find_element(self.city_input_locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", city_input)
            time.sleep(0.5)
            self.driver.execute_script("arguments[0].click();", city_input)
            city_input.send_keys(city_name)
            city_input.send_keys(Keys.RETURN)
        except Exception:
            # Fallback
            try:
                city_container = self.find_element((By.ID, "city"))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", city_container)
                time.sleep(0.5)
                self.driver.execute_script("arguments[0].click();", city_container)
                city_container.send_keys(Keys.ARROW_DOWN)
                city_container.send_keys(Keys.RETURN)
            except Exception:
                pass
    
    def submit_form(self):
        """Submete o formulário"""
        import time
        submit_button = self.find_element(self.submit_button_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].click();", submit_button)
        time.sleep(1.5)  # Aguardar modal aparecer
    
    def is_modal_open(self):
        """Verifica se o modal de resultado está aberto"""
        try:
            # Verificação rápida pelo ID principal
            element = self.driver.find_element(By.ID, "example-modal-sizes-title-lg")
            return element.is_displayed()
        except:
            return False
    
    def get_modal_data(self):
        """Extrai dados do modal de resultado"""
        table_rows = self.driver.find_elements(*self.modal_table_rows_locator)
        modal_data = {}
        
        for row in table_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 2:
                label = cells[0].text.strip()
                value = cells[1].text.strip()
                modal_data[label] = value
        
        return modal_data
    
    def close_modal(self):
        """Fecha o modal de resultado"""
        import time
        
        # Tentar fechar pelo botão principal
        try:
            close_button = self.driver.find_element(By.ID, "closeLargeModal")
            self.driver.execute_script("arguments[0].click();", close_button)
            time.sleep(0.2)
            return
        except:
            pass
        
        # Fallback: tentar ESC
        try:
            from selenium.webdriver.common.keys import Keys
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
            time.sleep(0.2)
        except:
            pass
    
    def fill_complete_form(self, form_data):
        """Preenche o formulário completo de forma linear e otimizada"""
        import time
        from selenium.webdriver.common.keys import Keys
        
        # Parte 1: Dados básicos (topo do formulário)
        self.fill_first_name(form_data["first_name"])
        self.fill_last_name(form_data["last_name"])
        self.fill_email(form_data["email"])
        self.select_gender(form_data.get("gender", "male"))
        self.fill_mobile(form_data["phone"])
        self.select_date_of_birth(form_data["birth_day"], form_data["birth_month"], form_data["birth_year"])
        
        # Parte 2: Subjects e Hobbies (SEM SCROLL - ainda visíveis)
        subjects_list = form_data.get("subjects", [])
        if subjects_list:
            subjects_input = self.find_element(self.subjects_input_locator)
            for subject in subjects_list:
                subjects_input.click()
                subjects_input.clear()
                subjects_input.send_keys(subject)
                time.sleep(0.5)  # Aguardar autocomplete
                subjects_input.send_keys(Keys.RETURN)
        
        hobbies_list = form_data.get("hobbies", [])
        hobbies_options = ["sports", "reading", "music"]
        for hobby in hobbies_list:
            if hobby in hobbies_options:
                hobby_id = f"hobbies-checkbox-{hobbies_options.index(hobby) + 1}"
                hobby_checkbox = self.find_element((By.ID, hobby_id))
                self.driver.execute_script("arguments[0].click();", hobby_checkbox)
        
        # Parte 3: Scroll ÚNICO para parte inferior
        self.scroll_to_bottom()
        time.sleep(0.3)
        
        # Parte 4: Upload, Endereço, Estado e Cidade (SEM SCROLLS INDIVIDUAIS)
        upload_field = self.find_element(self.upload_picture_locator)
        import os
        file_path = os.path.abspath(TEST_DATA["file_upload"])
        upload_field.send_keys(file_path)
        
        current_address_field = self.find_element(self.current_address_locator)
        self.driver.execute_script("arguments[0].click();", current_address_field)
        current_address_field.clear()
        current_address_field.send_keys(form_data["address"])
        
        # Estado
        try:
            state_input = self.find_element(self.state_input_locator)
            self.driver.execute_script("arguments[0].click();", state_input)
            state_input.send_keys(TEST_DATA["state"])
            state_input.send_keys(Keys.RETURN)
            time.sleep(0.2)
        except:
            pass
        
        # Cidade
        try:
            city_input = self.find_element(self.city_input_locator)
            self.driver.execute_script("arguments[0].click();", city_input)
            city_input.send_keys(TEST_DATA["city"])
            city_input.send_keys(Keys.RETURN)
        except:
            pass
    
    def fill_personal_data(self, form_data):
        """Preenche dados pessoais básicos"""
        print("\n📝 Preenchendo dados pessoais...")
        
        self.fill_first_name(form_data["first_name"])
        self.fill_last_name(form_data["last_name"])
        self.fill_email(form_data["email"])
        self.select_gender(form_data.get("gender", "male"))
        self.fill_mobile(form_data["phone"])
        self.select_date_of_birth(form_data["birth_day"], form_data["birth_month"], form_data["birth_year"])
        
        print("✅ Dados pessoais preenchidos!")
    
    def fill_subjects_and_hobbies(self, form_data):
        """Preenche subjects e hobbies"""
        import time
        
        if self.is_modal_open():
            self.close_modal()
            time.sleep(1)
        
        self.select_subjects(form_data.get("subjects", []))
        self.select_hobbies(form_data.get("hobbies", []))
    
    def fill_remaining_data(self, form_data):
        """Preenche dados restantes"""
        import time
        
        if self.is_modal_open():
            self.close_modal()
            time.sleep(1)
        
        self.upload_picture(TEST_DATA["file_upload"])
        self.fill_current_address(form_data["address"])
        self.select_state(TEST_DATA["state"])
        self.select_city(TEST_DATA["city"])
