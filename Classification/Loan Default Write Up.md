# Loan Default Predictor

### Abstract
In order for a lender to maximize profits, they should (typically) give out only loans to clients that will be able to pay off those loans. When a client defaults on a loan, the lender will take the a loss (for most, moderate interest rate loans). Thus, being able to predict if a client will default on a loan before issuing it could potentially save a lot of money for the lender.

### Design
The goal of this project is to build a model to classify whether or not a client will have payment difficulties (this should be correlated with loan defaults) before giving them a loan. ####################################

### Data
Data was from a Kaggle dataset that can be found [here](https://www.kaggle.com/gauravduttakiit/loan-defaulter). The data consists of >300k rows, which represent individual loans, and 121 columns, which represent features tied to that loan including the target feature which is a binary indicator of the presence of (or lack of) payment difficulty. The other 120 features are a mix of numerical and categorical features such as the principle of the loan, whether or not the client has a car, the number of children they have, etc.

### Algorithms
*Models*
- logistic regressor
- random forest classifier
- gradient boosted (decision tree) classifier
- voting classifier

*Model Evaluation and Selection*
#########################################################

### Tools
- Numpy, Pandas, and matplotlib were used for exploratory data analysis and visualization
- Scikit-learn was used to preprocess data, build and train the models, and tune model hyper-parameters

### Communication
A pdf presentation of the results of this project is in this repo as is the notebook used to build the model.
