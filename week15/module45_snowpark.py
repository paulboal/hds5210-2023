
# To use this code, you can create a new Python worksheet in the Snowflake web UI
# and paste in this code.


# The Snowpark package is required for Python Worksheets. 
# You can add more packages by selecting them using the Packages control and then importing them.

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

# Import Pandas to make sure you've got it
import pandas as pd

# Snowpark Python packages want you to create a "main()" function that 
# will control the main flow when you run this Python inside Snowflake.
def main(session: snowpark.Session): 

    # Snowpark "dataframes" are not exactly the same as Pandas dataframes
    # They follow a similar idea, but have different functions.
    # Snowpark syntax is modeled after the open source Apache Pyspark

    # If we call to_pandas(), we get a Pandas dataframe to work with
    df = session.table('DEMO.PUBLIC.NAMES').select(['FIRST_NAME','LAST_NAME']).to_pandas()

    # And we can do normal Pandas things
    # Make sure you use as_index=False so your grouped by fields are
    # represented as a new series.
    summary = df.groupby('LAST_NAME', as_index=False).count()

    # Print a sample of the dataframe to standard output.
    print(summary)

    # Convert the Pandas dataframe back to a Snowpark dataframe before returning it
    return session.create_dataframe(summary)
