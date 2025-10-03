@echo off
echo Executando testes BDD do DemoQA AFW - Browser Windows...

echo Ativando ambiente virtual...
call venv\Scripts\activate

echo Instalando dependências...
pip install -r requirements.txt
cls

echo Executando testes...
behave features/AFW-browser_windows.feature --format=pretty

echo.
echo Testes finalizados!
pause
