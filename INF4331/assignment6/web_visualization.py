from flask import Flask, render_template, request
import pandas as pd
from bokeh.charts import Histogram
from bokeh.embed import components
from temperature_CO2_plotter import *
app = Flask(__name__)

@app.route("/")
def index():
     months=["January","February","March","April","May","June","July","August","September","October","November","December"]
     
     month = request.args.get("month")
     if month == None or month == '':
          month = "January"
     tempfrom = request.args.get("tempfrom")
     if tempfrom == None or tempfrom == '':
          tempfrom = 1950
     tempto = request.args.get("tempto")
     if tempto == None or tempto == '':
          tempto = 1999
     co2from = request.args.get("co2from")
     if co2from == None or co2from == '':
          co2from = 1970
     co2to = request.args.get("co2to")
     if co2to == None or co2to == '':
          co2to = 2007

     cto = request.args.get("cto")
     if cto == None or cto == '':
          cto = 0
     cfrom = request.args.get("cfrom")
     if cfrom == None or cfrom == '':
          cfrom = 100

     arguments=[month,(int(co2from),int(co2to)),(int(tempfrom),int(tempto)),(int(cto),int(cfrom))]
     make_plot(arguments[0],arguments[1],arguments[2],arguments[3])

     return render_template("template.html", script=open("temp.html").read(),script2=open("co2.html").read(),script3=open("country.html").read(),script4=open("pred.html").read(),months=months,month=month,tempfrom=tempfrom,tempto=tempto,co2from=co2from,co2to=co2to,cto=cto,cfrom=cfrom)


if __name__=='__main__':
     app.run(debug=True)