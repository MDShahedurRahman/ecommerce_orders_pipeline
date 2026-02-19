from pyspark.sql.functions import col, to_date
from config import BRONZE_PATH, SILVER_PATH
from utils.helpers import ensure_dir


def run_silver_job(spark):
    print("Running Silver Cleaning Job...")

    ensure_dir(SILVER_PATH)

    df = spark.read.parquet(BRONZE_PATH)

    cleaned = (
        df.dropDuplicates(["order_id"])
    )

    return cleaned
