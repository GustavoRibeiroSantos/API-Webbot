from selenium import webdriver 
import os
import time
from tkinter import *

janela = Tk()
janela.title("Webbot Sherlockcups")
janela["bg"]="#3f51b5"

def bt_click():
    browser = webdriver.Chrome()

    prod = bebida_in.get()
    marca = marca_in.get()
    ml = ml_in.get()

    browser.get("https://www.carrefour.com.br/")
    barra = browser.find_element_by_id('js-site-search-input')
    barra.send_keys(prod," ",marca," ",ml)
    barra.submit() 

    browser.find_element_by_xpath('//*[@id="sort-navigation-form"]/div[2]').click()
    browser.find_element_by_xpath('//*[@id="sort-navigation-form"]/div[2]/div/select/option[4]').click()


    time.sleep(10)

    print("Fonte de pesquisa: ",browser.current_url)

    print('Search Results: ')
    search = []
    search = browser.find_elements_by_class_name('product') #Traz uma lista de elementos com a classe 'product' ou []

    for result in search:
        print(result.text) 
    
    browser.quit()

lb1 = Label(font=('Times Woman', 35,'bold'),text="Sherlockcups",bg ="white", width=18)
lb1.grid(row=0, column=0)

title_bebida = Label(font=('Times Woman', 9,'bold'),text="Informe a bebida:",bg ="white")
title_bebida.place(x=100, y=100)
bebida_in = Entry(janela)
bebida_in.place(x=220, y=100)

title_marca = Label(font=('Times Woman', 9,'bold'),text="Informe a marca:",bg ="white")
title_marca.place(x=100, y=130)
marca_in = Entry(janela)
marca_in.place(x=220, y=130)

title_quant = Label(font=('Times Woman', 9,'bold'),text="Informe a quant.:",bg ="white")
title_quant.place(x=100, y=160)
ml_in = Entry(janela)
ml_in.place(x=220, y=160) 
 
bt = Button(janela, text="Pesquisar", width=20, command= bt_click)
bt.place(x=100, y=190)

janela.geometry("500x300+200+200")
janela.mainloop()