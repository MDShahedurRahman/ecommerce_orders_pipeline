from pyspark.sql.types import (
    StructType, StructField,
    StringType, IntegerType,
    DoubleType, DateType
)


def order_schema():
    return StructType([
        StructField("order_id", IntegerType(), True),
        StructField("customer_id", StringType(), True),
        StructField("customer_name", StringType(), True),
        StructField("product", StringType(), True),
        StructField("category", StringType(), True),
        StructField("quantity", IntegerType(), True),
        StructField("price", DoubleType(), True),
        StructField("order_date", StringType(), True),
        StructField("country", StringType(), True),
        StructField("payment_type", StringType(), True)
    ])
