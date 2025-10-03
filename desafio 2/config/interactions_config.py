"""
Configurações para o teste de Interactions - Sortable
"""

# URL Base
BASE_URL = "https://demoqa.com"

# Seletores da página principal
MAIN_PAGE_SELECTORS = {
    "interactions_card": "//div[contains(@class, 'card')]//h5[text()='Interactions']",
    "sortable_menu": "//span[text()='Sortable']"
}

# Seletores da página Sortable
SORTABLE_SELECTORS = {
    "list_tab": "demo-tab-list",  # ID
    "grid_tab": "demo-tab-grid",  # ID
    "list_container": "//div[@id='demo-tabpane-list']//div[contains(@class, 'list-group')]",
    "list_items": "//div[@id='demo-tabpane-list']//div[contains(@class, 'list-group-item')]"
}

# Ordem esperada dos elementos (decrescente)
EXPECTED_ORDER = ["Six", "Five", "Four", "Three", "Two", "One"]

# Configurações do driver
DRIVER_CONFIG = {
    "timeout": 10,
    "implicit_wait": 2,
    "page_load_timeout": 30
}
