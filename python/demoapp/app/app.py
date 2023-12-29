import tradingeconomics as te
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('client.html')  # Client side page to select country name, API key and indicator

@app.route('/fetch_data', methods=['POST'])  # Page for fetched data in form table and chart
def fetch_data():
    api = request.form['api']  # Get API to login
    first_country = request.form['first_country']  # Get the first country name from the form
    second_country = request.form['second_country']  # Get the second country name from the form
    indicator_selected = request.form['indicator_selected']# Get a selected indictor
    te.login(api)
    data = te.getHistoricalData(country=[first_country, second_country], indicator=indicator_selected, initDate='2015-01-01')# Fetch the first and second selected country data from te api 
    

    return render_template('charttable.html', data=data)  # Render the data to a new HTML template called new.html

if __name__ == '__main__':
    app.run(debug=True)
