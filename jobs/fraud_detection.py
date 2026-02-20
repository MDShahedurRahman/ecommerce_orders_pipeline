from pyspark.sql.functions import when, col
from config import SILVER_PATH
from utils.helpers import ensure_dir


def run_fraud_detection(spark):
    print("Running Fraud Detection Job...")

    df = spark.read.parquet(SILVER_PATH)

    flagged = df.withColumn(
        "fraud_flag"
    )

    return flagged
