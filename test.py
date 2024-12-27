import time
import pickle
import selenium
import pytest
import unittest
import pyodbc

import os, sys
sys.path.append('./')


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


class TestRedirection(unittest.TestCase):

    
    @classmethod
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def get_query_results(connection_string, query, parameters=None):

        try:
            with pyodbc.connect(connection_string) as conn:
                with conn.cursor() as cursor:
                    if parameters:
                        cursor.execute(query, parameters)
                    else:
                        cursor.execute(query)
                    results = cursor.fetchall()
                    return results
        except pyodbc.Error as e:
            print(f"Database error: {e}")
            return None
    

    def test_evaluation_redirection(self):

        server = 'dev-mycos.database.windows.net'  
        database = 'MycosCenterDB_Dev' 
        username = 'mycosSA' 
        password = 'mycos234!@#'

        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
        sql_query = "SELECT expected_text FROM test_data WHERE id = ?;"
        query_params = (1,)  # Replace with actual parameters if needed
        results = self.get_query_results(connection_string, sql_query, query_params)

        if not results:
            print("No results from database query.")
            return

        with open("link.text") as file:
            url = file.read()

        print(url)

        driver = self.driver

        driver.get(url)
        time.sleep(10)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/a/button").click()
        time.sleep(10)

        

        try:
            checker = "Mycos Evaluation"
            assert driver.title == checker
            print("Test Passed")


        except AssertionError as error:
            print(error)
            print("Test Failed")


    
    @classmethod
    def test_tearDownClass(self):

        driver = self.driver
        driver.close()
        driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()
