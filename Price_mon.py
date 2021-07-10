from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mockito import when, mock, unstub
import re, sqlite3,time
import Utils
import busca
#pip install pipreqs
#pipreqs path/to/project
#$ pip install -r requirements.txt

class prices:
    def __init__(self,site, price,link_id):
        self.site       = site
        self.price      = price
        self.link_id    = link_id


if __name__ == '__main__':
    conn = sqlite3.connect('private/db_price_mon.db')
    cursor = conn.cursor()
    busca.init()
    busca.init() #Chamando duas vezes para teste do singleton
    
    prices_list=[]
    cursor.execute("""SELECT site_name, site_selector_type, site_selector_name, link_id, url FROM Links,Sites WHERE Links.site_id=Sites.site_id;""")
    for item in cursor.fetchall():
        site,seletor,nome,link_id,link=Utils.SQL_adapter(item)
        site,seletor,nome,link=Utils.handle_busca(site,seletor,nome,link)
        string_price=busca.get_price(site,seletor,nome,link)
        price=Utils.pricetofloat(string_price)
        prices_list.append(prices(site, price, link_id))

    busca.stop
    conn.close()

    print("\n\n    Resultados\n##################\n")
    time=Utils.current_time()
    for x in range(0,len(prices_list)):
        print (prices_list[x].price,"\t",prices_list[x].site)
        Utils.handle_db_write(prices_list[x].price, prices_list[x].link_id,time)
    print("end\t",time)

    import Price_plot