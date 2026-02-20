from config import SILVER_PATH, GOLD_PATH
from utils.helpers import ensure_dir


def run_gold_job(spark):
    print("Running Gold Star Schema Job...")

    ensure_dir(GOLD_PATH)

    df = spark.read.parquet(SILVER_PATH)

    dim_customer = df.select(
        "customer_id", "customer_name", "country"
    ).dropDuplicates()

    dim_product = df.select(
        "product", "category", "price"
    ).dropDuplicates()
