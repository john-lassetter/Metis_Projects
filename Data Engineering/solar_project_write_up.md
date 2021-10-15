# Solar Panel Power Estimator

### Abstract
The answer to the question of whether or not to install solar panels on your home or business can end up being quite complex in most cases. This is an investment
with a substantial up front cost and a speculative return over time that may take a decade or two to break even. There are many factors that affect the cost, as
well as the return, but the most elusive of these is the expected power production of the solar panels. The power production of solar panels depends primarily on 
the amount of sunlight they get as well as the air temperature (e.g. when they are too hot they lose efficiency) so estimating it can be difficult without access
to weather and solar irradiance data. To solve that problem, this app does that calculation for the consumer using weather and solar irradiance data from the National
Renewable Energy Laboratory (NREL) and allows them to compare their expected annual power produced with other counties or states around the country (currently limited to the west coast).

### Design
Hourly data was ingested from NREL, cleaned, and stored in an SQLite database. This data was then used, along with the solar panel efficiency specs from First Solar,
to compute daily solar panel power production for each county in CA, OR, and WA. This much smaller (downsampled) processed data was stored in a separate dataset
which was deployed with the interactive webapp to Heroku.

### Data
The weather and solar irradiance data used in this analysis is from the [NREL](https://www.nrel.gov/) and the example solar panel
efficiency data is from [First Solar](https://www.firstsolar.com/-/media/First-Solar/Technical-Documents/Series-6-Datasheets/Series-6-Datasheet.ashx). The data from
NREL was acquired through their api and amounted to about 500,000 rows of data, spanning 3 states and 1 year.

### Tools
Requests - data acquisition  
Pandas, numpy, matplotlib - EDA and data analysis  
SQLite - data storage  
Streamlit - web app design  
Heroku - web app hosting

### Communication
A pdf presentation of the results of this project is in this repo as are the notebooks used to scrape the data, analyze it, and build the app.
