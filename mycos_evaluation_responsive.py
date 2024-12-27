import time
import unittest
import pyodbc

import os, sys
sys.path.append('./')


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Form_checker import fetch_data_from_database
from collect_token import fetch_token_from_database
from link import url


class TestDesktopEvaluation(unittest.TestCase):

    
    @classmethod
    def setUp(self):

        iphone_se_emulation = {
        "deviceMetrics": {"width": 667, "height": 337, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
        }

        iphone_14_pro_max_emulation = {
        "deviceMetrics": {"width": 932, "height": 430, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
        }

        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", iphone_14_pro_max_emulation)
        self.driver = webdriver.Chrome(options=chrome_options)

    

    def test_evaluation_iphone(self):

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

        # with open('Form_checker.py', 'r') as file:
        #     exec(file.read())

        driver = self.driver
        driver.close()
        driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()
