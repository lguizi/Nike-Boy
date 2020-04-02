from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:\\Users\\XXX\\Desktop\\chromedriver') #Localização do Chromedriver


def inicio():
    driver.get('https://www.nike.com.br/')
    logar()

def logar():
    try:
        logBt =  WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable((By.ID, 'anchor-acessar'))
        )
        logBt.click()

        digitaEmail = WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located((By.NAME, 'emailAddress'))
        )
        digitaEmail.send_keys('testetesteteste')

        digitaSenha = WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located((By.NAME, 'password'))
        )
        digitaSenha.send_keys('testetesteteste')
        digitaSenha.send_keys(Keys.ENTER)

    except:
        inicio()

inicio()
