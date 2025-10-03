@echo off
echo ================================================
echo DESAFIO API BOOKSTORE
echo ================================================
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
