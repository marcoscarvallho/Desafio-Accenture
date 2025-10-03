@echo off
echo Executando testes BDD do DemoQA Elements - Web Tables...

echo Ativando ambiente virtual...
call venv\Scripts\activate

echo Instalando dependências...
pip install -r requirements.txt
cls

echo.
echo Executando teste: Criar e deletar 12 registros...
behave features/elements-Web_tables.feature --format=pretty

echo.
echo Testes finalizados!
pause
