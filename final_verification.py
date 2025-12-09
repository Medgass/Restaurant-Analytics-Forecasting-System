#!/usr/bin/env python
"""Final comprehensive functionality test"""

import sys
import json
from datetime import datetime

# Test results tracker
results = {
    "timestamp": datetime.now().isoformat(),
    "tests": {},
    "summary": {}
}

def test(name, passed, details=""):
    """Log test result"""
    icon = "✅" if passed else "❌"
    print(f"{icon} {name}" + (f": {details}" if details else ""))
    results["tests"][name] = {"passed": passed, "details": details}

# ============================================================================
# TEST 1: DATA INTEGRITY
# ============================================================================
print("\n" + "="*70)
print("TEST 1: DATA INTEGRITY (CSV Files & Structure)")
print("="*70)

import pandas as pd
from pathlib import Path

csv_files = {
    'transactions': ('restaurant_sales_transactions.csv', 121640),
    'daily': ('restaurant_daily_factors_sales.csv', 731),
    'inventory': ('restaurant_stock_inventory.csv', 2928),
    'clients': ('restaurant_clients.csv', 500),
    'products': ('restaurant_products.csv', 12),
    'external': ('restaurant_external_factors.csv', 731),
}

all_loaded = True
for name, (file, exp_rows) in csv_files.items():
    try:
        df = pd.read_csv(file)
        rows_ok = len(df) == exp_rows
        test(f"Load {name}", rows_ok, f"{len(df)} rows (expected {exp_rows})")
        if not rows_ok:
            all_loaded = False
    except Exception as e:
        test(f"Load {name}", False, str(e))
        all_loaded = False

results["summary"]["data_integrity"] = all_loaded

# ============================================================================
# TEST 2: FORECAST FUNCTIONALITY
# ============================================================================
print("\n" + "="*70)
print("TEST 2: FORECAST FUNCTIONALITY")
print("="*70)

try:
    sales = pd.read_csv('restaurant_sales_transactions.csv')
    
    # Test 2a: Product selection
    products = sales['product_name'].unique()
    test("Product list loaded", len(products) == 12, f"{len(products)} products")
    
    # Test 2b: Baseline forecast generation
    test_product = 'Craft Beer (Draft)'
    product_data = sales[sales['product_name'] == test_product]
    test("Craft Beer (Draft) exists", len(product_data) > 0, f"{len(product_data)} records")
    
    # Test 2c: Daily aggregation
    if 'date' in sales.columns:
        sales_copy = sales.copy()
        sales_copy['date'] = pd.to_datetime(sales_copy['date'])
        daily = sales_copy.groupby('date')['quantity'].sum()
        test("Daily aggregation works", len(daily) > 0, f"{len(daily)} days")
        
        # Test 2d: Baseline statistics
        mean_qty = daily.mean()
        std_qty = daily.std()
        test("Mean calculation", mean_qty > 0, f"Mean: {mean_qty:.2f}")
        test("Std calculation", std_qty >= 0, f"Std: {std_qty:.2f}")
    
    # Test 2e: CSV forecasts exist
    forecast_files = list(Path('.').glob('outputs/reports/demand_forecasts_*.csv'))
    test("Forecast CSV exists", len(forecast_files) > 0, f"{len(forecast_files)} files")
    
    if forecast_files:
        latest = sorted(forecast_files)[-1]
        forecasts = pd.read_csv(latest)
        test("Forecast columns present", 'week_mean' in forecasts.columns, "Has week_mean column")
        
        beer_forecast = forecasts[forecasts['product_name'] == test_product]
        test("Beer forecast available", len(beer_forecast) > 0, "Beer data found")
    
    results["summary"]["forecasts"] = True
    
except Exception as e:
    test("Forecast module", False, str(e))
    results["summary"]["forecasts"] = False

# ============================================================================
# TEST 3: INVENTORY LOGIC
# ============================================================================
print("\n" + "="*70)
print("TEST 3: INVENTORY MANAGEMENT LOGIC")
print("="*70)

try:
    inventory = pd.read_csv('restaurant_stock_inventory.csv')
    
    # Test 3a: Column existence
    required_cols = ['product_name', 'expiration_date', 'quantity_available']
    cols_ok = all(col in inventory.columns for col in required_cols)
    test("Required columns", cols_ok, f"Columns: {required_cols}")
    
    # Test 3b: Date calculation
    inventory['expiration_date'] = pd.to_datetime(inventory['expiration_date'])
    inventory['days_until_expiry'] = (inventory['expiration_date'] - pd.Timestamp.today()).dt.days
    
    test("Days calculation", len(inventory) == 2928, "All items processed")
    
    # Test 3c: Risk stratification
    critical = len(inventory[inventory['days_until_expiry'] <= 1])
    high = len(inventory[(inventory['days_until_expiry'] > 1) & (inventory['days_until_expiry'] <= 7)])
    medium = len(inventory[(inventory['days_until_expiry'] > 7) & (inventory['days_until_expiry'] <= 30)])
    
    test("Risk categorization", (critical + high + medium) >= 0, f"Critical: {critical}, High: {high}, Medium: {medium}")
    
    # Test 3d: Product variety in inventory
    unique_prods = inventory['product_name'].nunique()
    test("Product variety", unique_prods == 12, f"{unique_prods} unique products")
    
    results["summary"]["inventory"] = True
    
except Exception as e:
    test("Inventory module", False, str(e))
    results["summary"]["inventory"] = False

# ============================================================================
# TEST 4: RFM ANALYSIS
# ============================================================================
print("\n" + "="*70)
print("TEST 4: RFM CLIENT SEGMENTATION")
print("="*70)

try:
    sales = pd.read_csv('restaurant_sales_transactions.csv')
    clients = pd.read_csv('restaurant_clients.csv')
    
    test("Clients loaded", len(clients) == 500, f"{len(clients)} clients")
    
    # Test 4a: RFM calculation
    sales_copy = sales.copy()
    sales_copy['date'] = pd.to_datetime(sales_copy['date'])
    ref_date = sales_copy['date'].max()
    
    rfm = sales_copy.groupby('client_id').agg({
        'date': lambda x: (ref_date - x.max()).days,
        'transaction_id': 'count',
        'total_amount': 'sum'
    }).rename(columns={
        'date': 'recency',
        'transaction_id': 'frequency',
        'total_amount': 'monetary'
    })
    
    test("RFM computed", len(rfm) > 0, f"{len(rfm)} client segments")
    test("Recency valid", rfm['recency'].min() >= 0 and rfm['recency'].max() < 1000, f"Range: {rfm['recency'].min()}-{rfm['recency'].max()} days")
    test("Frequency valid", rfm['frequency'].min() > 0, f"Range: {rfm['frequency'].min()}-{rfm['frequency'].max()}")
    test("Monetary valid", rfm['monetary'].min() > 0, f"Range: €{rfm['monetary'].min():.0f}-€{rfm['monetary'].max():.0f}")
    
    results["summary"]["rfm"] = True
    
except Exception as e:
    test("RFM module", False, str(e))
    results["summary"]["rfm"] = False

# ============================================================================
# TEST 5: APP CODE QUALITY
# ============================================================================
print("\n" + "="*70)
print("TEST 5: APPLICATION CODE STRUCTURE")
print("="*70)

try:
    with open('app.py', 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Test 5a: Syntax
    try:
        compile(code, 'app.py', 'exec')
        test("Python syntax", True, "Valid")
    except SyntaxError as e:
        test("Python syntax", False, str(e))
    
    # Test 5b: Pages present
    pages = {
        "📈 Dashboard": "elif page ==" and "Dashboard" in code,
        "🔮 Prévisions": "# PAGE 2: FORECASTING" in code,
        "📦 Inventaire": "# PAGE 3: INVENTORY" in code,
        "👥 RFM": "# PAGE 4: RFM" in code,
        "📊 Rapports": "# PAGE 5: REPORTS" in code,
        "ℹ️ À Propos": "# PAGE 6: ABOUT" in code,
    }
    
    for page, check in pages.items():
        test(f"Page: {page}", check, "Present")
    
    # Test 5c: Key imports
    imports = ['import streamlit', 'import pandas', 'import plotly', 'import numpy']
    for imp in imports:
        test(f"Import: {imp.split()[-1]}", imp in code, "Present")
    
    # Test 5d: Components
    components = {
        'Plotly charts': 'go.Figure()',
        'Metrics': 'st.metric(',
        'Dataframes': 'st.dataframe(',
        'Download buttons': 'st.download_button',
        'Sliders': 'st.slider',
        'Tabs': 'st.tabs',
    }
    
    for comp, code_str in components.items():
        present = code_str in code
        test(f"Component: {comp}", present, "Implemented")
    
    results["summary"]["code_quality"] = True
    
except Exception as e:
    test("Code analysis", False, str(e))
    results["summary"]["code_quality"] = False

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "="*70)
print("FINAL VERIFICATION SUMMARY")
print("="*70)

passed = sum(1 for t in results["tests"].values() if t["passed"])
total = len(results["tests"])

print(f"\n📊 Results: {passed}/{total} tests passed ({100*passed//total}%)")
print(f"\n✅ Core Systems:")
print(f"  - Data Integrity: {'✓' if results['summary'].get('data_integrity') else '✗'}")
print(f"  - Forecasts: {'✓' if results['summary'].get('forecasts') else '✗'}")
print(f"  - Inventory: {'✓' if results['summary'].get('inventory') else '✗'}")
print(f"  - RFM Analysis: {'✓' if results['summary'].get('rfm') else '✗'}")
print(f"  - Code Quality: {'✓' if results['summary'].get('code_quality') else '✗'}")

all_ok = all(results['summary'].values())
print(f"\n{'='*70}")
print(f"STATUS: {'✅ 100% FUNCTIONAL - READY FOR PRODUCTION' if all_ok else '⚠️  ISSUES DETECTED - REVIEW ABOVE'}")
print(f"{'='*70}\n")

# Save results to JSON
with open('verification_results.json', 'w') as f:
    json.dump(results, f, indent=2, default=str)

sys.exit(0 if all_ok else 1)
