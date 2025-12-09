# Installation et Démarrage de l'Application Streamlit

## 🚀 Installation Rapide

### Option 1: PowerShell (Recommandé pour Windows)

```powershell
# 1. Installer Streamlit et dépendances
pip install streamlit plotly

# 2. Lancer l'application
streamlit run app.py
```

### Option 2: Invite de Commande

```cmd
pip install streamlit plotly
streamlit run app.py
```

---

## 📋 Prérequis

Assurez-vous que vous avez:
- ✅ Python 3.13.5 (ou compatible)
- ✅ Tous les fichiers CSV dans le dossier courant
- ✅ Le dossier `outputs/` avec les résultats générés
- ✅ Le notebook exécuté au moins une fois

---

## ✨ Fonctionnalités de l'Application

### 1️⃣ **Dashboard (📈)**
- Métriques principales: CA, unités, panier moyen
- Graphiques de tendances des ventes
- Top 5 et Bottom 5 produits
- Matrice de corrélation

### 2️⃣ **Prévisions (🔮)**
- Sélectionnez un produit
- Choisissez l'horizon de prévision (7-90 jours)
- Comparez 3 modèles: Random Forest ⭐, ETS, Advanced ETS
- Visualisez les intervalles de confiance
- Téléchargez les résultats

### 3️⃣ **Inventaire (📦)**
- Surveillance en temps réel du stock
- Articles en danger d'expiration avec code couleur
- Distribution par jours jusqu'à expiration
- Recommandations de réduction par risque
- Export de la liste complète

### 4️⃣ **Clients RFM (👥)**
- Segmentation en 3 clusters (VIP, Standard, Occasional)
- Profil détaillé de chaque segment
- Stratégies marketing adaptées
- Matrice RFM complète

### 5️⃣ **Rapports (📊)**
- Téléchargement des fichiers de prévision
- Accès aux résumés commerciaux mensuels
- Galerie des 170+ visualisations
- Export personnalisé

### 6️⃣ **À Propos (ℹ️)**
- Informations du projet
- Métriques de performance
- Ressources et liens
- Support

---

## 🎯 Utilisation

### Première visite?
1. Allez à **📈 Dashboard** pour une vue d'ensemble
2. Explorez **🔮 Prévisions** pour voir la puissance ML
3. Vérifiez **📦 Inventaire** pour les actions urgentes
4. Comprenez vos clients via **👥 Clients RFM**

### Utilisateur expert?
1. Accédez directement à **📊 Rapports** pour les données
2. Téléchargez les CSV pour traitement personnalisé
3. Utilisez **🔮 Prévisions** pour modéliser des scénarios

### Manager/Décideur?
1. Consultez **📈 Dashboard** pour KPI clés
2. Lisez **👥 Clients RFM** pour stratégies marketing
3. Revoyez **📦 Inventaire** pour décisions de stock

---

## 📊 Données Chargées

L'application charge automatiquement:

```
✅ restaurant_sales_transactions.csv      (121,640 lignes)
✅ restaurant_daily_factors_sales.csv     (731 lignes)
✅ restaurant_products.csv                (12 produits)
✅ restaurant_clients.csv                 (500 clients)
✅ restaurant_external_factors.csv        (facteurs externes)
✅ restaurant_stock_inventory.csv         (2,928 articles)
✅ outputs/reports/*.csv                  (prévisions)
✅ outputs/forecast/near_expiry_*.csv     (articles à risque)
```

---

## 🔧 Personnalisation

### Modifier les couleurs
Éditez la section **Custom CSS** dans `app.py`:
```python
h1 {
    color: #1f77b4;  # ← Changer cette couleur
}
```

### Ajouter des pages
Ajoutez une nouvelle option dans le menu de navigation:
```python
page = st.sidebar.radio(
    "Sélectionnez une page:",
    ["📈 Dashboard", "🔮 Prévisions", "🆕 Nouvelle Page"]  # Ajouter ici
)
```

### Modifier les graphiques
Trouvez les sections `plotly` ou `matplotlib` et customisez:
```python
fig = px.line(daily_data, x='date', y='ventes',
             title="Mon Titre",  # ← Changer le titre
             template='plotly_white')
```

---

## 🐛 Dépannage

### ❌ "Erreur lors du chargement des données"
- Vérifiez que tous les fichiers CSV sont dans le dossier courant
- Exécutez le notebook pour générer les fichiers `outputs/`

### ❌ "No module named 'streamlit'"
```powershell
pip install streamlit --upgrade
```

### ❌ "Port 8501 already in use"
```powershell
streamlit run app.py --server.port 8502
```

### ❌ Les graphiques ne s'affichent pas
- Actualisez la page (F5)
- Vérifiez votre connexion internet (plotly nécessite une connexion)
- Utilisez le mode offline: `plotly.offline.plot()`

---

## 📈 Performance

- **Chargement initial:** ~3-5 secondes
- **Navigation entre onglets:** Instantané
- **Génération graphiques:** <2 secondes
- **Rafraîchissement données:** @st.cache_data

---

## 🔄 Mise à jour des Données

Pour mettre à jour avec de nouvelles données:

1. Remplacez les fichiers CSV source
2. Exécutez le notebook `kweek-test-notebook.ipynb`
3. Actualisez l'application Streamlit (elle rechargera automatiquement)

---

## 📱 Accès Distant

Pour accéder depuis d'autres ordinateurs:

```powershell
# Écouter sur toutes les interfaces
streamlit run app.py --server.address 0.0.0.0

# Puis accédez via: http://YOUR_IP:8501
```

---

## 🎨 Thèmes

Créez un fichier `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

---

## 💾 Sauvegarde

L'application est **read-only** - les données ne sont pas modifiées. Pour sauvegarder des analyses:

1. Utilisez les boutons "Télécharger" dans l'app
2. Les fichiers seront sauvés dans votre dossier de téléchargement
3. Archivez les fichiers CSVs/PDFs selon vos besoins

---

## ✅ Checklist de Démarrage

- [ ] Installer Python 3.13+
- [ ] `pip install streamlit plotly`
- [ ] Vérifier présence de tous les CSV
- [ ] Exécuter le notebook au moins une fois
- [ ] `streamlit run app.py`
- [ ] Accéder à http://localhost:8501
- [ ] Tester toutes les pages
- [ ] Personnaliser si besoin
- [ ] Partager avec l'équipe!

---

## 🚀 Prochaines Étapes

### Court terme (1-2 semaines)
- ✅ Déployer l'app localement
- ✅ Former l'équipe à l'utilisation
- ✅ Implémenter les recommandations prioritaires

### Moyen terme (1-3 mois)
- 🔄 Ajouter dashboard temps réel avec webhooks
- 🔄 Intégrer API POS pour données live
- 🔄 Ajouter alertes email pour risques critiques

### Long terme (3-6 mois)
- 🚀 Déployer en cloud (Streamlit Cloud, Heroku, AWS)
- 🚀 Ajouter authentification utilisateurs
- 🚀 Créer rapports automatisés quotidiens/hebdos
- 🚀 Intégrer avec système ERP restaurant

---

**Besoin d'aide?** Consultez les autres fichiers de documentation du projet!
