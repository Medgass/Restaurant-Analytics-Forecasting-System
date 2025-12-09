# 📚 GUIDE EXPLICATIF COMPLET - CODE POUR DÉBUTANTS

## 🎯 Introduction

Ce document explique **ligne par ligne** comment fonctionne le code de l'application KWEEK Restaurant Analytics. Parfait pour les débutants qui veulent comprendre Python, Streamlit, et l'analyse de données.

---

## 📖 Table des Matières

1. [Structure Générale](#structure-générale)
2. [Imports et Bibliothèques](#imports-et-bibliothèques)
3. [Configuration de la Page](#configuration-de-la-page)
4. [Chargement des Données](#chargement-des-données)
5. [Page Dashboard](#page-dashboard)
6. [Page Prévisions](#page-prévisions)
7. [Page Inventaire](#page-inventaire)
8. [Page Clients RFM](#page-clients-rfm)
9. [Concepts Python Importants](#concepts-python-importants)
10. [Glossaire des Termes](#glossaire-des-termes)

---

## 1. Structure Générale

### Qu'est-ce qu'une Application Streamlit?

**Streamlit** est une bibliothèque Python qui transforme votre code Python en une application web interactive. Pas besoin de HTML, CSS ou JavaScript!

```python
import streamlit as st

# Afficher un titre
st.title("Mon Application")

# Afficher du texte
st.write("Bonjour le monde!")

# Créer un bouton
if st.button("Cliquez-moi"):
    st.write("Vous avez cliqué!")
```

**Résultat:** Une page web avec un titre, du texte et un bouton cliquable.

### Structure de Notre Application

```
app.py
│
├── Imports (lignes 1-20)
│   └── Charger les outils nécessaires
│
├── Configuration (lignes 21-50)
│   └── Définir l'apparence de la page
│
├── Chargement Données (lignes 51-100)
│   └── Lire les fichiers CSV
│
├── Interface (lignes 101-150)
│   └── Créer le menu de navigation
│
└── Pages (lignes 151-726)
    ├── Dashboard (📈)
    ├── Prévisions (🔮)
    ├── Inventaire (📦)
    ├── Clients RFM (👥)
    ├── Rapports (📊)
    └── À Propos (ℹ️)
```

---

## 2. Imports et Bibliothèques

### Qu'est-ce qu'un Import?

Un **import** charge du code que d'autres personnes ont écrit pour vous. C'est comme utiliser des outils déjà fabriqués au lieu de tout construire vous-même.

### Code Expliqué

```python
import streamlit as st
```
**Signification:**
- `import streamlit` = Charger la bibliothèque Streamlit
- `as st` = Créer un raccourci. Au lieu d'écrire `streamlit.title()`, on peut écrire `st.title()`

**Analogie:** C'est comme dire "Appelle Streamlit par son surnom 'st' pour aller plus vite"

---

```python
import pandas as pd
```
**Signification:**
- `pandas` = Bibliothèque pour manipuler des tableaux de données (comme Excel en Python)
- `as pd` = Raccourci

**Ce que pandas fait:**
```python
# Lire un fichier CSV
df = pd.read_csv("ventes.csv")

# Voir les 5 premières lignes
df.head()

# Calculer la somme d'une colonne
total = df['prix'].sum()
```

---

```python
import numpy as np
```
**Signification:**
- `numpy` = Bibliothèque pour calculs mathématiques
- `as np` = Raccourci

**Ce que numpy fait:**
```python
# Créer un tableau de nombres
nombres = np.array([1, 2, 3, 4, 5])

# Calculer la moyenne
moyenne = np.mean(nombres)  # Résultat: 3.0

# Calculer l'écart-type
ecart = np.std(nombres)
```

---

```python
import matplotlib.pyplot as plt
import seaborn as sns
```
**Signification:**
- `matplotlib` = Bibliothèque pour créer des graphiques
- `seaborn` = Extension de matplotlib avec des graphiques plus jolis

**Exemple:**
```python
# Créer un graphique simple
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Mon Graphique")
plt.show()
```

---

```python
import plotly.graph_objects as go
import plotly.express as px
```
**Signification:**
- `plotly` = Bibliothèque pour créer des graphiques **interactifs** (vous pouvez zoomer, survoler, etc.)

**Différence avec matplotlib:**
- **matplotlib** = Graphiques statiques (images fixes)
- **plotly** = Graphiques interactifs (vous pouvez interagir avec la souris)

**Exemple:**
```python
# Graphique interactif
fig = px.line(x=[1, 2, 3], y=[4, 5, 6])
fig.show()  # Vous pouvez zoomer, survoler les points
```

---

```python
from pathlib import Path
```
**Signification:**
- `Path` = Outil pour manipuler les chemins de fichiers de manière facile

**Exemple:**
```python
# Ancien style (compliqué)
fichier = "C:\\Users\\Dell\\Desktop\\data.csv"

# Nouveau style avec Path (facile)
fichier = Path(".") / "data.csv"
```

---

```python
from datetime import datetime, timedelta
```
**Signification:**
- `datetime` = Outil pour manipuler les dates et heures

**Exemple:**
```python
# Date actuelle
maintenant = datetime.now()
print(maintenant)  # 2025-12-09 15:30:00

# Formater une date
date_formatée = maintenant.strftime("%Y-%m-%d")
print(date_formatée)  # 2025-12-09

# Ajouter 7 jours
dans_7_jours = maintenant + timedelta(days=7)
```

---

```python
import warnings
warnings.filterwarnings('ignore')
```
**Signification:**
- Désactiver les messages d'avertissement (warnings)
- Rend l'application plus propre pour l'utilisateur

**Analogie:** C'est comme mettre votre téléphone en mode silencieux.

---

## 3. Configuration de la Page

### Code: Configuration Streamlit

```python
st.set_page_config(
    page_title="KWEEK - Restaurant Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

**Explication ligne par ligne:**

#### `page_title="KWEEK - Restaurant Analytics"`
- **Ce que ça fait:** Change le titre dans l'onglet du navigateur
- **Résultat visible:** L'onglet affiche "📊 KWEEK - Restaurant Analytics"

#### `page_icon="📊"`
- **Ce que ça fait:** Change l'icône (favicon) dans l'onglet
- **Résultat visible:** Un emoji graphique 📊 apparaît à côté du titre

#### `layout="wide"`
- **Ce que ça fait:** Utilise toute la largeur de l'écran (au lieu d'une colonne étroite)
- **Options:**
  - `"centered"` = Colonne étroite au centre (par défaut)
  - `"wide"` = Toute la largeur de l'écran

#### `initial_sidebar_state="expanded"`
- **Ce que ça fait:** La barre latérale (sidebar) est ouverte au démarrage
- **Options:**
  - `"expanded"` = Ouverte
  - `"collapsed"` = Fermée

---

### Code: CSS Personnalisé

```python
st.markdown("""
    <style>
        .main {
            padding: 0rem 1rem;
        }
        h1 {
            color: #1f77b4;
        }
    </style>
""", unsafe_allow_html=True)
```

**Explication:**

#### Qu'est-ce que CSS?
**CSS** (Cascading Style Sheets) = Langage pour styliser les pages web (couleurs, tailles, positions)

#### `.main { padding: 0rem 1rem; }`
- **`.main`** = Sélecteur qui cible la zone principale
- **`padding`** = Espace intérieur
- **`0rem 1rem`** = 0 en haut/bas, 1rem gauche/droite
- **Résultat:** Ajoute de l'espace sur les côtés

#### `h1 { color: #1f77b4; }`
- **`h1`** = Tous les titres de niveau 1
- **`color`** = Couleur du texte
- **`#1f77b4`** = Code couleur hexadécimal (bleu)
- **Résultat:** Les titres deviennent bleus

#### `unsafe_allow_html=True`
- **Ce que ça fait:** Permet d'insérer du HTML/CSS dans Streamlit
- **Pourquoi "unsafe"?** Streamlit avertit que le HTML peut causer des problèmes de sécurité

**Analogie CSS:**
```css
/* CSS c'est comme une feuille de style pour votre application */
element {
    propriété: valeur;
}
```

---

## 4. Chargement des Données

### Qu'est-ce qu'une Fonction?

Une **fonction** est un bloc de code réutilisable. Au lieu de réécrire le même code plusieurs fois, vous l'écrivez une fois dans une fonction.

```python
# Sans fonction (répétitif)
resultat1 = 5 + 3
resultat2 = 10 + 7
resultat3 = 2 + 9

# Avec fonction (réutilisable)
def additionner(a, b):
    return a + b

resultat1 = additionner(5, 3)   # 8
resultat2 = additionner(10, 7)  # 17
resultat3 = additionner(2, 9)   # 11
```

---

### Code: Fonction de Chargement

```python
@st.cache_data
def load_data():
    """Charger toutes les données du projet"""
    data_path = Path(".")
    
    transactions = pd.read_csv(data_path / "restaurant_sales_transactions.csv")
    daily = pd.read_csv(data_path / "restaurant_daily_factors_sales.csv")
    
    return {
        'transactions': transactions,
        'daily': daily
    }
```

**Explication ligne par ligne:**

#### `@st.cache_data`
**Qu'est-ce qu'un décorateur?**
- Un décorateur (`@`) ajoute des fonctionnalités à une fonction
- `@st.cache_data` = Met en cache (sauvegarde) les données

**Pourquoi c'est important?**
```python
# Sans cache
# Chaque fois qu'on actualise la page:
données = load_data()  # Recharge les CSV → LENT ❌

# Avec @st.cache_data
# Première fois:
données = load_data()  # Charge les CSV → 5 secondes

# Fois suivantes:
données = load_data()  # Utilise le cache → INSTANTANÉ ✅
```

**Analogie:** C'est comme garder un livre ouvert à la bonne page au lieu de le chercher à chaque fois.

---

#### `def load_data():`
- **`def`** = Mot-clé pour définir une fonction
- **`load_data`** = Nom de la fonction (vous choisissez ce nom)
- **`()`** = Parenthèses pour les paramètres (ici aucun paramètre)
- **`:`** = Début du bloc de code de la fonction

**Structure d'une fonction:**
```python
def nom_fonction(parametre1, parametre2):
    # Code de la fonction
    resultat = parametre1 + parametre2
    return resultat
```

---

#### `"""Charger toutes les données du projet"""`
**Qu'est-ce qu'une docstring?**
- Texte entre `"""` qui explique ce que fait la fonction
- Apparaît quand vous tapez `help(load_data)`

```python
def ma_fonction():
    """Cette fonction fait quelque chose d'important"""
    pass

# Afficher l'aide
help(ma_fonction)
# Output: Cette fonction fait quelque chose d'important
```

---

#### `data_path = Path(".")`
- **`Path(".")`** = Chemin du dossier actuel
- **`"."`** = Dossier où se trouve le script Python

**Exemple:**
```python
# Si app.py est dans:
# C:\Users\Dell\Desktop\machine learning\

data_path = Path(".")
# data_path = C:\Users\Dell\Desktop\machine learning\
```

---

#### `transactions = pd.read_csv(data_path / "restaurant_sales_transactions.csv")`

**Décomposition:**
1. **`data_path / "restaurant_sales_transactions.csv"`**
   - Combine le chemin du dossier avec le nom du fichier
   - Résultat: `C:\Users\Dell\Desktop\machine learning\restaurant_sales_transactions.csv`

2. **`pd.read_csv(...)`**
   - Fonction pandas qui lit un fichier CSV
   - Retourne un **DataFrame** (tableau de données)

3. **`transactions =`**
   - Stocke le DataFrame dans la variable `transactions`

**Qu'est-ce qu'un DataFrame?**
```python
# Un DataFrame est comme un tableau Excel en Python
#
#   transaction_id     date      product_name  quantity  total_amount
# 0  TRX_000001    2023-01-01  Fresh Salmon      1         32.0
# 1  TRX_000002    2023-01-01  Fresh Salmon      1         32.0
# 2  TRX_000003    2023-01-01  Ribeye Steak      2         88.0
```

---

#### `return { 'transactions': transactions, 'daily': daily }`

**Qu'est-ce qu'un dictionnaire?**
Un dictionnaire (`{}`) stocke des paires clé-valeur:

```python
# Créer un dictionnaire
personne = {
    'nom': 'Alice',
    'age': 30,
    'ville': 'Paris'
}

# Accéder aux valeurs
print(personne['nom'])   # Alice
print(personne['age'])   # 30
```

**Dans notre code:**
```python
return {
    'transactions': transactions,  # Clé: 'transactions', Valeur: DataFrame
    'daily': daily                 # Clé: 'daily', Valeur: DataFrame
}
```

**Utilisation:**
```python
data = load_data()
print(data['transactions'])  # Affiche le DataFrame transactions
print(data['daily'])         # Affiche le DataFrame daily
```

---

### Code: Appel de la Fonction

```python
try:
    data = load_data()
    st.session_state.data_loaded = True
except Exception as e:
    st.error(f"❌ Erreur lors du chargement des données: {str(e)}")
    st.stop()
```

**Explication:**

#### `try:` et `except:`
**Qu'est-ce que la gestion d'erreurs?**
- `try:` = Essaie d'exécuter ce code
- `except:` = Si une erreur se produit, exécute ce code à la place

```python
# Sans gestion d'erreurs
resultat = 10 / 0  # CRASH! Division par zéro

# Avec gestion d'erreurs
try:
    resultat = 10 / 0
except:
    print("Impossible de diviser par zéro!")
    resultat = 0
```

**Dans notre code:**
```python
try:
    data = load_data()  # Essaie de charger les données
except Exception as e:  # Si erreur, capture l'exception
    st.error(...)       # Affiche un message d'erreur
    st.stop()           # Arrête l'application
```

---

#### `st.session_state.data_loaded = True`
**Qu'est-ce que session_state?**
- Variable qui persiste entre les actualisations de page
- Comme une mémoire pour l'application

```python
# Compteur de clics
if 'compteur' not in st.session_state:
    st.session_state.compteur = 0

if st.button("Cliquer"):
    st.session_state.compteur += 1

st.write(f"Clics: {st.session_state.compteur}")
```

---

#### `st.error(f"❌ Erreur: {str(e)}")`
**f-string (formatted string):**
- `f"..."` = Chaîne formatée
- `{variable}` = Insère la valeur de la variable dans la chaîne

```python
nom = "Alice"
age = 30

# Sans f-string
message = "Bonjour " + nom + ", vous avez " + str(age) + " ans"

# Avec f-string (plus facile!)
message = f"Bonjour {nom}, vous avez {age} ans"
```

---

## 5. Page Dashboard

### Code: Métriques

```python
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_sales = data['transactions']['total_amount'].sum()
    st.metric("💰 Chiffre d'Affaires Total", f"€{total_sales:,.0f}")
```

**Explication:**

#### `st.columns(4)`
**Qu'est-ce que ça fait?**
- Crée 4 colonnes de même largeur sur la page
- Permet d'afficher des éléments côte à côte

```python
# Créer 3 colonnes
col1, col2, col3 = st.columns(3)

# Mettre du contenu dans chaque colonne
with col1:
    st.write("Colonne 1")

with col2:
    st.write("Colonne 2")

with col3:
    st.write("Colonne 3")
```

**Résultat visuel:**
```
┌──────────┬──────────┬──────────┐
│ Colonne 1│ Colonne 2│ Colonne 3│
└──────────┴──────────┴──────────┘
```

---

#### `with col1:`
**Qu'est-ce qu'un context manager?**
- `with` = Mot-clé pour entrer dans un contexte
- Tout ce qui est indenté sous `with col1:` sera placé dans la colonne 1

```python
# Sans with (compliqué)
col1.write("Texte")
col1.metric("Métrique", "100")

# Avec with (plus clair)
with col1:
    st.write("Texte")
    st.metric("Métrique", "100")
```

---

#### `data['transactions']['total_amount'].sum()`

**Décomposition:**
1. **`data['transactions']`**
   - Accède au DataFrame transactions dans le dictionnaire data
   - Type: DataFrame pandas

2. **`['total_amount']`**
   - Accède à la colonne 'total_amount' du DataFrame
   - Type: Series pandas (colonne)

3. **`.sum()`**
   - Calcule la somme de tous les nombres dans cette colonne
   - Type: float (nombre décimal)

**Exemple:**
```python
# Données
transactions = pd.DataFrame({
    'produit': ['Salmon', 'Steak', 'Salad'],
    'total_amount': [32.0, 88.0, 15.0]
})

# Calculer la somme
total = transactions['total_amount'].sum()
print(total)  # 135.0
```

---

#### `f"€{total_sales:,.0f}"`

**Format de nombres:**
- `{total_sales:,.0f}` = Format spécial pour les nombres
  - `:` = Début du format
  - `,` = Séparateur de milliers (1,000 au lieu de 1000)
  - `.0f` = 0 décimales, format float

**Exemples:**
```python
nombre = 12345.67

f"{nombre:,.2f}"   # 12,345.67 (2 décimales)
f"{nombre:,.0f}"   # 12,346 (0 décimale, arrondi)
f"{nombre:,.1f}"   # 12,345.7 (1 décimale)
```

---

#### `st.metric("💰 Chiffre d'Affaires Total", f"€{total_sales:,.0f}")`

**Qu'est-ce qu'une métrique?**
- Widget Streamlit qui affiche une valeur avec un label
- Peut aussi afficher un changement (delta)

```python
st.metric(
    label="Temperature",
    value="25°C",
    delta="2°C"  # Optionnel: montre le changement
)
```

**Résultat visuel:**
```
┌────────────────────┐
│ Temperature        │
│      25°C          │
│      +2°C ▲        │
└────────────────────┘
```

---

### Code: Graphiques

```python
fig = px.line(
    daily_data, 
    x='date', 
    y='total_revenue',
    title="Évolution des Ventes",
    labels={'date': 'Date', 'total_revenue': 'Ventes (€)'},
    template='plotly_white'
)
fig.update_layout(hovermode='x unified', height=400)
st.plotly_chart(fig, use_container_width=True)
```

**Explication:**

#### `px.line(...)`
**Plotly Express:**
- `px` = Plotly Express (version simplifiée de plotly)
- `.line()` = Créer un graphique en ligne

**Paramètres:**
- `daily_data` = DataFrame contenant les données
- `x='date'` = Colonne pour l'axe X (horizontal)
- `y='total_revenue'` = Colonne pour l'axe Y (vertical)
- `title="..."` = Titre du graphique
- `labels={...}` = Renommer les axes
- `template='plotly_white'` = Style visuel (fond blanc)

---

#### `fig.update_layout(hovermode='x unified', height=400)`
**Personnaliser le graphique:**
- `hovermode='x unified'` = Affiche toutes les valeurs pour un X donné
- `height=400` = Hauteur de 400 pixels

**Options hovermode:**
```python
hovermode='x'         # Info pour un point X
hovermode='y'         # Info pour un point Y
hovermode='closest'   # Point le plus proche
hovermode='x unified' # Tous les points pour un X
```

---

#### `st.plotly_chart(fig, use_container_width=True)`
**Afficher le graphique:**
- `st.plotly_chart()` = Fonction Streamlit pour afficher un graphique Plotly
- `fig` = Le graphique créé
- `use_container_width=True` = Utilise toute la largeur disponible

---

## 6. Page Prévisions

### Code: Sélecteur

```python
selected_product = st.selectbox(
    "Sélectionnez un produit:",
    options=sorted(data['transactions']['product_name'].unique())
)
```

**Explication:**

#### `st.selectbox(...)`
**Qu'est-ce qu'un selectbox?**
- Menu déroulant pour choisir une option
- Retourne la valeur sélectionnée

```python
# Exemple simple
couleur = st.selectbox(
    "Choisissez une couleur:",
    options=["Rouge", "Vert", "Bleu"]
)

st.write(f"Vous avez choisi: {couleur}")
```

---

#### `data['transactions']['product_name'].unique()`

**Décomposition:**
1. **`data['transactions']`** = DataFrame transactions
2. **`['product_name']`** = Colonne des noms de produits
3. **`.unique()`** = Retourne uniquement les valeurs uniques (sans doublons)

**Exemple:**
```python
# Données avec doublons
produits = ['Salmon', 'Steak', 'Salmon', 'Salad', 'Steak']

# Obtenir valeurs uniques
uniques = pd.Series(produits).unique()
print(uniques)  # ['Salmon', 'Steak', 'Salad']
```

---

#### `sorted(...)`
**Trier par ordre alphabétique:**
```python
# Liste non triée
fruits = ['Orange', 'Apple', 'Banana']

# Trier
triés = sorted(fruits)
print(triés)  # ['Apple', 'Banana', 'Orange']
```

---

### Code: Slider

```python
forecast_days = st.slider(
    "Horizon de prévision (jours):",
    min_value=7, 
    max_value=90, 
    value=30, 
    step=7
)
```

**Explication:**

#### `st.slider(...)`
**Qu'est-ce qu'un slider?**
- Barre de défilement pour sélectionner une valeur
- Retourne la valeur sélectionnée (nombre)

**Paramètres:**
- `min_value=7` = Valeur minimale
- `max_value=90` = Valeur maximale
- `value=30` = Valeur par défaut
- `step=7` = Incrément (saute de 7 en 7)

**Résultat visuel:**
```
Horizon de prévision (jours):
├────────●────────┤
7               90
```

---

## 7. Page Inventaire

### Code: Métriques Conditionnelles

```python
with col1:
    total_stock = data['inventory']['quantity_available'].sum() if 'quantity_available' in data['inventory'].columns else 0
    st.metric("Total Stock", f"{total_stock:,} unités")
```

**Explication:**

#### Expression Conditionnelle (Ternaire)

**Structure:**
```python
valeur = A if condition else B
```
- Si `condition` est vraie, `valeur = A`
- Sinon, `valeur = B`

**Exemples:**
```python
# Exemple 1
age = 20
statut = "Majeur" if age >= 18 else "Mineur"
# statut = "Majeur"

# Exemple 2
temperature = 15
message = "Chaud" if temperature > 25 else "Froid"
# message = "Froid"
```

**Dans notre code:**
```python
total_stock = data['inventory']['quantity_available'].sum() if 'quantity_available' in data['inventory'].columns else 0
```

**Décomposition:**
1. **Condition:** `'quantity_available' in data['inventory'].columns`
   - Vérifie si la colonne existe
2. **Si vrai:** `.sum()` calcule la somme
3. **Si faux:** Retourne `0`

---

### Code: Coloration des Lignes

```python
def highlight_risk(row):
    days = row.get('days_until_expiry', 999)
    if days <= 1:
        return ['background-color: #ff6b6b'] * len(row)
    elif days <= 3:
        return ['background-color: #ffa500'] * len(row)
    else:
        return ['background-color: white'] * len(row)
```

**Explication:**

#### `.get('days_until_expiry', 999)`
**Méthode sûre pour accéder à une valeur:**
- `row.get(clé, défaut)` = Retourne la valeur de `clé` ou `défaut` si inexistante

```python
# Dictionnaire
personne = {'nom': 'Alice', 'age': 30}

# Sans get (peut crasher)
ville = personne['ville']  # KeyError!

# Avec get (safe)
ville = personne.get('ville', 'Inconnue')  # 'Inconnue'
```

---

#### `['background-color: #ff6b6b'] * len(row)`

**Multiplication de listes:**
```python
# Créer une liste répétée
couleur = ['rouge'] * 3
print(couleur)  # ['rouge', 'rouge', 'rouge']

# Pour chaque colonne du row
['background-color: red'] * 5
# ['background-color: red', 'background-color: red', ...]
```

**Pourquoi?**
- Pandas `.style.apply()` attend une liste de styles (un par colonne)
- `len(row)` = Nombre de colonnes
- On doit retourner autant de styles que de colonnes

---

#### Conditions `if/elif/else`

**Structure:**
```python
if condition1:
    # Code si condition1 vraie
elif condition2:
    # Code si condition2 vraie
else:
    # Code si aucune condition vraie
```

**Exemple:**
```python
note = 15

if note >= 16:
    mention = "Très bien"
elif note >= 14:
    mention = "Bien"
elif note >= 12:
    mention = "Assez bien"
else:
    mention = "Passable"
```

---

### Code: Histogramme

```python
fig = px.histogram(
    filtered_data, 
    x='days_until_expiry', 
    nbins=30,
    template='plotly_white',
    labels={'days_until_expiry': 'Jours jusqu\'à Expiration'},
    title="Distribution"
)
```

**Explication:**

#### `px.histogram(...)`
**Qu'est-ce qu'un histogramme?**
- Graphique qui montre la distribution des données
- Regroupe les valeurs en "bins" (intervalles)

**Exemple:**
```
Âges: [20, 22, 25, 28, 30, 32, 35, 38]

Histogramme:
   │
 4 │     ██
 3 │ ██  ██  ██
 2 │ ██  ██  ██  ██
 1 │ ██  ██  ██  ██
   └───────────────
    20  25  30  35
```

---

#### `nbins=30`
**Nombre de barres:**
- `nbins` = Number of bins (nombre d'intervalles)
- Plus le nombre est grand, plus les barres sont fines

```python
# Peu de bins (5)
│ ████
│ ████  ████
│ ████  ████  ████

# Beaucoup de bins (20)
│ ██
│ ██ ██
│ ██ ██ ██ ██
```

---

## 8. Page Clients RFM

### Code: Dictionnaire de Données

```python
cluster_data = pd.DataFrame({
    'Cluster': ['VIP', 'Standard', 'Occasional'],
    'Clients': [45, 250, 205],
    'AOV (€)': [850, 320, 120]
})
```

**Explication:**

#### Créer un DataFrame depuis un Dictionnaire

**Structure:**
```python
df = pd.DataFrame({
    'colonne1': [valeur1, valeur2, valeur3],
    'colonne2': [valeur1, valeur2, valeur3]
})
```

**Résultat:**
```
      Cluster  Clients  AOV (€)
0         VIP       45      850
1    Standard      250      320
2  Occasional      205      120
```

**Analogie:** C'est comme créer un tableau Excel directement dans le code.

---

### Code: Graphique Circulaire

```python
fig = px.pie(
    values=cluster_data['Clients'], 
    names=cluster_data['Cluster'],
    template='plotly_white'
)
```

**Explication:**

#### `px.pie(...)`
**Qu'est-ce qu'un pie chart (graphique circulaire)?**
- Montre les proportions de chaque catégorie
- Chaque tranche = un pourcentage du total

**Paramètres:**
- `values` = Valeurs numériques (tailles des tranches)
- `names` = Noms des catégories (labels)

**Résultat visuel:**
```
        ╱───╲
      ╱       ╲
    ╱   VIP    ╲─────  9%
   │            │
   │  Standard  │────  50%
    ╲          ╱
      ╲───────╱  Occasional 41%
```

---

## 9. Concepts Python Importants

### Listes

**Qu'est-ce qu'une liste?**
- Collection ordonnée d'éléments
- Peut contenir n'importe quoi (nombres, textes, objets)

```python
# Créer une liste
fruits = ['pomme', 'banane', 'orange']

# Accéder à un élément (index commence à 0)
premier = fruits[0]  # 'pomme'
dernier = fruits[-1] # 'orange'

# Ajouter un élément
fruits.append('fraise')

# Longueur
nombre = len(fruits)  # 4

# Boucle sur les éléments
for fruit in fruits:
    print(fruit)
```

---

### Dictionnaires

**Qu'est-ce qu'un dictionnaire?**
- Collection de paires clé-valeur
- Comme un carnet d'adresses (nom → numéro)

```python
# Créer un dictionnaire
personne = {
    'nom': 'Alice',
    'age': 30,
    'ville': 'Paris'
}

# Accéder à une valeur
nom = personne['nom']  # 'Alice'

# Ajouter/Modifier
personne['email'] = 'alice@email.com'

# Vérifier si clé existe
if 'age' in personne:
    print(f"Age: {personne['age']}")

# Boucle sur les items
for clé, valeur in personne.items():
    print(f"{clé}: {valeur}")
```

---

### Boucles

#### Boucle `for`

**Itérer sur une séquence:**
```python
# Boucle sur une liste
for nombre in [1, 2, 3, 4, 5]:
    print(nombre)

# Boucle sur un range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Boucle sur un DataFrame
for index, row in df.iterrows():
    print(row['colonne'])
```

#### Boucle `while`

**Répéter tant qu'une condition est vraie:**
```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1  # compteur = compteur + 1
```

---

### Conditions

```python
age = 20

# If simple
if age >= 18:
    print("Majeur")

# If-else
if age >= 18:
    print("Majeur")
else:
    print("Mineur")

# If-elif-else
if age < 13:
    print("Enfant")
elif age < 18:
    print("Adolescent")
else:
    print("Adulte")

# Opérateurs de comparaison
==  # Égal
!=  # Différent
>   # Supérieur
<   # Inférieur
>=  # Supérieur ou égal
<=  # Inférieur ou égal

# Opérateurs logiques
and  # ET (les deux conditions vraies)
or   # OU (au moins une condition vraie)
not  # NON (inverse)

# Exemple
if age >= 18 and age < 65:
    print("Adulte en âge de travailler")
```

---

### Fonctions

**Structure complète:**
```python
def nom_fonction(parametre1, parametre2, parametre3=valeur_defaut):
    """Documentation de la fonction"""
    # Code
    resultat = parametre1 + parametre2
    return resultat

# Appel
valeur = nom_fonction(5, 3)  # 8
valeur = nom_fonction(5, 3, 10)  # utilise parametre3
```

**Paramètres par défaut:**
```python
def saluer(nom, formule="Bonjour"):
    return f"{formule} {nom}!"

print(saluer("Alice"))           # Bonjour Alice!
print(saluer("Bob", "Salut"))    # Salut Bob!
```

---

### Compréhensions de Liste

**Créer des listes de manière concise:**
```python
# Sans compréhension (long)
carrés = []
for i in range(5):
    carrés.append(i ** 2)

# Avec compréhension (court)
carrés = [i ** 2 for i in range(5)]
# [0, 1, 4, 9, 16]

# Avec condition
pairs = [i for i in range(10) if i % 2 == 0]
# [0, 2, 4, 6, 8]
```

---

## 10. Glossaire des Termes

### Termes Généraux

**API (Application Programming Interface)**
- Interface pour interagir avec un logiciel
- Exemple: Streamlit API = fonctions comme `st.write()`

**Bibliothèque (Library)**
- Collection de code réutilisable
- Exemple: pandas, numpy, streamlit

**Module**
- Fichier Python contenant du code
- Peut être importé: `import mon_module`

**Package**
- Collection de modules
- Exemple: `numpy` est un package avec plusieurs modules

**Framework**
- Structure pour construire des applications
- Exemple: Streamlit est un framework web

---

### Termes Données

**DataFrame**
- Tableau de données en 2D (lignes et colonnes)
- Comme une feuille Excel en Python

**Series**
- Une colonne d'un DataFrame
- Tableau en 1D

**Index**
- Identifiants des lignes d'un DataFrame
- Souvent des nombres (0, 1, 2...)

**CSV (Comma-Separated Values)**
- Format de fichier texte pour stocker des données
- Colonnes séparées par des virgules

**Agrégation**
- Combiner plusieurs valeurs en une seule
- Exemple: somme, moyenne, maximum

---

### Termes Streamlit

**Widget**
- Élément interactif (bouton, slider, selectbox)

**Sidebar**
- Barre latérale pour navigation/contrôles

**Layout**
- Organisation des éléments sur la page

**Cache**
- Mémoire temporaire pour accélérer l'application

**Session State**
- Variables qui persistent entre les actualisations

---

### Termes Statistiques

**Moyenne (Mean)**
```python
moyenne = sum(valeurs) / len(valeurs)
# ou
moyenne = np.mean(valeurs)
```

**Médiane (Median)**
- Valeur du milieu quand les données sont triées
```python
mediane = np.median(valeurs)
```

**Écart-type (Standard Deviation)**
- Mesure de dispersion des données
```python
ecart = np.std(valeurs)
```

**Corrélation**
- Relation entre deux variables (-1 à +1)
- +1 = Corrélation positive parfaite
- -1 = Corrélation négative parfaite
- 0 = Aucune corrélation

---

### Termes Graphiques

**Axe X (Horizontal)**
- Axe horizontal d'un graphique

**Axe Y (Vertical)**
- Axe vertical d'un graphique

**Légende**
- Explication des symboles/couleurs

**Tooltip**
- Info-bulle au survol de la souris

**Heatmap**
- Graphique où les valeurs sont représentées par des couleurs

---

## 🎓 Exercices Pratiques

### Exercice 1: Modifier les Couleurs

**Objectif:** Changer la couleur des titres

**Code actuel:**
```python
h1 {
    color: #1f77b4;  /* Bleu */
}
```

**À faire:**
1. Ouvrez `app.py`
2. Cherchez `color: #1f77b4`
3. Remplacez par `color: #ff0000` (rouge)
4. Sauvegardez et actualisez l'app

**Autres couleurs:**
- `#00ff00` = Vert
- `#ff00ff` = Magenta
- `#ffaa00` = Orange

---

### Exercice 2: Ajouter une Métrique

**Objectif:** Ajouter une 5ème métrique au Dashboard

**Code à ajouter après col4:**
```python
with col5:
    avg_price = data['transactions']['unit_price'].mean()
    st.metric("💵 Prix Unitaire Moyen", f"€{avg_price:.2f}")
```

**Modifications nécessaires:**
```python
# Changer de 4 à 5 colonnes
col1, col2, col3, col4, col5 = st.columns(5)
```

---

### Exercice 3: Créer un Nouveau Graphique

**Objectif:** Ajouter un graphique bar chart

```python
# Après les graphiques existants
st.subheader("📊 Ventes par Catégorie")

# Grouper par catégorie
category_sales = data['transactions'].groupby('category')['total_amount'].sum()

# Créer le graphique
fig = px.bar(
    x=category_sales.index,
    y=category_sales.values,
    labels={'x': 'Catégorie', 'y': 'Ventes (€)'},
    title="Total des Ventes par Catégorie"
)

st.plotly_chart(fig, use_container_width=True)
```

---

## 📝 Résumé des Concepts Clés

### 1. Streamlit Basics
```python
st.write("Texte")                    # Afficher du texte
st.title("Titre")                    # Titre principal
st.header("En-tête")                 # En-tête de section
st.subheader("Sous-titre")           # Sous-titre
st.metric("Label", "Valeur")         # Métrique
st.button("Cliquer")                 # Bouton
st.selectbox("Label", options)       # Menu déroulant
st.slider("Label", min, max)         # Slider
```

### 2. Pandas Basics
```python
df = pd.read_csv("file.csv")         # Lire CSV
df.head()                            # 5 premières lignes
df['colonne']                        # Accéder à une colonne
df['colonne'].sum()                  # Somme
df['colonne'].mean()                 # Moyenne
df.groupby('col1')['col2'].sum()     # Grouper et agréger
```

### 3. Plotly Basics
```python
px.line(df, x='x', y='y')            # Graphique en ligne
px.bar(x=vals, y=names)              # Graphique en barres
px.pie(values=vals, names=names)     # Graphique circulaire
px.histogram(df, x='col')            # Histogramme
```

---

## 🚀 Prochaines Étapes

### Pour Continuer à Apprendre

1. **Pratiquez avec les exercices** de ce guide
2. **Modifiez l'application** pour ajouter vos propres features
3. **Lisez la documentation:**
   - Streamlit: docs.streamlit.io
   - Pandas: pandas.pydata.org
   - Plotly: plotly.com/python

4. **Créez votre propre projet:**
   - Commencez petit (analyse simple)
   - Ajoutez des features progressivement
   - Testez et itérez

---

## ❓ Questions Fréquentes

### Q1: Pourquoi mon code ne fonctionne pas?
**R:** Vérifiez:
1. Les **indentations** (espaces au début des lignes)
2. Les **noms de variables** (respectez majuscules/minuscules)
3. Les **parenthèses** (ouvertes et fermées)
4. Les **guillemets** (simples ou doubles, mais cohérents)

### Q2: Comment déboguer?
**R:** Utilisez `st.write()` pour afficher des valeurs:
```python
st.write(f"Valeur de x: {x}")
st.write(f"Type: {type(x)}")
st.write(data)  # Afficher tout un DataFrame
```

### Q3: Comment installer une nouvelle bibliothèque?
**R:** Dans le terminal:
```powershell
pip install nom_bibliotheque
```

### Q4: L'app est lente, pourquoi?
**R:** Utilisez `@st.cache_data` pour les fonctions lourdes:
```python
@st.cache_data
def fonction_lente():
    # Code lourd
    return resultat
```

---

## 🎉 Conclusion

Vous avez maintenant une compréhension complète de:
- ✅ Comment fonctionne Streamlit
- ✅ Les bases de Python
- ✅ La manipulation de données avec Pandas
- ✅ La création de graphiques avec Plotly
- ✅ L'architecture de l'application KWEEK

**Continuez à pratiquer et à expérimenter!** 🚀

---

**Bon apprentissage! 📚**
