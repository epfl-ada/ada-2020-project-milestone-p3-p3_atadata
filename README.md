#  Extension of Linguistic Harbingers of Betrayal

## Abstract
***A 150 word description of the project idea, goals, datasets used. What's the motivation behind your project? How do you propose to extend the analysis from the paper? What story would you like to tell, and why?***

The paper written by Niculae et al (2015) explains how the messages ex-changed between every two players of an online strategygame, Diplomacy, contain subtle signs of imminent be-trayal, which victim is not able to seize. Using the gamedata is a novel approach, giving access to more insightsinto the act of betrayal, where no consistent work ordatasets were considered before. The researchers ana-lyze different particularities of the exchanged messages,such as politeness and sentiment, ending on the possi-bility to train a model that could predict an imminentbetrayal better than a human player. Relying on thisresult, we will explore the possibilities of improvementof the prediction by using different well known modelsof machine learning. Beside this objective of pure opti-mization, we will explore the possibilities of predictionin an arbitrary number of seasons ahead of the betrayaland attempt to understand what other features can beindicative of betrayal in the socially complex phenom-ena of betrayal. 

## Research Questions

***A list of research questions you would like to address during the project.***
The questions we would like to explore in our project are:

- Can we predict imminent betrayal better?
- What is the probability of getting betrayed as a player ?
- How early (how many seasons before the betrayal happens) can we predict the incoming betrayal?
- What features are more indicative of betrayal? Can the semantic of words help to foretell betrayal?

## Proposed dataset
***List the dataset(s) you want to use, and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you've read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible given the datasets at hand.***

Given that the dataset provided in the cited paper consists of high-level features extracted from messages, our freedom of extension becomes quite limited. We analyzed the possibility of other datasets that can complement our goal, but were not able to find original raw data or other sources containing betrayal clues. We found a project based on the Diplomacy game, consisting of 156k games and 13M messages, but we were not granted access to it. Thus, we have decided to work on the data provided by the authors allowing us to compare our methods with the authors' results.

## Methods
Our methods will target getting a model with a better prediction, based on the features presented above, except for embeddings. As we will focus on providing more insightul predicition and output the probability an existing player will betray, our task is a classification one. We propose the following models for our exploration:
- logistic regression
- a feed-forward neural network
- decision-trees based models (Random Forest, XGBoost)

We will apply the K-fold cross validation to tune the hyperparameters and choose the best performing model based on ability to predict the betrayal to address the first to questions. Afterwards, we will consider the data by leaving out a subset of relationships and retrain the models. On this subset, we will analyze how early can we actually predict the incoming betrayal (earliest season).
Ultimately, we will try to add the embeddings and train a multimodal neural network to see if the models get any improvement.

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
