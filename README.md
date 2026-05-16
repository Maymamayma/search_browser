# Search Browser

A mini search engine using an asynchronous crawler, an inverted index, and a FastAPI API.

## Installation
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Run the API
python run.py

## Folders
- crawler/ : fetches web pages
- indexer/ : indexation et scoring
- api/ : backend FastAPI
- frontend/ : user interface
