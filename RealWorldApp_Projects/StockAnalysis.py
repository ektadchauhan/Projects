from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file

startdate = datetime.datetime(2016,3,1)
enddate = datetime.datetime(2016,3,10)
df = data.DataReader(name="AAPL", data_source="yahoo", start = startdate, end = enddate )
#print(df)

## to get other kinds of financial data from other sources go to pandas-datareader.readthedocs.org

def inc_dec(c,o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value

df["Status"] = [inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
df["Middle"] = (df.Close + df.Open)/2
df["Height"] = abs(df.Close - df.Open)
print(df)

p = figure(title="Candlestick Chart", x_axis_type='datetime', width = 1000, height = 300)

hours_12 = 12 * 60 * 60 * 1000

p.rect(df.index[df.Status=="Increase"], df.Middle[df.Status=="Increase"], hours_12,
       df.Height[df.Status=="Increase"], fill_color="green", line_color="black")

p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"], hours_12,
       df.Height[df.Status=="Decrease"], fill_color="red", line_color="black")

output_file("CS.html")
show(p)