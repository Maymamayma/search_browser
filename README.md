# Search Browser

Mini moteur de recherche utilisant un crawler asynchrone, un index inversé
et une API FastAPI.

## Installation
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Lancer l'API
python run.py

## Dossiers
- crawler/ : récupère les pages web
- indexer/ : indexation et scoring
- api/ : backend FastAPI
- frontend/ : interface utilisateur
