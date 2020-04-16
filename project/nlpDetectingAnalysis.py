#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 13:48:46 2019

@author: mertdemirezen
"""

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier


import nltk
#nltk.download('twitter_samples')
#nltk.download('stopwords')
import re, string, random


import sys
from PyQt5 import  QtWidgets

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []
    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)
        
def getTestData (data) :
    custom_tweet = data
    custom_tokens = remove_noise(word_tokenize(custom_tweet))
    print (custom_tokens)
    print (custom_tweet,"---", classifier.classify(dict([token, True] for token in custom_tokens)))
    return (custom_tweet,"---", classifier.classify(dict([token, True] for token in custom_tokens)))
    

if __name__ == "__main__":

    positive_tweets = twitter_samples.strings('positive_tweets.json')
    #print(positive_tweets[:20])
    for i in positive_tweets[:20]:
        print(i)
    negative_tweets = twitter_samples.strings('negative_tweets.json')
    text = twitter_samples.strings('tweets.20150430-223406.json')
    print("Text = ",text)
    tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0]

    stop_words = stopwords.words('english')
#    print("stop words",stop_words)

    positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
#    print("positive tokens",positive_tweet_tokens[:2])
    negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')
    #print("negative tokens",negative_tweet_tokens[:2])

    all_pos_words = get_all_words(positive_tweet_tokens)

    #print("all_pos_words",all_pos_words)
    freq_dist_pos = FreqDist(all_pos_words)
    #print(freq_dist_pos.most_common(10),"burada")

    positive_tokens_for_model = get_tweets_for_model(positive_tweet_tokens)
    negative_tokens_for_model = get_tweets_for_model(negative_tweet_tokens)
    #print("positive tokens model",positive_tokens_for_model[1])
    #print("negative tokens model",negative_tokens_for_model[:2])
    
    positive_dataset = [(tweet_dict, "Positive")
                         for tweet_dict in positive_tokens_for_model]
    #print(positive_dataset[0:2],"burada 2")

    negative_dataset = [(tweet_dict, "Negative")
                         for tweet_dict in negative_tokens_for_model]
    #print(negative_dataset[0:2],"burada negative")

    dataset = positive_dataset + negative_dataset

    random.shuffle(dataset)

    train_data = dataset[:7000]
    #print("train data",train_data[:2])
    test_data = dataset[7000:]

    classifier = NaiveBayesClassifier.train(train_data)

    print("Accuracy is:", classify.accuracy(classifier, test_data))

    #print(classifier.show_most_informative_features(10))









    
    custom_tweet = 'Congrats #SportStar on your 7th best goal from last season winning goal of the year :) #Baller #Topbin #oneofmanyworldies'
    






class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Mert Demirezen") 
        self.init_ui()

    def init_ui(self):
        self.etiket1 = QtWidgets.QLabel()
        self.result = QtWidgets.QLabel()
        self.etiket1.setText("Mert Demirezen Sentimental Analysis App")
        self.yazı_alanı = QtWidgets.QLineEdit()
        
        self.temizle = QtWidgets.QPushButton("Clear")
        self.yazdır = QtWidgets.QPushButton("Go!")
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.etiket1)
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdır)
        v_box.addWidget(self.result)

        v_box.addStretch()
        
        self.setLayout(v_box)
       


        self.temizle.clicked.connect(self.click)
        self.yazdır.clicked.connect(self.click)



        self.show()
    
        
        
        

    def click(self):
        sender = self.sender()

        if sender.text() == "Clear":
            self.yazı_alanı.clear()

        else:
            context = self.yazı_alanı.text()
            print(context)
            data_resultt = getTestData(context)
            print(data_resultt)
            self.result.setText("{}".format(data_resultt))
  
            
    


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

    