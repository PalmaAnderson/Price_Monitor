from selenium import webdriver
from mockito import when, mock, unstub
import re


#pip install pipreqs
#pipreqs path/to/project
#$ pip install -r requirements.txt

class prices:
    def __init__(self,site, price):
        self.site = site
        self.price = price

def pricetofloat(price):
    try:
        price=price.replace(".", "")
    except:
        pass
    
    try:
        price=price.replace(",", ".")
    except:
        pass

    try:
        price=price.replace(" ", "")
    except:
        pass

    try:
        price=price.replace("R$", "")
    except:
        pass

    return float(price)

def busca(site,seletor,nome,link):

    driver.get(link)
    try:
        price=0
        if seletor=="Class":
            price=driver.find_element_by_class_name(nome).text
        if seletor=="Id":
            price = driver.find_element_by_id(nome).text
    except:
        price=0

    return price

if __name__ == '__main__':
    PATH = "C:\Program Files\chromedriver90.exe"
    driver = webdriver.Chrome(PATH)
    file = open("Links.csv", "r")

    enablemock=0
    if enablemock:
        string="\nAmericanas;Class;priceSales;https://www.americanas.com.br/produto/2918844258?opn=YSMESP&WT.srch=1&sellerid=5140309000109\n"
        when(file).read(...).thenReturn(string)

    param = file.read()
    itens = param.split("\n")

    prices_list=[]
    for x in range(1, len(itens)-1):
        item = itens[x].split(";")
        site = str(item[0])
        seletor = str(item[1])
        nome = str(item[2])
        link = str(item[3])

        price=busca(site,seletor,nome,link)
        price=pricetofloat(price)
        
        prices_list.append(prices(site, price))
    driver.quit
    print("\n\n    Resultados\n##################\n")
    for x in range(0,len(prices_list)):
        print (prices_list[x].site,"\t",prices_list[x].price)