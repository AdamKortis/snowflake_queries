# snowflake_queries
A module used to enhance connection and retrieval of data from a Snowflake database.

## Description
I built this module to allow me to connect to Snowflake databases more quickly. I did not want to have to type the connection information information and the required methods each time I needeed code. Now I create the query object and use one method call to grab the data as a pandas dataframe. Using environment variables, a query object can be created and then a SQL string can be passed to the get_query() method. This will create the connection, query the database, return the data as a dataframe, and close out the connection.

## Required 3rd Party Modules
[pandas](https://pandas.pydata.org/docs/getting_started/install.html)
[snowflake-connector-python](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-install)

## Instructions
1. Install the required modules listed above.
2. Create enviroment variables for the Snowflake Databse connection for your Username, Password, and Connection information. (Note: it can take the information directly, but I highly recommend using env variables).
3. Import the module to your primary source code.
4. Create a Query object.
5. Create SQL string to query the database.
6. Used get_query() method to connect to the database and return the query.

## Module Information

### Query Object
Query(user: str, password: str, account: str, environment: bool = True)
Initializes the Query object with information to connect to the snowflake database.
* "user" is a string representing the name of the enviromemnt variable or the direct username.
* "password" is a string representing the name of the enviromemnt variable or the direct password.
* "account" is a string representing the name of the account enviromemnt variable or the direct account name.
* "environment" is a bool value: True would use the information stored in environment variables. False would use the specific values passed to the Query object on initialization.

#### get_query(query_str: str)
This method connects and queries the snowflake database returning the data as a pandas dataframe.
* "query_str" a string object that should be a SQL query "SELECT COL_1, COL_2 FROM DATABASE WHERE CONDITION = VALUE ORDER BY COL_1".

## Note this module was only run on windows. Some adjustments may need to be made for Mac or Linux based systems.

## Example:
```python
import snowflake_query
import pandas as pd

query = Query('ENV_SNOWFLAKE_USER', 'ENV_SNOWFLAKE_PASSWORD', 'ENV_SNOWFLAKE_ACCOUNT')

simple_query = '''
  SELECT COL_1
    , COL_2
  FROM SNOWFLAKE.DATABASE
  WHERE COL_3 = VALUE
  ORDER BY COL_2, COL_1
'''

df = query.get_query(simple_query)
```
