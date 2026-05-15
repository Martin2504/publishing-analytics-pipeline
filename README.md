# Publishing Analytics Pipeline

A production-style data pipeline and API system built in Python to simulate a real-world publishing analytics platform.

## 🚀 Overview

This project ingests, processes, validates, and stores data related to book sales, authors, and genres.  
It exposes clean, structured insights through a REST API.

The goal is to replicate real-world backend data engineering workflows.

---

## 🛠️ Tech Stack

- Python
- Pandas (data processing)
- FastAPI (API layer)
- SQLAlchemy (database ORM)
- SQLite / PostgreSQL (database)
- Pytest (testing)

---

## 📂 Project Structure
```
publishing-analytics-pipeline/
├── data/
│   ├── raw/          # raw input data (CSV files)
│   ├── processed/    # cleaned/transformed data
├── pipeline/         # ingestion, cleaning, validation logic
├── api/              # FastAPI application
├── db/               # database models and connection
├── tests/            # test suite
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\Activate
pip install -r requirements.txt # Install Dependencies
python run_pipeline.py # Run pipeline
```
---

## 🌐 Running the API

Start the FastAPI server:

```bash
uvicorn api.main:app --reload
```

Access the API at:

- Base URL: http://127.0.0.1:8000  
- Swagger Docs: http://127.0.0.1:8000/docs  

### Available Endpoints

- `GET /books` → Retrieve all books  
- `GET /books/{id}` → Retrieve a specific book  
- `POST /ingest` → Trigger the full data pipeline  
- `GET /analytics/top-selling` → Get top-selling books  

---

## 🧪 Running Tests

Run all tests using:

```bash
pytest
```

Tests include:

- Data cleaning logic  
- Validation rules  
- API endpoint testing 