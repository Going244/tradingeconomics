<h1> GDP Comparison Project<h1>

<p> This project is a Flask web application that allows users to compare the GDP (Gross Domestic Product) of two different countries. Users can select the country name from a dropdown menu, and the application will fetch the GDP data for the selected country. The GDP data is then displayed in the form of a table and a chart, allowing users to visually compare the GDP trends of the two countries.</p>
</h3>To run this project locally, follow these steps:</h3>

<h2>1. Clone the repository: </h2>

   `git clone https://github.com/Going244/tradingeconomics.git`
      
   

3. Install the required dependencies:

 `cd python/demoapp/app`

   pip install tradingeconomics


   pip install flask `
   

5. Run the Flask application:

  ` cd demoapp/app<br>python app.py `
   

7. Open a web browser and go to http://localhost:5000 to access the application.


<h2> Usage </h2>

<p>1. Select Country: On the home page, users will see a dropdown menu where they can select the country name for which they want to compare the GDP.

2. Fetch Data: After selecting the country, users can click on a "Fetch Data" button to retrieve the GDP data for the selected country.

3. View Comparison: Once the data is fetched, users will see a table displaying the GDP values for each year or time period, as well as a chart that visually compares the GDP trends of the selected country with another default country (e.g., Mexico and Sweden).</p>

<h2> Project Structure</h2>

<h5>The project consists of the following files and directories:</h5>

<p>- app.py: This file contains the Flask application code, including routes and data fetching logic.
- templates/: This directory contains HTML templates for the web pages, including the home page and result page.


</p>
