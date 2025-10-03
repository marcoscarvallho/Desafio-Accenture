"""
Classe base para todas as interações com API
Implementa o padrão Page Object para APIs
"""
import requests
from config.config import BASE_URL, REQUEST_TIMEOUT


class BaseAPI:
    
    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = REQUEST_TIMEOUT
        self.session = requests.Session()
    
    def get(self, endpoint, headers=None, params=None):
        """Realiza requisição GET"""
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(
            url, 
            headers=headers, 
            params=params, 
            timeout=self.timeout
        )
        return response
    
    def post(self, endpoint, json_data=None, headers=None):
        """Realiza requisição POST"""
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(
            url, 
            json=json_data, 
            headers=headers, 
            timeout=self.timeout
        )
        return response
