# language: pt
Funcionalidade: Widgets - Progress Bar
  Como um usuário do site DemoQA
  Eu quero testar a funcionalidade de barra de progresso
  Para verificar se consigo controlar e validar o progresso

  Contexto:
    Dado que eu estou na página inicial do DemoQA

  Cenário: Controlar progress bar e validar valores
    Quando eu clico no card "Widgets"
    Então devo ser redirecionado para a página de Widgets
    
    Quando eu clico no menu "Progress Bar"
    Então devo ser redirecionado para a página de Progress Bar
    
    Quando eu inicio e paro a barra antes de chegar aos 25%
    Então o valor da progress bar deve ser menor ou igual a 25%
    
    Quando eu clico no botão Start novamente
    E aguardo a barra chegar aos 100%
    Então o valor da progress bar deve ser 100%
    
    Quando eu clico no botão Reset
    Então a progress bar deve voltar para 0%
