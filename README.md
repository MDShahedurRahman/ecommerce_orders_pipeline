# Smart E-Commerce Orders Data Engineering Pipeline (PySpark)

A full end-to-end **Data Engineering Pipeline project** built using **PySpark** and a modern **Bronze → Silver → Gold** layered architecture.

This project simulates how real-world companies process raw e-commerce transaction data into clean analytics-ready datasets, build Star Schema models, generate KPI reports, and detect fraud patterns.

It is designed as a strong portfolio project for Data Engineering roles.

---

## 🚀 Project Overview

This pipeline processes raw online order data and performs:

- Data ingestion from CSV (Bronze Layer)
- Cleaning and transformation (Silver Layer)
- Fraud detection logic
- Star Schema modeling (Gold Layer)
- Business KPI reporting for analytics

The output datasets are stored in **Parquet format**, which is widely used in production data lakes.

---

## ✅ Key Features

- Ingest raw e-commerce transaction data from CSV
- Store raw data into **Bronze Parquet layer**
- Clean, standardize, and enrich data into **Silver layer**
- Add calculated fields such as `total_amount`
- Detect high-value orders with fraud flagging
- Build a complete **Star Schema** (dim + fact tables)
- Generate revenue KPI reports
- Modular job-based PySpark architecture
- Professional GitHub commit workflow (50 commits)

---

## 🏗 Architecture: Bronze → Silver → Gold

| Layer   | Purpose |
|--------|---------|
| Bronze | Raw ingestion from source systems |
| Silver | Cleaned and transformed datasets |
| Gold   | Analytics-ready Star Schema + KPIs |

---

## 📂 Project Structure

```
ecommerce_orders_pipeline/
│
├── main.py
├── config.py
├── requirements.txt
│
├── data/
│ └── orders.csv
│
├── jobs/
│ ├── bronze_ingestion.py
│ ├── silver_cleaning.py
│ ├── fraud_detection.py
│ ├── gold_star_schema.py
│ └── business_kpis.py
│
├── utils/
│ ├── spark_session.py
│ ├── schema.py
│ └── helpers.py
│
└── output/
├── bronze/
├── silver/
├── gold/
└── reports/
```

---

## ⚙️ Tech Stack

- Python 3.9+
- Apache Spark (PySpark)
- Parquet Data Lake Storage
- Layered Data Engineering Design
- Star Schema Modeling
- Business Analytics Queries

---

## 📌 Dataset Example

Sample input file:

`data/orders.csv`

```csv
order_id,customer_id,customer_name,product,category,quantity,price,order_date,country,payment_type
1,C001,John Smith,Laptop,Electronics,1,1200,2025-01-05,USA,Credit Card
2,C002,Amina Rahman,Phone,Electronics,2,800,2025-01-06,Canada,PayPal
3,C003,Sarah Lee,Shoes,Fashion,5,120,2025-01-08,USA,Debit Card
4,C004,Mohammed Ali,TV,Electronics,1,3000,2025-01-10,UK,Credit Card
5,C005,Raj Patel,Watch,Fashion,10,600,2025-01-12,India,Cash

---
