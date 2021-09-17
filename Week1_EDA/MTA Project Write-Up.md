# Maximizing Outreach for the WTWY Gala
John Lassetter
## Abstract
The organization WomenTechWomenYes (WTWY) wants to raise awareness and funds for their cause at a summer Gala and desires help recruiting attendants. They already plan to deploy street teams at New York subway station entrances to collect emails from commuters and send out invites to them electronically. However, they would like assistance in determining where to station their teams in order to collect the most emails. My task is to provide WTWY with the best locations (and times) to deploy their street teams to maximize email collection.
## Design
To fulfill this task I explored subway turnstile data to calculate the stations and times with the most foot traffic. Specifically, I cleaned the turnstile data, converted the cumulative traffic counts to a rate, and queried the busiest stations and times.
## Data
I used 3 months of Metropolitan Transportation Authority (MTA) turnstile data (June 2021 - September 2021) for my analysis ([found here](http://web.mta.info/developers/turnstile.html)). The data consisted of cumulative entries and exits at periodic time stamps from 5030 turnstiles accross 379 subway stations in New York City.
## Algorithms
Data cleaning was accomplished using a custom function to remove outliers (defined using IQR), remove broken turnstiles, and flip turnstiles which counted down rather than up. Additionally, pandas was used to remove null values which accounted for less than 5% of the data. Further, a rate of entries and exits per hour was computed using pandas.
## Tools
Pandas and numpy were used extensively for the exploration, cleaning, and analyzing of the data. SQLAlchemy was also used to query the data initially and matplotlib and seaborn were used to visualize the data and communicate the results of the analysis.
## Communication
A presentation was given to WTWY which can be found in this repo.
