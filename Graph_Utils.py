def read():
    file = open("Google_Graph_template.html", "r")
    html = file.read()
    return html

def save_to_file(html):
    file = open("test.html","w")
    file.write(html)
    file.close()

def jsdata_format(data):
    string=""
    string+="[new Date('"
    string+=data[0:4]
    string+="-"
    string+=data[4:6]
    string+="-"
    string+=data[6:8]
    string+="T"
    string+=data[8:10]
    string+=":00'),"
    return (string)

def add_dados(html,priceline_list,timeline):
    data=""
    for event in range (0,len(priceline_list[0])):
        linha = jsdata_format(str(timeline[event]))
        for pos in range(0,len(priceline_list)):
            linha+=str(priceline_list[pos][event])+","
        linha+="],"
        data+=linha
    html=html.replace("_data_",data)
    return html

#Todo Sort names by last price, low to high
def add_nomes(html,name_list):
    string=""
    for name in name_list:
        newstring="data.addColumn('number', '_name_');"
        string+=newstring.replace("_name_",name)
    html=html.replace("_legend_",string)
    return html

if __name__ == '__main__':
    jsdata_format("2020050612:34")