from selenium import webdriver
PATH="C:\Program Files\chromedriver90.exe"

driver=webdriver.Chrome(PATH)

driver.get("https://www.kabum.com.br/produto/99679/placa-de-video-zotac-nvidia-geforce-rtx-2060-twin-fan-6gb-gddr6-zt-t20600f-10m")
print(driver.title)

#preco=driver.find_element_by_class_name("preco_desconto")
#print(preco.text)
##
driver.get("https://www.mercadolivre.com.br/placa-de-video-nvidia-galax-geforce-rtx-20-series-rtx-2060-26nrl7hpx7oc-6gb/p/MLB15971892")
print(driver.title)

preco=driver.find_element_by_class_name("price-tag-fraction")
print(preco.text)
##
driver.get("https://www.terabyteshop.com.br/produto/10304/placa-de-video-galax-geforce-rtx-2060-1-click-oc-6gb-26nrl7hpx7oc-gddr6-pci-exps")
print(driver.title)

preco=driver.find_element_by_id("valVista")
print(preco.text)

driver.quit