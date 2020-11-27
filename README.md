# Title

## Abstract
***A 150 word description of the project idea, goals, datasets used. What's the motivation behind your project? How do you propose to extend the analysis from the paper? What story would you like to tell, and why?***

The motivation behind our project is to understand various clues that indicate betrayal in dyadic relationships, as well as to better predict a future betrayal from textual, conversational data. Our analysis will expand the current work that relies mostly on high-level features extracted from the text by considering raw words. This can be done by experimenting with different word embeddings and using unsupervised approaches (K-means, DBSCAN) to identify words or classes of words that are more indicative of betrayal. We would also try to address the classification problem from a time series perspective given the seasons data and see if the key for classifying betrayal relies on how the friendship evolves over time, using supervised methods based on neural networks and decision trees.

## Research Questions

***A list of research questions you would like to address during the project.***
The questions we would like to explore in our project are:
- What words are more indicative of a betraying behaviour?
- Can we predict betrayal better?
- What features can explain the betrayal best?

## Proposed dataset
***List the dataset(s) you want to use, and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you've read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible given the datasets at hand.***

We analyzed what datasets can complement the existing work, but we were unable to find the original raw data or other datasets containing betrayal clues/labeling. However, we identified a project based on training a bot to play the Diplomacy game, using a dataset of 156k games, containing 13 million messages. We emailed the author of the research, as it says the 'dataset is available upon request'. We are currently pending an answer.

Given the current dataset provided by the paper's authors consists of extracted high-level features, it is difficult to expand the features further to get more insights. One possible approach is to consider another representation for the words given, either in the 'frequent words' or in 'lexicon words'. Because the frequent words mostly consist of linking words and pronouns, they are not very valuable after removing stop words. Therefore, we will consider also the lexicon words and convert both of them to their word embeddings, in addition to the politeness score and number of requests, and explore with various existing embeddings (Glove, word2vec). A good idea would also be to include the discourse words in our analysis and see if there are improvements. Because we are only given the words and not have the positional information, we cannot use more complex representations such as the ones given by BERT. Out of the existing features, we will attempt to understand based on our models, which ones are more significant for our classification problem. Another possible approach to represent the lexicon words is by building the co-occurrence matrix probabilities of words in the messages of betrayal and non-betrayal, which we can normalize and generate new word embeddings by applying PCA. 

## Methods
Our proposed methods will mostly rely on unsupervised approaches to understand betrayal behavior. We will start by considering only the embedding representation and attempt to apply clustering methods such as K-means or DBSCAN depending on the shapes of the clusters to identify various classes of words that can indicate betrayal. We believe a good distance metric for this scenario would be the cosine similarity or the Hellinger distance for the embeddings computed by us. Furthermore, we can expand the features we used to also cover the sentiment score, as well as the number of requests or the length of messages sent.

From a supervised perspective, we intend to look at a dimension that was ignored in the paper: the time dimension. Because these relationships build upon existing relationships each season, we can analyze our problem from a time series perspective and see how previous steps influence the current one when the betrayal takes place. Therefore, we can consider the aforementioned features and because of the complexity given by the embeddings, we will explore how an LSTM-based architecture would improve the classification scores. Furthermore, we can explore using a sliding window based on the number of seasons, how decision tree models like Random Forest of XGBoost perform on the task of classifying betrayal.

## Proposed timeline
## Organization within the team
A list of internal milestones up until project milestone P4. Add here a sketch of your planning for the next project milestone.

Feature engineering:
- combine lexicon, frequent, discourse words and clean it (remove contractions, stopping words, stemming)
- load various word embeddings (Glove, word2vec)
- create co-occurance matrix and get own embeddings
- normalize/standardize features like number of requests/length of messages
- expand features for timeseries using a sliding window

Modeling:
- visualize the resulted features
- clustering using some distance metrics
- train an LSTM model
- train a Random Forest and XGBoost

Results:
- analyze clusters and see most common words
- draw comparison between models using as baseline the models presented in the paper
## Questions for TAs (optional)

***Add here any questions you have for us related to the proposed project.***


## Ideas :

* Use several feature engineering approaches (word embedding, matrices (Irina).., combining other features, PCA)
* Try to apply Supervised Learning to classify the betrayal and see if we can get better result than the paper
* Try to apply Unsupervised Learning if we can observe to distinct classes ..??
