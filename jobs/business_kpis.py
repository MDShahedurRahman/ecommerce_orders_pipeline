from pyspark.sql.functions import sum, desc
from config import GOLD_PATH, REPORT_PATH
from utils.helpers import ensure_dir


def run_kpi_job(spark):
    print("Running Business KPI Job...")

    ensure_dir(REPORT_PATH)

    fact = spark.read.parquet(GOLD_PATH + "fact_orders/")

    revenue_by_payment = (
        fact.groupBy("payment_type")
        .agg(sum("total_amount").alias("total_revenue"))
        .orderBy(desc("total_revenue"))
    )

    revenue_by_payment.show()

    revenue_by_payment.write.mode("overwrite").csv(
        REPORT_PATH + "revenue_by_payment/",
        header=True
    )

    print("KPI Reports Generated Successfully.")
