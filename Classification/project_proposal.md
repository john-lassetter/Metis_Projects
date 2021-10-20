# Proposal for Loan Default Predictor

### Question/Need

In order for a lender to maximize profits (in an ethical way), they should give out only loans to clients that will be able to pay off those loans. When a client defaults on a loan, the lender will take the a loss (for most, moderate interest rate loans). Thus, being able to predict if a client will default on a loan before issuing it could potentially save a lot of money for the lender.

### Data Description

The data consists of >300k rows, which represent individual loans, and 121 columns, which represent features tied to that loan including the target feature which is the presence of payment difficulty (not default vs. not default but is correlated to defaulting). The other 120 features are a mix of numerical and categorical features such as the principle of the loan, whether or not the client has a car, the  number of children they have, etc. 

### Tools

I plan to use sklearn and xgboost to build and train different classification models to do the prediction.

### MVP Goal

My MVP would be a baseline model (read un-optimized) that classifies the target based on either a subset of the features or all of the features.
