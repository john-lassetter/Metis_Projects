# Estimate Solar Power Production Web App Proposal

### Questions
1. How much monthly/annual power generation should I expect to receive from X m^2 solar panels should I install them on my house/business?
2. How long will it take for the solar panels to pay for themselves? (stretch goal)
3. Which solar panels should I install based on what is cheapest, most efficient, etc.? (stretch goal)

### Data Description
The 2 data sets will be irradiance and weather data from NASA POWER API and solar panel efficiency data
from the manufacturer's website. This first dataset is large and dynamic (updated ~daily) so I will collect it
using the api and store it in a SQLite database. The second, will be a simple, static dictionary of solar panels 
and their parameters (i.e. cost, max efficiency, etc.) that I will (at least initially) collect manually and store
as a .json file. An individual unit in my analysis will be a time stamp representing a 1 hour time window with the 
single-point measure of or average value of irradiance, temperature, and perhaps more features such as wind speed and
cloud cover at that time stamp. These data will then be used in conjunction with solar panel performance data to
produce an estimate of the average power produced by the solar panel in that hour long time stamp. As a stretch goal,
The user of the end product dashboard could also feed in what they pay for electricity, what size solar panel
installation they are considering, and the cost of the solar panels + installation to see how much money they would
save annually and how long it will take the solar panels to pay themselves off.

### Tools
I plan to use SQLite to hold the NASA POWER metrology data and Flask to make the web app. Potentially, I may instead
store the data on an AWS server and use it to do the data processing if I have the time and it is not too expensive.
I also might try to use spark to store and manipulate the data.

### MVP Goal
An MVP for this project would consist of having data for at least a year and at least 1 location in a DB along with
the ability to query that data and produce a plot of average monthly energy production for a single type of solar panel.
