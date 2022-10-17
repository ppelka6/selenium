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

# Data for registration
first_name = "Arnold"
last_name = "123"
e_mail = "arnoldmasatestpython@test.pl"
password = "tooshort123"

Wait_time = 60

class Registration(unittest.TestCase):
    def setUp(self):
        # Preconditions
        # 1. Registration page open
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://pl-pl.facebook.com/reg")
        # 2. The user is not to be logged in
        # 3. Accept cookies
        self.driver.find_element(By.CSS_SELECTOR, '[data-testid="cookie-policy-manage-dialog-accept-button"]').click()

    def tearDown(self):
        # Finish test
        self.driver.quit()

    def testIncorrectLastName(self):
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
        # select day
        day = Select(self.driver.find_element(By.ID, "day"))
        day.select_by_visible_text("17")
        day.select_by_value('1')
        sleep(1)

        # select month
        month = Select(self.driver.find_element(By.ID, "month"))
        month.select_by_visible_text("paź")
        month.select_by_value('6')
        sleep(1)

        # select year
        year = Select(self.driver.find_element(By.ID, "year"))
        year.select_by_visible_text("2022")
        year.select_by_value('1993')
        sleep(1)

        # 6. Select sex
        self.driver.find_element(By.XPATH, "//input[@value='1']").click()
        sleep(1)

        # 7. Click button "Zarejestruj się"
        self.driver.find_element(By.NAME, "websubmit").click()
        sleep(1)

        # 8. I'm looking for the name and last name field
        fisrtname = self.driver.find_element(By.NAME, "firstname")
        sleep(1)
        lastname = self.driver.find_element(By.NAME, "lastname")
        sleep(1)

        # 9. I am looking for information about a wrongly given DOB
        error_text = self.driver.find_element(locate_with(By.ID, "reg_error_inner"))

        # 10. I check if there is only one such span
        errory = self.driver.find_elements(By.XPATH, '//div[@id="reg_error_inner"]')
        liczba_errorow = len(errory)
        self.assertEqual(liczba_errorow, 1)

        # 11. I check if the content of the slept sounds the same
        self.assertEqual("To imię lub nazwisko zawiera niedozwolone znaki. Dowiedz się więcej na temat naszych zasad dotyczących imion i nazwisk.", error_text.text)

if __name__ == '_main_':
    # to uruchom testy
    unittest.main()




