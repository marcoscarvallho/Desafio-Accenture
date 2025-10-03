# language: pt
Funcionalidade: Alerts, Frame & Windows - Browser Windows
  Como um usuário do site DemoQA
  Eu quero testar a funcionalidade de múltiplas janelas
  Para verificar se novas janelas são abertas corretamente

  Contexto:
    Dado que eu estou na página inicial do DemoQA

  Cenário: Abrir nova janela e validar conteúdo
    Quando eu clico no card "Alerts, Frame & Windows"
    Então devo ser redirecionado para a página de AFW
    
    Quando eu clico no menu "Browser Windows"
    Então devo ser redirecionado para a página de Browser Windows
    
    Quando eu clico no botão "New Window"
    Então uma nova janela deve ser aberta
    
    Quando eu mudo para a nova janela
    Então devo ver a mensagem "This is a sample page"
    
    Quando eu fecho a nova janela
    E volto para a janela original
    Então devo estar de volta na página de Browser Windows
