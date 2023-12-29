## Flask Economic Indicator Data Visualization App

This Flask app is designed to display an HTML form for users to input their API key, select an economic indicator, and choose a country. When the user clicks the "Fetch Data" button, the app will display a table and chart of the fetched data on a separate page.
#

## To run this project locally, follow these steps:

Clone the repository: 

` git clone https://github.com/Going244/tradingeconomics.git`
      
Install the required packages:

```
cd tradingeconomics/python/demoapp

pip install tradingeconomics

pip install flask 
   ```

Run the Flask application:

  ```
  cd app
  python app.py

```
   

Open a web browser and go to http://localhost:5000 to access the application.

#

<h2> Usage </h2>

1. Enter your API key 
2. Select Country: On the home page, users will see a dropdown menu where they can select the country name for which they want to compare the economic.

3. Select economic indicator

4. Click fetch data: Once the data is fetched, users will see a table displaying the economic indicator selected values for each year or time period, as well as a chart that visually compares the selected indicator trends of the selected country with another default country (e.g., Mexico and Sweden).</p>

<h2> Project Structure</h2>

<h5>The project consists of the following files and directories:</h5>

<p>- app.py: This file contains the Flask application code, including routes and data fetching logic.
- templates/: This directory contains HTML templates for the web pages, including the home page and result page.


</p>
