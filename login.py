from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import os
import time
from tqdm import tqdm
import telebot

# write options for webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(options)
report_url = 'https://app.powerbi.com/groups/me/reports/3544cb46-8f17-411d-8d6a-f874ef078eb3/ReportSection?experience=power-bi'
driver.get(report_url)

for i in tqdm(range(1)):
    time.sleep(0.3)

# load login and password from .env
load_dotenv()
pbi_user = os.getenv("USER_PBI")
pbi_pass = os.getenv("PASSWORD_PBI")
TOKEN_ver = os.getenv("TG_TOKEN2")
ID_TG2 = os.getenv("ID_TG2")

tries = 4
for num_of_tries in range(tries):
# submit email
    try:
        email = driver.find_element(By.ID, "email")
        email.send_keys(pbi_user)
        submit_email = driver.find_element(By.ID, "submitBtn")
        submit_email.click()
        for i in tqdm(range(3)):
            time.sleep(1)
        print('EMAIL WAS WRITTEN SUCCESSFULLY')

# submit password
        password = driver.find_element(By.ID, "i0118")
        password.send_keys(pbi_pass)
        submit_pass = driver.find_element(By.ID, "idSIButton9")
        submit_pass.click()
        for i in tqdm(range(2)):
            time.sleep(1)
        print('PASSWORD WAS WRITTEN SUCCESSFULLY')

# submit in another way (2-factor authentication)
        check_method = driver.find_element(By.XPATH, '//*[@id="idRichContext_DisplaySign"]')
        bot2 = telebot.TeleBot(TOKEN_ver, parse_mode=None)
        bot2.send_message(ID_TG2,check_method.text)
        for i in tqdm(range(20)):
            time.sleep(1)

# don`t log out
        dont_log = driver.find_element(By.ID, 'idBtn_Back')
        dont_log.click()
        print("ACCOUNT LOGGED SUCCESSFULLY")


    except BaseException as error:
        if num_of_tries < tries - 1:
            continue
        else:
            raise
    break



