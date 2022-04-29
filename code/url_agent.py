from mongodb_connection import *
from browser import *
import json
import requests
import urllib.request
from bs4 import BeautifulSoup

class Url_Agent:
    
    browser = None
    
    def __init__(self):
        self.browser = Browser()
    
    def get_requests_headers(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'
        }
        return headers

    def get_requests_response(self, url):
        headers = self.get_requests_headers()
        return requests.get(url, headers=headers)
    
    def find_results_scraping(self, name):
        result_url = self.browser.get_webDrive_result_Page(name, "https://busca.carrefour.com.br")
        response = self.get_requests_response(result_url)
        soup = BeautifulSoup(response.text, "html.parser")
        json_strings = self.make_json(soup.findAll(class_='nm-product-item'))
        
        return json_strings
    
    def make_json(self, raw_strings):
        json_strings = "["
        size = len(raw_strings)-1
        
        for i, raw_string in enumerate(raw_strings):
            if i == size:
                json_strings = json_strings + raw_string.get('data-product-attr')
            else:
                json_strings = json_strings + raw_string.get('data-product-attr')  + ","
        json_strings = json_strings + "]"

        json_values = json.loads(json_strings)
        
        return json_values
  
    
    def print_results(self, json_strings, brand):
        for json_item in json_strings:
            json_x = json_item.get('data-product-attr')
        json_value = json.loads(json_x)

        try:
            if brand in json_value["brand"]:
                print('Marca: ' + json_value["brand"])
                print('Nome: ' + json_value["productName"])
                print('Preço: ' + json_value["price"])
                print('--------------------------------------------------------')
        except KeyError:
            print('Marca: ')
            print('Nome: ' + json_value["productName"])
            print('Preço: ' + json_value["price"])
            print('--------------------------------------------------------')
            