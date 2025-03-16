#!/bin/bash

# Vérifier si l'environnement est Windows ou Linux/Mac
if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "darwin"* ]]; then
    # Si c'est Linux/Mac, activer l'environnement virtuel (Linux/Mac)
    source venv/bin/activate
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Si c'est Windows, activer l'environnement virtuel avec activate.ps1 (PowerShell)
    source venv/Scripts/activate
fi

# Vérification de l'environnement virtuel
echo "Environnement virtuel activé : $(which python)"

# Démarrer l'application FastAPI avec Uvicorn
echo "Démarrage de l'application FastAPI avec uvicorn..."
uvicorn main:app --reload