"""
Configurações para o teste de Widgets - Progress Bar
"""

# URL Base
BASE_URL = "https://demoqa.com"

# Seletores da página principal
MAIN_PAGE_SELECTORS = {
    "widgets_card": "//div[contains(@class, 'card')]//h5[text()='Widgets']",
    "progress_bar_menu": "//span[text()='Progress Bar']"
}

# Seletores da página Progress Bar
PROGRESS_BAR_SELECTORS = {
    "start_stop_button": "startStopButton",  # ID
    "reset_button": "resetButton",  # ID
    "progress_bar": "//div[@role='progressbar']",  # XPATH
    "progress_value": "//div[@role='progressbar']/@aria-valuenow"  # XPATH para atributo
}

# Configurações do driver
DRIVER_CONFIG = {
    "timeout": 10,
    "implicit_wait": 2,
    "page_load_timeout": 30
}

# Limites de validação
VALIDATION = {
    "max_percentage_before_stop": 25,
    "target_stop_percentage": 15,  # Para em 15% (valor mais baixo e seguro)
    "check_interval": 0.03  # Verifica a cada 30ms (ainda mais rápido!)
}
