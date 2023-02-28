import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import elem
from data import input

def base_location(driver):
    # steps
    driver.find_element(By.XPATH, elem.menu_admin).click()
    time.sleep(3)
    driver.find_element(By.XPATH, elem.dropdown).click()
    time.sleep(3)
    driver.find_element(By.XPATH, elem.dp_location).click()
    time.sleep(3)
