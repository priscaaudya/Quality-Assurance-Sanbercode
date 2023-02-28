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


class TestCreate(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_create(self):
        # steps
        driver = self.browser #buka web browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        
        driver.find_element(By.XPATH,elem.btn_add).click()
        time.sleep(3)
        driver.find_element(By.XPATH,elem.input_jobtitle).send_keys(input.input_jobtitle) # isi nama
        time.sleep(3)
        driver.find_element(By.XPATH,elem.input_description).send_keys(input.input_description) # isi nama
        time.sleep(5)
        driver.find_element(By.CLASS_NAME,elem.input_specification).send_keys(input.input_specification) # isi nama
        time.sleep(3)
        driver.find_element(By.XPATH,elem.input_note).send_keys(input.input_note) # isi nama
        time.sleep(3)
        driver.find_element(By.XPATH,elem.btn_save).click()
        time.sleep(5)

    # validasi
        response_data = driver.current_url
        self.assertEqual(response_data, elem.list_url)

    def test_b_success_create_name(self):
        # steps
        driver = self.browser #buka web browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        
        driver.find_element(By.XPATH,elem.btn_add).click()
        time.sleep(3)
        driver.find_element(By.XPATH,elem.input_jobtitle2).send_keys(input.input_jobtitle2) # isi nama
        time.sleep(3)
        driver.find_element(By.XPATH,elem.btn_save).click()
        time.sleep(5)

    # validasi
        response_data = driver.current_url
        self.assertEqual(response_data, elem.list_url)

    def test_c_failed_create_name_kosong(self):
            # steps
        driver = self.browser #buka web browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        driver.find_element(By.XPATH,elem.btn_add).click()
        time.sleep(3)
        driver.find_element(By.XPATH,elem.btn_save).click()
        time.sleep(5)

    # validasi
        response_data = driver.find_element(By.XPATH, elem.validasi_required).text
        self.assertEqual(response_data, input.Req)
    
    def test_d_failed_file_maksimum(self):
            # steps
        driver = self.browser #buka web browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        driver.find_element(By.XPATH,elem.btn_add).click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME,elem.input_specification).send_keys(input.input_specification2) # isi nama
        time.sleep(3)
        driver.find_element(By.XPATH,elem.btn_save).click()
        time.sleep(5)

    # validasi
        response_data = driver.find_element(By.XPATH, elem.val_max).text
        self.assertEqual(response_data, input.max)

    def test_e_cancel(self):
            #step
        driver = self.browser #buka browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        driver.find_element(By.XPATH,elem.btn_add).click()
        time.sleep(3)
        driver.find_element(By.XPATH,elem.btn_cancelcreate).click()
        time.sleep(3)

    # validasi
        response_data = driver.current_url
        self.assertEqual(response_data, elem.list_url)


def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()


