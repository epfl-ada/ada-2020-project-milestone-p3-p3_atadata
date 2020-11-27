# Title

## Abstract
***A 150 word description of the project idea, goals, datasets used. What's the motivation behind your project? How do you propose to extend the analysis from the paper? What story would you like to tell, and why?***

We would like to know what features can explain the betrayal better than the politeness score. What kind of sub-features that we can extract from each set of messages can be correlated with a betrayal ? The idea would be to try several approaches, several feature engineering techniques and several methods to tackle this question.

## Research Questions

***A list of research questions you would like to address during the project.***
The questions we would like to explore in our exploration are:
- What words are more indicative of a betraying behaviour?
- Can we predict betrayal better?
- What features can explain the betrayal best?

## Proposed dataset
List the dataset(s) you want to use, and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you've read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible given the datasets at hand.

We analysed what datasets can complement the existing work, but we were unable to find the original raw data or another datasets containing betrayal clues/labeling. However, we identified a project based on training a bot to play the Diplomacy game, using a dataset of 156k games, containing 13 million messages. We emailed the author of the research, as it says the 'dataset is available upon request'. We are currently pending an answer.

Given the current dataset provided by the paper's authors consists of extracted high level features, it is difficult to expand the features further to get more insights. One possible approach is to consider another representation for the words given, either in the 'frequent words' or in 'lexicon words'. Because the frequent words mostly consist of linking words and pronouns, they are not very valuable after removing stop words. Therefore, we will consider the lexicon words converted to their word embeddings, in addition to the existing features, and explore with various given embeddings (Glove, word2vec). Also, because we are only given the words and not have the positional information, we cannot use more complex representation such as the ones given by BERT. Out of the existing features we will atempt to understand based on our models, which one are more significant for our classification problem. Another possible approach to represent the lexicon words is by building the co-occurance matrix probabilities of words in the messages of betrayal and non-betrayal, which we can normalize and generate new word embeddings by applying PCA. 

**TODO: some aspects about how many lexicon words have in avg messages ?

## Methods
Our proposed methods will mostly rely on unsupervised approaches to understand the betrayal behaviour. We will start by considering the embedding representation and attempt to apply clustering methods such as K-means or DBSCAN depending on the clusters shapes to identify various classes of words that can indicate betrayal. We believe a good distance metric for this scenario would be the cosine similarity or the Hellinger distance for the embeddings computed by us. Furthermore, we can expand the features we used to also cover sentiment score, as well as .... 

## Proposed timeline
## Organization within the team
A list of internal milestones up until project milestone P4. Add here a sketch of your planning for the next project milestone.
## Questions for TAs (optional)

***Add here any questions you have for us related to the proposed project.***


## Ideas :

* Use several feature engineering approaches (word embedding, matrices (Irina).., combining other features, PCA)
* Try to apply Supervised Learning to classify the betrayal and see if we can get better result than the paper
* Try to apply Unsupervised Learning if we can observe to distinct classes ..??
