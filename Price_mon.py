from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mockito import when, mock, unstub
import re, sqlite3,time
import Utils



#pip install pipreqs
#pipreqs path/to/project
#$ pip install -r requirements.txt

class prices:
    def __init__(self,site, price,link_id):
        self.site       = site
        self.price      = price
        self.link_id    = link_id

def busca(site,seletor,nome,link):

    if site=="Kabum":
        try:
            import secret
            string_price=secret.loja_que_explode(link)
        except:
            string_price="0"
        print(string_price)
        return string_price
        
    driver.get(link)
    if site=="Casasbahia":
        time.sleep(3)

    try:
        string_price="0"
        if seletor=="Class":
            string_price=driver.find_element_by_class_name(nome).text
        if seletor=="Id":
            string_price = driver.find_element_by_id(nome).text
        if seletor=="Css":
            string_price = driver.find_element_by_css_selector(nome).text
    except:
        string_price="0"

    if site=="Carrefour":
        time.sleep(3)
        try:
            string_price=driver.find_elements_by_class_name(nome)[1].text
        except:
            string_price="0"



    print(string_price)
    return string_price

if __name__ == '__main__':
    PATH = "C:/Program Files/geckodriver.exe"
    profile = webdriver.FirefoxProfile()
    #profile = webdriver.FirefoxProfile('C:\\Users\\aande\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\umjmt3v7.default-release')
    #PROXY_HOST = "12.12.12.123"
    #PROXY_PORT = "1234"
    #profile.set_preference("network.proxy.type", 1)
    #profile.set_preference("network.proxy.http", PROXY_HOST)
    #profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    desired = DesiredCapabilities.FIREFOX
    driver = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired)

    conn = sqlite3.connect('private/db_price_mon.db')
    cursor = conn.cursor()
  
    prices_list=[]
    cursor.execute("""SELECT site_name, site_selector_type, site_selector_name, link_id, url FROM Links,Sites WHERE Links.site_id=Sites.site_id;""")
    for item in cursor.fetchall():
        site,seletor,nome,link_id,link=Utils.handle_link_read(item)
        site,seletor,nome,link=Utils.handle_busca(site,seletor,nome,link)
        string_price=busca(site,seletor,nome,link)
        price=Utils.pricetofloat(string_price)
        prices_list.append(prices(site, price, link_id))

    driver.quit
    conn.close()

    print("\n\n    Resultados\n##################\n")
    time=Utils.current_time()
    for x in range(0,len(prices_list)):
        print (prices_list[x].price,"\t",prices_list[x].site)
        Utils.handle_db_write(prices_list[x].price, prices_list[x].link_id,time)
    print("end\t",time)

 