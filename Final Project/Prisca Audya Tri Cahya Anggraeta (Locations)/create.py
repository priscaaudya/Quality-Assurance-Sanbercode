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

class TestCreate(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_add_location_completed(self):
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
        driver.find_element(By.XPATH, elem.btn_add).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.name).send_keys(input.name) # isi name
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.city).send_keys(input.city) # isi city
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.province).send_keys(input.province) # isi province
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.zip).send_keys(input.zip) # isi zip
        time.sleep(1)      
        # isi country  
        wait = WebDriverWait(driver,10) 
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, elem.country)))

        dropdown.click()
        time.sleep(1)
        dropdown.send_keys(input.country)
        time.sleep(3)        
        dropdown.send_keys(Keys.RETURN)
        time.sleep(5)   

        driver.find_element(By.XPATH, elem.phone).send_keys(input.phone) # isi phone
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.fax).send_keys(input.fax) # isi fax
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.address).send_keys(input.address) # isi address
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.notes).send_keys(input.notes) # isi notes
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.btn_save ).click()

        # #validation
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,elem.alert))).get_attribute(input.alert_success)


    def test_b_success_add_location_name_country(self):
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
        driver.find_element(By.XPATH, elem.btn_add).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.name).send_keys(input.name2) # isi name
        time.sleep(1)       
   
        # isi country  
        wait = WebDriverWait(driver,10) 
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, elem.country)))

        dropdown.click()
        time.sleep(1)
        dropdown.send_keys(input.country)
        time.sleep(3)        
        dropdown.send_keys(Keys.RETURN)
        time.sleep(5)   

        driver.find_element(By.XPATH, elem.btn_save ).click()


        # #validation
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,elem.alert))).get_attribute(input.alert_success)



    def test_c_failed_add_location_same_name(self):
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
        driver.find_element(By.XPATH, elem.btn_add).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.name).send_keys(input.i_name) # isi name
        time.sleep(1)       


        #validation
        response_data = driver.find_element(By.XPATH,elem.req_name).text
        self.assertIn(input.val_name, response_data)


    def test_d_failed_add_location_phone(self):
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
        driver.find_element(By.XPATH, elem.btn_add).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.phone).send_keys(input.i_phone) # isi name
        time.sleep(1)       


        #validation
        response_data = driver.find_element(By.XPATH,elem.val_phone).text
        self.assertIn(input.val, response_data)


    def test_e_failed_add_location_fax(self):
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
        driver.find_element(By.XPATH, elem.btn_add).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.fax).send_keys(input.i_fax) # isi name
        time.sleep(1)       


        #validation
        response_data = driver.find_element(By.XPATH,elem.val_fax).text
        self.assertIn(input.val, response_data)


    def test_f_failed_add_location_blank_field(self):
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
        driver.find_element(By.XPATH, elem.btn_add).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.btn_save ).click()
        time.sleep(1)       


        #validation
        response_data = driver.find_element(By.XPATH,elem.req_name).text
        self.assertIn(input.req, response_data)
        response_data2 = driver.find_element(By.XPATH,elem.req_country).text
        self.assertIn(input.req, response_data2)


    def test_g_cancel_button(self):
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
        driver.find_element(By.XPATH, elem.btn_add).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.btn_cancel ).click()
        time.sleep(3)       


        #validation
        response_data = driver.current_url
        self.assertEqual(elem.location_url, response_data)


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()      

