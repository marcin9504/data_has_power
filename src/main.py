import json

import pyspark.sql.functions as f
from pyspark import SQLContext
from pyspark import SparkFiles
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, StructType, StructField


# docker exec -it data_has_power-spark-1 spark-submit /home/src/main.py
def main():
    spark = SparkSession.builder.getOrCreate()
    sc = spark.sparkContext
    sql_context = SQLContext(sc)

    url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"

    sc.addFile(url)

    dataset = spark.read.csv(SparkFiles.get("titanic.csv"), header=True)

    # dataset.show()

    def get_percentage_survived(df, group_by=None):
        if group_by is None:
            return 100 * df.select(f.avg(f.col("Survived"))).collect()[0][0]
        else:
            return [json.loads(row) for row in df.groupby(f.col(group_by)).agg(
                (100 * f.avg(f.col("Survived"))).alias("percentage")).orderBy(
                f.asc(f.col(group_by))).toJSON().collect()]

    results = []

    # 1. jaki procent dzieci (dziecko < 18 lat) przeżył katastrofę
    under_18 = dataset.filter(f.col("Age") < 18)
    res = get_percentage_survived(under_18)
    results.append((1, str(res)))

    # 2. jaki procent dorosłych do 40 roku życia przeżył katastrofę
    adults_under_40 = dataset.filter(
        (f.col("Age") >= 18) & (f.col("Age") <= 40))
    res = get_percentage_survived(adults_under_40)
    results.append((2, str(res)))

    # 3. jaki procent dorosłych do 40 roku życia przeżył katastrofę z podziałem na płeć
    res = get_percentage_survived(adults_under_40, group_by="Sex")
    results.append((3, str(res)))

    # 4. jaki procent dorosłych powyżej 40 roku życia przeżył katastrofę
    adults_over_40 = dataset.filter(f.col("Age") > 40)
    res = get_percentage_survived(adults_over_40)
    results.append((4, str(res)))

    # 5. jaki procent dorosłych powyżej 40 roku życia przeżył katastrofę z podziałem na płeć
    res = get_percentage_survived(adults_over_40, group_by="Sex")
    results.append((5, str(res)))

    # 6. jaki procent przeżywalności był w danej klasie z podziałem na płeć
    res = get_percentage_survived(dataset, group_by="Pclass")
    results.append((6, str(res)))

    schema = StructType([StructField("question", IntegerType()),
                         StructField("answer", StringType())])

    res_df = spark.createDataFrame(data=results, schema=schema)

    options = {
        "url": "jdbc:mysql://mysql:3306/data_has_power",
        "driver": "com.mysql.cj.jdbc.Driver",
        "dbtable": "results",
        "user": "spark",
        "password": "spark"}

    res_df.write.format("jdbc").options(**options).mode("overwrite").save()

    sql_context.read.format("jdbc").options(**options).load().show()


if __name__ == '__main__':
    main()
