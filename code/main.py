from scraper import *
from pprint import pprint

def menu ():
    print('1 - Fazer uma pesquisa: ')
    print('2 - Produtos mais pesquisados: ')
    print('3 - Sair')
    return input()

scraper_instance = scraper()

while(1):
    option = menu()
    if option == '1':
        print("Encontre um produto: ")
        busca = input()
        result = scraper_instance.search(busca)
        for jsn in result:
            #print(jsn)
            print(jsn['productName'])
        
    elif option == '2':
        print("WIP")
    elif option == '3':
        break
    elif option == '666':
        scraper_instance.clear_db()
    else:
        print('Opção inválida!')
        

