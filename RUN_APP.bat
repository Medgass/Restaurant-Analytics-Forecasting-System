@echo off
REM ============================================================================
REM KWEEK Restaurant Analytics - Application Launcher
REM Lanceur Windows pour l'interface Streamlit
REM ============================================================================

echo.
echo ============================================================================
echo ^|  KWEEK Restaurant Analytics ^& Forecasting System                      ^|
echo ^|  Interface Graphique Interactive - Streamlit                           ^|
echo ============================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.13+ from python.org
    pause
    exit /b 1
)

REM Check if streamlit is installed
python -m pip show streamlit >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Streamlit and Plotly...
    pip install streamlit plotly
)

echo.
echo Launching KWEEK Application...
echo.
echo Opening http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

REM Launch the app
python -m streamlit run app.py

pause
