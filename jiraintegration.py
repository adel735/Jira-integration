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
login=driver.find_element(By.ID, 'user_login')
login.send_keys(GITLAB_USER)
password=driver.find_element(By.ID, 'user_password')
password.send_keys(GITLAB_PASS)
login_butt = driver.find_element(By.NAME, 'commit')
login_butt.click()

driver.switch_to.new_window('window')
driver.get(ADMINAREA)
jira_url = driver.find_element(By.ID, 'service_url')
jira_url.send_keys(JIRA_URL)
#service_url = driver.find_element(By.ID, 'service_api_url')
#service_url.send_keys(JIRA_API)
jira_user = driver.find_element(By.ID, 'service_username')
jira_user.send_keys(JIRA_USER)
jira_pass = driver.find_element(By.ID, 'service_password')
jira_pass.send_keys(JIRA_PASS)
confirm = driver.find_element(By.CLASS_NAME, 'gl-button-text')
confirm.click()
save = driver.find_element(By.XPATH,'//*[@id="confirmSaveIntegration___BV_modal_footer_"]/button[2]/span')
save.click()