# language: pt
Funcionalidade: Interactions - Sortable
  Como um usuário do site DemoQA
  Eu quero testar a funcionalidade de ordenação com drag and drop
  Para verificar se consigo reordenar elementos

  Contexto:
    Dado que eu estou na página inicial do DemoQA

  Cenário: Ordenar elementos em ordem decrescente usando drag and drop
    Quando eu clico no card "Interactions"
    Então devo ser redirecionado para a página de Interactions
    
    Quando eu clico no menu "Sortable"
    Então devo ser redirecionado para a página de Sortable
    
    Quando eu ordeno os elementos em ordem decrescente
    Então os elementos devem estar na ordem: Six, Five, Four, Three, Two, One
