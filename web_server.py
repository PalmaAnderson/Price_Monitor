from flask import Flask, render_template, request,send_from_directory
import os
from importlib import reload 

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#@app.route('./assets/<path:path>')
#def send_file(path):
#    return send_from_directory('assets', path)

@app.route('/')
def index():
    #os.system("python Spread_Plotter.py")
    #graph   = open("graph.html", "r")
    #graph = file.read()
    graph_file    = open("graph.html", "r")
    Graph = graph_file.read()

    html_file    = open("index.html", "r")
    Html = html_file.read()



    Html=Html.replace ("_graph_",Graph)

    #Spread_Plotter.plot(Graph_mode, sell,buy,start,end,vline_min,vline_max)
    #
    #del Spread_Plotter
    #import Spread_Plotter
    return Html
    #return "000"


if __name__ == '__main__':
    app.run(debug=True)
