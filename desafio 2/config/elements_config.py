"""
Configurações para o teste de Elements - Web Tables
"""

# URL Base
BASE_URL = "https://demoqa.com"

# Seletores da página principal
MAIN_PAGE_SELECTORS = {
    "elements_card": "//div[contains(@class, 'card')]//h5[text()='Elements']",
    "web_tables_menu": "//span[text()='Web Tables']"
}

# Seletores da página Web Tables
WEB_TABLES_SELECTORS = {
    "add_button": "addNewRecordButton",  # ID
    "first_name": "firstName",  # ID
    "last_name": "lastName",  # ID
    "email": "userEmail",  # ID
    "age": "age",  # ID
    "salary": "salary",  # ID
    "department": "department",  # ID
    "submit_button": "submit",  # ID
    "table_rows": "//div[@class='rt-tbody']//div[@class='rt-tr-group']",
    "edit_button": "//span[@title='Edit']",
    "delete_button": "//span[@title='Delete']",
    "search_box": "searchBox"  # ID
}

# Configurações do driver
DRIVER_CONFIG = {
    "timeout": 10,
    "implicit_wait": 2,
    "page_load_timeout": 30
}
