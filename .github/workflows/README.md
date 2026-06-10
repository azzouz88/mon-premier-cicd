[![Ma Premiere CI](https://github.com/azzouz88/mon-premier-cicd/actions/workflows/pipeline.yml/badge.svg)](https://github.com/azzouz88/mon-premier-cicd/actions/workflows/pipeline.yml)
# 🧮 Projet Calculatrice Automatisée - Stack CI/CD

[ICI TU COLLES LE LIEN COPIÉ SUR GITHUB]

Ce projet est une application web de calculatrice développée en Python avec **Streamlit**, mettant en œuvre un pipeline complet de **CI/CD (Intégration et Déploiement Continus)**.

## 🚀 Architecture de l'Infrastructure

### 1. Intégration Continue (CI) - GitHub Actions
* **Déclencheur** : Automatique à chaque `git push` sur la branche `main`.
* **Matrice de Tests (Matrix)** : Exécution parallèle des tests sur les versions **Python 3.9, 3.10 et 3.11** sur un runner Ubuntu virtuel.
* **Qualité du code** : Validation automatique de la logique métier via des tests unitaires configurés avec `pytest`.

### 2. Déploiement Continu (CD) - Streamlit Cloud
* **Déploiement automatisé** : Dès que la CI passe au vert, l'application cloud se met à jour en production sans intervention humaine.
* **Sécurité (Secrets)** : Gestion et injection des variables d'environnement chiffrées via les **GitHub Secrets** pour simuler une connexion API sécurisée.