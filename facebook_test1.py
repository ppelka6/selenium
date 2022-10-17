import unittest
from selenium import webdriver
from selenium import webdriver # general modul for selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select # for handling select drop down
from selenium.webdriver.support.wait import WebDriverWait # selenium modul for waiting response browser
from selenium.webdriver.support import expected_conditions as EC # modul selenium for condition
from selenium.webdriver.common.by import By # modul selenium handle after wait for search element
import os
import time

REGISTRATION_URL = 'https://pl-pl.facebook.com/reg/'

# Dane do rejestracji
first_name = "Arnold"
last_name = "Masa"
e_mail = "arnoldmasatestpython@test.pl"
password = "tooshort123"

Wait_time = 60

class Registration(unittest.TestCase):
    def setUp(self):
        # WARUNKI WSTĘPNE
        # 1. Otwarta strona do rejestracji
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://pl-pl.facebook.com/reg")
        # 2. Użytkownik ma byc niezalogowany
        # 3. Akceptacja ciasteczek
        self.driver.find_element(By.CSS_SELECTOR, '[data-testid="cookie-policy-manage-dialog-accept-button"]').click()

    def tearDown(self):
        # Finish test
        self.driver.quit()

    def testIncorrectDOB(self):
        sleep(1)
        # driver = self.driver
        # 1.Input first_name
        name = self.driver.find_element(By.NAME, "firstname")
        name.send_keys(first_name)
        sleep(1)

        # 2. Input last_name
        lastname = self.driver.find_element(By.NAME, "lastname")
        lastname.send_keys(last_name)

        # 3. Input email
        mail = self.driver.find_element(By.NAME, "reg_email__")
        mail.send_keys(e_mail)
        sleep(1)

        # 4. Input email again - confirm
        email = self.driver.find_element(By.NAME, "reg_email_confirmation__")
        email.send_keys(e_mail)

        # 5. Input password
        passw = self.driver.find_element(By.NAME, "reg_passwd__")
        passw.send_keys(password)
        sleep(1)

        # 6. Select DOB
        day = Select(self.driver.find_element(By.ID, "day"))
        day.select_by_visible_text("17")
        # day.select_by_value('1')
        sleep(1)

        month = Select(self.driver.find_element(By.ID, "month"))
        month.select_by_visible_text("paź")
        # month.select_by_value('6')
        sleep(1)

        year = Select(self.driver.find_element(By.ID, "year"))
        year.select_by_visible_text("2022")
        # year.select_by_value('1993')
        sleep(1)

        # 6. Select sex
        self.driver.find_element(By.XPATH, "//input[@value='1']").click()
        sleep(1)

        # 7. Click button "Zarejestruj się"
        self.driver.find_element(By.NAME, "websubmit").click()
        sleep(1)


if __name__ == '_main_':
    # to uruchom testy
    unittest.main()




