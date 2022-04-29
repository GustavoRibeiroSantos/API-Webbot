from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    
    chrome = None
    
    def __init__(self):
        self.chrome = self.start_WebDrive()

    def start_WebDrive(self):
        options = Options()
        options.headless = True
        options.add_argument('log-level=3')
        try:
            self.chrome = webdriver.chrome(
                            executable_path="..\Dependencies\chromedriver79_win32\chromedriver.exe",
                            options=options,
                            service_log_path='NUL')
        except :
            try:
                self.chrome = webdriver.Chrome(
                                executable_path="..\Dependencies\chromedriver78_win32\chromedriver.exe",
                                options=options,
                                service_log_path='NUL')
            except :
                self.chrome = webdriver.Chrome(
                                executable_path="..\Dependencies\chromedriver77_win32\chromedriver.exe",
                                options=options,
                                service_log_path='NUL')
        finally:
            return self.chrome
          
    def Wait_Url_Change(self, chrome, Curl):
        WebDriverWait(self.chrome, 60).until(
        lambda driver: self.chrome.current_url != Curl)

    def get_webDrive_result_Page(self, name, url="https://busca.carrefour.com.br"):
        self.chrome.get(url)
        try:
            WebDriverWait(self.chrome, 60).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@class,"js-site-search-input")]'))).send_keys(name)
            WebDriverWait(self.chrome, 60).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@class,"submit-search-icon")]'))).click()
            WebDriverWait(self.chrome, 60).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@class,"neemu-results-per-page-container")]/div/select/option[text()=80]'))).click()
            self.Wait_Url_Change(self.chrome, self.chrome.current_url)
        except:
            return ''
        print(self.chrome.current_url)
        return self.chrome.current_url
        