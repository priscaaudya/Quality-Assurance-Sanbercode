import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from page import elem
from data import input
import baseLocation
import baseLogin

class TestEdit(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_g_success_edit_location_completed(self):
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
        driver.find_element(By.XPATH, elem.btn_edit).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.name).send_keys(input.e_name) # isi name
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.city).send_keys(input.e_city) # isi city
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.province).send_keys(input.e_province) # isi province
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.zip).send_keys(input.zip) # isi zip
        time.sleep(1)      
        # isi country  
        wait = WebDriverWait(driver,10) 
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, elem.country)))

        dropdown.click()
        time.sleep(1)
        dropdown.send_keys(input.e_country)
        time.sleep(3)        
        dropdown.send_keys(Keys.RETURN)
        time.sleep(5)   

        driver.find_element(By.XPATH, elem.phone).send_keys(input.e_phone) # isi phone
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.fax).send_keys(input.e_fax) # isi fax
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.address).send_keys(input.e_address) # isi address
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.notes).send_keys(input.e_notes) # isi notes
        time.sleep(1)       
        driver.find_element(By.XPATH, elem.btn_save ).click()


        #validation
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,elem.alert))).get_attribute(input.alert_updated)


    def test_f_success_edit_location_name_country(self):
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
        driver.find_element(By.XPATH, elem.btn_edit).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.name).send_keys(input.e_name) # isi name
        time.sleep(1)       
   
        # isi country  
        wait = WebDriverWait(driver,10) 
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, elem.country)))

        dropdown.click()
        time.sleep(1)
        dropdown.send_keys(input.e_country)
        time.sleep(3)        
        dropdown.send_keys(Keys.RETURN)
        time.sleep(5)   
        driver.find_element(By.XPATH, elem.btn_save ).click()


        #validation
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,elem.alert))).get_attribute(input.alert_updated)


    def test_a_failed_edit_location_same_name(self):
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
        driver.find_element(By.XPATH, elem.btn_edit).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.name).send_keys("a") # isi name    


        #validation
        response_data = driver.find_element(By.XPATH,elem.req_name).text
        self.assertIn(input.val_name, response_data)


    def test_b_failed_edit_location_phone(self):
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
        driver.find_element(By.XPATH, elem.btn_edit).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.phone).send_keys(input.i_phone) # isi name
        time.sleep(1)       


        #validation
        response_data = driver.find_element(By.XPATH,elem.val_phone).text
        self.assertIn(input.val, response_data)


    def test_c_failed_edit_location_fax(self):
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
        driver.find_element(By.XPATH, elem.btn_edit).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.fax).send_keys(input.i_fax) # isi name
        time.sleep(1)       


        #validation
        response_data = driver.find_element(By.XPATH,elem.val_fax).text
        self.assertIn(input.val, response_data)


    def test_d_failed_edit_location_blank_field(self):
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
        driver.find_element(By.XPATH, elem.btn_edit).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.name).send_keys(Keys.CONTROL + "a") #delete name
        driver.find_element(By.XPATH, elem.name).send_keys(Keys.DELETE)
        time.sleep(3)


        #validation
        response_data = driver.find_element(By.XPATH,elem.req_name).text
        self.assertIn(input.req, response_data)


    def test_e_cancel_button(self):
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
        driver.find_element(By.XPATH, elem.btn_edit).click()
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