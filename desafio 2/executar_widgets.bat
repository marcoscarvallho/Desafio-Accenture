@echo off
echo Executando testes BDD do DemoQA Widgets - Progress Bar...

echo Ativando ambiente virtual...
call venv\Scripts\activate

echo Instalando dependências...
pip install -r requirements.txt
cls

echo.
echo Executando teste: Progress Bar...
behave features/Widgets-Progress_bar.feature --format=pretty

echo.
echo Testes finalizados!
pause
