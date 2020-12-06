# Title

## Abstract
***A 150 word description of the project idea, goals, datasets used. What's the motivation behind your project? How do you propose to extend the analysis from the paper? What story would you like to tell, and why?***

The motivation behind our project relies on the prediction of future betrayals in dyadic relationships. We would like to use the same dataset as the authors and exploit it further to get better prediction, but also more insightful ones, by being able to tell what is the chance to be betrayed by our ally. Our methods will explore the ability of three different classification models to capture the betraying behaviour and we will consider these models to analyze the earliest in a relationship the betrayal becomes visibile. Furthermore, we are interested to go beyond the high-level features extracted and see if certain words can play a role in betraying, which we will represent through word embeddings, given how relevant discourse turned out to be in the analysis done by authors. We consider the ability to predict this behaviour valuable in the social context and we consider insights into the timeline of betrayal and identifying factors that contribute to betrayal foretelling to be interesting discussion points.

## Research Questions

***A list of research questions you would like to address during the project.***
The questions we would like to explore in our project are:

- Can we predict better betrayal?
- What is the probability of getting betrayed?
- How early (how many seasons before the betrayal happens) can we predict the incoming betrayal?
- [Possible] Does using certain words foretell betrayal?

## Proposed dataset
***List the dataset(s) you want to use, and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you've read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible given the datasets at hand.***

We analyzed what datasets can complement the existing work, but we were unable to find the original raw data or other datasets containing betrayal clues/labeling. However, we identified a project based on training a bot to play the Diplomacy game, using a dataset of 156k games, containing 13 million messages. We emailed the author of the research, as it says the 'dataset is available upon request'. We are currently pending an answer.

Given the current dataset provided by the paper's authors consists of extracted high-level features, our approaches are limited. Based on the feature already extracted, we will consider the sentiment, the politeness, number of words, number of requests, the number of season since the beginning of the relationship and the number of messages sent to date.

To see if different words can be tied to the betrayal outcome, we will expand the feature set with the words we are given in 'frequent words', 'lexicon words' and 'discourse words'. As the authors already showed that presence of discourse in messages is more likely to indicate future betrayal, this is an interesting path to explore. Our preprocessing will involve removing the linking words and pronouns, further lemmatization and load low dimensional pre-trained embeddings like GloVe and word2vec to represent them. 

## Methods
Our methods will target getting a model with a better prediction, based on the features presented above, except for embeddings. As we will focus on providing more insightul predicition and output the probability an existing player will betray, our task is a classification one. We propose the following models for our exploration:
- logistic regression
- a feed-forward neural network
- decision-trees based models (Random Forest, XGBoost)

We will apply the K-fold cross validation to tune the hyperparameters and choose the best performing model based on ability to predict the betrayal to address the first to questions. Afterwards, we will consider the data by leaving out a subset of relationships and retrain the models. On this subset, we will analyze how early can we actually predict the incoming betrayal (earliest season).
Ultimately, we will try to add the embeddings to our models and rerun the pipeline, to see if the models get any improvement.

## Proposed timeline
The proposed timeline may change throughout the realisation of the project.

* Week 1: Getting the dataset, prepare the features 
* Week 2: Implementing the training process of the models and analyze results
* Week 3: Continue with analysis, preparing the data story and short video.

## Organization within the team
A list of internal milestones up until project milestone P4. Add here a sketch of your planning for the next project milestone.

Feature engineering:
- Prepare the features (normalization, standardization)
- Combine lexicon, frequent, discourse words and clean it (remove contractions, stopping words, stemming)
- Load the word embeddings (Glove, word2vec)

Modeling:
- Each to train a model and do hyperparameters tuning
- Analyze how early betrayal can be predicted
- Add the word embeddings to feature and retrain

Results:
- Analyze the results obtained by the models, drive insights on what contributes most to the prediction
- Draw comparison between models using as baseline the models presented in the paper
## Questions for TAs (optional)

***Add here any questions you have for us related to the proposed project.***
