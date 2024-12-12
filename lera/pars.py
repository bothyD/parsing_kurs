from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.log_on import LogOn
from time import sleep

def inint_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Запуск в фоновом режиме (без GUI)
    # chrome_options.add_argument("--no-sandbox")  # Отключение песочницы
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--disable-dev-shm-usage")  # Отключение использования /dev/shm
    # chrome_options.add_argument("--enable-unsafe-swiftshader")
    # chrome_options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36") 
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def main():
    driver = inint_driver()
    url = 'https://pizzasinizza.ru/novosibirsk'
    page = LogOn(driver)
    page.open(url)
    page.button_log_on_click()
    sleep(2)
    # page_html = driver.page_source
    page.get_all_pizza()
    sleep(2)
    driver.quit()



if __name__ == '__main__':
    main()