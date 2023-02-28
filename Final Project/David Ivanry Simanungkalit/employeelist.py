import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import login1
import menuemploye

class TestAdd(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_search_succes(self):
        driver=self.browser

        #login
        login1.login_(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div").text
        self.assertIn('Dashboard', response_data)

        #employeelist
        menuemploye.menuemployee_(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").text
        self.assertIn('Employee List', response_data)     

        #steps
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("David") # isi first name
        time.sleep(1)     
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("0066") # isi id
        time.sleep(1)  
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(1)

        #validasi
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]").text
        self.assertIn('0066', response_data)

    def test_b_search_succes_by_id(self):
        driver=self.browser

        #login
        login1.login_(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div").text
        self.assertIn('Dashboard', response_data)

        #employeelist
        menuemploye.menuemployee_(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").text
        self.assertIn('Employee List', response_data)  

        #step
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("0066") # isi id
        time.sleep(1)  
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(1)

        #validasi
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]").text
        self.assertIn('0066', response_data) 

    def test_c_search_succes_by_name(self):
        driver=self.browser

        #login
        login1.login_(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div").text
        self.assertIn('Dashboard', response_data)

        #employeelist
        menuemploye.menuemployee_(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").text
        self.assertIn('Employee List', response_data)  
  
        #steps
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("David") # isi first name
        time.sleep(1)   
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(1)

        #validasi
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div").text
        self.assertIn('Morris', response_data)

    def test_d_search_notlisted(self):
        driver=self.browser

        #login
        login1.login_(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div").text
        self.assertIn('Dashboard', response_data)

        #employeelist
        menuemploye.menuemployee_(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").text
        self.assertIn('Employee List', response_data)

        #steps
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("ououou") # isi first name
        time.sleep(1)     
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("747483") # isi id
        time.sleep(1)   
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(1)

          #validasi
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text
        self.assertIn('No Records Found', response_data)
        
    def test_f_addlist(self):
        driver=self.browser

        #login
        login1.login_(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div").text
        self.assertIn('Dashboard', response_data)

        #employeelist
        menuemploye.menuemployee_(self)
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").text
        self.assertIn('Employee List', response_data)

        #Steps
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("Maylin") # isi first name
        time.sleep(1)   
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys("sormin") # isi last name
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(1)

         #validasi
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text
        self.assertIn('Personal Details', response_data)




        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()

   