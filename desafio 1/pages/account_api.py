"""
API Object para gerenciamento de contas de usuário
Implementa o padrão Page Object para endpoints de Account
"""
from pages.base_api import BaseAPI
from config.config import ENDPOINTS


class AccountAPI(BaseAPI):
    
    def criar_usuario(self, username, password):
        """Cria um novo usuário no sistema"""
        payload = {
            "userName": username,
            "password": password
        }
        return self.post(ENDPOINTS["create_user"], json_data=payload)
    
    def gerar_token(self, username, password):
        """Gera um token de autenticação para o usuário"""
        payload = {
            "userName": username,
            "password": password
        }
        return self.post(ENDPOINTS["generate_token"], json_data=payload)
    
    def verificar_autorizacao(self, username, password):
        """Verifica se o usuário está autorizado"""
        payload = {
            "userName": username,
            "password": password
        }
        return self.post(ENDPOINTS["authorized"], json_data=payload)
    
    def obter_detalhes_usuario(self, user_id, token):
        """Obtém os detalhes do usuário incluindo livros reservados"""
        endpoint = f"{ENDPOINTS['user_details']}/{user_id}"
        headers = {
            "Authorization": f"Bearer {token}"
        }
        return self.get(endpoint, headers=headers)
