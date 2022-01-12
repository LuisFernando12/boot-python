import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome() 
driver.get('https://theonegenerator.com/pt/geradores/documentos/gerador-de-email/')

def getEmail() :    
    time.sleep(5)  
    password = str(uuid.uuid4())
    password = password.split("-")[-1]
    
    time.sleep(5)  
    driver.find_element(By.CSS_SELECTOR,'#app-content > section > div.container > div > div.col > div.generator-container > div > div > div > div.generator > form > button').click()
    email = driver.find_element(By.CSS_SELECTOR,'#copyToClipboard-email').get_attribute("value")
    username = email.split('@')[0]
    fullname = email.split('@')[0]
   
    time.sleep(5)  

    create(fullname, username, email, password)
    
def create (fullname, username, email, password) :
    driver.get("https://soclaieau.xyz/3062363869014")
    test = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/div/div/div/div[2]/div/div[1]/a').get_attribute("href")
    print(test)
    time.sleep(5)
    driver.get('https://soclaiegb.xyz/register.php')
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '#fullname').send_keys(fullname)
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, '#email').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '#passwordAgain').send_keys(password)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'custom-control-input').click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, ".btn-auth").click()
    time.sleep(10)
    driver.quit()
    time.sleep(5) 
    getEmail()
      
time.sleep(5) 

getEmail()

