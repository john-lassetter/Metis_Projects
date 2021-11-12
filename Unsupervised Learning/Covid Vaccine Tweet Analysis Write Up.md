# Covid-19 Vaccine Hesitancy Analysis Using Twitter Data
John Lassetter

### Abstract
The vaccination rate for covid-19 in the US has slowed significantly, despite an increase in the supply of vaccines and an overall vaccination rate of only 58% of the US population. This suggests that a large minority of adults are choosing not to get vaccinated for covid-19. This unvaccinated population continues to strain the US healthcare system and endanger the lives of those unable to receive a covid vaccine such as those who are allergic to them. Thus, it is in the public interest to determine why this population is hesitant to get vaccinated in order to most effectively deliver them the information needed to make a better informed decision, if applicable. To achieve this goal, I gathered tweets from the last year that included names of covid-19 vaccines and performed sentiment analysis and topic modeling on the data to group tweets about similar subjects. I found that negative tweets about covid-19 vaccines most often displayed a fundamental distrust of the US pharmaceutical industry or cited one of a handful of conspiracy theories. This suggests that the primary reasons for vaccine hesitancy shared on social media is belief in misinformation.

### Design
~200k tweets including names of vaccines were cleaned and prepared for sentiment analysis. Then, tweets with a negative sentiment were stemmed, tokenized, and then modeled using latent Dirichlet allocation (LDA). Topics were then identified and cross correlated with popular hashtags also found within the dataset. Conclusions were then drawn primarily from the most frequent words appearing in these topics as well as sample tweets and prevalent hashtags from each topic.

### Data
>200k tweets from >80k unique users. The users consisted of a wide variety from verified news sources to personal accounts with few followers. The median followers for a user was 275 and 3.5% of all users were verified. All tweets contained a name of a covid-19 vaccine or vaccine producer in their text (e.g. Pfizer/BioNTech, Sinopharm, Sinovac, Moderna, Oxford/AstraZeneca, Covaxin, Sputnik V).

### Algorithms
Sentiment analysis was performed using (VADER sentiment analysis)[https://github.com/cjhutto/vaderSentiment]. Topic modeling was performed primarily using latent Dirichlet allocation (LDA). SVD and NMF were also explored for topic modeling, but were found to be less effective than LDA in this case.

### Tools
**Data Preprocessing and Visualization:**  Pandas, Scikit-Learn, Matplotlib </br>
**Sentiment Analysis:**  VADER sentiment analyzer </br>
**Topic Modeling:** Scikit-Learn


### Communication
A pdf presentation of the results of this project is in this repo as is the notebook used to build the model.
