# Covid Tweet Analysis MVP

**Question:**  How has sentiment towards the covid-19 vaccine changed over time?

**Solution:**  A simple vader sentiment analysis shows a slightly positive average sentiment towards covid-19 vaccines which has not changed much over the last year.

<div>
<img src="https://github.com/john-lassetter/Metis_Projects/blob/main/NLP%20and%20Unsupervised%20Learning/polarity_over_time.png" width="800px"/>
</div>

**Discussion**:  I am not quite where I wanted to be by this point due to many unexpected road blocks in acquiring better data than the initial dataset I started with. The data is still quite noisy and no work has been done yet to cluster users based on their biographies which would likely provide a deeper analysis of the data. I have also performed topic analysis using pyLDAVis, but, as expected, there is not a lot of info to be gained here so far as the topics have either a lot of overlap or are indicating types of users that I need to remove from the dataset (i.e. ads and repetetive announcements such as appointment availability).

**Future Work**: 
- Improve data cleaning by adding spellchecking and removing more users that are producing automated and unintersting tweets such as vaccine appointment schedules. 
- Classify users by their twitter bio's using the classifier from [this paper](https://arxiv.org/abs/2008.08364) (if implementable in a reasonable amount of time)
