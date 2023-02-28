import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from page import elem
from data import input
import baseLocation
import baseLogin

class TestDelete(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_delete_one_data(self):
        #buka web browser
        driver = self.browser 

        #login
        baseLogin.base_login(driver)
        response_data = driver.find_element(By.XPATH,elem.header).text
        self.assertIn(input.resp_header, response_data)

        #locations
        baseLocation.base_location(driver)
        response_data = driver.find_element(By.XPATH,elem.header_loct).text
        self.assertIn(input.resp_loct, response_data)

        #step
        driver.find_element(By.XPATH, elem.btn_delete).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.btn_yes_delete ).click()
        time.sleep(3)  

        #validation
        # response_data = driver.find_element(By.XPATH,elem.alert).text
        # self.assertIn(input.alert_deleted, response_data)


    def test_b_delete_many_data(self):
        #buka web browser
        driver = self.browser 

        #login
        baseLogin.base_login(driver)
        response_data = driver.find_element(By.XPATH,elem.header).text
        self.assertIn(input.resp_header, response_data)

        #locations
        baseLocation.base_location(driver)
        response_data = driver.find_element(By.XPATH,elem.header_loct).text
        self.assertIn(input.resp_loct, response_data)

        #step
        driver.find_element(By.XPATH, elem.c_delete).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.btn_selected).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.btn_yes_delete ).click()
        time.sleep(3)  

        #validation
        # response_data = driver.find_element(By.XPATH,elem.alert).text
        # self.assertIn(input.alert_deleted, response_data)


    def test_d_delete_all_data(self):
        #buka web browser
        driver = self.browser 

        #login
        baseLogin.base_login(driver)
        response_data = driver.find_element(By.XPATH,elem.header).text
        self.assertIn(input.resp_header, response_data)

        #locations
        baseLocation.base_location(driver)
        response_data = driver.find_element(By.XPATH,elem.header_loct).text
        self.assertIn(input.resp_loct, response_data)

        #step
        driver.find_element(By.XPATH, elem.all_delete).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.btn_selected).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.btn_yes_delete ).click()
        time.sleep(3)  

        #validation
        # response_data = driver.find_element(By.XPATH,elem.alert).text
        # self.assertIn(input.alert_deleted, response_data)


    def test_c_cancel_button(self):
        #buka web browser
        driver = self.browser 

        #login
        baseLogin.base_login(driver)
        response_data = driver.find_element(By.XPATH,elem.header).text
        self.assertIn(input.resp_header, response_data)

        #locations
        baseLocation.base_location(driver)
        response_data = driver.find_element(By.XPATH,elem.header_loct).text
        self.assertIn(input.resp_loct, response_data)

        #step
        driver.find_element(By.XPATH, elem.btn_delete).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.btn_no_cancel ).click()
        time.sleep(3)  

        #validation
        response_data = driver.current_url
        self.assertEqual(elem.location_url, response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()      
