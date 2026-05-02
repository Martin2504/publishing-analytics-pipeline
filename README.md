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
Publishing Analytics Pipeline
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
python test_env.py # Verify Setup