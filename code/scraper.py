from mongodb_connection import *
from url_agent import *
import json
import requests
import urllib.request
from bs4 import BeautifulSoup

class scraper:
    
    db_instance = None
    url_agent = None
    
    def __init__(self):
        self.db_instance = MongoDB_Connection()
        self.url_agent = Url_Agent()
        
    # def find_results_db(self, name, brand='', price=None):
    #     collection = self.db_instance.get_collection()
    #     results = self.db_instance.find_products(name, brand, collection)
    #     return results

    def search(self, productName):
        results = self.db_instance.find_products(productName)
        if results.count() == 0:
            print("Scraping...")
            results = self.url_agent.find_results_scraping(productName)
            self.db_instance.insert_products(results)
            
        else:
            print("Database response...")
        return results
    
    def get_item_timeline(self, productName):
        results = self.db_instance.find_products_older(productName)
        return results
    
    def clear_db(self):
        self.db_instance.clear_collection()