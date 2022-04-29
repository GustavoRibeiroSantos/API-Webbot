import pymongo
from pymongo import MongoClient
from scraper import *
from datetime import datetime
from datetime import date, timedelta
        

class MongoDB_Connection:
    
    db_instance = None
    collection = None
    
    def __init__(self):
        self.db_instance = self.create_connection()
        self.collection = self.get_collection()

    def create_connection(self):
        return pymongo.MongoClient(
            "mongodb+srv://biqc:admin123@scraperpi-cd9zl.gcp.mongodb.net/test?retryWrites=true&w=majority")

    def get_collection(self):
        return self.db_instance.web_bot.products

    def insert_product(self, product):
        product['created_time'] = datetime.now()
        return self.collection.insert_one(product)

    def insert_products(self, products):
        for product in products:
            product['created_time'] = datetime.now()
        return self.collection.insert_many(products)

    # def find_products_by_name(self, name):
    #     return self.collection.find({"name": name})

    # def find_products_by_brand(self, brand):
    #     return self.collection.find({"brand": brand})

    def find_products(self, value):
        
        today = datetime.now()
        
        yesterday = (datetime.now()-timedelta(1))
        
        queryArray = value.split()
        queryText = ''
        for string in queryArray:
            queryText += "\"" + string + "\""
             
        result = self.collection.find({
                                       '$text' : { '$search' : queryText },
                                       'created_time' : { '$gte': yesterday }
                                       },
                                      { 
                                       'score' : { '$meta' : "textScore" }
                                       }).sort([
                                               ('score' , { '$meta' : "textScore" })
                                               ])
        return result
            
    def find_products_older(self, value):
        return self.collection.find({"name": value},{'score' : { '$meta' : "textScore" }}).sort([('score' , { '$meta' : "textScore" }),('created_time' , 1 )])
    
    def clear_collection(self):
        self.collection.delete_many({})
        
#db.system.namespace.find( { name: 'test.' + collName } ); encontrar uma coleção