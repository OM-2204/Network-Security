import sys
import os

import certifi
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()
mongo_db_url = os.getenv("MONGO_DB_URL")

import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.staticfiles import StaticFiles
from uvicorn import run as app_run
from fastapi.responses import Response, HTMLResponse
from starlette.responses import RedirectResponse
import pandas as pd

from networksecurity.utils.main_utils.utils import load_object
from networksecurity.utils.ml_utils.model.estimator import NetworkModel

client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

from networksecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI(
    title="NetGuard AI — Network Security Intelligence",
    description="ML-powered network intrusion detection using Random Forest on NSL-KDD features.",
    version="1.0.0",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="./templates")

# Serve the dashboard UI at "/"
@app.get("/", response_class=HTMLResponse, tags=["UI"])
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Redirect /dashboard to root as well
@app.get("/dashboard", response_class=HTMLResponse, include_in_schema=False)
async def dashboard(request: Request):
    return RedirectResponse(url="/")

@app.get("/train", tags=["ML Pipeline"])
async def train_route():
    """
    Trigger the full training pipeline:
    Data Ingestion → Validation → Transformation → Model Training → Evaluation
    """
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training is successful")
    except Exception as e:
        raise NetworkSecurityException(e, sys)

@app.post("/predict", tags=["ML Pipeline"])
async def predict_route(request: Request, file: UploadFile = File(...)):
    """
    Upload a CSV file with network traffic features.
    Returns an HTML page with the prediction results table.
    """
    try:
        df = pd.read_csv(file.file)
        if "Result" in df.columns:
            df = df.drop(columns=["Result"])
            
        preprocessor = load_object("final_model/preprocessor.pkl")
        final_model = load_object("final_model/model.pkl")
        network_model = NetworkModel(preprocessor=preprocessor, model=final_model)
        y_pred = network_model.predict(df)
        df['predicted_column'] = y_pred

        if "Result" in df.columns:
            df = df.drop(columns=["Result"])

        # Save output
        os.makedirs('prediction_output', exist_ok=True)
        df.to_csv('prediction_output/output.csv', index=False)

        table_html = df.to_html(classes='table', border=0, index=False)
        return templates.TemplateResponse(
            "table.html",
            {"request": request, "table": table_html}
        )
    except Exception as e:
        raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=8000)
