'''
brew install openjdk@17
pip install pyspark
export JAVA_HOME=/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home
'''
import os
os.environ['SPARK_LOCAL_IP'] = '192.168.0.191' 
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv('/Users/scottalexander/Downloads/Govt_Units_2024_Final/Special District-Table 1.csv', header=True)

df.createOrReplaceTempView("tableA")

spark.sql("SELECT count(*) from tableA").show()