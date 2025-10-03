# language: pt
Funcionalidade: Formulário de Prática DemoQA
  Como um usuário do site DemoQA
  Eu quero preencher o formulário de prática
  Para testar a funcionalidade de formulários

  Contexto:
    Dado que eu estou na página inicial do DemoQA

  Cenário: Preenchimento completo do formulário de prática
    Quando eu clico no card "Forms"
    Então devo ser redirecionado para a página de Forms
    
    Quando eu clico no menu "Practice Form"
    Então devo ser redirecionado para a página do formulário
    
    Quando eu preencho todos os campos do formulário com dados válidos
    Então o formulário deve ser preenchido com sucesso
    
    Quando eu submeto o formulário
    Então deve aparecer um modal com os dados preenchidos
    
    Quando eu verifico se os dados no modal estão corretos
    Então os dados devem corresponder aos dados inseridos
    
    Quando eu fecho o modal
    Então o modal deve ser fechado e retornar ao formulário
