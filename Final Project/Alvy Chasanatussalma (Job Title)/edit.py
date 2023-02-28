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


class TestEdit(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_edit_jobtitle_lengkap(self):
        #step
        driver = self.browser #buka browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        driver.find_element(By.XPATH,elem.btn_edit).click()
        time.sleep(3)
        driver.find_element(By.XPATH,elem.edit_jobtitle).send_keys(input.edit_jobtitle) # isi nama
        time.sleep(3)
        driver.find_element(By.XPATH,elem.edit_description).send_keys(input.edit_description) # isi nama
        time.sleep(5)
        #driver.find_element(By.CLASS_NAME,elem.edit_specification).send_keys(input.edit_specification) # isi nama
        #time.sleep(3)
        driver.find_element(By.XPATH,elem.edit_note).send_keys(input.edit_note) # isi nama
        time.sleep(3)
        driver.find_element(By.XPATH,elem.btn_save).click()
        time.sleep(5)

    # validasi
        response_data = driver.current_url
        self.assertEqual(response_data, elem.list_url)

    def test_b_success_edit_name(self):
        #step
        driver = self.browser #buka browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        driver.find_element(By.XPATH,elem.btn_edit).click()
        time.sleep(3)
        driver.find_element(By.XPATH,elem.edit_jobtitle).send_keys(input.edit_jobtitle3) # isi nama
        time.sleep(3)
        driver.find_element(By.XPATH,elem.btn_save).click()
        time.sleep(5)

    # validasi
        response_data = driver.current_url
        self.assertEqual(response_data, elem.list_url)


    def test_c_failed_edit_name_kosong(self):
            #step
        driver = self.browser #buka browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        driver.find_element(By.XPATH,elem.btn_edit).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.edit_jobtitle).send_keys(Keys.CONTROL + "a") #delete name
        driver.find_element(By.XPATH, elem.edit_jobtitle).send_keys(Keys.DELETE)
        driver.find_element(By.XPATH,elem.btn_save).click()
        time.sleep(5)

    # validasi
        response_data = driver.find_element(By.XPATH, elem.validasi_required).text
        self.assertEqual(response_data, input.Req)

    def test_d_failed_edit_name_same(self):
            #step
        driver = self.browser #buka browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        driver.find_element(By.XPATH,elem.btn_edit).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.edit_jobtitle).send_keys(Keys.CONTROL + "a") #delete name
        driver.find_element(By.XPATH, elem.edit_jobtitle).send_keys(Keys.DELETE)
        driver.find_element(By.XPATH,elem.edit_jobtitle).send_keys(input.edit_jobtitle2) # isi nama
        time.sleep(3)
        driver.find_element(By.XPATH,elem.btn_save).click()
        time.sleep(5)

    # validasi
        response_data = driver.find_element(By.XPATH, elem.validasi_same).text
        self.assertEqual(response_data, input.same)

    def test_e_cancel(self):
            #step
        driver = self.browser #buka browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.dashboard_url)

        base_jobtitle.jobtitle(driver)
        response_data = driver.find_element(By.XPATH,elem.header_jobtitle).text
        self.assertIn(input.resp_jobtitle, response_data)

        driver.find_element(By.XPATH,elem.btn_edit).click()
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