## Sentiment Analysis of Fine Food reviews scraped from Amazon
Project Report: Report.pdf<br>
There are 3 relevant files-
#### 1) Setup- setup.py
This is the file that downloads the dataset from SNAP and converts it into a human readable csv file. To execute it run python setup.py

#### 2) Preprocessing and EDA notebook- PP_EDA.ipynb
This Jupyter Notebook does the initial data pre- processing. It further contains the Exploratory Data Analysis.

#### 3) Data modelling notebook- data_modelling.ipynb
This Jupyter Notebook contains the code for the processes involved in modelling such as selection, feature extraction, model validation, etc. to classify the sentiment of the Amazon Fine Food Review. 


(SYS 6018 - Data Mining, Final Term Project, Graded - 100/100 A+)

In this final term project, I partnered with another student in my class to leverage sentiment analysis from scratch on the Amazon Fine Food Reviews dataset. The entire project along with literature review,text mining methodology,hypothesis,results and evaluation is detailed in the PDF report. We have used Python to code and scikit for NLP.

I have briefly described some aspects of the text mining methods used in the analysis below.

#### General Description
Amazon reviews are often the most publicly visible reviews of consumer products. Studies have shown that there is a strong relationship between reviews and sale conversation rates. Reviews and ratings also help increase discoverability as potential buyers tend to filter their options based on ratings. Hence, customer feedback in form of reviews and ratings has become an important source for businesses to improve upon. The problem today is that for many businesses, it can be tough to analyze a large corpus of customer reviews and quantify how good or bad a product is and with that understand what features make a product favorable or unfavorable. Additionally, relevant information about products and its features can sometimes be hard to identify or extract from a large volume of reviews. Understanding what online users think of its content can help a company market its product as well as mange its online reputation. The purpose of this paper is to investigate a small part of this large problem: positive and negative attitudes towards products. Sentiment analysis attempts to determine which features of text are indicative of its context (positive, negative, objective, subjective, etc.) and build systems to take advantage of these features. The problem of classifying text as positive or negative is not the whole problem in and of itself, but it offers a simple enough premise to build upon further. There exists some data on the web to understand and address such issues such as the ‘Fine Food Reviews’ dataset sourced from Amazon that we have leveraged for this analysis. The data contains reviews of various food items reviewed by users on Amazon. Each product reviewed has a review and rating associated with it given by a single user. There are other attributes provided as well.

In this analysis, we have applied techniques such as TFIDF, Word2Vec and LDA for feature extraction that are eventually used in the binary classification of sentiment of reviews. Topic modeling of reviews using LDA can help cluster reviews of a similar kind under a group as well. Such structure can help merchants better understand their user feedback in context with the product features. It’s also equally helpful to other users who depend upon reading these reviews before they make a judgement about buying a product.

#### Data
This dataset sourced from Stanford SNAP consists of reviews of fine food products sold on Amazon. The data spans over a period of more than 10 years, including all ~500,000 reviews up to October 2012 in one sqlite database.

Our data pipeline involved pre-processing data, performing exploratory data analysis, leveraging text processing on it followed by building classification models and evaluating them.

#### Text Processing
Prior to building the classification model we implemented text processing to extract features that could be used in modeling.

* Stop words removal: stop words refer to the most common words in any language. They usually don’t have any predictive value and just increase the size of the feature set.

* Punctuation Removal: refers to removing common punctuation marks such as !,?,$* etc.

* Lower case transformation: convert all upper-case letters to lower case letters.

* Stemming: the goal of both stemming is to reduce inflectional forms and sometimes derivationally related forms of a word to a common base form. For e.g. the words - organize, organizes, and organizing are reduced to one form. The first problem that needs to be tackled is that most of the classification algorithms expect inputs in the form of feature vectors having numerical values and having fixed size instead of raw text documents (reviews in this case) of variable size. We tackled this by using the Bag-of-Words framework which involved tokenization and normalization of words in the text. We used the following techniques to obtain feature vectors from text that could be leveraged in model building.

* Tf-idf : Tf-idf allows us to weight terms based on how important they are to a document. In a large text corpus, some words will be present very often but will carry very little meaningful information about the actual contents of the document (such as “the”, “a” and “is”). If we were to feed the count data directly to a classifier those very frequent terms would shadow the frequencies of rarer yet more interesting terms. We instantiated the tf–idf vectorizer and fit it to our training data. The generalized formula for this measure:<br><br>Tfidf (t,d,D) = tf (t,d) × idf (t,D)<br><br>
  Where t denotes the terms; d denotes each document; D denotes the collection of documents.

* Word2Vec: Word2Vec is a group of models (first introduced by Mikolov et al. in 2014) used for constructing vector representations of words, also known as word embeddings. Word2Vec (w2v) uses a shallow neural network to learn how words are used in a particular text corpus. The dense vector representations of words learned by word2vec have remarkably been shown to carry semantic meanings and are useful in a wide range of use cases ranging from natural language processing to network flow data analysis. These vector encodings effectively capture the semantic meanings of the words. For instance, words that we know to be synonyms tend to have similar vectors in terms of cosine similarity and antonyms tend to have dissimilar vectors. Even more surprisingly, word vectors tend to obey the laws of analogy.

* n-grams: Our model contained misclassifications owing to loss in context interpretability of sentences. For eg – misclassifying the text “The candy is not good, I will never buy them again” as a positive review, and misclassifying the text “The candy is not bad, I will buy them again” as a negative review. We addressed this issue by implementing a n-grams or in this case a bi-grams model below the word2vec approach. Bi-grams count pairs of adjacent words and could give us features such as bad versus not bad.

* Latent Dirichlet Allocation: There were no product names or descriptions in the dataset that were easily accessible. Review summaries sometimes mentioned the product under review, otherwise there is no category label that provides a way to simply group products and user preferences. We attempted to represent text reviews in the terms of the topics they describe, i.e. topic modeling. The technique used to extract topics from Amazon fine food reviews is Latent Dirichlet Analysis (LDA). We assume that there is some number of topics (chosen manually), each topic has an associated probability distribution over words and each document has its own probability distribution over topics; which looks like the following:<br><br>
𝑝(𝑑|𝜃, ∅, 𝑍) = Π𝑗=1 𝑙𝑒𝑛𝑔𝑡ℎ 𝑜𝑓𝑑 𝜃𝑧𝑑,𝑗 ∅𝑧𝑑,𝑗 ,𝑤𝑑,j<br><br>
Every word in all the text reviews is assigned a topic at random, iterating through each word, weights are constructed for each topic that depend on the current distribution of words and topics in the document

#### Modeling
We used 2 classifiers in this project – Decision Trees Classifier and Logistic Regression. Since the number of samples in the training set is huge, we abstained from running classification algorithms like K-Nearest Neighbors or Random Forests etc. which would be inefficient in this case particularly. We trained our models on the training set implementing k-fold validation and then tested the performance of the classifier on the test set. The models were implemented using combination of the feature vectors produced through wrd2vec, tf-idf and bi-grams along with latent dirichlet allocation.

#### Evaluation and Results
Generally, the results of this experiment were very successful. The classifiers managed to accurately tag a great amount of user-generated data much further past the random baseline of 50%. Our takeaway was that the model trained on the Logistic Classifier using all the features together – tf-idf, LDA and bi-gram with Word2Vec gave us the best performance in terms of accuracy and other metrics mentioned above. The Logistic classifier trained solely on tf-idf also gave us similarly good results. Compared to the logistic model, decision trees fared poorly. We tested certain hypothesis that we had formulated at the beginning of our analysis and were able to evaluate it through our exploratory analysis and model building approach.<br><br>
* Adding regressor ‘helpfulness_score’ to model M which in this case was Logistic with tf-idf did not improve the accuracy performance of the model. The previous accuracy was 88.51% and it marginally went upto 88.7% which wasn’t a considerable improvement.
* We did not find that the verbosity of a review is related to its helpfulness. In fact, through the EDA we concluded that reviews that are voted helpful tend to be concise and shorter in length hence invalidating our hypothesis.

#### Refer to the PDF report for more detail on the analysis.
