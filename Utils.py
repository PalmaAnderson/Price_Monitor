import sqlite3, time

def SQL_adapter(item):
    site_name           = str(item[0])
    site_selector_type  = str(item[1])
    site_selector_name  = str(item[2])
    link_id             = str(item[3])
    url                 = str(item[4])
    print (site_name, end="\t")

    return (site_name,site_selector_type,site_selector_name,link_id,url)

def handle_busca(site,seletor,nome,link):
    if site=="Kabum":
        #link="about:blank"
        pass

    if link=="":
        link="about:blank"

    enableSkip=0
    if enableSkip:
        if site!="Americanas":
            link="about:blank"

    return site,seletor,nome,link

def pricetofloat(i_price):
    price=i_price
    try:
        price=price.replace("à vista ", "")
    except:
        pass
    
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

def current_time():
    return (time.strftime('%Y%m%d%H%M'))
    #202105101630

def handle_db_write(price,link_id,time):
    #todo keep connection open
    enableSQLwrite=1
    if enableSQLwrite:
            
        conn = sqlite3.connect('private/db_price_mon.db')
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO Quotes (link_id, price,time) VALUES (?,?,?) """, (link_id,price,time))
        conn.commit()

        conn.close()
    else:
        print("!!", end="")
        
if __name__ == '__main__':
    print("Utils.py não deve ser executada isolamente")


