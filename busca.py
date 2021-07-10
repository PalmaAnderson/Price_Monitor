from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mockito import when, mock, unstub
import re, sqlite3,time
import Utils

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

def stop():
    driver.quit

def get_price(site,seletor,nome,link):
    
    #b2w "Please verify you are a human"

    if site=="Kabum":
        try:
            import secret
            string_price=secret.loja_que_explode(link)
        except:
            string_price="0"
        finally:
            print(string_price)
            return string_price

    driver.get(link)

    #todo implementar o loop wait element
    if site=="Casasbahia" or site=="Extra":
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

# somente um browser aberto
@singleton     #decorator
def init():
    PATH = "C:/Program Files/geckodriver.exe"
    profile = webdriver.FirefoxProfile()
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    desired = DesiredCapabilities.FIREFOX

    global driver
    driver = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired)