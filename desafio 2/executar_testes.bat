@echo off
echo ========================================
echo   Executando testes BDD do DemoQA
echo ========================================
echo.

REM Ativar ambiente virtual se existir
if exist "venv\Scripts\activate.bat" (
    echo Ativando ambiente virtual...
    call venv\Scripts\activate.bat
)

echo Instalando dependencias...
pip install -r requirements.txt
cls

echo ========================================
echo   Iniciando execucao dos testes
echo ========================================
echo.

REM Executar todos os testes
echo [1/5] Executando teste: Forms - Practice Form
echo ----------------------------------------
behave features/Forms-practice_form.feature --format=pretty
echo.

echo [2/5] Executando teste: AFW - Browser Windows
echo ----------------------------------------
behave features/AFW-browser_windows.feature --format=pretty
echo.

echo [3/5] Executando teste: Elements - Web Tables (12 registros)
echo ----------------------------------------
behave features/elements-Web_tables.feature --format=pretty
echo.

echo [4/5] Executando teste: Widgets - Progress Bar
echo ----------------------------------------
behave features/Widgets-Progress_bar.feature --format=pretty
echo.

echo [5/5] Executando teste: Interactions - Sortable
echo ----------------------------------------
behave features/interactions-sortable.feature --format=pretty
echo.

echo ========================================
echo   Todos os testes finalizados!
echo ========================================
pause
