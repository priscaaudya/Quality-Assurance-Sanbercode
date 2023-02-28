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
import baseLogin
import baseLocation

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_search_by_name(self):
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
        driver.find_element(By.XPATH, elem.s_name).send_keys(input.s_name) # isi name
        time.sleep(1)           
        driver.find_element(By.XPATH, elem.btn_search ).click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)     

        #validation
        response_data = driver.find_element(By.XPATH,elem.h_name).text
        self.assertIn(input.s_name, response_data)


    def test_b_search_by_city(self):
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
        driver.find_element(By.XPATH, elem.s_city).send_keys(input.s_city) # isi city
        time.sleep(1)           
        driver.find_element(By.XPATH, elem.btn_search ).click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)   

        #validation
        response_data = driver.find_element(By.XPATH,elem.h_city).text
        self.assertIn(input.s_city, response_data)



    def test_c_search_by_country(self):
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
        wait = WebDriverWait(driver,10)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, elem.s_country)))

        dropdown.click()
        time.sleep(1)
        dropdown.send_keys(input.s_country)
        time.sleep(3)        
        dropdown.send_keys(Keys.RETURN)
        time.sleep(5)           
        driver.find_element(By.XPATH, elem.btn_search ).click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)   

        #validation
        response_data = driver.find_element(By.XPATH,elem.h_country).text
        self.assertIn(input.resp_country, response_data)

    def test_d_search_by_invalid_name(self):
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
        driver.find_element(By.XPATH, elem.s_name).send_keys(input.i_search) # isi name
        time.sleep(1)           
        driver.find_element(By.XPATH, elem.btn_search ).click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)     

        #validation
        response_data = driver.find_element(By.XPATH,elem.resp_no_found).text
        self.assertIn(input.no_found, response_data)


    def test_e_search_by_invalid_city(self):
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
        driver.find_element(By.XPATH, elem.s_city).send_keys(input.i_search) # isi city
        time.sleep(1)           
        driver.find_element(By.XPATH, elem.btn_search ).click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)   

        #validation
        response_data = driver.find_element(By.XPATH,elem.resp_no_found).text
        self.assertIn(input.no_found, response_data)


    def test_f_reset_button(self):
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
        driver.find_element(By.XPATH, elem.s_name).send_keys(input.s_name) # isi name
        time.sleep(1)    
        driver.find_element(By.XPATH, elem.s_city).send_keys(input.s_city) # isi city
        time.sleep(1)           
        driver.find_element(By.XPATH, elem.btn_reset ).click()
        time.sleep(1)


        #validation
        response_data = driver.find_element(By.XPATH,elem.header_loct).text
        self.assertIn(input.resp_loct, response_data)
        response_data2 = driver.current_url
        self.assertEqual(elem.location_url, response_data2)


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()      