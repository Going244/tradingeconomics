import tradingeconomics as te
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('client.html')#Client side page to select country name

@app.route('/fetch_data', methods=['POST'])#page for fetched data in form table and chart
def fetch_data():
    te.login('93a6bef24a10492:rp7gmj213iemy5i')
    first_country = request.form['first_country']# Get the first country name from the form
    second_country = request.form['second_country']# Get the second country name from the form

    data1 = te.getHistoricalData(country=[first_country, second_country], indicator='gdp', initDate='2015-01-01')# Get the first and second selected country data from te api
    data1 = data1[1:]

    data = te.getHistoricalData(country=first_country, indicator='gdp', initDate='2010-01-01')# Get the first selected country data from te api
    first_data = list(reversed(data))

    data2 = te.getHistoricalData(country=second_country, indicator='gdp', initDate='2010-01-01')# Get the second selected country data from te api
    second_data = list(reversed(data2))

    return render_template('charttable.html', data=data1, first_data=first_data, second_data=second_data)# Render the data to a new HTML template called charttable.html

if __name__ == '__main__':
    app.run(debug=True)
 
