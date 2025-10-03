# Desafio Web - Automação DemoQA

## Descrição
Automação de testes web usando Python com Behave (BDD) e Page Object Pattern.

## Tecnologias
- Python 3.x
- Selenium WebDriver
- Behave (BDD)
- Page Object Pattern

## Como Executar

### Execução com BDD (Behave)
```bash
pip install -r requirements.txt
behave features/
```

## Personalização de Dados

Para adicionar ou remover nomes de pessoas nos testes, edite o arquivo:
```
features/environment.py
```

Localize as listas `first_names` e `last_names` (linhas 23-24) e adicione/remova nomes conforme necessário:
```python
first_names = ["Ana", "Joao", "Maria", "Pedro", ...]
last_names = ["Silva", "Santos", "Oliveira", ...]
```
