###IMPORT MODULES###
import snowflake.connector as snflk
import pandas as pd
import logging
from os import getenv

###QUERY CLASS###
class Query():
    def __init__(self, user:str, password:str, account:str, environment:bool=True):
        #snowflake connection variables
        self.__user = user
        self.__password = password
        self.__account = account

        #variable to tell system to get env vars or not
        self.__environment = environment

        #set enviroment variables
        self.__get_enviroment_variables()

    def __get_enviroment_variables(self):
        #if True pull enviroment variables
        if self.__environment:
            self.__user = getenv(self.__user)
            self.__password = getenv(self.__password)
            self.__account = getenv(self.__account)
        #log issues with pulling variables
        if self.__user is None:
            try:
                logging.warning('User variable is not set.')
            except:
                print('User variable is not set.')
        if self.__password is None:
            try:
                logging.warning('Password variable is not set.')
            except:
                print('Password variable is not set.')
        if self.__account is None:
            try:
                logging.warning('Account variable is not set.')
            except:
                print('Account variable is not set.')

    #query db, return pandas df
    def get_query(self, query_str:str):
        db_conn = snflk.connect(user=self.__user, password=self.__password, account=self.__account)
        curs = db_conn.cursor()
        try:
            curs.execute(query_str)
            df = curs.fetch_pandas_all()
            curs.close()
            db_conn.close()
        except:
            try:
                logging.ERROR('There was in an issue while pulling the data. Please check your connection or query.')
            except:
                print('ERROR: There was in an issue while pulling the data. Please check your connection or query.')
            curs.close()
            db_conn.close()
            return None
        return df
