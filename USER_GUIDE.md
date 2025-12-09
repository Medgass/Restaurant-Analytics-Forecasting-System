# 🎯 GUIDE UTILISATEUR - Interface Streamlit KWEEK

## 🚀 Démarrage Rapide

### Windows - 3 Options

#### Option 1️⃣: Double-clic (Plus Simple)
1. Allez dans le dossier `c:\Users\Dell\Desktop\machine learning\`
2. Double-cliquez sur **`RUN_APP.bat`**
3. L'application s'ouvrira automatiquement dans votre navigateur

#### Option 2️⃣: PowerShell
```powershell
cd "c:\Users\Dell\Desktop\machine learning"
.\RUN_APP.ps1
```

#### Option 3️⃣: Terminal Manuel
```powershell
cd "c:\Users\Dell\Desktop\machine learning"
streamlit run app.py
```

### ✅ Quand vous verrez ceci:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

**C'est bon!** → Ouvrez `http://localhost:8501` dans votre navigateur

---

## 📖 Guide des Pages

### 1️⃣ **📈 DASHBOARD** - Vue d'ensemble

**C'est la première page - Point de départ idéal**

#### Que vois-je?
- **4 métriques principales** en haut
  - 💰 Chiffre d'Affaires Total
  - 📦 Unités Vendues
  - 🛒 Panier Moyen
  - 🍽️ Produits Distincts

- **Graphiques interactifs**
  - Tendance des ventes quotidiennes (ligne)
  - Volume quotidien (barres)
  - Top 5 produits par chiffre d'affaires
  - Bottom 5 produits (underperformers)
  - Corrélation entre facteurs externes et ventes

#### Comment l'utiliser?
- **Survol souris** sur un graphique = Infos détaillées
- **Zoom**: Sélectionnez une zone pour zoomer
- **Pan**: Cliquez et glissez pour déplacer
- **Reset**: Double-cliquez sur un graphique pour réinitialiser
- **Télécharger**: Icon "camera" en haut à droite de chaque graphique

#### Questions que ça répond
- ✅ Quel est mon chiffre d'affaires?
- ✅ Comment varient les ventes?
- ✅ Quels produits vendent le mieux?
- ✅ Quels facteurs affectent les ventes? (température, pluie, etc.)

---

### 2️⃣ **🔮 PRÉVISIONS** - Modèles de Demande

**Pour les managers et planificateurs**

#### Interface
1. **À gauche: Paramètres**
   - Sélectionnez un produit (dropdown)
   - Choisissez l'horizon de prévision (7-90 jours)
   - Comparez 3 modèles disponibles

2. **À droite: Métriques du Produit**
   - Ventes totales
   - Quantité vendue
   - Nombre de transactions
   - Prix moyen

#### Graphique Principal
- **Ligne bleue** = Historique (données réelles)
- **Ligne rouge pointillée** = Prévision
- **Zone rouge pâle** = Intervalle de confiance (95%)

#### Comment interpréter?
```
Si la prévision monte → Stock plus de produit
Si la prévision baisse → Préparez des promotions
Si la zone grise est large → Incertitude élevée
Si la zone grise est fine → Prévision fiable
```

#### Modèles Disponibles
| Modèle | Performance | Quand l'utiliser |
|--------|------------|------------------|
| Random Forest ⭐ | R²=0.483 (Meilleur) | Décisions importantes |
| ETS Baseline | R²=0.386 (Bon) | Prévisions rapides |
| Advanced ETS | Analyste | Recherche/Tests |

#### Actions à Faire
1. Sélectionnez **Random Forest** (meilleur modèle)
2. Choisissez votre produit préféré
3. Regardez la prévision 30 jours
4. Préparez vos commandes en conséquence
5. Téléchargez les données si nécessaire

#### Tableau de Données
- Affiche les 30 prochains jours
- Colonnes:
  - `prévision` = Quantité prédite
  - `intervalle_inf` = Minimum probable (95%)
  - `intervalle_sup` = Maximum probable (95%)

---

### 3️⃣ **📦 INVENTAIRE** - Gestion du Stock

**URGENT - Pour les achats/opérations**

#### 4 Métriques d'Alerte
```
💾 Total Stock          = Unités physiques totales
📊 Articles Différents  = Nombre de SKU différents
⚠️  À Risque            = Unités proches expiration
🚨 Critique             = Expiration ≤ 1 jour
```

#### 3 Onglets

**Onglet 1: ⚠️ Articles à Risque**
- Liste rouge = Critique (≤1 jour) 🚨
- Liste orange = Haute (2-3 jours) ⚠️
- Liste jaune = Moyenne (4-7 jours)

Actions:
- ✅ Téléchargez la liste complète (CSV)
- ✅ Appliquez les réductions recommandées (voir Tab 3)
- ✅ Communiquez avec la cuisine/service

**Onglet 2: 📊 Distribution**
- Graphique montrant combien d'articles pour X jours
- Permet d'identifier les pics d'urgence

**Onglet 3: 💰 Recommandations**
```
🚨 Critique (≤1 jour)     → 80% de réduction
⚠️  Haute (2-3 jours)      → 60% de réduction
🟡 Moyenne (4-7 jours)    → 40% de réduction
🟢 Basse (8-14 jours)     → 20% de réduction
```

#### Exemple d'Action
```
Situation: 500 unités d'huître à J+0
Action: 80% de réduction immédiate
Résultat: Écoulement rapide, perte minimale
Impact: Économies estimées €2,500
```

---

### 4️⃣ **👥 CLIENTS RFM** - Segmentation

**Pour le marketing et la stratégie commerciale**

#### Concept RFM
- **R (Recency)** = Dernière visite (combien de jours ago)
- **F (Frequency)** = Fréquence d'achat (fois par mois)
- **M (Monetary)** = Montant dépensé (euros)

#### 3 Segments Automatiques

**🎯 VIP (45 clients - 9%)**
- Achètent souvent (2-3x/mois)
- Dépensent beaucoup (€850 panier moyen)
- Fidèles (95% rétention)

Stratégie:
- Programme VIP premium
- Offres exclusives
- Service personnalisé
- Invitations événements

**📊 Standard (250 clients - 50%)**
- Achètent régulièrement (1x/semaine)
- Budget moyen (€320)
- Loyalité moyenne (65%)

Stratégie:
- Promotions régulières
- Bundles et combos
- Programme de fidélité points
- Email marketing hebdo

**🆕 Occasional (205 clients - 41%)**
- Achètent rarement
- Budget faible (€120)
- À convertir

Stratégie:
- Offres généreuses
- Email d'acquisition
- Réductions d'essai
- Upgrade vers Standard

#### Matrice Détaillée
Tableau montrant pour chaque segment:
- Recency (jours depuis dernière visite)
- Frequency (achats/mois)
- Monetary (€ par transaction)
- Action recommandée

#### Actions Concrètes
```
1. Créer 3 campagnes email (une par segment)
2. VIP: "Merci d'être fidèle - Offre exclusive"
3. Standard: "20% si achat cette semaine"
4. Occasional: "50% pour revenir"
```

---

### 5️⃣ **📊 RAPPORTS** - Téléchargements

**Pour exporter et analyser hors application**

#### Section 1: Données de Prévision
- Fichiers CSV avec prévisions 30 jours
- Formats: demand_forecasts_YYYYMMDD.csv
- Colonnes: produit, prévision, intervalle_inf, intervalle_sup

**Comment l'utiliser:**
```
Excel → Importer le CSV
Excel → Créer vos propres graphiques
Excel → Partager avec les équipes
```

#### Section 2: Résumés Commerciaux
- Fichiers CSV avec analyses mensuelles
- 120 lignes (10 ans × 12 mois)
- Colonnes: mois, produit, ventes, tendance, rang

#### Section 3: Galerie Visualisations
- 170+ images PNG affichées en aperçu
- Cliquez sur une image pour la voir en détail
- Téléchargez en cliquant sur l'image

**Catégories:**
- EDA (4 images): Tendances, corrélations
- Mensuel (52 images): Top/Bottom par mois
- Produits (100 images): Prévisions quotidiennes/hebdos
- Risques (5 images): Expiration, inventaire
- RFM (9 images): Segmentation clients

#### Section 4: Export Personnalisé
- Format: CSV, Excel (future), PDF (future)
- Sélectionnez: Prévisions, Inventaire, Clients, Rapports
- Génère un export combiné

---

### 6️⃣ **ℹ️ À PROPOS** - Infos du Projet

**Documentation du système**

#### Sections
1. **📊 KWEEK Restaurant Analytics**
   - Version, date, statut
   - Objectifs du projet
   - Technologies utilisées

2. **📈 Performance**
   - Scores des modèles ML
   - Temps d'exécution

3. **📊 Dataset**
   - Nombre de transactions
   - Historique
   - Produits, clients, articles stock

4. **🔗 Liens**
   - Documentation (README, INDEX, TECHNICAL)
   - Rapports (VERIFICATION, EXECUTIVE_SUMMARY, STATUS)
   - Code (Notebook, app.py)

5. **📞 Support**
   - Comment obtenir de l'aide
   - Où trouver la documentation

---

## 🎮 Astuces d'Utilisation

### Navigation
- **Sidebar à gauche** = Menu de pages
- **Sidebar en bas** = Statistiques clés
- **⚠️ À risque** = Tous les onglets ont des sous-onglets (tabs)

### Graphiques Interactifs (Plotly)
```
Survol       → Info bulle
Zoom         → Sélectionner zone avec souris
Pan          → Shift + Drag
Reset        → Double-cliquer
Télécharger  → Icon "camera" (haut droit)
Basculer     → Cliquer sur label (affiche/cache)
```

### Performances
- Première charge: 3-5 secondes
- Navigation entre pages: Instantané
- Actualisation données: Automatique après notebook
- Graphiques lourds: <2 secondes chacun

### Personnalisation
Pour changer les couleurs/style:
1. Éditez `app.py`
2. Cherchez `st.markdown("""<style>""")`
3. Modifiez les couleurs HEX
4. Sauvegardez et actualisez l'app

---

## ❓ FAQ

### Q: L'app ne démarre pas
**R:** Lancez via PowerShell pour voir les erreurs
```powershell
streamlit run app.py
```

### Q: Les graphiques sont vides
**R:** Les données n'ont pas été générées
- Exécutez d'abord le notebook `kweek-test-notebook.ipynb`
- Puis relancez l'app

### Q: Comment modifier les données?
**R:** Les CSVs source sont modifiables directement
- Modifiez `restaurant_*.csv`
- Réexécutez le notebook
- L'app rechardera les données

### Q: Peut-on l'utiliser hors ligne?
**R:** Partiellement - Plotly en ligne nécessite une connexion
- Dashboard basique: OK hors ligne
- Graphiques: Nécessitent internet
- Solution: Installer plotly en mode offline (avancé)

### Q: Comment ajouter plus de produits?
**R:** Modifiez `restaurant_products.csv`
- Ajoutez une ligne
- Réexécutez le notebook
- Les prévisions seront générées

### Q: Peut-on déployer en ligne?
**R:** Oui, plusieurs options
- **Streamlit Cloud** (gratuit): cloud.streamlit.app
- **Heroku**: Payant mais simple
- **AWS/Azure**: Complet mais complexe
- Consultez `APP_STARTUP.md` pour les détails

---

## 📚 Ressources Supplémentaires

### Documentation dans le Projet
- **README.md** - Vue d'ensemble
- **INDEX.md** - Guide de navigation (tous fichiers)
- **TECHNICAL_DOCUMENTATION.md** - Formules ML
- **VERIFICATION_REPORT.md** - Tests et validation
- **EXECUTIVE_SUMMARY.md** - Résumé pour décideurs
- **APP_STARTUP.md** - Configuration avancée

### Liens Utiles
- Streamlit Docs: streamlit.io/docs
- Plotly Docs: plotly.com/python
- Pandas Docs: pandas.pydata.org

---

## ✅ Checklist Première Utilisation

- [ ] Installer Streamlit: `pip install streamlit plotly`
- [ ] Lancer l'app: Double-clic `RUN_APP.bat`
- [ ] Attendre `http://localhost:8501`
- [ ] Ouvrir dans navigateur
- [ ] Visiter **📈 Dashboard** (1 min)
- [ ] Jouer avec les graphiques (3 min)
- [ ] Consulter **🔮 Prévisions** (5 min)
- [ ] Vérifier **📦 Inventaire** (2 min)
- [ ] Explorer **👥 Clients RFM** (3 min)
- [ ] Télécharger un rapport depuis **📊 Rapports** (1 min)
- [ ] Revenir au Dashboard et explorer davantage
- [ ] Vous êtes maintenant expert! 🎉

---

## 🆘 Support

Besoin d'aide?
1. Vérifiez ce guide
2. Consultez **ℹ️ À Propos** dans l'app
3. Lisez la documentation complète
4. Testez sur une copie des données

---

**Bon usage! Profitez de votre interface KWEEK! 🚀**
