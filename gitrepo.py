from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import lxml

##############################
email =  '***************'
password = '*******'
##############################


username='//*[@id="login_field"]'
Password='//*[@id="password"]'
login='/html/body/div[3]/main/div/div[4]/form/div/input[12]'

Create_repo='/html/body/div[4]/main/div/form/div[4]/button'
repo_name='//*[@id="repository_name"]'

def makerepo(reponame):
    try:
        driver = webdriver.Firefox(executable_path=r'geckodriver.exe')

        driver.get('https://github.com/new')
        time.sleep(2)
        driver.find_element_by_xpath(username).send_keys(email)
        driver.find_element_by_xpath(Password).send_keys(password)
        time.sleep(0.25)
        driver.find_element_by_xpath(login).click()
        time.sleep(2)
        driver.find_element_by_xpath(repo_name).send_keys(reponame)
        time.sleep(3)
        driver.find_element_by_xpath(Create_repo).click()
        
        result='repository was created successfully.'
    except:
        result='Erreur repository not created!'

    return(result)




