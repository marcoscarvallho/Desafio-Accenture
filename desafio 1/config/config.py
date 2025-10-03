"""
Configurações do projeto
"""

# API Base URL
BASE_URL = "https://demoqa.com"

# Endpoints
ENDPOINTS = {
    "create_user": "/Account/v1/User",
    "generate_token": "/Account/v1/GenerateToken",
    "authorized": "/Account/v1/Authorized",
    "books": "/BookStore/v1/Books",
    "user_details": "/Account/v1/User"
}

# Credenciais de teste
TEST_USER = {
    "userName": "MarcosAccenture",
    "password": "Teste123321*"
}

# Timeout padrão para requisições
REQUEST_TIMEOUT = 30

