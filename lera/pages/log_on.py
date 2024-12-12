from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
import pandas as pd
import random

input_username    = (By.CSS_SELECTOR, 'input[id = "username"]')

button_true       = (By.CSS_SELECTOR, 'button[class = "sc-llJcti sc-iIPllB gxHLvf cJuTeS"]')
block_pizza       = (By.CLASS_NAME,   'ContainerForProducts-sc-1cx266l-1 iyxpYe')
pizza             = (By.CLASS_NAME,     'Container-sc-1mnl7tj-0 klRWiP')

button_buy        = (By.CLASS_NAME,  'MainButton-sc-5w3zfk-2 hJsiUL')

class LogOn(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self, link):
        self.browser.get(link)

    def button_log_on_click(self):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.presence_of_element_located(button_true))
        button_click = self.find(button_true)
        button_click.click()

     
    def get_all_pizza(self):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.presence_of_element_located(block_pizza))
        blokc_dam = self.find(block_pizza)
        blocks = self.find_elements_from_block(pizza, blokc_dam)
        # soup = bs(response, "html.parser")
        # all_pizza = soup.find_all(class_='ContainerForProducts-sc-1cx266l-1 iyxpYe')
        # all_pizzas = all_pizza[1].find_all(class_='Container-sc-1mnl7tj-0 klRWiP')
        # print(all_pizzas)
        select = random.randint(0,len(blocks))
        
        button_click = blocks[select].find(button_buy)
        button_click.click()



    # def input_username_block(self, name):  
    #     wait = WebDriverWait(self.browser, 15)
    #     wait.until(EC.presence_of_element_located(input_username))
    #     userName = self.find(input_username)
    #     userName.send_keys(name)

   
    



    
        
    