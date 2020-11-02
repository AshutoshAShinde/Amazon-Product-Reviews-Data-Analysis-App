# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:53:28 2020

@author: Lenovo
"""
import time
import streamlit as st
import csv
import re
import cv2

from textblob import TextBlob
from wordcloud import WordCloud
import string
import nltk
from nltk.corpus import stopwords

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_colwidth', 200)
st.set_option('deprecation.showPyplotGlobalUse', False)
#image = cv2.imread('ama2.jpg')
#cv2.imshow('Image',image)
#st.image(image, width = 400)
st.title('Sentiment Analyzer for Amazon Products')


st.subheader("This App gives the Sentiment Analysis of the reviews of various Products on Amazon.com")

Product_Name = st.sidebar.selectbox("Select Product", ("Sennheiser Wireless Headphones","CONTROVERSIAL PRODUCT_1","CONTROVERSIAL PRODUCT_2","CONTROVERSIAL PRODUCT_3","CONTROVERSIAL PRODUCT_4"))     
                
review_category = ["All Reviews","Positive Reviews","Negative Reviews"]
choice = st.sidebar.selectbox("Select Your Category", review_category)
                
if Product_Name == "Sennheiser Wireless Headphones":
    
    df = pd.read_csv("reviews_amz4.csv", names = ['Review','Rating'])
    df['Review'].fillna("", inplace = True)
    df['Rating'].fillna(df['Rating'].median(), inplace=True)
    
    Polarity_score = [round(TextBlob(review).sentiment.polarity, 3) for review in df['Review']]
    Subjectivity_score = [round(TextBlob(review).sentiment.subjectivity, 3) for review in df['Review']]
    df['Polarity']= Polarity_score
    df['Subjectivity'] = Subjectivity_score
    
    sentiment = ['positive' if score > 0 
                             else 'negative' if score < 0 
                                 else 'neutral' 
                                     for score in Polarity_score]
    
    df['Sentiment'] = sentiment
    
    pos_count = sum(df['Sentiment']=='positive')
    neg_count = sum(df['Sentiment']=='negative')
    neu_count = sum(df['Sentiment']=='neutral')
    df["Word_Count"] = df["Review"].apply(lambda review: len(review.split()))
    
    gp = df.groupby(by=['Sentiment'])
    positive_reviews = gp.get_group('positive')
    negative_reviews = gp.get_group('negative')
      
    def wordcloud(data):
    
        words_corpus = ''
        words_list = []

        for rev in data["Review"]:
        
            text = str(rev).lower()
            text = re.sub(r'[^\w\s]','',text)
            text = ''.join([i for i in text if not i.isdigit()])
        
            tokens = nltk.word_tokenize(text)
            tokens = [word for word in tokens if word not in stopwords.words('english')]
   
            for words in tokens:
            
                words_corpus = words_corpus + words + " "
                words_list.append(words)
            
        return words_corpus, words_list

    def plot_Cloud(wordCloud):
        plt.figure(figsize=(20,10), facecolor='w')
        plt.imshow(wordCloud)
        plt.axis("off")
        plt.tight_layout(pad=0)

    if choice == 'Positive Reviews':       
    
        st.subheader("This is the Sentiment Analysis of all the Positive Reviews for Sennheiser Momentum 3 Wireless Headphones")
        image1 = cv2.imread('snh2.jpg')
        cv2.imshow('Image',image1)
        st.image(image1, width = 400)
        st.write('The total number of positive reviews for Sennheiser Wireless Headphones are: ', positive_reviews.shape[0])

        st.subheader("The functions performed by the Sentiment Analyzer are :")

        st.write("1. Displays the dataset for all the Positive Reviews for Sennheiser Momentum 3 Wireless Headphones, along with the sentiment category for each review.")
        st.write("2. Displays the distribution of Positive Reviews on a pie plot.")
        st.write("3. Displays the distribution of ratings for all the positive reviews.")
        st.write("4. Generates a wordcloud for the positive reviews.")
        st.write("5. Generates a barplot for the Most Frequent words used in the positive reviews.")
        st.write("6. Displays the most positive review.")
        st.write("7. Displays the word count distribution for positive reviews for all ratings")
        st.write("8. Displays the Subjectivity Distribution for the reviews.")   
        
        Analyzer_choice = st.selectbox("Analysis Choice",  ["Display the positive reviews dataset for the product",
                                                            "Display the Pie Plot for Sentiment Distribution",
                                                            "Display the distribution of the Ratings for all the positive reviews",
                                                            "Generate a WordCloud for the positive reviews",
                                                            "Generate a barplot for the Most Frequent words used in the positive reviews",
                                                            "Display the most positive review",
                                                            "Display the word count distribution for the positive reviews for all ratings",
                                                            "Display the Subjectivity Distribution for all the positive reviews"])
          
        if st.button("Analyze"):
        
            if Analyzer_choice == "Display the positive reviews dataset for the product":
                st.write(positive_reviews.head(5))
                
            elif Analyzer_choice == "Display the Pie Plot for Sentiment Distribution":
                labels = ['positive reviews', 'negative reviews', 'neutral reviews']
                sizes = [pos_count, neg_count, neu_count]
                colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
                explode = (0.05,0.05,0.05)
                centre_circle = plt.Circle((0,0),0.70,fc='white')
                fig = plt.gcf()
                fig.gca().add_artist(centre_circle)
                plt.tight_layout()
                st.write(plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode))
                st.pyplot(use_container_width=True)
            
            elif Analyzer_choice == "Display the distribution of the Ratings for all the positive reviews":
                
                st.write(sns.countplot(x='Rating',data=positive_reviews, palette='RdBu'))
                st.pyplot(use_container_width=True)
                
            elif Analyzer_choice == "Generate a WordCloud for the positive reviews":
                
                positive_wordcloud = WordCloud(width=900, height=500).generate(wordcloud(positive_reviews)[0])
                st.write(plot_Cloud(positive_wordcloud))
                st.pyplot(use_container_width=True)
                
            elif Analyzer_choice == "Generate a barplot for the Most Frequent words used in the positive reviews":
                
                aa = nltk.FreqDist(wordcloud(positive_reviews)[1])
                dd = pd.DataFrame({'Wordcount': list(aa.keys()),
                  'Count': list(aa.values())})
                dd = dd.nlargest(columns="Count", n = 10) 
                plt.figure(figsize=(19,19))
                plt.title('Most Frequent Words')
                st.write(sns.barplot(data=dd, x= "Wordcount", y = "Count"))
                st.pyplot(use_container_width=True)
                
            elif Analyzer_choice == "Display the most positive review":
                
                pos_max = positive_reviews.loc[positive_reviews['Polarity']==max(positive_reviews['Polarity'])]
                st.write(pos_max)
                
            elif Analyzer_choice == "Display the word count distribution for the positive reviews for all ratings":
                
                st.write(sns.boxplot(x='Rating',y='Word_Count', data=positive_reviews, palette='RdBu', showfliers=False))
                st.pyplot(use_container_width=True)
                
            else:
                
                st.write(sns.distplot(positive_reviews['Subjectivity']))
                st.pyplot(use_container_width=True)
                
    
    elif choice == "Negative Reviews":
    
        st.subheader("This is the Sentiment Analysis of all the Negative Reviews for Sennheiser Momentum 3 Wireless Headphones")
        image1 = cv2.imread('snh2.jpg')
        cv2.imshow('Image',image1)
        st.image(image1, width = 400)
        st.write('The total number of negative reviews for Sennheiser Momentum 3 Wireless Headphones are: ',negative_reviews.shape[0])

        st.subheader("The functions performed by the Sentiment Analyzer are :")

        st.write("1. Displays the dataset for all the Negative Reviews for Sennheiser Momentum 3 Wireless Headphones, along with the sentiment category for each review.")
        st.write("2. Displays the distribution of Negative Reviews on a pie plot.")
        st.write("3. Displays the distribution of ratings for all the negative reviews.")
        st.write("4. Generates a wordcloud for the negative reviews.")
        st.write("5. Generates a barplot for the Most Frequent words used in the negative reviews.")
        st.write("6. Displays the most negative review.")     
        st.write("7. Displays the word count distribution for negative reviews for all ratings")
        st.write("8. Displays the Subjectivity Distribution for the negative reviews.")      
        

        Analyzer_choice = st.selectbox("Analysis Choice",  ["Display the negative reviews dataset for the product",
                                                            "Display the Pie Plot for Sentiment Distribution",
                                                            "Display the distribution of the Ratings for all the negative reviews",
                                                            "Generate a WordCloud for the negative reviews",
                                                            "Generate a barplot for the Most Frequent words used in the negative reviews",
                                                            "Display the most negative review",
                                                            "Display the word count distribution for the negative reviews for all ratings",
                                                            "Display the Subjectivity Distribution for all the negative reviews"])

        
        if st.button("Analyze"):
        
            if Analyzer_choice == "Display the negative reviews dataset for the product":
                st.write(negative_reviews.head(5))
                
            elif Analyzer_choice == "Display the Pie Plot for Sentiment Distribution":
                labels = ['positive reviews', 'negative reviews', 'neutral reviews']
                sizes = [pos_count, neg_count, neu_count]
                colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
                explode = (0.05,0.05,0.05)
                centre_circle = plt.Circle((0,0),0.70,fc='white')
                fig = plt.gcf()
                fig.gca().add_artist(centre_circle)
                plt.tight_layout()
                st.write(plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode))
                st.pyplot(use_container_width=True)
            
            elif Analyzer_choice == "Display the distribution of the Ratings for all the negative reviews":
                
                st.write(sns.countplot(x='Rating',data=negative_reviews, palette='RdBu'))
                st.pyplot(use_container_width=True)
                
            elif Analyzer_choice == "Generate a WordCloud for the negative reviews":
                
                negative_wordcloud = WordCloud(width=900, height=500).generate(wordcloud(negative_reviews)[0])
                st.write(plot_Cloud(negative_wordcloud))
                st.pyplot(use_container_width=True)
                
            elif Analyzer_choice == "Generate a barplot for the Most Frequent words used in the negative reviews":
                
                aa = nltk.FreqDist(wordcloud(positive_reviews)[1])
                dd = pd.DataFrame({'Wordcount': list(aa.keys()),
                  'Count': list(aa.values())})
                dd = dd.nlargest(columns="Count", n = 10) 
                plt.figure(figsize=(19,19))
                plt.title('Most Frequent Words')
                st.write(sns.barplot(data=dd, x= "Wordcount", y = "Count"))
                st.pyplot(use_container_width=True)
                
            elif Analyzer_choice == "Display the most negative review":
                
                pol_min = negative_reviews.loc[negative_reviews['Polarity']==min(negative_reviews['Polarity'])]
                st.write(pol_min)
                
            elif Analyzer_choice == "Display the word count distribution for the negative reviews for all ratings":
                
                st.write(sns.boxplot(x='Rating',y='Word_Count', data=negative_reviews, palette='RdBu', showfliers=False))
                st.pyplot(use_container_width=True)
                
            else:
                
                st.write(sns.distplot(negative_reviews['Subjectivity']))
                st.pyplot(use_container_width=True)

        
    else:
    
        st.subheader("This is the Sentiment Analysis of all of the Reviews for Sennheiser Momentum 3 Wireless Headphones")
        image1 = cv2.imread('snh2.jpg')
        cv2.imshow('Image',image1)
        st.image(image1, width = 400)
        st.write('The total number of reviews for Sennheiser Momentum 3 Wireless Headphones are: ',df.shape[0])

        st.subheader("The functions performed by the Sentiment Analyzer are :")

        st.write("1. Displays the dataset for all the Reviews for Sennheiser Momentum 3 Wireless Headphones, along with the sentiment category for each review.")
        st.write("2. Displays the pie plot for the sentiment distribution of the reviews.")
        st.write("3. Displays the distribution of ratings for all the reviews.")
        st.write("4. Generates a wordcloud for the reviews.")
        st.write("5. Generates a barplot for the Most Frequent words used in all the reviews.")
        st.write("6. Displays the most positive review.")
        st.write("7. Displays the most negative review.")
        st.write("8. Displays the word count distribution for the reviews for all ratings")        
        st.write("9. Generates the scatterplot for Polarity and Subjectivity, hued with the sentiment category.")        
        st.write("10. Displays the Polarity Distribution for the reviews.")
        st.write("11. Displays the Subjectivity Distribution for the reviews.")
        

        
        Analyzer_choice = st.selectbox("Analysis Choice",  ["Display the reviews dataset for the product",
                                                            "Display the Pie Plot for Sentiment Distribution",
                                                            "Display the distribution of the Ratings for all the Reviews",
                                                            "Generate a WordCloud for all the reviews",
                                                            "Generate a barplot for the Most Frequent words used in all the reviews",
                                                            "Display the most positive review",
                                                            "Display the most negative review",
                                                            "Display the word count distribution for the reviews for all ratings",
                                                            "Generate the scatterplot for Polarity and Subjectivity, hued with the sentiment category",
                                                            "Display the Polarity Distribution for all the reviews",
                                                            "Display the Subjectivity Distribution for all the reviews"])
        
        
        if st.button("Analyze"):
        
            if Analyzer_choice == "Display the reviews dataset for the product":
                st.write(df.head(5))
                
            elif Analyzer_choice == "Display the Pie Plot for Sentiment Distribution":
                
                labels = ['positive reviews', 'negative reviews', 'neutral reviews']
                sizes = [pos_count, neg_count, neu_count]
                colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
                explode = (0.05,0.05,0.05)
                centre_circle = plt.Circle((0,0),0.70,fc='white')
                fig = plt.gcf()
                fig.gca().add_artist(centre_circle)
                plt.tight_layout()
                st.write(plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode))
                st.pyplot(use_container_width=True)
                
            elif Analyzer_choice == "Display the distribution of the Ratings for all the Reviews":
            
                st.write(sns.countplot(x='Rating',data=df, palette='RdBu'))
                st.pyplot(use_container_width=True)
                
            elif Analyzer_choice == "Generate a WordCloud for all the reviews":
                
                wc = WordCloud(width=900, height=500).generate(wordcloud(df)[0])
                st.write(plot_Cloud(wc))
                st.pyplot(use_container_width=True)

                
            elif Analyzer_choice == "Generate a barplot for the Most Frequent words used in all the reviews":
                
                aa = nltk.FreqDist(wordcloud(df)[1])
                dd = pd.DataFrame({'Wordcount': list(aa.keys()),
                  'Count': list(aa.values())})
                dd = dd.nlargest(columns="Count", n = 10) 
                plt.figure(figsize=(19,19))
                plt.title('Most Frequent Words')
                st.write(sns.barplot(data=dd, x= "Wordcount", y = "Count"))
                st.pyplot(use_container_width=True)

                
            elif Analyzer_choice == "Display the most positive review":
                
                pos_max = df.loc[df['Polarity']==max(df['Polarity'])]
                st.write(pos_max)
                
            elif Analyzer_choice == "Display the most negative review":
                
                neg_max = df.loc[df['Polarity']==min(df['Polarity'])]
                st.write(neg_max)
            
            elif Analyzer_choice == "Display the word count distribution for the reviews for all ratings":
                
                st.write(sns.boxplot(x='Rating',y='Word_Count', data=df, palette='RdBu', showfliers=False))
                st.pyplot(use_container_width=True)
                
            elif Analyzer_choice == "Generate the scatterplot for Polarity and Subjectivity, hued with the sentiment category":
                
                st.write(sns.scatterplot(x='Polarity', y = 'Subjectivity', hue='Sentiment', data = df))
                st.pyplot(use_container_width=True)
                
            
            elif Analyzer_choice == "Display the Polarity Distribution for all the reviews":
                
                st.write(sns.distplot(df['Polarity']))
                st.pyplot(use_container_width=True)
                
            
            else:   
                
                st.write(sns.distplot(df['Subjectivity']))
                st.pyplot(use_container_width=True)
                
                pass
                
        
elif Product_Name == "CONTROVERSIAL PRODUCT_1":
    
    
    if choice == 'Positive Reviews':       
    
       pass
   
    elif choice == "Negative Reviews":
    
        pass
                
    else:
        pass
        
elif Product_Name == "CONTROVERSIAL PRODUCT_2":
    
    
    if choice == 'Positive Reviews':       
    
       pass
   
    elif choice == "Negative Reviews":
    
        pass
                
    else:
        pass
    
elif Product_Name == "CONTROVERSIAL PRODUCT_3":
    
    
    if choice == 'Positive Reviews':       
    
       pass
   
    elif choice == "Negative Reviews":
    
        pass
                
    else:
        pass
    
elif Product_Name == "CONTROVERSIAL PRODUCT_4":
    
    
    if choice == 'Positive Reviews':       
    
       pass
   
    elif choice == "Negative Reviews":
    
        pass
                
    else:
        pass