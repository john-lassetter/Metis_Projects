# Loan Default Predictor

### Abstract
In order for a lender to maximize profits, they should (typically) give out only loans to clients that will be able to pay off those loans. When a client defaults on a loan, the lender will take the a loss (for most, moderate interest rate loans). Thus, being able to predict if a client will default on a loan before issuing it could potentially save a lot of money for the lender.

### Design
The goal of this project is to build a model to classify whether or not a client will have payment difficulties (this should be correlated with loan defaults) before giving them a loan. 

### Data
Data was from a Kaggle dataset that can be found [here](https://www.kaggle.com/gauravduttakiit/loan-defaulter). The data consists of >300k rows, which represent individual loans, and 121 columns, which represent features tied to that loan including the target feature which is a binary indicator of the presence of (or lack of) payment difficulty. The other 120 features are a mix of numerical and categorical features such as the principle of the loan, whether or not the client has a car, how long they have had their current job, etc.

### Algorithms
*Models and the Hyperparameters Used to Tune Them*
- logistic regressor - l2 penalty
- random forest classifier - number of estimators
- gradient boosted (decision tree) classifier - number of estimators
- voting classifier - l2 penalty (logistic regressor), number of estimators (random forest)

*Model Evaluation and Selection*
Models were compared by looking at ROC AUC, max(F1 score), and interpretability (except for the voting classifier which was eliminated from the selection process early for have an ROC AUC slightly worse than logistic regression).

| Model | ROC AUC | F1 Score | Interpretability | Training Time |
| ------|---------|----------|------------------| ------------- |
| Logistic Regression | 0.67 | 0.22 | High | 7s |
| Random Forest | 0.65 | 0.22 | Medium | 15s |
| Gradient Boosted Classifier | 0.69 | 0.25 | Low | 199s |

From the table above, the gradient boosted classifier clearly had a marginal advantage in performance over the other two models. However, the logistic regression was ultimately chosen as the most appropriate model for the problem due to its higher interpretability and much short training time for only slightly less performance.

### Tools
- Numpy, Pandas, and matplotlib were used for exploratory data analysis and visualization
- Scikit-learn was used to preprocess data, build and train the models, and tune model hyper-parameters

### Communication
A pdf presentation of the results of this project is in this repo as is the notebook used to build the model.
