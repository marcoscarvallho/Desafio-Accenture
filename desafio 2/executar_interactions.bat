@echo off
echo Executando testes BDD do DemoQA Interactions - Sortable...

echo Ativando ambiente virtual...
call venv\Scripts\activate

echo Instalando dependências...
pip install -r requirements.txt
cls

echo.
echo Executando teste: Sortable (Drag and Drop)...
behave features/interactions-sortable.feature --format=pretty

echo.
echo Testes finalizados!
pause
