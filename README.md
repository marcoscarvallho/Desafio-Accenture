# Desafio Accenture

Repositório contendo os 2 desafios de automação de testes.

## 📁 Estrutura do Projeto

```
Desafio-Accenture/
├── desafio 1/          # Testes de API - Bookstore
│   ├── config/
│   ├── features/
│   ├── pages/
│   ├── executar_testes.bat
│   ├── requirements.txt
│   └── README.md
│
└── desafio 2/          # Testes Web - DemoQA
    ├── config/
    ├── features/
    ├── pages/
    ├── executar_testes.bat
    ├── requirements.txt
    └── README.md
```

## 🚀 Como Executar

### Opção 1: Clicando no arquivo .bat
Navegue até a pasta do desafio desejado e clique duas vezes no arquivo `executar_testes.bat`

### Opção 2: Via linha de comando

**Desafio 1 - API Bookstore**
```bash
cd "desafio 1"
executar_testes.bat
```

**Desafio 2 - Web DemoQA**
```bash
cd "desafio 2"
executar_testes.bat
```

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Navegador Firefox (para desafio 2)
- Geckodriver (incluído no desafio 2)

## 📝 Observações

Os scripts `.bat` criam automaticamente o ambiente virtual (venv) e instalam as dependências necessárias.

Cada desafio possui seu próprio README com instruções específicas.

