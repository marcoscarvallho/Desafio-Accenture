# language: pt
Funcionalidade: Sistema de Reserva de Livros
  Como um usuário do sistema
  Eu quero reservar livros
  Para poder ler posteriormente

  Contexto:
    Dado que eu tenho credenciais válidas de usuário

  Cenário: Fluxo completo de reserva de livros
    Quando eu crio um novo usuário no sistema
    Então o usuário deve ser criado com sucesso
    
    Quando eu gero um token de autenticação
    Então o token deve ser gerado com sucesso
    
    Quando eu verifico se o usuário está autorizado
    Então o usuário deve estar autorizado
    
    Quando eu listo os livros disponíveis
    Então devo ver a lista de livros disponíveis
    
    Quando eu reservo 2 livros da lista
    Então os livros devem ser reservados com sucesso
    
    Quando eu consulto os detalhes do usuário
    Então devo ver os livros reservados no perfil do usuário
