from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder \
    .appName("KafkaStreaming") \
    .config("spark.jars.packages","org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .getOrCreate()

# Read data from Kafka topic
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "TestTopic") \
    .load()

# Extract the value field from Kafka message (bytes -> string)
df = df.selectExpr("CAST(value AS STRING)")

# Print the output of the stream
query = df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Wait for the stream to finish
query.awaitTermination()
