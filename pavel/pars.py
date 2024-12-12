from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.log_on import LogOn
from time import sleep
from KEYS_SECRET import PASSWORD_KEY, LOGIN_KEY

def inint_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Запуск в фоновом режиме (без GUI)
    chrome_options.add_argument("--no-sandbox")  # Отключение песочницы
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")  # Отключение использования /dev/shm
    chrome_options.add_argument("--enable-unsafe-swiftshader")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36") 
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def main():
    driver = inint_driver()
    url = 'https://eios.sibsutis.ru/login/index.php'
    page = LogOn(driver)
    page.open(url)
    page.input_username_block(LOGIN_KEY)
    page.input_password_block(PASSWORD_KEY)
    sleep(1)
    page.button_log_on_click()
    page.open('https://eios.sibsutis.ru/mod/attendance/view.php?id=58889')
    try:
        page.try_to_set_here()
    except:
        print("not time to study :)\nsee you later!")
    
    page.open('https://eios.sibsutis.ru/mod/attendance/view.php?id=58889&view=5')
    sleep(2)
    page_html = driver.page_source
    page.get_all_visit(page_html)
    sleep(2)
    driver.quit()



if __name__ == '__main__':
    main()