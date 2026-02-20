from pyspark.sql.functions import when, col
from config import SILVER_PATH
from utils.helpers import ensure_dir


def run_fraud_detection(spark):
    print("Running Fraud Detection Job...")

    df = spark.read.parquet(SILVER_PATH)

    flagged = df.withColumn(
        "fraud_flag",
        when(col("total_amount") > 5000, "HIGH_VALUE_ORDER").otherwise("NORMAL")
    )

    fraud_path = "output/silver/fraud_flagged/"
    ensure_dir(fraud_path)

    flagged.write.mode("overwrite").parquet(fraud_path)

    print("Fraud Detection Output Saved.")
    return flagged
