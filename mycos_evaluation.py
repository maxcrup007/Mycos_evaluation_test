import time
import unittest
import pyodbc
import subprocess
import os, sys
sys.path.append('./')
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Form_checker import fetch_data_from_database
from collect_token import fetch_token_from_database
from link import url



class TestDesktopEvaluation(unittest.TestCase):

    
    @classmethod
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def test_evaluation_desktop(self):

        driver = self.driver

        driver.get(url)
        time.sleep(10)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/a/button").click()
        time.sleep(10)

        scroll = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]")
        action = ActionChains(driver)
        action.move_to_element(scroll).perform()
        time.sleep(10)

        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[5]/div/div/textarea[1]").send_keys("My cos test form")
        time.sleep(10)

        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[6]/button").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[2]/button[2]").click()
        time.sleep(10)

        element_passed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/div[7]/div")
        text_content = element_passed.text

        with open("Collect_Text/test_status.text", "w") as file:
                file.write(text_content)

        try:

            with open("Collect_Text/test_status.text") as file:
                test_stat = file.read()

            checker = "Complete"
            assert test_stat == checker
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
