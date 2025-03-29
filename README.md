# Projet 7 - Formation IA Engineer d'OpenClassrooms

## Réalisez une analyse de sentiments grâce au Deep Learning

Dans le cadre d'une mission pour la compagnie aérienne Air Paradis, nous développons un prototype de solution d'intelligence artificielle capable d'anticiper les bad buzz sur les réseaux sociaux. L'objectif est de prédire le sentiment d'un tweet (positif ou négatif) en s'appuyant sur des modèles de Machine Learning.

L'API que nous développons permet d'exposer le meilleur modèle et de le rendre accessible via une interface utilisateur Streamlit. L'API reçoit un tweet en entrée et retourne une prédiction du sentiment associé.

En parallèle, ce projet intègre des pratiques MLOps, incluant le tracking des expérimentations avec MLflow, le déploiement via une solution Cloud Azure WebApp, et un suivi de la performance du modèle en production avec Azure Application Insights.


Notebooks complets et commentés ci-dessous :

https://github.com/CelineLesur/OCR_IAEngineer_Projet7/blob/main/P7_EDA.ipynb

https://github.com/CelineLesur/OCR_IAEngineer_Projet7/blob/main/P7_modele_base.ipynb

https://github.com/CelineLesur/OCR_IAEngineer_Projet7/blob/main/P7_modele_avance.ipynb


Découpage des dossiers :
📂 /

app.py → Code principal de l’API Flask/FastAPI

model/ → Contient le modèle de prédiction (fichiers .pkl ou .h5)

requirements.txt → Liste des packages nécessaires

config.py → Paramètres de configuration

📂 notebooks/

exploration.ipynb → Analyse exploratoire des données

train_model.ipynb → Entraînement et évaluation des modèles

📂 test/

mlflow_tracking/ → Gestion des expériences avec MLflow

ci_cd/ → Scripts pour le pipeline CI/CD (GitHub Actions, tests unitaires)

monitoring/ → Intégration de la surveillance avec Azure Application Insights
