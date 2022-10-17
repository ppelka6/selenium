import unittest
from selenium import webdriver
from selenium import webdriver # general modul for selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select # for handling select drop down
from selenium.webdriver.support.wait import WebDriverWait # selenium modul for waiting response browser
from selenium.webdriver.support import expected_conditions as EC # modul selenium for condition
from selenium.webdriver.common.by import By # modul selenium handle after wait for search element
import os
import time

REGISTRATION_URL = 'https://pl-pl.facebook.com/reg/'

# Dane do rejestracji
first_name = "Arnold"
last_name = "Masa"
email = "arnoldmasatestpython@test.pl"
password = "tooshort"

Wait_time = 60

ser = Service(os.path.abspath("chromedriver"))

driver = webdriver.Chrome(service = ser)
driver.get("https://pl-pl.facebook.com/reg/")

#Check if there is a Register button
Zarejestruj_sie = driver.find_element(By.ID, "u_0_s_G+")
print("Zarejestruj się:", Zarejestruj_sie.text)

name = WebDriverWait(driver, Wait_time).until(
    EC.element_to_be_clickable((By.ID, "u_0_b_bT")) # search element from id
) # method for waiting process until element is clickable
name.send_keys(first_name) # input for first name

# Dane do rejestracji
driver.find_element_by_id("u_0_d_Ve").send_keys(last_name)
driver.find_element_by_id("u_0_g_6a").send_keys(email)
driver.find_element_by_id("password_step_input").send_keys(password)

# Select DOB
dzien = Select(driver.find_element_by_id("day"))
dzien.select_by_visible_text("22")

miesiac = Select(driver.find_element_by_id("month"))
miesiac.select_by_visible_text("cze")

rok = Select(driver.find_element_by_id("year"))
rok.select_by_visible_text("1993")

driver.find_element_by_css_selector("input[type='radio'][value='2']").click()

driver.find_element_by_id("u_1_s").click()



