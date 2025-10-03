# Desafio 2 - Automação Web com BDD e POM

Este projeto implementa automação web para o formulário de prática do DemoQA usando BDD (Behavior Driven Development) com Behave e o padrão Page Object Model (POM).

## Estrutura do Projeto

```
desafio 2/
├── config/
│   ├── __init__.py
│   └── config.py              # Configurações e seletores
├── features/
│   ├── __init__.py
│   ├── environment.py         # Configuração do Behave
│   ├── practice_form.feature  # Cenários BDD
│   └── steps/
│       ├── __init__.py
│       └── practice_form_steps.py  # Implementação dos steps
├── pages/
│   ├── __init__.py
│   ├── base_page.py           # Classe base para todas as páginas
│   ├── main_page.py           # Page Object da página principal
│   └── practice_form_page.py  # Page Object do formulário
├── requirements.txt           # Dependências Python
├── executar_testes.bat       # Script para executar testes
└── README.md                 # Este arquivo
```

## Tecnologias Utilizadas

- **Python 3.x**
- **Selenium WebDriver** - Automação web
- **Behave** - Framework BDD
- **Firefox** - Navegador para execução dos testes

## Instalação

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Certifique-se de que o geckodriver.exe está no diretório do projeto

## Execução dos Testes

### Opção 1: Usando o script batch
```bash
executar_testes.bat
```

### Opção 2: Comando direto
```bash
behave features/practice_form.feature --format=pretty
```

## Cenários de Teste

O projeto implementa o seguinte cenário:

1. **Navegação**: Acessa a página inicial do DemoQA
2. **Seleção**: Clica no card "Forms" e no menu "Practice Form"
3. **Preenchimento**: Preenche todos os campos do formulário com dados aleatórios
4. **Submissão**: Submete o formulário
5. **Verificação**: Verifica se o modal de resultado aparece com os dados corretos
6. **Finalização**: Fecha o modal

## Dados de Teste

O sistema gera automaticamente dados aleatórios para:
- Nome e sobrenome
- Email baseado no nome
- Número de telefone
- Data de nascimento (entre 18 e 65 anos)
- Endereço
- Hobbies e subjects selecionados aleatoriamente
- Gênero

## Padrões Implementados

### Page Object Model (POM)
- **BasePage**: Classe base com métodos comuns para interação com elementos
- **MainPage**: Encapsula interações com a página principal
- **PracticeFormPage**: Encapsula todas as interações com o formulário

### BDD com Behave
- Cenários descritos em linguagem natural (Gherkin)
- Steps implementados em Python
- Configuração centralizada no environment.py

### Configuração Centralizada
- Seletores organizados em config.py
- URLs e constantes centralizadas
- Configurações do driver em um local único

## Melhorias Implementadas

- Removidos prints desnecessários e time.sleep
- Implementado wait explícito para melhor estabilidade
- Tratamento de exceções com fallbacks
- Código limpo e bem organizado
- Reutilização de código através de herança
