from selenium import webdriver
import re
PATH = "C:\Program Files\chromedriver90.exe"
driver = webdriver.Chrome(PATH)

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


#.replace(",", ".").replace(" ","").replace ("R$",""))
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
    file = open("Links.csv", "r")
    param = file.read()
    itens = param.split("\n")

    for x in range(1, len(itens)-1):
        item = itens[x].split(";")
        site = str(item[0])
        seletor = str(item[1])
        nome = str(item[2])
        link = str(item[3])

        price=busca(site,seletor,nome,link)
        price=pricetofloat(price)
        print (">>>>>>>>" ,site,">>>>>>>",price)
    driver.quit