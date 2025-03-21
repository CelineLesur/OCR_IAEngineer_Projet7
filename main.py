from fastapi import FastAPI,Request
import torch
# import uvicorn
import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from contextlib import asynccontextmanager
from azure.storage.blob import BlobServiceClient

# Configuration Azure
AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=stockp7;AccountKey=/pTx40p/d/Eu3Sv82DqddLJqRjc4f2HwEC2ZL0pKIztSX87XdhXEztc2GtFRa6J5CTTsgLC2anTQ+AStsaPofA==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "contp7"
MODEL_BLOB_PREFIX = ""
LOCAL_MODEL_DIR = "D:/tutorial-env/OCR/Projet7/APImodel"

def download_model_from_blob():
    # Initialiser le client BlobService
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    # Télécharger chaque fichier du modèle
    blob_list = container_client.list_blobs(name_starts_with=MODEL_BLOB_PREFIX)
    for blob in blob_list:
        blob_client = container_client.get_blob_client(blob)
        # Créer les répertoires locaux si nécessaire
        local_file_path = os.path.join(LOCAL_MODEL_DIR, os.path.relpath(blob.name, MODEL_BLOB_PREFIX))
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
        # Télécharger le fichier
        with open(local_file_path, "wb") as f:
            f.write(blob_client.download_blob().readall())

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Chargement du meilleur modèle et ses poids entrainés depuis le container AZURE
    # (avant le yield, s'effectue avant le démarrage +- initialisation)
    download_model_from_blob()
    app.state.tokenizer = AutoTokenizer.from_pretrained("answerdotai/ModernBERT-base")
    app.state.model = AutoModelForSequenceClassification.from_pretrained(LOCAL_MODEL_DIR, num_labels=2)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return "Aucun tweet détecté - Classification impossible"


@app.get("/{tweet}")
def read_tweet(tweet: str):
    return {"tweet": tweet}


@app.post("/predict")
async def predict(request: Request, tweet: str):
    # Pré-processing des données
    encodings = request.app.state.tokenizer(tweet, padding=True, truncation=True, max_length=30, return_tensors="pt")

    # Prédiction
    with torch.no_grad() :
        outputs = request.app.state.model(**encodings)

    logits = outputs.logits
    prediction = torch.argmax(logits,dim=1).item()

    return {"prediction": prediction,
           "probabilité": logits}

if __name__=='__main__' :
    import uvicorn
    port=int(os.getenv("PORT",8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
