import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.charts import Bar
import bokeh.plotting as bh
from collections import OrderedDict
from bokeh.charts import Bar, output_file, show
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn import svm



def read_files(file0='co2.csv',file1='temperature.csv',file2='CO2_by_country.csv'):
    """
    Reads in the csv files and stores them as csv obj
    """

    infile0=pd.read_csv(file0)                                          
    infile1=pd.read_csv(file1)                                          
    infile2=pd.read_csv(file2)                                          
    
    return infile0,infile1,infile2
def make_plot(temp_month="January",co2_range=(1940,2007),temp_range=(1943,2001),cUL=(1,2)):
    """
    Make plots takes in different parameters and converts it to html files that can be read later
    
    """
    
    co2,temp,c=read_files()
    
    """
    Co2 first
    """
    p = bh.figure(title="co2", x_axis_label='Year', y_axis_label='Carbon')
    l=list(co2.get("Year"))
    lfrom=l.index(co2_range[0])
    lto=l.index(co2_range[1])
    m=list(co2.get("Carbon"))
    p.line(l[lfrom:lto],m[lfrom:lto], legend=f"{co2_range[0]}-{co2_range[1]}", line_width=2)
    if __name__=='__main__':
        bh.show(p)    
    else:
        bh.save(p, filename="co2.html")

    
    """
    Temp second
    """
    p = bh.figure(title="temperature", x_axis_label='Year', y_axis_label=temp_month)
    l=list(temp.get("Year"))
    lfrom=l.index(temp_range[0])
    lto=l.index(temp_range[1])
    m=list(temp.get(temp_month))
    p.line(l[lfrom:lto],m[lfrom:lto], legend=f"{temp_month} {temp_range[0]}-{temp_range[1]}", line_width=2)
    if __name__=='__main__':
        bh.show(p)    
    else:
        bh.save(p, filename="temp.html")
   
    """
    country third
    """
    c=c.drop("Country Name",1)
    c=c.drop("Indicator Name",1)
    c=c.drop("Indicator Code",1)
    c=c.T
    c=c.fillna(0)
    val=[]
    country=[]
    upper=cUL[0]
    lower=cUL[1]
    for i in range(1,len(c.axes[1])):
        tmp=sum(c.get(i)[1:-1])
        if tmp> upper and tmp < lower: 
            val.append(tmp)
            country.append(c.get(i)[0])
    data = {
        'sample': country,
        'timing': val
    }
    p = Bar(data, values='timing', label='sample',
          title="Emissions",
          legend='top_left', plot_width=1000, xlabel="Country", ylabel="Co2")
    if __name__=='__main__':
        bh.show(p)    
    else:
        bh.save(p, filename="country.html")
   

 
    """
    prediction 4th
    """
    p = bh.figure(title="prediction", x_axis_label='x', y_axis_label='y')
    l=list(co2.get("Year"))
    lfrom=l.index(co2_range[0])
    lto=l.index(co2_range[1])
    m=list(co2.get("Carbon"))
    a,b,c,d=interpolation(temp_range[1])
    p.line(a,b, legend=f"prediction", line_width=2)
    p.line(c,d, legend=f"actual", line_width=2)
    if __name__=='__main__':
        bh.show(p)    
    else:
        bh.save(p, filename="pred.html")

def interpolation(to):
    """
    Does an interpolation in to the future equal to the year "to"
    """
    a,b,c=read_files()
    
    l=list(a.get("Year"))
    m=np.array(list(a.get("Carbon")))
    n=np.array(list(b.get("Year")))
    o=np.array(list(b.get("January")))
    start=l.index(n[0])
    l=l[start:]
    m=m[start:]
    svmn=[]
    for i in range(len(n)):
        svmn.append([n[i],m[i]])
        
    svmn=np.array(svmn)
    svmn = svmn[:, np.newaxis]
    #m = m[:, np.newaxis]
    #o = o[:, np.newaxis]
    n1 = n[:, np.newaxis]
    
    
    linreg = LinearRegression(normalize=True)
    logreg = LogisticRegression()
    svmreg = svm.SVR()
    
    logreg.fit(n1,m)
    linreg.fit(n1,m)
    svmreg.fit(n1,o)
    ret=[]
    ret1=[]
    ret2=[]
    n2=list(n)+list(np.arange(n[-1]+1,to))
    for i in n2:
        ret.append(linreg.predict(i)) 
        ret1.append(logreg.predict(i)) 
        ret2.append(svmreg.predict(i)) 
    plt.plot(n2,ret)
    return n2,ret,n,m
