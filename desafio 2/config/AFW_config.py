"""
Configurações para o teste de Alerts, Frame & Windows - Browser Windows
"""

# URL Base
BASE_URL = "https://demoqa.com"

# Seletores da página principal
MAIN_PAGE_SELECTORS = {
    "afw_card": "//div[contains(@class, 'card')]//h5[text()='Alerts, Frame & Windows']",
    "browser_windows_menu": "//span[text()='Browser Windows']"
}

# Seletores da página Browser Windows
BROWSER_WINDOWS_SELECTORS = {
    "new_window_button": "windowButton",  # ID
    "sample_heading": "sampleHeading"  # ID do elemento na nova janela
}

# Dados de teste
TEST_DATA = {
    "expected_message": "This is a sample page"
}

# Configurações do driver
DRIVER_CONFIG = {
    "timeout": 10,
    "implicit_wait": 2,
    "page_load_timeout": 30
}
