# Proposal for Apartment Rent Predictor

### Question/Need

The questions I hope to answer are where are the most and least expensive places to rent on the west coast and which features, locations, 
and amenities add the most to the cost of rent?

An apartment hunter could benefit from this analysis to help prioritize which features they should include in their apartment search. Additionally, a developer 
could use this analysis (especially in conjunction with a database of real estate prices) to maximize return on investment when building or renovating apartments.

### Data Description

I will scrape apartments.com using requests and beautifulsoup to get my data. An individual sample of analysis would be 1
apartment. Rent will by my target variable and I intend to include the following as features sq. feet, number of bedrooms, number of bathrooms,
age of building, location (state, county, city), pet friendly vs not (maybe separate dog and cat), distance to closest college (maybe include size of college),
distance to closest airport (maybe closest int. airport).

Potential Additional Datasets: US Census data to use city population as a feature, college  attendance data to get close to small/medium/large/collge feature

### Tools

I will use BeautifulSoup to scrape the data, pandas to clean it, and sklearn to model it using a linear model.

### MVP Goal

My goal for an MVP is to observe a correlation between 1 or more of the features listed above and rent.
