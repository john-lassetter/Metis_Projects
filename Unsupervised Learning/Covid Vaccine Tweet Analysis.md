# Proposal Covid Vaccine Tweet Analysis

### Question

Mass vaccination against COVID-19 is the most effective way to reduce the spread of COVID-19 and minimize COVID-19 related deaths. It is also a crucial step
in accelerating the reopening of the economy in a safe manner. However, while vaccine supplies are abundantly available in the US, demand for it has petered out.
Many Americans believe that they are better off without the vaccine for a variety of reasons including concern about the novelty of the vaccine technology,
distrust of the pharmesutical industry, and belief in COVID related conspiracy theories. 

The questions I want to answer relating to these observations are:
- What are all the reasons Americans are choosing not to get vaccinated?
- When were these reasons popularized and how have their popularity changed over time?
- How much overlap is there between communities that tweet about different reasons to not get vaccinated?
- Who are the some of the biggest (COVID-19) anti-vax Twitter accounts?
- How has the influence of the subject matter experts on COVID-19 vaccines (e.g. CDC and WHO) changed over time?

### Data Description

The data I have is a Kaggle dataset of >200k tweets from Twitter that have #tags related to the most popular COVID-19 vaccines. In addition to the text of the tweet,
each row of data has additional information including user name, if the tweet is a retweet, user followers at the time of the post, etc. I plan to mostly use the
text of the tweet for sentiment analysis and the username, retweet boolean, and number of retweets to build a network of the tweets and do community detection.
I may also get more data from Twitter using Tweepy

### Tools

These are the tools I plan to use:

*Data Preprocessing*: Pandas, Scikit-Learn, NLTK, NMF <br/>
*Classification*: Scikit Learn <br/>
*Network Modeling*: NetworkX <br/>


### MVP Goal

My MVP goal is to perform Non-negative Matrix Factorization on my text data to extract the most common topics in the COVID-19 vaccine debate on Twitter.
