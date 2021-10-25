# Loan Default MVP

**Question:**  Given a loan application, what is the probability that the loaner, if approved, will have difficulty paying the loan back?

**Solution:**  A logistic regression model was trained to predict the outcome of the loan (payment difficulty or no payment difficulty) based on an input loan
application.

<div>
<img src="https://github.com/john-lassetter/Metis_Projects/blob/main/Classification/baseline_confusion_matrix.png" width="350px"/>
<img src="https://github.com/john-lassetter/Metis_Projects/blob/main/Classification/baseline_roc_curve.png" width="500px"/>
</div>

###### Note: If the figures appear to be missing axes labels, please view this document using the github light theme

**Discussion**: Because the training data is so imbalanced (~9% of all loans have payment difficulties), this means that precision is generally inflated relative to recall. Therefore, the model used to produce the above confusion matrix uses a threshold much lower than 50%, otherwise it would predict close to 0 cases of payment difficulty and have a precision of ~91%. With the threshold above the precision is merely 13% but the recall is 63%. In other words, this model flags 63% of all loans with payment difficulties as loans with payment difficulties, but it also incorrectly flags ~7 loans that will actually not have payment issues for every 1 loan that it flags correctly.

**Future Work**:  Going forward, I plan to do more feature engineering and model tuning to, hopefully, get a little more performance out of my model. I also, intend to deliver the results using more useful metrics such as likelihood of payment difficulties as a percentile (i.e. this loan is in the top 90% of loans with respect to the chance to have payment difficulties). Plus, I hope to keep my model interpretable, and, if I can without losing too much performance, I would also like to have the model output the top contributing features for each output so that the lender can understand why the model is suggesting to approve or deny the loan and potentially investigate further those features.
