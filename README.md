# 🕌 Ma Foi — Application de suivi islamique (PWA)

Application web progressive (PWA) installable sur iPhone sans passer par l'App Store.

## 📱 Fonctionnalités
- **Salat** : suivi des 5 prières avec horaires géolocalisés (API Aladhan)
- **Dhikr** : compteur de wird quotidien (Subhânallah, Alhamdulillah, Allahou Akbar, La ilaha illallah)
- **Coran** : lecture des 114 sourates avec texte arabe, phonétique et traduction française
- **Objectifs** : suivi d'objectifs spirituels quotidiens et à long terme
- **Rappels** : configuration des rappels de prière
- **Stats** : progression, séries et badges

---

## 🚀 Mise en ligne sur GitHub Pages (étape par étape)

### Étape 1 — Créer le dépôt GitHub
1. Va sur **github.com** et connecte-toi
2. Clique sur le bouton vert **"New"** (nouveau dépôt)
3. Nomme-le : `ma-foi-app` (ou ce que tu veux)
4. Coche **"Public"** (obligatoire pour GitHub Pages gratuit)
5. Clique sur **"Create repository"**

### Étape 2 — Uploader les fichiers
1. Sur la page de ton dépôt vide, clique **"uploading an existing file"**
2. Glisse-dépose ces fichiers (tous en même temps) :
   - `index.html`
   - `manifest.json`
   - `sw.js`
3. Pour le dossier `icons/`, clique **"choose your files"** et sélectionne :
   - `icons/icon-192.png`
   - `icons/icon-512.png`
   ⚠️ GitHub ne permet pas d'uploader des dossiers via l'interface web.
   Les icônes doivent être uploadées à la racine ou via l'étape ci-dessous.
4. Écris un message de commit : `"Première version de Ma Foi"`
5. Clique **"Commit changes"**

### Étape 3 — Activer GitHub Pages
1. Dans ton dépôt, clique sur **"Settings"** (onglet en haut)
2. Dans le menu gauche, clique **"Pages"**
3. Sous "Source", sélectionne **"Deploy from a branch"**
4. Sélectionne la branche **"main"** et le dossier **"/ (root)"**
5. Clique **"Save"**
6. Attends 1-2 minutes ⏳

### Étape 4 — Accéder à ton app
GitHub Pages te donnera une URL du style :
```
https://TON-USERNAME.github.io/ma-foi-app/
```
Tu la trouveras dans Settings → Pages.

---

## 📲 Installer sur iPhone

1. Ouvre l'URL dans **Safari** (pas Chrome, Safari uniquement pour iOS)
2. Appuie sur le bouton **Partager** (carré avec une flèche ↑)
3. Défile vers le bas et appuie sur **"Sur l'écran d'accueil"**
4. Appuie sur **"Ajouter"** en haut à droite
5. ✅ L'application apparaît sur ton écran d'accueil !

---

## ⚠️ Note sur les icônes
Si les icônes ne s'affichent pas, c'est parce que GitHub ne permet pas d'uploader
des sous-dossiers via l'interface web. Dans ce cas :
- Utilise l'application GitHub Desktop (gratuite) pour uploader le dossier `icons/`
- Ou modifie `manifest.json` et remplace les chemins des icônes par les URLs complètes

---

## 🔧 APIs utilisées
- **Aladhan.com** : horaires de prière selon ta position GPS
- **AlQuran.cloud** : texte arabe, phonétique et traduction française du Coran
- **Nominatim (OpenStreetMap)** : nom de ta ville via les coordonnées GPS

Toutes ces APIs sont **gratuites** et ne nécessitent pas de clé.
