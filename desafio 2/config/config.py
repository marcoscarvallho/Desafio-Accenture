"""
Configurações do projeto de automação web
"""

# URL Base
BASE_URL = "https://demoqa.com"

# Seletores da página principal
MAIN_PAGE_SELECTORS = {
    "forms_card": "//div[contains(@class, 'card')]//h5[text()='Forms']",
    "practice_form_menu": "//span[text()='Practice Form']"
}

# Seletores do formulário
FORM_SELECTORS = {
    "first_name": "firstName",
    "last_name": "lastName", 
    "email": "userEmail",
    "gender_male": "gender-radio-1",
    "gender_female": "gender-radio-2", 
    "gender_other": "gender-radio-3",
    "mobile": "userNumber",
    "date_of_birth": "dateOfBirthInput",
    "subjects_input": "subjectsInput",
    "hobbies_sports": "hobbies-checkbox-1",
    "hobbies_reading": "hobbies-checkbox-2",
    "hobbies_music": "hobbies-checkbox-3",
    "current_address": "currentAddress",
    "upload_picture": "uploadPicture",
    "state_input": "//div[@id='state']//input",
    "city_input": "//div[@id='city']//input",
    "submit_button": "submit"
}

# Seletores do modal de resultado
MODAL_SELECTORS = {
    "modal_title": "example-modal-sizes-title-lg",
    "modal_table_rows": "//tbody//tr",
    "close_button": "closeLargeModal"
}

# Configurações do driver
DRIVER_CONFIG = {
    "timeout": 10,
    "implicit_wait": 2,  # Reduzido de 10 para 2 segundos
    "page_load_timeout": 30
}

# Dados de teste
TEST_DATA = {
    "file_upload": "txtteste.txt",
    "state": "Haryana",
    "city": "Karnal"
}
