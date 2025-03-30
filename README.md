# Projet 7 - Formation IA Engineer d'OpenClassrooms

## Réalisez une analyse de sentiments grâce au Deep Learning

### Contexte

Dans le cadre d'une mission pour la compagnie aérienne Air Paradis, nous développons un prototype de solution d'intelligence artificielle capable d'anticiper les bad buzz sur les réseaux sociaux. L'objectif est de prédire le sentiment d'un tweet (positif ou négatif) en s'appuyant sur des modèles de Machine Learning.

L'API que nous développons permet d'exposer le meilleur modèle et de le rendre accessible via une interface utilisateur Streamlit. L'API reçoit un tweet en entrée et retourne une prédiction du sentiment associé.

En parallèle, ce projet intègre des pratiques MLOps, incluant le tracking des expérimentations avec MLflow, le déploiement via une solution Cloud Azure WebApp, et un suivi de la performance du modèle en production avec Azure Application Insights.


### Notebooks complets et commentés ci-dessous :

https://github.com/CelineLesur/OCR_IAEngineer_Projet7/blob/main/P7_EDA.ipynb

https://github.com/CelineLesur/OCR_IAEngineer_Projet7/blob/main/P7_modele_base.ipynb

https://github.com/CelineLesur/OCR_IAEngineer_Projet7/blob/main/P7_modele_avance.ipynb


### Découpage des dossiers :
📂 /

main.py → Code principal de l’API FastAPI

startup.sh → Code de démarrage d'Azure

requirements.txt → Liste des packages nécessaires

oryx-manifest.toml → Métadonnées sur le déploiement

README.md → Explication du contexte du projet, de la hierarchie des fichiers et des packages utilisés

📂 notebooks/

P7_EDA.ipynb → Analyse exploratoire des données

P7_modele_base.ipynb → Entraînement et évaluation du modèle de base : régression logistique

P7_modele_avance.ipynb → Entraînement et évaluation de modèles de RNN (sans embeddings, avec embeddings GloVe, avec embeddings Fastext) et ModernBERT

📂 test/

test_api.py → Tests unitaires

### Installation

#### Prerequisites

Python 3.11

#### Dependencies

- fastapi - version : 0.115.11
- torch (https://download.pytorch.org/whl/cpu)
- transformers - version : 4.49.0
- azure-storage-blob
- uvicorn
