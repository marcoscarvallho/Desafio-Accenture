"""
API Object para gerenciamento de livros
Implementa o padrão Page Object para endpoints de BookStore
"""
from pages.base_api import BaseAPI
from config.config import ENDPOINTS


class BookStoreAPI(BaseAPI):
    
    def listar_livros(self):
        """Lista todos os livros disponíveis no sistema"""
        return self.get(ENDPOINTS["books"])
    
    def reservar_livros(self, user_id, token, isbn_list):
        """Reserva livros para o usuário"""
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        collection_of_isbns = [{"isbn": isbn} for isbn in isbn_list]
        
        payload = {
            "userId": user_id,
            "collectionOfIsbns": collection_of_isbns
        }
        
        return self.post(ENDPOINTS["books"], json_data=payload, headers=headers)
