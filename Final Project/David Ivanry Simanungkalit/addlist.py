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



    def test_a_fail_addlist(self):
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
        time.sleep(3) 
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(3)

         #validasi
        response_data = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/span").text
        self.assertIn('Required', response_data)

    def test_b_succes_addlist(self):
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
        time.sleep(3) 
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("Maylin") # isi first name
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys("sormin") # isi last name
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(3)

         #validasi
        response_data = driver.current_url
        self.assertEqual(response_data, "(https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/61)")




        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()