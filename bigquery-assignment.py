from google.cloud import bigquery
import pandas as pd

def query_nyc_trip():
    client = bigquery.Client()
    query_job = client.query(
        """
        SELECT *
        FROM alt.property_data
        """
    )
    results = query_job.result()
    df = pd.DataFrame(results)
    return print(df.head())


query_nyc_trip()