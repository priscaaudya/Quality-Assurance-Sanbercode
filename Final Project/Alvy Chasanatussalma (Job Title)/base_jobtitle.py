import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import elem

def jobtitle(driver):

    driver.find_element(By.XPATH, elem.menu_admin).click()
    time.sleep(3)
    driver.find_element(By.XPATH, elem.dropdown_job).click()
    time.sleep(3)
    driver.find_element(By.XPATH, elem.jobtitle).click()
    time.sleep(3)
    