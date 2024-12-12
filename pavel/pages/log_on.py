from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
import pandas as pd


input_username    = (By.CSS_SELECTOR, 'input[id = "username"]')
input_password    = (By.CSS_SELECTOR, 'input[id = "password"]')
button_log_on     = (By.CSS_SELECTOR, 'button[id = "loginbtn"]')
button_my_course  = (By.CLASS_NAME,   'paging paging-morelink')
list_visit        = (By.CLASS_NAME,   'attlist')
list_normal       = (By.CLASS_NAME,   'normal')
list_highlight    = (By.CLASS_NAME,   'highlight')

first             = (By.CLASS_NAME,   'cell c0')
second            = (By.CLASS_NAME,   'cell c1 lastcol')

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

    def try_to_set_here(self):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.presence_of_element_located(button_log_on))
        button_click = self.find(button_log_on)
        button_click.click()
        
    def get_all_visit(self, response):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.presence_of_element_located(list_visit))
        soup = bs(response, "html.parser")
        all_stats = soup.find(class_='attlist')
        data = []
        for row in all_stats.find_all('tr'):
            title = row.find('td', class_='c0').text.strip()
            value = row.find('td', class_='c1').text.strip()
            data.append((title, value))
        df = pd.DataFrame(data, columns=['Название', 'Показатель'])
        print(df)



    



    
        
    