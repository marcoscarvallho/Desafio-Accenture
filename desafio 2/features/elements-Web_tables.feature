# language: pt
Funcionalidade: Elements - Web Tables
  Como um usuário do site DemoQA
  Eu quero gerenciar registros em tabelas web
  Para testar operações CRUD em tabelas dinâmicas

  Contexto:
    Dado que eu estou na página inicial do DemoQA

  Cenário: Criar e deletar 12 registros dinamicamente
    Quando eu clico no card "Elements"
    Então devo ser redirecionado para a página de Elements
    
    Quando eu clico no menu "Web Tables"
    Então devo ser redirecionado para a página de Web Tables
    
    Quando eu crio 12 novos registros dinamicamente
    Então todos os 12 registros devem aparecer na tabela
    E eu deleto todos os 12 registros criados
    Então nenhum dos 12 registros deve aparecer na tabela
