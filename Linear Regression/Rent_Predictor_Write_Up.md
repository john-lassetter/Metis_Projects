# West Coast Rent Predictor

### Abstract
The goal of this project was to build a model to predict the monthly rent of apartments on the west coast (WA, OR, and CA). Among other uses, such a model could
be used to optimize development of new apartment buildings to maximize revenue. The primary data used to train this model was scraped from Apartments.com while 
supplementary data on US demographics was obtained from openintro.org and data.ers.usda.gov. LASSO was used to fit a linear regressor to the data. After optimization
the model achieved an R^2 of 0.44 and a mean absolute error (MAE) of $772 or 34% of the median monthly rent.

### Design
To predict monthly rent for apartments, a linear regression model was trained using data scraped from Apartments.com along with some supplementary data from other
websites.

### Data
The primary data source for this project was Apartments.com and consisted of 8200 data points. Data collected from this site included monthly rent, sq. footage, number of bedrooms, nearest airports
and colleges and their distances, and several other features. This data was supplemented with census data from openintro.org and data.ers.usda.gov which contained
median household income, population, population density, number of private jobs, and percent change in number of private jobs for each county.

### Algorithms
Feature Engineering:
- LASSO was used to help reduce model complexity and multicolinearity
- A box-cox power transformation was performed on the target variable to normalize it since it was highly right skewed
- Degree 2 polynomial features were tested, though none were useful enough to add to the final model

Model:
- A LASSO model was used as it slightly outperformed ordinary least squares regression. The regularization constant was optimized on the validation data.
- The R^2 of the optimized model on test data was 0.44 and the MAE was $772 (for scale the median rent was $2,295)

### Tools
- BeautifulSoup was used to scrape the data from Apartments.com
- Numpy, Pandas, matplotlib, and seaborn were used for exploratory data analysis and visualization
- Scikit-learn was used to preprocess data and build and train the model

### Communication
A pdf presentation of the results of this project is in this repo as are the notebooks used to scrape the data and bulid the model.
