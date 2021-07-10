import sqlite3
import Graph_Utils

conn = sqlite3.connect('private/db_price_mon.db')
cursor = conn.cursor()

timeline_list=[]
priceline_list=[]
name_list=[]
time_list=[]
fuckinmatrix=[]
cursor.execute("""SELECT * FROM (SELECT distinct(time) FROM Quotes ORDER BY time desc limit 100)  ORDER BY time ASC""")
for time in cursor.fetchall():
    time_list.append(time[0])

for x in range (0, len (time_list)):
    sql="SELECT Quotes.link_id,site_name, price,time FROM Links,Sites, Quotes where Links.site_id=Sites.site_id and Quotes.link_id=Links.link_id and time="+str(time_list[x])+";"
    cursor.execute(sql)
    for j in cursor.fetchall():
        print (j)
        #todo > entre N americanas(s), encontrar o link mais barato, sobrando só um preço pra cada loja (ou grupo)
        # append encadeado X appendy
####



###### OLD ####
for x in range (4,11):
    sql="Select Quotes.link_id,site_name, price,time from Links,Sites, Quotes where Links.site_id=Sites.site_id and Quotes.link_id=Links.link_id and Quotes.link_id=?"
    cursor.execute(sql.replace("?",str(x)))
    
    timeline=[]
    priceline=[]
    for item in cursor.fetchall():
        timeline.append(item[3])
        if item[2]>0:
            priceline.append(item[2])
        else:
            priceline.append('null')
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

#todo passar tudo em ingles
#todo pastas

html=Graph_Utils.read()
html=Graph_Utils.add_info(html,priceline_list,timeline)
html=Graph_Utils.add_names(html,name_list)
Graph_Utils.save_to_file(html)

print ("End Plot")  