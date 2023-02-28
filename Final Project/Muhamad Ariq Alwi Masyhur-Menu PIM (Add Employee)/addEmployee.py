import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import login
import employee

class TestAdd(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_success_add_employee_completed(self):
        #buka web browser
        driver = self.browser 

        #login
        login.login(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div").text
        self.assertIn('Dashboard', response_data)

        #employee
        employee.employee(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]").text
        self.assertIn('Add Employee', response_data)

        #steps
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("Muhamad") # isi first name
        time.sleep(1)   

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input").send_keys("Nur") # isi middle name
        time.sleep(1)     

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys("Ramadhan") # isi last name
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("muhamadnur123") # isi username
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("Nurganteng123@") # isi password
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("Nurganteng123@") # isi confirm password
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(3)
    
    def test_a_success_add_employee_notcompleted_a(self):
        #buka web browser
        driver = self.browser 

        #login
        login.login(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div").text
        self.assertIn('Dashboard', response_data)

        #employee
        employee.employee(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]").text
        self.assertIn('Add Employee', response_data)

        #steps
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("Muhamad") # isi first name
        time.sleep(1)   

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input").send_keys("Ariq Alwi") # isi middle name
        time.sleep(1)     

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys("Masyhur") # isi last name
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(3)

    
    def test_a_success_add_employee_notcompleted_b(self):
        #buka web browser
        driver = self.browser 

        #login
        login.login(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div").text
        self.assertIn('Dashboard', response_data)

        #employee
        employee.employee(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]").text
        self.assertIn('Add Employee', response_data)

        #steps
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("Ikhsan") # isi first name
        time.sleep(1)   

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys("Ramaditya") # isi last name
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("ihsanaja123") # isi username
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("Ihsanganteng123_") # isi password
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("Ihsanganteng123_") # isi confirm password
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(3)

    
    def test_a_failed_add_employee(self):
        #buka web browser
        driver = self.browser 

        #login
        login.login(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div").text
        self.assertIn('Dashboard', response_data)

        #employee
        employee.employee(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]").text
        self.assertIn('Add Employee', response_data)

        #steps
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("") # isi first name
        time.sleep(1)   

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input").send_keys("") # isi middle name
        time.sleep(1)     

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys("") # isi last name
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("") # isi username
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("") # isi password
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("") # isi confirm password
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(3)
    

    def test_a_failed_add_employee_notcompleted(self):
        #buka web browser
        driver = self.browser 

        #login
        login.login(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div").text
        self.assertIn('Dashboard', response_data)

        #employee
        employee.employee(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]").text
        self.assertIn('Add Employee', response_data)

        #steps
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("Bambang") # isi first name
        time.sleep(1)   

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input").send_keys("") # isi middle name
        time.sleep(1)     

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys("") # isi last name
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(3)
    

    def test_a_failed_add_employee_password(self):
        #buka web browser
        driver = self.browser 

        #login
        login.login(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div").text
        self.assertIn('Dashboard', response_data)

        #employee
        employee.employee(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]").text
        self.assertIn('Add Employee', response_data)

        #steps
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("Armand") # isi first name
        time.sleep(1)   

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input").send_keys("Riyan") # isi middle name
        time.sleep(1)     

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys("Maulana") # isi last name
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("armandmaulana04") # isi username
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("armandmau00") # isi password
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("armandmau00") # isi confirm password
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(3)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()