@echo off
echo ================================================
echo DESAFIO API BOOKSTORE
echo ================================================
echo.

REM Criar ambiente virtual se não existir
if not exist "venv" (
    echo Criando ambiente virtual...
    python -m venv venv
    echo.
)

REM Ativar ambiente virtual
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat
echo.

echo Instalando dependencias...
pip install -q -r requirements.txt
echo.

echo Executando testes...
echo ================================================
behave -v
echo ================================================
echo.

pause
