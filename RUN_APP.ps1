# ============================================================================
# KWEEK Restaurant Analytics - Application Launcher (PowerShell)
# Lanceur pour l'interface Streamlit
# ============================================================================

Write-Host ""
Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host "|  KWEEK Restaurant Analytics & Forecasting System                      |" -ForegroundColor Cyan
Write-Host "|  Interface Graphique Interactive - Streamlit                           |" -ForegroundColor Cyan
Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    python --version | Out-Null
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.13+ from python.org" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if streamlit is installed
$streamlit_check = pip show streamlit 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Installing Streamlit and Plotly..." -ForegroundColor Yellow
    pip install streamlit plotly -q
}

Write-Host ""
Write-Host "✅ Launching KWEEK Application..." -ForegroundColor Green
Write-Host ""
Write-Host "🌐 Opening http://localhost:8501" -ForegroundColor Blue
Write-Host ""
Write-Host "⏹️  Press Ctrl+C to stop the application" -ForegroundColor Yellow
Write-Host ""

# Launch the app
python -m streamlit run app.py

Read-Host "Press Enter to exit"
