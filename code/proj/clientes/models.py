from django.db import models
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Model:

    def buscarProdutoCarrefour(browser, product_procurado):
        
        browser.get("https://mercado.carrefour.com.br/")
        time.sleep(15)
        browser.find_element(By.CSS_SELECTOR, ".css-161xdxb:nth-child(2) > .css-9sqocg").click()
        time.sleep(15)
        browser.find_element(By.CSS_SELECTOR, ".searchPickupPointsSelect").click()
        dropdown = browser.find_element(By.CSS_SELECTOR, ".searchPickupPointsSelect")
        dropdown.find_element(By.XPATH, "//option[. = 'UBERLANDIA - MG']").click()
        browser.find_element(By.CSS_SELECTOR, ".css-11sx5j3").click()
        element = browser.find_element(By.CSS_SELECTOR, ".css-17363ei")
        time.sleep(15)
        browser.find_element(By.CSS_SELECTOR, ".css-hnst61 input").click()
        browser.find_element(By.CSS_SELECTOR, ".css-hnst61 input").send_keys(product_procurado)
        browser.find_element(By.CSS_SELECTOR, ".css-hnst61 input").send_keys(Keys.ENTER)
        time.sleep(15)

        products_carrefour = []
        imgs_products = browser.find_elements(By.CSS_SELECTOR, ".css-j0j5gy")
        desc_products = browser.find_elements(By.CSS_SELECTOR, ".css-1rgidqc")
        price_products = browser.find_elements(By.CSS_SELECTOR, ".css-1ntr1be")
        # Traz uma lista de elementos com a classe 'product' ou []
        for i in range(0,len(imgs_products)):
            product = { 
                'img': imgs_products[i].get_attribute("src"),
                'desc': desc_products[i].text,
                'price': price_products[i].text
            }
            products_carrefour.append(product)

        return products_carrefour;


# Create your models here.
