# three_charts.py

import matplotlib.pyplot as plt # import chart-making package
#import operator # helps to sort correctly
#from pylab import *
import plotly
import plotly.graph_objs as go
import altair as alt
import pandas as pd


#
# CHART 1 (PIE)
#

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

print("----------------")
print("GENERATING PIE CHART...")
#print(pie_data) # TODO: create a pie chart based on the pie_data

# FILTERING

companies =  []
for p in pie_data:
    companies.append(p["company"])

shares =  []
for p in pie_data:
    shares.append(p["market_share"])

# CHART GENERATION (# adapted from: https://plot.ly/python/pie-charts/)

labels = companies
values = shares

trace = go.Pie(labels=labels, values=values)

plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)

# OTHER FORM

#fig1, ax1 = plt.subplots()
#ax1.pie(shares, labels=companies, autopct='%1.1f%%', shadow=True, startangle=90)
#ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

#plt.show() # need to explicitly "show" the chart window


#
# CHART 2 (LINE)
#

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

print("----------------")
print("GENERATING LINE GRAPH...")
#print(line_data) # TODO: create a line graph based on the line_data

# FILTERING

list_dates =  []
for p in line_data:
    list_dates.append(p["date"])

stock_price =  []
for p in line_data:
    stock_price.append(p["stock_price_usd"])

# CHART GENERATION 

plotly.offline.plot({
    "data": [go.Scatter(x=list_dates, y=stock_price)],
    "layout": go.Layout(title="Stock Price Chart")
}, auto_open=True)
plot(list_dates, stock_price)
show()

#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

print("----------------")
print("GENERATING BAR CHART...")
#print(bar_data) # TODO: create a horizontal bar chart based on the bar_data

# FILTERING

genres =  []
for p in bar_data:
    genres.append(p["genre"])

watching =  []
for t in bar_data:
    watching.append(t["viewers"])

# CHART GENERATION 

source = pd.DataFrame({
    "a": genres,
    "b": watching
})

chart = alt.Chart(source).mark_bar().encode(
    x="a",
    y="b"
)

chart.serve()