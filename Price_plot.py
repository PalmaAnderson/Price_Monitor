import sqlite3
import Graph_Utils

conn = sqlite3.connect('private/db_price_mon.db')
cursor = conn.cursor()

timeline_list=[]
priceline_list=[]
name_list=[]
for x in range (4,11):
    sql="Select Quotes.link_id,site_name, price,time from Links,Sites, Quotes where Links.site_id=Sites.site_id and Quotes.link_id=Links.link_id and Quotes.link_id=?"
    cursor.execute(sql.replace("?",str(x)))

    timeline=[]
    priceline=[]
    for item in cursor.fetchall():
        timeline.append(item[3])
        priceline.append(item[2])
        timeline.clear
        priceline.clear

    timeline_list.append(timeline)
    priceline_list.append(priceline)
    timeline.clear
    priceline.clear

for x in range (4,11):
    sql="Select site_name from Links,Sites, Quotes where Links.site_id=Sites.site_id and Quotes.link_id=Links.link_id and Quotes.link_id=?"
    cursor.execute(sql.replace("?",str(x)))
    for item in cursor.fetchall():
        name_list.append(item[0])
        break

html=Graph_Utils.read()
html=Graph_Utils.add_dados(html,priceline_list,timeline)
html=Graph_Utils.add_nomes(html,name_list)
Graph_Utils.save_to_file(html)

print ("End ")  