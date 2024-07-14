from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from settings import CHROMEDRIVER_PATH, GITLAB_IP, GITLAB_USER, GITLAB_PASS, ADMINAREA,JIRA_URL, JIRA_USER, JIRA_PASS, JIRA_API
from selenium.webdriver.chrome.options import Options

import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path=CHROMEDRIVER_PATH)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(GITLAB_IP)

driver.find_element(By.ID, 'user_login').send_keys(GITLAB_USER)

driver.find_element(By.ID, 'user_password').send_keys(GITLAB_PASS)

driver.find_element(By.NAME, 'commit').click()


driver.switch_to.new_window('window')

driver.get(ADMINAREA)

driver.find_element(By.ID, 'service_url').send_keys(JIRA_URL)

#driver.find_element(By.ID, 'service_api_url').send_keys(JIRA_API)

driver.find_element(By.ID, 'service_username').send_keys(JIRA_USER)

driver.find_element(By.ID, 'service_password').send_keys(JIRA_PASS)

driver.find_element(By.CLASS_NAME, 'gl-button-text').click()

driver.find_element(By.XPATH,'//*[@id="confirmSaveIntegration___BV_modal_footer_"]/button[2]/span').click()
