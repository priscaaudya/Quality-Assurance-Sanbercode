import unittest
import time
import base_login
import base_jobtitle
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 
from page import elem
from data import input

class TestHapus(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_delete_satu_data(self):
        #step
        driver = self.browser #buka browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        driver.find_element(By.XPATH,elem.btn_hapus).click()
        time.sleep(3)
        driver.find_element(By.XPATH,elem.btn_yes_delete).click()
        time.sleep(3)

    # validasi
        response_data = driver.current_url
        self.assertEqual(response_data, elem.list_url)


    def test_c_delete_keseluruhan(self):
        #step
        driver = self.browser #buka browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        driver.find_element(By.XPATH,elem.btn_checkbox).click()
        time.sleep(3)
        driver.find_element(By.XPATH,elem.btn_delete_selected).click()
        time.sleep(3)

    # validasi
        response_data = driver.current_url
        self.assertEqual(response_data, elem.list_url)

    def test_b_delete_beberapa_data(self):
        #step
        driver = self.browser #buka browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        driver.find_element(By.XPATH,elem.btn_checkbox2).click()
        time.sleep(3)
        driver.find_element(By.XPATH,elem.btn_delete_selected).click()
        time.sleep(3)

    # validasi
        response_data = driver.current_url
        self.assertEqual(response_data, elem.list_url)

    def test_d_cancel(self):
        #step
        driver = self.browser #buka browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        driver.find_element(By.XPATH,elem.btn_hapus).click()
        time.sleep(3)
        driver.find_element(By.XPATH,elem.btn_cancelhapus).click()
        time.sleep(3)

    # validasi
        response_data = driver.current_url
        self.assertEqual(response_data, elem.list_url)


def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()