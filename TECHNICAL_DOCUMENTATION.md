# 🔧 DOCUMENTATION TECHNIQUE - Restaurant Analytics

## 📋 Table des Matières
1. [Architecture](#architecture)
2. [Pipeline de Données](#pipeline-de-données)
3. [Modèles Implémentés](#modèles-implémentés)
4. [Formules & Calculs](#formules--calculs)
5. [Optimisations](#optimisations)
6. [Troubleshooting](#troubleshooting)

---

## Architecture

### **Vue d'ensemble du Pipeline**

```
┌─────────────────────────────────────────────────────────┐
│         6 CSV FILES (Raw Data)                          │
│  - sales_transactions (121,640 rows)                   │
│  - daily_factors_sales (731 days)                      │
│  - external_factors (weather, events)                  │
│  - stock_inventory (2,928 items)                       │
│  - clients (500 customers)                             │
│  - products (12 items)                                 │
└──────────────────────┬──────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────┐
│      DATA LOADING & VALIDATION (Cell 4)                │
│  - Parse timestamps                                    │
│  - Validate completeness                               │
│  - Check for nulls/duplicates                          │
└──────────────────────┬──────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────┐
│   DATA PREPARATION (Cells 5-6)                         │
│  - Daily aggregation (731 rows)                        │
│  - Monthly pivot analysis                              │
│  - Feature engineering (weekday, holidays)             │
└──────────────────────┬──────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────┐
│   EXPLORATORY DATA ANALYSIS (Cell 7)                   │
│  - Temporal trends                                     │
│  - Correlation matrix                                  │
│  - Distribution analysis                               │
└──────────────────────┬──────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────┐
│   TIME SERIES FORECASTING (Cells 8-10)                 │
│  ├─ Cell 8: Advanced ETS + External Regressors        │
│  ├─ Cell 9: ETS Baseline (7-day seasonality)          │
│  └─ Cell 10: Random Forest (Feature-based)            │
└──────────────────────┬──────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────┐
│   BUSINESS ANALYSIS (Cells 11-13)                      │
│  ├─ Inventory risk & expiration analysis              │
│  ├─ RFM customer segmentation                          │
│  ├─ Product bundle analysis                            │
│  └─ Demand forecasting + Reorder recommendations       │
└──────────────────────┬──────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────┐
│   VISUALIZATION & REPORTING (Cells 14-26)              │
│  - 170+ PNG visualizations                             │
│  - 10 CSV reports                                      │
│  - Final business recommendations                      │
└─────────────────────────────────────────────────────────┘
```

---

## Pipeline de Données

### **1. Chargement (Cell 4)**

```python
# Lecture des 6 fichiers CSV
sales = pd.read_csv('restaurant_sales_transactions.csv', 
                    parse_dates=['date', 'timestamp'])
daily = pd.read_csv('restaurant_daily_factors_sales.csv',
                   parse_dates=['date'])
stock = pd.read_csv('restaurant_stock_inventory.csv',
                   parse_dates=['arrival_date', 'expiration_date'])
```

**Validations:**
- Tous les fichiers présents
- Pas de NaN critiques
- Index temporels en ordre croissant

### **2. Agrégation Quotidienne (Cell 5)**

```python
daily_sales = sales.groupby('date').agg({
    'total_amount': 'sum',    # Revenu
    'quantity': 'sum',        # Unités vendues
    'transaction_id': 'nunique'  # Nombre transactions
}).reset_index()

# Fusion avec facteurs externes
daily_ts = daily_sales.merge(external[...], on='date', how='left')
```

**Output:** 731 lignes (2 ans de données)

### **3. Analyse Mensuelle (Cell 6)**

```python
monthly_products = sales.groupby(['month', 'product_name']).agg({
    'quantity': 'sum',
    'total_revenue': 'sum'
}).reset_index()

# Top 5 / Bottom 5 par mois
top5 = monthly_products.groupby('month').apply(
    lambda x: x.nlargest(5, 'total_revenue')
)
```

**Output:** 120 lignes (12 mois × 10 produits)

---

## Modèles Implémentés

### **1. Advanced ETS + External Regressors (Cell 8)**

**Approche Hybride:**
```
Prévision Finale = ETS_Forecast + Ridge_Adjustment
```

**Détails:**
- **ETS Component:** 
  - Trend: Additif
  - Seasonal: Additif (période=7 jours)
  - Lissage exponentiel double

- **Ridge Regression Component:**
  - Entrées: température, précipitation, weekend
  - Cible: résidus ETS
  - Alpha: 1.0

**Performance:**
```
RMSE:  47.27 unités
MAPE:  15.48%
R²:    -0.264 (négatif sur test - ETS limitation sur période volatile)
```

**Utilisation:** Analyse des effets externes sur la demande

### **2. ETS Baseline (Cell 9)**

**Architecture Simple:**
```python
ets_model = ExponentialSmoothing(
    y_train,
    trend='add',
    seasonal='add',
    seasonal_periods=7  # Hebdomadaire
).fit()
forecast = ets_model.forecast(30)  # 30 jours
```

**Performance:**
```
RMSE:  38.30 unités ✅
MAPE:  11.16%
R²:    0.386 (Acceptable)
```

**Utilisation:** Production (meilleur rapport qualité/stabilité)

### **3. Random Forest (Cell 10) ⭐ MEILLEUR**

**Features utilisées:**
```python
features = [
    'temperature',          # Corrélation 0.75 avec demande
    'humidity',
    'precipitation',
    'sunshine_hours',       # Corrélation 0.74
    'is_weekend',          # Corrélation 0.38
    'event_impact_factor'
]

model = RandomForestRegressor(
    n_estimators=300,
    max_depth=8,
    random_state=42
)
```

**Feature Importance:**
```
température          : 42% (dominante)
sunshine_hours       : 28%
is_weekend          : 14%
event_impact_factor : 8%
humidity            : 5%
precipitation       : 3%
```

**Performance:**
```
RMSE:  30.25 unités 🏆 MEILLEUR
MAPE:  10.36%
R²:    0.483 (Très bon)
```

**Utilisation:** Recommandé pour planification

---

## Formules & Calculs

### **1. Metrics d'Évaluation**

#### RMSE (Root Mean Squared Error)
```
RMSE = √(1/n × Σ(y_true - y_pred)²)

Interprétation:
- 30.25: Erreur moyenne en unités
- Bonne métrique pour outliers
```

#### MAPE (Mean Absolute Percentage Error)
```
MAPE = (1/n × Σ|y_true - y_pred|/y_true) × 100%

Interprétation:
- 10.36%: Le modèle s'écarte en moyenne de 10.36%
- Indépendant de l'échelle
```

#### R² (Coefficient de Détermination)
```
R² = 1 - (SS_res / SS_tot)

Interprétation:
- 0.483: Le modèle explique 48.3% de la variance
- Varie de -∞ à 1 (1 = parfait)
- Négatif = pire qu'une prédiction constante
```

### **2. Stock de Sécurité (Cell 13)**

```
Safety_Stock = Z × σ_d × √L

Où:
- Z = 1.645 (pour 95% de niveau de service)
- σ_d = écart-type de la demande quotidienne
- L = lead time (7 jours par défaut)

Exemple:
- σ_d = 45 unités
- L = 7 jours
- Safety_Stock = 1.645 × 45 × √7 = 197 unités
```

### **3. Quantité à Commander**

```
Reorder_Qty = max(0, Demand_LeadTime + Safety_Stock - Current_Stock)

Exemple:
- Demand sur lead time: 350 unités
- Safety stock: 197 unités
- Stock actuel: 250 unités
- Reorder_Qty = max(0, 350 + 197 - 250) = 297 unités
```

### **4. Score de Risque d'Expiration**

```
Expiry_Risk_Score = 0.7 × Ratio_NearExpiry + 0.3 × Qty_Normalized

Où:
- Ratio_NearExpiry = Qty_expiring_soon / Total_Qty
- Qty_Normalized = (NearExpiry_Qty - min) / (max - min)

Pondérations:
- 70% = ratio (importance relative)
- 30% = quantité (volume absolu)
```

### **5. RFM Score**

```
Recency: Jours depuis dernier achat
Frequency: Nombre de transactions
Monetary: Valeur totale dépensée

KMeans clustering sur (R, F, M) normalisés
Silhouette score utilisé pour k optimale
```

---

## Optimisations

### **1. Gestion des Données Volumineuses**

```python
# Au lieu de charger tout en mémoire
sales = pd.read_csv('large_file.csv')  # Risqué

# Utiliser chunks
chunks = pd.read_csv('large_file.csv', chunksize=10000)
df = pd.concat(chunks)  # Ou traiter par chunk
```

### **2. Vectorization avec NumPy**

```python
# Lent (boucle Python)
for i in range(len(data)):
    result[i] = data[i] * 2

# Rapide (vectorisé)
result = data * 2  # NumPy/Pandas
```

### **3. Mise en Cache des Modèles**

```python
# Les modèles ETS et RF sont stockés en mémoire
# Pas de recalcul à chaque cellule
ets_model, rf_model, etc.
```

### **4. Réduction de la Dimensionnalité**

```python
# Utiliser features importantes pour RF
# Éviter curse of dimensionality
# 6 features → optimal pour ensemble methods
```

---

## Troubleshooting

### **❌ Erreur: Prophet backend**

```
Error: 'Prophet' object has no attribute 'stan_backend'
Root Cause: CmdStan initialization fails in Python 3.13.5
Solution: Utiliser ETS (meilleure performance de toute façon)
```

### **❌ Erreur: CSV not found**

```
Error: FileNotFoundError
Solution:
1. Vérifier tous les 6 fichiers CSV présents
2. Vérifier chemins relatifs vs absolus
3. Utiliser Path('.').glob('*.csv') pour découvrir
```

### **❌ Erreur: NaN dans prévisions**

```
Error: NaN values in forecast output
Cause: Données manquantes ou séries trop courtes
Solution:
1. Remplir NaN: df.fillna(method='ffill')
2. Vérifier min 14 jours d'historique (pour ETS)
3. Fallback vers moyenne simple si data < min
```

### **❌ Erreur: Mémoire insuffisante**

```
Error: MemoryError
Solution:
1. Réduire TOP_N_PRODUCTS (défaut=50, min=12)
2. Utiliser chunks pour agrégation
3. Supprimer visualisations intermédiaires
```

### **❌ Erreur: Kernel crash**

```
Solution:
1. Kernel → Restart & Clear All Output
2. Exécuter Cell → Run All
3. Si problème persiste: redémarrer Jupyter
```

---

## Performance Benchmarks

### **Cellule par Cellule**

| Cellule | Opération | Temps | Dépendance |
|---------|-----------|-------|-----------|
| 4 | CSV Load (6 files, 125K rows) | 216ms | - |
| 5 | Daily aggregation | 23ms | Cell 4 |
| 6 | Monthly pivot (120 rows) | 3,972ms | Cell 4 |
| 7 | EDA plots (2 viz) | 914ms | Cell 5 |
| 8 | Advanced forecast | 1,701ms | Cell 5 |
| 9 | ETS baseline | 209ms | Cell 5 |
| 10 | Random Forest (300 trees) | 386ms | Cell 5 |
| 11 | Inventory analysis | 407ms | Cell 4 |
| 12 | Commercial strategy | 8,898ms | Cell 4, 11 |
| 13 | Demand forecast (12 products) | 1,227ms | Cell 5 |
| 14-26 | Visualizations | ~8,500ms | Various |

**Total:** ~24 secondes pour exécution complète

### **Optimization Opportunities**

```python
# Prioriser:
# 1. Cell 12 (8.9s) - pourrait être parallélisé
# 2. Cell 6 (4.0s) - pivot peut être optimisé
# 3. Cell 14-26 (8.5s) - plots générés séquentiellement

# Amélioration possible:
# - Parallel processing (multiprocessing)
# - Caching intermédiaire
# - Lazy evaluation des plots
```

---

## Fichiers de Configuration

### **Paramètres Modifiables**

```python
# Cell 8: Advanced Forecast
FORECAST_HORIZON = 30      # Jours à prévoir
USE_EXTERNAL_REGRESSORS = True

# Cell 13: Demand Forecast
TOP_N_PRODUCTS = 50        # Nombre produits (min=12, tous=None)
LEAD_TIME_DAYS = 7        # Délai fournisseur
SERVICE_LEVEL = 0.95      # Probabilité en stock (95% = Z=1.645)
FORECAST_DAYS = 30        # Horizon prévision

# Cell 12: RFM Clustering
MAX_K = 6                 # Nombre clusters max à tester
THRESHOLD_RATIO = 0.2     # Ratio expiration pour "risque"
```

---

## Version Control

```
Version: 1.0 - Production Ready
Date: 9 Décembre 2025
Python: 3.13.5
Jupyter: Compatible avec JupyterLab 4.x

Commits clés:
- Fix Prophet backend incompatibility
- Optimize ETS forecasting
- Add Random Forest model
- Complete commercial strategy analysis
```

---

## Références & Ressources

### **Time Series Forecasting**
- Holt-Winters ETS: https://www.statsmodels.org/stable/generated/statsmodels.tsa.holtwinters.ExponentialSmoothing.html
- Random Forest: https://scikit-learn.org/stable/modules/ensemble.html#random-forests

### **Inventory Management**
- Safety Stock Formula: https://en.wikipedia.org/wiki/Safety_stock
- Service Level: https://en.wikipedia.org/wiki/Service_level

### **Customer Segmentation**
- RFM Analysis: https://en.wikipedia.org/wiki/RFM_%28customer_value%29
- K-Means Clustering: https://scikit-learn.org/stable/modules/clustering.html#k-means

