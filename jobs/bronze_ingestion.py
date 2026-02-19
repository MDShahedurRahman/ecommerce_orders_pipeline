from utils.schema import order_schema
from utils.helpers import ensure_dir
from config import BRONZE_PATH, SOURCE_FILE


def run_bronze_job(spark):
    print("Running Bronze Ingestion Job...")

    ensure_dir(BRONZE_PATH)

    df = (
        spark.read.format("csv")
        .option("header", True)
        .schema(order_schema())
        .load(SOURCE_FILE)
    )

    return df
