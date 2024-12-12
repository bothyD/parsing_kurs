from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from time import sleep
import re


input_username = (By.CSS_SELECTOR, 'input[id = "username"]')
input_password = (By.CSS_SELECTOR, 'input[id = "password"]')
button_log_on  = (By.CSS_SELECTOR, 'button[id = "loginbtn"]')



class LogOn(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self, link):
        self.browser.get(link)



    def button_log_on_click(self):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.presence_of_element_located(button_log_on))
        button_click = self.find(button_log_on)
        button_click.click()

    def input_username_block(self, name):  
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.presence_of_element_located(input_username))
        userName = self.find(input_username)
        userName.send_keys(name)
        
    def input_password_block(self, password):  
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.presence_of_element_located(input_password))
        passwordUser = self.find(input_password)
        passwordUser.send_keys(password)  

    



    
        
    