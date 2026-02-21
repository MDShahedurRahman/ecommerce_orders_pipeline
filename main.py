from utils.spark_session import get_spark_session

from jobs.bronze_ingestion import run_bronze_job
from jobs.silver_cleaning import run_silver_job
from jobs.fraud_detection import run_fraud_detection
from jobs.gold_star_schema import run_gold_job
from jobs.business_kpis import run_kpi_job


def main():
    spark = get_spark_session()

    run_bronze_job(spark)
    run_silver_job(spark)

    spark.stop()
    print("Pipeline Completed Successfully!")


if __name__ == "__main__":
    main()
