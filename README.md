<div align="center">

```
███╗   ██╗███████╗████████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
██╔██╗ ██║█████╗     ██║   ██║  ███╗██║   ██║███████║██████╔╝██║  ██║
██║╚██╗██║██╔══╝     ██║   ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
██║ ╚████║███████╗   ██║   ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝
```

# 🛡️ NetGuard AI — Network Security Intelligence Platform

**End-to-End MLOps Pipeline for Network Intrusion Detection**  
**FastAPI · Scikit-learn · MongoDB · MLflow · Docker · AWS EC2**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![MLflow](https://img.shields.io/badge/MLflow-3.5.1-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)](https://mlflow.org)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Latest-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Overview

**NetGuard AI** is a production-grade, end-to-end **MLOps system** for detecting network intrusions and classifying malicious traffic. Built on the **NSL-KDD dataset**, it implements a complete **ETL pipeline**, automated ML training with **Random Forest**, and **CI/CD deployment to AWS EC2** via Docker and GitHub Actions.

The system achieves **99.14% F1-score** across experiment runs tracked on **MLflow + DagsHub**, and ships a professional **cyberpunk-themed web dashboard** for real-time threat prediction.

> **TL;DR:** CSV network traffic → ETL → Train → Predict → Deploy to AWS. Every stage automated.

---

## 🖥️ UI Preview

### Dashboard — NetGuard AI
![NetGuard AI Dashboard](assets\dashboard.png)

> Dark-mode dashboard with drag-and-drop CSV upload, 5-stage pipeline visualizer, live prediction counter, and row-by-row threat classification results.

---

## 📊 MLflow Experiment Tracking

### Experiment Runs on DagsHub
![MLflow Experiments](assets\experiments.png)

| Run | F1 Score | Precision | Recall |
|-----|----------|-----------|--------|
| handsome-el... | **0.9914** | **0.9892** | **0.9936** |
| gentle-cow-6... | 0.9910 | 0.9891 | 0.9928 |
| respected-sh... | 0.9733 | 0.9680 | 0.9787 |
| adaptable-sh... | 0.9739 | 0.9666 | 0.9814 |

### Parallel Coordinates Plot — MLflow UI
![MLflow Parallel Coordinates](assets\mlflow_parallel.png)

> 4 runs compared across F1, Precision, and Recall. Top 2 runs (red) consistently outperform across all three metrics.

---

## 🏗️ Full System Architecture

```
╔══════════════════════════════════════════════════════════════════════╗
║                        ETL PIPELINE                                  ║
║                  [ Extract · Transform · Load ]                      ║
║                                                                      ║
║  SOURCE                  TRANSFORM               DESTINATION         ║
║  ┌─────────────┐        ┌─────────────┐        ┌──────────────┐     ║
║  │ CSV Dataset │        │ Basic Pre-  │        │ MongoDB Atlas│     ║
║  │ APIs        │ ─────► │ processing  │ ─────► │ AWS DynamoDB │     ║
║  │ S3 Buckets  │        │ Clean Data  │        │ MySQL        │     ║
║  │ Paid APIs   │        │ → JSON      │        │ S3 Buckets   │     ║
║  │ Internal DB │        └─────────────┘        └──────────────┘     ║
║  └─────────────┘                                                     ║
╚══════════════════════════════════════════════════════════════════════╝
                                   │
                                   ▼
╔══════════════════════════════════════════════════════════════════════╗
║                     ML TRAINING PIPELINE                             ║
║                                                                      ║
║  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────┐  ║
║  │  Data    │  │  Data    │  │  Data    │  │  Model   │  │Model │  ║
║  │Ingestion │─►│Validation│─►│Transform │─►│ Trainer  │─►│ Eval │  ║
║  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  └──┬───┘  ║
║       │             │             │              │            │      ║
║  raw.csv       drift_report  preprocessing   model.pkl   Accepted?  ║
║  train.csv     valid paths    .pkl            metrics    Yes → Push  ║
║  test.csv                    train.npy                   No  → None  ║
║                               test.npy                               ║
╚══════════════════════════════════════════════════════════════════════╝
                                   │
                                   ▼
╔══════════════════════════════════════════════════════════════════════╗
║                     CI/CD DEPLOYMENT                                 ║
║                                                                      ║
║  GitHub Push ──► GitHub Actions ──► Docker Build ──► AWS ECR        ║
║                       CI/CD             Image          Registry      ║
║                         │                                  │         ║
║                    App Runner ◄──────────────── AWS EC2 ◄──┘        ║
║                   (CD Pipeline)                 Instance             ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## ⚙️ Pipeline Deep Dive

### 1️⃣ Data Ingestion

Pulls raw data from **MongoDB Atlas**, exports to a feature store, drops irrelevant columns, and splits into train/test CSVs — all timestamped.

```
Config: Ingestion Dir · Feature Store Path · Train/Test Path · Split Ratio · Collection Name

MongoDB Atlas
     │
     ▼
Initiate Data Ingestion
     ├──► Export to Feature Store  →  raw.csv  (timestamped)
     ├──► Drop Columns             (schema file)
     └──► Split Data               →  train.csv + test.csv  (ingested/)
```

**Output Artifact:** `raw.csv` · `train.csv` · `test.csv`

---

### 2️⃣ Data Validation

Three checks ensure data quality before training:

```
① Same Schema       →  Validate same number of features (10 features expected)
② Data Drift        →  Compare train vs test distributions → drift report
③ Column Validation →  Validate column count + numerical columns exist

Data Ingestion Artifact
     │
     ▼
Read Data (train.csv + test.csv)
     ├──► Validate Number of Columns  ──►  Train Status / Test Status
     ├──► Numerical Columns Exist     ──►  Train Status / Test Status
     └──► Detect Dataset Drift        ──►  Drift Status
               ├── True  ──► Validation Status ──► Artifact ✅
               └── False ──► Validation Error  ❌
```

**Output Artifact:** validation status · valid/invalid train & test paths · drift report

---

### 3️⃣ Data Transformation

Handles missing values, scales features, and balances class imbalance using **SMOTE-Tomek**.

```
Data Validation Artifact
     │
     ▼
Read Data  →  Drop Target Column  →  Target Value Mapping
     │
     ├──► Handle Missing Values
     │         ├── KNN Imputer    (fills NaN using K-nearest neighbors)
     │         └── Simple Imputer (fallback)
     │
     ├──► Robust Scaler           (scale features, outlier-resistant)
     │
     ├──► SMOTE-Tomek             (balance imbalanced classes)
     │         ├── fit_transform  →  Train data
     │         └── transform      →  Test data
     │
     └──► Save Preprocessor Object  →  preprocessing.pkl
               Output: train.npy + test.npy
```

**Output Artifact:** `train.npy` · `test.npy` · `preprocessing.pkl`

---

### 4️⃣ Model Trainer

Trains a **Random Forest classifier**, selects the best model if it meets the expected accuracy threshold, and saves it as a `NetworkModel` object.

```
Data Transformation Artifact
     │
     ▼
Load numpy arrays (train.npy + test.npy)
     │
     ├──► Split → X_train · y_train · X_test · y_test
     │
     ├──► Model Factory → get_best_model()
     │         └── Calculate Metrics (F1, Precision, Recall)
     │
     ├──► best_score >= expected_accuracy?
     │         ├── YES → NetworkModel(preprocessing.pkl + model.pkl)
     │         │              └── Save → model.pkl + metric artifact
     │         └── NO  → Exception: No best model found
     │
     └──► Model Trainer Artifact
```

**Output Artifact:** `model.pkl` · `preprocessing.pkl` · metric artifact

---

### 5️⃣ Model Evaluation → Model Pusher

```
Model Evaluation
     ├── Model Accepted? ──► YES ──► Model Pusher ──► Cloud / AWS / Azure
     └── Model Accepted? ──► NO  ──► None (no push)
```

---

## 🐳 CI/CD — AWS EC2 Deployment

Full automated deployment via **GitHub Actions + Docker + AWS**:

```
① Developer pushes code to GitHub
          │
          ▼
② GitHub Actions triggers CI pipeline
   └── Runs tests, linting
          │
          ▼
③ Docker Image built from Dockerfile
          │
          ▼
④ Image pushed to AWS ECR (Elastic Container Registry)
          │
          ▼
⑤ AWS EC2 instance pulls latest image via App Runner (CD)
          │
          ▼
⑥ FastAPI app live on EC2 — serving predictions
```

**GitHub Secrets required:**

| Secret | Description |
|--------|-------------|
| `AWS_ACCESS_KEY_ID` | AWS IAM access key |
| `AWS_SECRET_ACCESS_KEY` | AWS IAM secret key |
| `AWS_DEFAULT_REGION` | e.g. `us-east-1` |
| `ECR_REPOSITORY_NAME` | Your ECR repo name |
| `AWS_ECR_LOGIN_URI` | ECR login URI |

---

## 📁 Project Structure

```
Network-Security/
│
├── app.py                              # FastAPI entry point
├── requirements.txt                    # Python dependencies
├── Dockerfile                          # Docker image config
├── .env                                # Environment variables (not committed)
├── .github/
│   └── workflows/main.yaml             # GitHub Actions CI/CD pipeline
│
├── templates/
│   ├── index.html                      # Dashboard UI
│   └── table.html                      # Prediction results page
│
├── networksecurity/
│   ├── components/
│   │   ├── data_ingestion.py           # Stage 1: MongoDB → Feature Store → Split
│   │   ├── data_validation.py          # Stage 2: Schema + Drift detection
│   │   ├── data_transformation.py      # Stage 3: KNN Impute + SMOTE + Scale
│   │   ├── model_trainer.py            # Stage 4: Random Forest + best model selection
│   │   └── model_evaluation.py         # Stage 5: Metrics + MLflow logging
│   │
│   ├── pipeline/
│   │   └── training_pipeline.py        # Orchestrates all 5 stages
│   │
│   ├── constant/
│   │   └── training_pipeline.py        # DB names, file paths, constants
│   │
│   ├── entity/                         # Config & artifact dataclasses
│   ├── exception/                      # Custom exception handler
│   ├── logging/                        # Logger setup
│   └── utils/
│       ├── main_utils/utils.py         # load_object / save_object (pkl, yaml)
│       └── ml_utils/model/estimator.py # NetworkModel wrapper class
│
├── final_model/                        # Auto-created after training
│   ├── model.pkl
│   └── preprocessor.pkl
│
└── prediction_output/                  # Auto-created after prediction
    └── output.csv
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔁 **ETL Pipeline** | Extract from CSV/APIs/S3 → preprocess → load to MongoDB Atlas |
| 🧪 **Data Validation** | Schema check, data drift detection (3 validation checks) |
| ⚗️ **Data Transformation** | KNN Imputer, Robust Scaler, SMOTE-Tomek class balancing |
| 🤖 **Model Training** | Random Forest with automated best-model selection gate |
| 📊 **Experiment Tracking** | MLflow 3.5.1 + DagsHub — 4 runs with full metrics |
| 🌐 **FastAPI Backend** | Production REST API with Swagger at `/docs` |
| 🖥️ **Professional Dashboard** | Cyberpunk dark UI with drag-and-drop CSV prediction |
| 🐳 **Docker + CI/CD** | GitHub Actions → AWS ECR → AWS EC2 auto-deploy |
| 📁 **CSV Prediction** | Upload NSL-KDD CSV → row-by-row ✅ Safe / ⚠️ Threat labels |
| ✅ **99.14% F1-Score** | Best run across 4 MLflow-tracked experiments |

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **API Framework** | FastAPI + Uvicorn |
| **ML Model** | Scikit-learn — Random Forest Classifier |
| **Imbalance Handling** | SMOTE-Tomek (imbalanced-learn) |
| **Missing Values** | KNN Imputer + Simple Imputer |
| **Feature Scaling** | Robust Scaler |
| **Data Processing** | Pandas, NumPy |
| **Experiment Tracking** | MLflow 3.5.1 + DagsHub |
| **Database** | MongoDB Atlas (PyMongo) |
| **Containerization** | Docker |
| **CI/CD** | GitHub Actions |
| **Cloud Registry** | AWS ECR (Elastic Container Registry) |
| **Cloud Compute** | AWS EC2 + App Runner |
| **Dataset** | NSL-KDD Network Intrusion Dataset |
| **Frontend** | Jinja2 Templates + Vanilla JS |

---

## 🚀 Getting Started (Local)

### 1. Clone & Setup

```bash
git clone https://github.com/OM-2204/Network-Security.git
cd Network-Security

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Create .env file
echo "MONGO_DB_URL=mongodb+srv://<user>:<pass>@cluster.mongodb.net/" > .env
```

### 3. Run

```bash
python app.py
# OR
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Open `http://localhost:8000` · API docs at `http://localhost:8000/docs`

---

## 🐳 Docker (Local)

```bash
docker build -t netguard-ai .
docker run -p 8000:8000 --env-file .env netguard-ai
```

---

## 🔁 Usage Guide

| Action | Steps |
|--------|-------|
| **Train** | Dashboard → "Launch Training Pipeline" → Confirm modal → wait for all 5 stages |
| **Predict** | Upload `.csv` → "Analyze Traffic" → view Safe/Threat per row → Download CSV |
| **API Docs** | `http://localhost:8000/docs` |
| **MLflow UI** | `mlflow ui` in terminal → `http://localhost:5000` |

> ⚠️ You must run training before predictions — `final_model/` must exist.

---

## 📈 Model Performance

```
Best Run (handsome-el...):

F1 Score   →  0.9914  ████████████████████░  99.14%
Precision  →  0.9892  ████████████████████░  98.92%
Recall     →  0.9936  ████████████████████░  99.36%
```

All runs tracked and comparable at [DagsHub MLflow UI](https://dagshub.com).

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m 'Add feature'`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

[MIT License](LICENSE)

---

## 👤 Author

**OM-2204**

[![GitHub](https://img.shields.io/badge/GitHub-OM--2204-181717?style=for-the-badge&logo=github)](https://github.com/OM-2204)

---

<div align="center">

⭐ **Star this repo if it helped you!** ⭐

Built with 🛡️ for network security & MLOps enthusiasts

</div>
