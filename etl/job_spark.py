# import libraries

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
import pyspark.sql.functions as f

# define buckets

load_bucket = 's3://datalake-igti-fabio-edc-desafio-final/raw-data'
save_bucket = 's3://datalake-igti-fabio-edc-desafio-final/staging-zone'

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# read files

spark_df = (
    spark
    .read
    .format('csv')
    .option('header', True)
    .option('inferSchema', True)
    .option('delimiter', ';')
    .option('enconding', 'latin1')
    .load(load_bucket)
)

# save data in parquet formar

(
    spark_df
    .coalesce(50)
    .write.mode('overwrite')
    .format('parquet')
    .save(save_bucket)
)

job.commit()