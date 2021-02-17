# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:51:08 2020

@author: Lenovo
"""

import time
import streamlit as st
import csv
import re
import cv2
import pandas as pd
from textblob import TextBlob
from wordcloud import WordCloud
import string
import nltk
from nltk.corpus import stopwords
pd.set_option('display.max_colwidth', -1)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#pd.options.display.width = 0
#pd.set_option('display.width', 20)
st.title('Amazon Product Reviews Analysis Data App')

image1 = cv2.imread('snh2.jpg')
image2 = cv2.imread('sentiment_distribution1.png')
image6 = cv2.imread('positive_reviews_wc1.png')
image7 = cv2.imread('negative_reviews_wc1.png')
image8 = cv2.imread('positive_reviews_wf1.png')
image9 = cv2.imread('negative_reviews_wf1.png')
image10 = cv2.imread('total_reviews_wc1.png')
image11 = cv2.imread('total_reviews_wf1.png')
image12 = cv2.imread('neutral_reviews_wc1.png')
image13 = cv2.imread('neutral_reviews_wf1.png')

image21 = cv2.imread('ring.jpg') 
image22 = cv2.imread('sentiment_distribution2.png')
image26 = cv2.imread('positive_reviews_wc2.png')
image27 = cv2.imread('negative_reviews_wc2.png')
image28 = cv2.imread('positive_reviews_wf2.png')
image29 = cv2.imread('negative_reviews_wf2.png')
image210 = cv2.imread('total_reviews_wc2.png')
image211 = cv2.imread('total_reviews_wf2.png')
image212 = cv2.imread('neutral_reviews_wc2.png')
image213 = cv2.imread('neutral_reviews_wf2.png')

image31 = cv2.imread('hannah.png')
image32 = cv2.imread('sentiment_distribution3.png')
image36 = cv2.imread('positive_reviews_wc3.png')
image37 = cv2.imread('negative_reviews_wc3.png')
image38 = cv2.imread('positive_reviews_wf3.png')
image39 = cv2.imread('negative_reviews_wf3.png')
image310 = cv2.imread('total_reviews_wc3.png')
image311 = cv2.imread('total_reviews_wf3.png')
image312 = cv2.imread('neutral_reviews_wc3.png')
image313 = cv2.imread('neutral_reviews_wf3.png')

image41 = cv2.imread('kindle.jpg')
image42 = cv2.imread('sentiment_distribution4.png')
image46 = cv2.imread('positive_reviews_wc4.png')
image47 = cv2.imread('negative_reviews_wc4.png')
image48 = cv2.imread('positive_reviews_wf4.png')
image49 = cv2.imread('negative_reviews_wf4.png')
image410 = cv2.imread('total_reviews_wc4.png')
image411 = cv2.imread('total_reviews_wf4.png')
image412 = cv2.imread('neutral_reviews_wc4.png')
image413 = cv2.imread('neutral_reviews_wf4.png')

image51 = cv2.imread('k95.png')
image52 = cv2.imread('sentiment_distribution5.png')
image56 = cv2.imread('positive_reviews_wc5.png')
image57 = cv2.imread('negative_reviews_wc5.png')
image58 = cv2.imread('positive_reviews_wf5.png')
image59 = cv2.imread('negative_reviews_wf5.png')
image510 = cv2.imread('total_reviews_wc5.png')
image511 = cv2.imread('total_reviews_wf5.png')
image512 = cv2.imread('neutral_reviews_wc5.png')
image513 = cv2.imread('neutral_reviews_wf5.png')

image61 = cv2.imread('echo.jpg')
image62 = cv2.imread('sentiment_distribution6.png')
image66 = cv2.imread('positive_reviews_wc6.png')
image67 = cv2.imread('negative_reviews_wc6.png')
image68 = cv2.imread('positive_reviews_wf6.png')
image69 = cv2.imread('negative_reviews_wf6.png')
image610 = cv2.imread('total_reviews_wc6.png')
image611 = cv2.imread('total_reviews_wf6.png')
image612 = cv2.imread('neutral_reviews_wc6.png')
image613 = cv2.imread('neutral_reviews_wf6.png')

image71 = cv2.imread('firestick.jpg')
image72 = cv2.imread('sentiment_distribution7.png')
image76 = cv2.imread('positive_reviews_wc7.png')
image77 = cv2.imread('negative_reviews_wc7.png')
image78 = cv2.imread('positive_reviews_wf7.png')
image79 = cv2.imread('negative_reviews_wf7.png')
image710 = cv2.imread('total_reviews_wc7.png')
image711 = cv2.imread('total_reviews_wf7.png')
image712 = cv2.imread('neutral_reviews_wc7.png')
image713 = cv2.imread('neutral_reviews_wf7.png')

st.subheader("This App gives the Sentiment Analysis of the reviews of various Products on Amazon.com")

st.sidebar.title("Navigation")
Others = ["Data App", "Source Code","YouTube Project Walkthrough", "Data App Description", "Contact"]
choice = st.sidebar.radio("Select the Navigation", Others)


if choice == "Data App":

    st.sidebar.title("Amazon Products")
    Products = ["Sennheiser Wireless Headphones","Ring Security Camera","The Four Winds: A Novel","Amazon Kindle","K95 Face Mask"," Amazon Echo Studio"," Amazon Alexa Voice Remote"]     
    Product_Name = st.sidebar.radio("Select the Product", Products)
    
    if Product_Name == "Sennheiser Wireless Headphones":
    
        dfs = pd.read_csv("snhzhr.csv")
        dfs['reviews'].fillna("", inplace = True)
        dfs['stars'].fillna(dfs['stars'].mode(), inplace=True)
    
        pos_max = dfs.loc[dfs['Compound Score']==max(dfs['Compound Score'])]
        neg_max = dfs.loc[dfs['Compound Score']==min(dfs['Compound Score'])]
    
        gp = dfs.groupby(by=['Sentiment'])
        positive_reviews = gp.get_group('Positive')
        negative_reviews = gp.get_group('Negative')
        neutral_reviews = gp.get_group('Neutral')
    
        st.subheader("This is the Sentiment Analysis of all the Reviews for Sennheiser Momentum 3 Wireless Headphones")
        image1 = cv2.imread('snh2.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for Sennheiser Wireless Headphones are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Sentiment Analyzer are :")

        st.write("1. Displays the Reviews for Sennheiser Momentum 3 Wireless Headphones, along with the sentiment category for each review.")
        st.write("2. Displays the Sentiment Distribution of the reviews.")
        st.write("3. Generate a wordcloud for all the Reviews")
        st.write("4. Display the Most Frequent Words used in all the Reviews")
                
        Analyzer_choice1 = st.selectbox("Analysis Choice",  ["Display few Reviews for the product", "Display the Sentiment Distribution of the Reviews","Generate a wordcloud for all the Reviews",
                                                        "Display the Most Frequent Words used in all the Reviews"])
    
        if st.button("Analyze"):
        
            if Analyzer_choice1 == "Display few Reviews for the product":
                st.table(dfs.head(2))
                
            elif Analyzer_choice1 == "Display the Sentiment Distribution of the Reviews":
                st.image(image2, height = 1000, width = 1000)
            
            elif Analyzer_choice1 == "Generate a wordcloud for all the Reviews":
                st.image(image10,  height = 1000, width = 1000)
            
            else:
                st.image(image11, height = 1000, width = 1000)       
        
        
        st.write("5. Displays the the Positive Reviews")
        st.write("6. Displays the Most Positive Review")
        st.write("7. Generates a wordcloud for the Positive Reviews")            
        st.write("8. Displays the Most Frequent Words used in the Positive Reviews")
    
    
          
        Analyzer_choice2 = st.selectbox("Analysis Choice",  ["Display the Positive Reviews","Display the Most Positive Review",
                                                        "Generate a wordcloud for the Positive Reviews",
                                                        "Display the Most Frequent Words used in the Positive Reviews"])          
                
        if st.button("Analyze "):
        
            if Analyzer_choice2 == "Display the Positive Reviews":
                st.table(positive_reviews.head(2))
                
            elif Analyzer_choice2 == "Display the Most Positive Review":
                st.table(pos_max)
                
            elif Analyzer_choice2 == "Generate a wordcloud for the Positive Reviews":
                st.image(image6,  height = 1000, width = 1000)
                
            else:
                st.image(image8,  height = 1000, width = 1000)
                
            
        st.write("9. Displays the Negative Reviews")
        st.write("10. Displays the Most Negative Review")
        st.write("11. Generates a wordcloud for the Negative Reviews")            
        st.write("12. Displays the Most Frequent Words used in the Negative Reviews")
              
        Analyzer_choice3 = st.selectbox("Analysis Choice",  ["Displays the Negative Reviews","Display the Most Negative Review",
                                                        "Generate a wordcloud for the Negative Reviews",
                                                        "Display the Most Frequent Words used in the Negative Reviews"])          
                
        if st.button("Analyze  "):
        
            if Analyzer_choice3 == "Displays the Negative Reviews":
                st.table(negative_reviews.head(2))
                
            elif Analyzer_choice3 == "Display the Most Negative Review":
                st.table(neg_max[:1])
                
            elif Analyzer_choice3 == "Generate a wordcloud for the Negative Reviews":
                st.image(image7, height = 1000, width = 1000)
                
            else:
                st.image(image9, height = 1000, width = 1000)
   
        st.write("13. Displays the Neutral Reviews")
        st.write("14. Generate a wordcloud for the Neutral Reviews")
        st.write("15. Displays the Most Frequent Words used in the Neutral Reviews")

        Analyzer_choice4 = st.selectbox("Analysis Choice",  ["Display the Neutral Reviews","Generate a wordcloud for the Neutral Reviews",
                                                        "Display the Most Frequent Words used in the Neutral Reviews"])
        if st.button("Analyze   "):     
        
            if Analyzer_choice4 == "Display the Neutral Reviews":
                st.table(neutral_reviews.head(2))
            
            elif Analyzer_choice4 == "Generate a wordcloud for the Neutral Reviews":
                st.image(image12, height = 1000, width = 1000)
            
            else:
                st.image(image13, height = 1000, width = 1000)
        
          
    elif Product_Name == "Ring Security Camera":
    
        dfs = pd.read_csv("p22.csv") 
        dfs['reviews'].fillna("", inplace = True)
        dfs['stars'].fillna(dfs['stars'].mode(), inplace=True)
    
        pos_max = dfs.loc[dfs['Compound Score']==max(dfs['Compound Score'])]
        neg_max = dfs.loc[dfs['Compound Score']==min(dfs['Compound Score'])]
    
        gp = dfs.groupby(by=['Sentiment'])
        positive_reviews = gp.get_group('Positive')
        negative_reviews = gp.get_group('Negative')
        neutral_reviews = gp.get_group('Neutral')
    
        st.subheader("This is the Sentiment Analysis of all the Reviews for Ring Security Camera")
        image1 = cv2.imread('ring.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for Ring Security Camera are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Sentiment Analyzer are :")

        st.write("1. Displays the Reviews for Ring Security Camera, along with the sentiment category for each review.")
        st.write("2. Displays the Sentiment Distribution of the reviews.")
        st.write("3. Generate a wordcloud for all the Reviews")
        st.write("4. Display the Most Frequent Words used in all the Reviews")
                
        Analyzer_choice1 = st.selectbox("Analysis Choice",  ["Display few Reviews for the product", "Display the Sentiment Distribution of the Reviews","Generate a wordcloud for all the Reviews",
                                                        "Display the Most Frequent Words used in all the Reviews"])
    
        if st.button("Analyze"):
        
            if Analyzer_choice1 == "Display few Reviews for the product":
                st.table(dfs.head(2))
                
            elif Analyzer_choice1 == "Display the Sentiment Distribution of the Reviews":
                st.image(image22, height = 1000, width = 1000)
            
            elif Analyzer_choice1 == "Generate a wordcloud for all the Reviews":
                st.image(image210,  height = 1000, width = 1000)
            
            else:
                st.image(image211, height = 1000, width = 1000)       
        
        
        st.write("5. Displays the the Positive Reviews")
        st.write("6. Displays the Most Positive Review")
        st.write("7. Generates a wordcloud for the Positive Reviews")            
        st.write("8. Displays the Most Frequent Words used in the Positive Reviews")
    
    
          
        Analyzer_choice2 = st.selectbox("Analysis Choice",  ["Display the Positive Reviews","Display the Most Positive Review",
                                                        "Generate a wordcloud for the Positive Reviews",
                                                        "Display the Most Frequent Words used in the Positive Reviews"])          
                
        if st.button("Analyze "):
        
            if Analyzer_choice2 == "Display the Positive Reviews":
                st.table(positive_reviews.head(2))
                
            elif Analyzer_choice2 == "Display the Most Positive Review":
                st.table(pos_max)
                
            elif Analyzer_choice2 == "Generate a wordcloud for the Positive Reviews":
                st.image(image26,  height = 1000, width = 1000)
                
            else:
                st.image(image28,  height = 1000, width = 1000)
                
            
        st.write("9. Displays the Negative Reviews")
        st.write("10. Displays the Most Negative Review")
        st.write("11. Generates a wordcloud for the Negative Reviews")            
        st.write("12. Displays the Most Frequent Words used in the Negative Reviews")
              
        Analyzer_choice3 = st.selectbox("Analysis Choice",  ["Displays the Negative Reviews","Display the Most Negative Review",
                                                        "Generate a wordcloud for the Negative Reviews",
                                                        "Display the Most Frequent Words used in the Negative Reviews"])          
                
        if st.button("Analyze  "):
        
            if Analyzer_choice3 == "Displays the Negative Reviews":
                st.table(negative_reviews.head(2))
                
            elif Analyzer_choice3 == "Display the Most Negative Review":
                st.table(neg_max[:1])
                
            elif Analyzer_choice3 == "Generate a wordcloud for the Negative Reviews":
                st.image(image27, height = 1000, width = 1000)
                
            else:
                st.image(image29, height = 1000, width = 1000)
   
        st.write("13. Displays the Neutral Reviews")
        st.write("14. Generate a wordcloud for the Neutral Reviews")
        st.write("15. Displays the Most Frequent Words used in the Neutral Reviews")

        Analyzer_choice4 = st.selectbox("Analysis Choice",  ["Display the Neutral Reviews","Generate a wordcloud for the Neutral Reviews",
                                                        "Display the Most Frequent Words used in the Neutral Reviews"])
        if st.button("Analyze   "):     
        
            if Analyzer_choice4 == "Display the Neutral Reviews":
                st.table(neutral_reviews.head(2))
            
            elif Analyzer_choice4 == "Generate a wordcloud for the Neutral Reviews":
                st.image(image212, height = 1000, width = 1000)
            
            else:
                st.image(image213, height = 1000, width = 1000)
        
    elif Product_Name == "The Four Winds: A Novel":

        dfs = pd.read_csv("p33.csv") 
        dfs['reviews'].fillna("", inplace = True)
        dfs['stars'].fillna(dfs['stars'].mode(), inplace=True)
    
        pos_max = dfs.loc[dfs['Compound Score']==max(dfs['Compound Score'])]
        neg_max = dfs.loc[dfs['Compound Score']==min(dfs['Compound Score'])]
    
        gp = dfs.groupby(by=['Sentiment'])
        positive_reviews = gp.get_group('Positive')
        negative_reviews = gp.get_group('Negative')
        neutral_reviews = gp.get_group('Neutral')
    
        st.subheader("This is the Sentiment Analysis of all the Reviews for The Four Winds: A Novel")
        image1 = cv2.imread('hannah.png')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for The Four Winds: A Novel are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Sentiment Analyzer are :")

        st.write("1. Displays the Reviews for The Four Winds: A Novel, along with the sentiment category for each review.")
        st.write("2. Displays the Sentiment Distribution of the reviews.")
        st.write("3. Generate a wordcloud for all the Reviews")
        st.write("4. Display the Most Frequent Words used in all the Reviews")
                
        Analyzer_choice1 = st.selectbox("Analysis Choice",  ["Display few Reviews for the product", "Display the Sentiment Distribution of the Reviews","Generate a wordcloud for all the Reviews",
                                                        "Display the Most Frequent Words used in all the Reviews"])
    
        if st.button("Analyze"):
        
            if Analyzer_choice1 == "Display few Reviews for the product":
                st.table(dfs.head(2))
                
            elif Analyzer_choice1 == "Display the Sentiment Distribution of the Reviews":
                st.image(image32, height = 1000, width = 1000)
            
            elif Analyzer_choice1 == "Generate a wordcloud for all the Reviews":
                st.image(image310,  height = 1000, width = 1000)
            
            else:
                st.image(image311, height = 1000, width = 1000)       
        
        
        st.write("5. Displays the the Positive Reviews")
        st.write("6. Displays the Most Positive Review")
        st.write("7. Generates a wordcloud for the Positive Reviews")            
        st.write("8. Displays the Most Frequent Words used in the Positive Reviews")
    
    
          
        Analyzer_choice2 = st.selectbox("Analysis Choice",  ["Display the Positive Reviews","Display the Most Positive Review",
                                                        "Generate a wordcloud for the Positive Reviews",
                                                        "Display the Most Frequent Words used in the Positive Reviews"])          
                
        if st.button("Analyze "):
        
            if Analyzer_choice2 == "Display the Positive Reviews":
                st.table(positive_reviews.head(2))
                
            elif Analyzer_choice2 == "Display the Most Positive Review":
                st.table(pos_max)
                
            elif Analyzer_choice2 == "Generate a wordcloud for the Positive Reviews":
                st.image(image36,  height = 1000, width = 1000)
                
            else:
                st.image(image38,  height = 1000, width = 1000)
                
            
        st.write("9. Displays the Negative Reviews")
        st.write("10. Displays the Most Negative Review")
        st.write("11. Generates a wordcloud for the Negative Reviews")            
        st.write("12. Displays the Most Frequent Words used in the Negative Reviews")
              
        Analyzer_choice3 = st.selectbox("Analysis Choice",  ["Displays the Negative Reviews","Display the Most Negative Review",
                                                        "Generate a wordcloud for the Negative Reviews",
                                                        "Display the Most Frequent Words used in the Negative Reviews"])          
                
        if st.button("Analyze  "):
        
            if Analyzer_choice3 == "Displays the Negative Reviews":
                st.table(negative_reviews.head(2))
                
            elif Analyzer_choice3 == "Display the Most Negative Review":
                st.table(neg_max[:1])
                
            elif Analyzer_choice3 == "Generate a wordcloud for the Negative Reviews":
                st.image(image37, height = 1000, width = 1000)
                
            else:
                st.image(image39, height = 1000, width = 1000)
   
        st.write("13. Displays the Neutral Reviews")
        st.write("14. Generate a wordcloud for the Neutral Reviews")
        st.write("15. Displays the Most Frequent Words used in the Neutral Reviews")

        Analyzer_choice4 = st.selectbox("Analysis Choice",  ["Display the Neutral Reviews","Generate a wordcloud for the Neutral Reviews",
                                                        "Display the Most Frequent Words used in the Neutral Reviews"])
        if st.button("Analyze   "):     
        
            if Analyzer_choice4 == "Display the Neutral Reviews":
                st.table(neutral_reviews.head(2))
            
            elif Analyzer_choice4 == "Generate a wordcloud for the Neutral Reviews":
                st.image(image312, height = 1000, width = 1000)
            
            else:
                st.image(image313, height = 1000, width = 1000)        
                  
    elif Product_Name == "Amazon Kindle":   

        dfs = pd.read_csv("p33.csv") 
        dfs['reviews'].fillna("", inplace = True)
        dfs['stars'].fillna(dfs['stars'].mode(), inplace=True)
    
        pos_max = dfs.loc[dfs['Compound Score']==max(dfs['Compound Score'])]
        neg_max = dfs.loc[dfs['Compound Score']==min(dfs['Compound Score'])]
    
        gp = dfs.groupby(by=['Sentiment'])
        positive_reviews = gp.get_group('Positive')
        negative_reviews = gp.get_group('Negative')
        neutral_reviews = gp.get_group('Neutral')
    
        st.subheader("This is the Sentiment Analysis of all the Reviews for Amazon Kindle")
        image1 = cv2.imread('kindle.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for the Amazon Kindle are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Sentiment Analyzer are :")

        st.write("1. Displays the Reviews for the Amazon Kindle, along with the sentiment category for each review.")
        st.write("2. Displays the Sentiment Distribution of the reviews.")
        st.write("3. Generate a wordcloud for all the Reviews")
        st.write("4. Display the Most Frequent Words used in all the Reviews")
                
        Analyzer_choice1 = st.selectbox("Analysis Choice",  ["Display few Reviews for the product", "Display the Sentiment Distribution of the Reviews","Generate a wordcloud for all the Reviews",
                                                        "Display the Most Frequent Words used in all the Reviews"])
    
        if st.button("Analyze"):
        
            if Analyzer_choice1 == "Display few Reviews for the product":
                st.table(dfs.head(2))
                
            elif Analyzer_choice1 == "Display the Sentiment Distribution of the Reviews":
                st.image(image42, height = 1000, width = 1000)
            
            elif Analyzer_choice1 == "Generate a wordcloud for all the Reviews":
                st.image(image410,  height = 1000, width = 1000)
            
            else:
                st.image(image411, height = 1000, width = 1000)       
        
        
        st.write("5. Displays the the Positive Reviews")
        st.write("6. Displays the Most Positive Review")
        st.write("7. Generates a wordcloud for the Positive Reviews")            
        st.write("8. Displays the Most Frequent Words used in the Positive Reviews")
    
    
          
        Analyzer_choice2 = st.selectbox("Analysis Choice",  ["Display the Positive Reviews","Display the Most Positive Review",
                                                        "Generate a wordcloud for the Positive Reviews",
                                                        "Display the Most Frequent Words used in the Positive Reviews"])          
                
        if st.button("Analyze "):
        
            if Analyzer_choice2 == "Display the Positive Reviews":
                st.table(positive_reviews.head(2))
                
            elif Analyzer_choice2 == "Display the Most Positive Review":
                st.table(pos_max)
                
            elif Analyzer_choice2 == "Generate a wordcloud for the Positive Reviews":
                st.image(image46,  height = 1000, width = 1000)
                
            else:
                st.image(image48,  height = 1000, width = 1000)
                
            
        st.write("9. Displays the Negative Reviews")
        st.write("10. Displays the Most Negative Review")
        st.write("11. Generates a wordcloud for the Negative Reviews")            
        st.write("12. Displays the Most Frequent Words used in the Negative Reviews")
              
        Analyzer_choice3 = st.selectbox("Analysis Choice",  ["Displays the Negative Reviews","Display the Most Negative Review",
                                                        "Generate a wordcloud for the Negative Reviews",
                                                        "Display the Most Frequent Words used in the Negative Reviews"])          
                
        if st.button("Analyze  "):
        
            if Analyzer_choice3 == "Displays the Negative Reviews":
                st.table(negative_reviews.head(2))
                
            elif Analyzer_choice3 == "Display the Most Negative Review":
                st.table(neg_max[:1])
                
            elif Analyzer_choice3 == "Generate a wordcloud for the Negative Reviews":
                st.image(image47, height = 1000, width = 1000)
                
            else:
                st.image(image49, height = 1000, width = 1000)
   
        st.write("13. Displays the Neutral Reviews")
        st.write("14. Generate a wordcloud for the Neutral Reviews")
        st.write("15. Displays the Most Frequent Words used in the Neutral Reviews")

        Analyzer_choice4 = st.selectbox("Analysis Choice",  ["Display the Neutral Reviews","Generate a wordcloud for the Neutral Reviews",
                                                        "Display the Most Frequent Words used in the Neutral Reviews"])
        if st.button("Analyze   "):     
        
            if Analyzer_choice4 == "Display the Neutral Reviews":
                st.table(neutral_reviews.head(2))
            
            elif Analyzer_choice4 == "Generate a wordcloud for the Neutral Reviews":
                st.image(image412, height = 1000, width = 1000)
            
            else:
                st.image(image413, height = 1000, width = 1000)
    
    elif Product_Name == "K95 Face Mask":  

        dfs = pd.read_csv("p55.csv") 
        dfs['reviews'].fillna("", inplace = True)
        dfs['stars'].fillna(dfs['stars'].mode(), inplace=True)
    
        pos_max = dfs.loc[dfs['Compound Score']==max(dfs['Compound Score'])]
        neg_max = dfs.loc[dfs['Compound Score']==min(dfs['Compound Score'])]
    
        gp = dfs.groupby(by=['Sentiment'])
        positive_reviews = gp.get_group('Positive')
        negative_reviews = gp.get_group('Negative')
        neutral_reviews = gp.get_group('Neutral')
    
        st.subheader("This is the Sentiment Analysis of all the Reviews for K95 Face Mask")
        image1 = cv2.imread('k95.png')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for the K95 Face Mask are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Sentiment Analyzer are :")

        st.write("1. Displays the Reviews for the K95 Face Mask, along with the sentiment category for each review.")
        st.write("2. Displays the Sentiment Distribution of the reviews.")
        st.write("3. Generate a wordcloud for all the Reviews")
        st.write("4. Display the Most Frequent Words used in all the Reviews")
                
        Analyzer_choice1 = st.selectbox("Analysis Choice",  ["Display few Reviews for the product", "Display the Sentiment Distribution of the Reviews","Generate a wordcloud for all the Reviews",
                                                        "Display the Most Frequent Words used in all the Reviews"])
    
        if st.button("Analyze"):
        
            if Analyzer_choice1 == "Display few Reviews for the product":
                st.table(dfs.head(2))
                
            elif Analyzer_choice1 == "Display the Sentiment Distribution of the Reviews":
                st.image(image52, height = 1000, width = 1000)
            
            elif Analyzer_choice1 == "Generate a wordcloud for all the Reviews":
                st.image(image510,  height = 1000, width = 1000)
            
            else:
                st.image(image511, height = 1000, width = 1000)       
        
        
        st.write("5. Displays the the Positive Reviews")
        st.write("6. Displays the Most Positive Review")
        st.write("7. Generates a wordcloud for the Positive Reviews")            
        st.write("8. Displays the Most Frequent Words used in the Positive Reviews")
    
    
          
        Analyzer_choice2 = st.selectbox("Analysis Choice",  ["Display the Positive Reviews","Display the Most Positive Review",
                                                        "Generate a wordcloud for the Positive Reviews",
                                                        "Display the Most Frequent Words used in the Positive Reviews"])          
                
        if st.button("Analyze "):
        
            if Analyzer_choice2 == "Display the Positive Reviews":
                st.table(positive_reviews.head(2))
                
            elif Analyzer_choice2 == "Display the Most Positive Review":
                st.table(pos_max)
                
            elif Analyzer_choice2 == "Generate a wordcloud for the Positive Reviews":
                st.image(image56,  height = 1000, width = 1000)
                
            else:
                st.image(image58,  height = 1000, width = 1000)
                
            
        st.write("9. Displays the Negative Reviews")
        st.write("10. Displays the Most Negative Review")
        st.write("11. Generates a wordcloud for the Negative Reviews")            
        st.write("12. Displays the Most Frequent Words used in the Negative Reviews")
              
        Analyzer_choice3 = st.selectbox("Analysis Choice",  ["Displays the Negative Reviews","Display the Most Negative Review",
                                                        "Generate a wordcloud for the Negative Reviews",
                                                        "Display the Most Frequent Words used in the Negative Reviews"])          
                
        if st.button("Analyze  "):
        
            if Analyzer_choice3 == "Displays the Negative Reviews":
                st.table(negative_reviews.head(2))
                
            elif Analyzer_choice3 == "Display the Most Negative Review":
                st.table(neg_max[:1])
                
            elif Analyzer_choice3 == "Generate a wordcloud for the Negative Reviews":
                st.image(image57, height = 1000, width = 1000)
                
            else:
                st.image(image59, height = 1000, width = 1000)
   
        st.write("13. Displays the Neutral Reviews")
        st.write("14. Generate a wordcloud for the Neutral Reviews")
        st.write("15. Displays the Most Frequent Words used in the Neutral Reviews")

        Analyzer_choice4 = st.selectbox("Analysis Choice",  ["Display the Neutral Reviews","Generate a wordcloud for the Neutral Reviews",
                                                        "Display the Most Frequent Words used in the Neutral Reviews"])
        if st.button("Analyze   "):     
        
            if Analyzer_choice4 == "Display the Neutral Reviews":
                st.table(neutral_reviews.head(2))
            
            elif Analyzer_choice4 == "Generate a wordcloud for the Neutral Reviews":
                st.image(image512, height = 1000, width = 1000)
            
            else:
                st.image(image513, height = 1000, width = 1000)
    
    elif Product_Name == " Amazon Echo Studio":

        dfs = pd.read_csv("p66.csv") 
        dfs['reviews'].fillna("", inplace = True)
        dfs['stars'].fillna(dfs['stars'].mode(), inplace=True)
    
        pos_max = dfs.loc[dfs['Compound Score']==max(dfs['Compound Score'])]
        neg_max = dfs.loc[dfs['Compound Score']==min(dfs['Compound Score'])]
    
        gp = dfs.groupby(by=['Sentiment'])
        positive_reviews = gp.get_group('Positive')
        negative_reviews = gp.get_group('Negative')
        neutral_reviews = gp.get_group('Neutral')
    
        st.subheader("This is the Sentiment Analysis of all the Reviews for Amazon Echo Studio")
        image1 = cv2.imread('echo.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for the Amazon Echo Studio are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Sentiment Analyzer are :")

        st.write("1. Displays the Reviews for the Amazon Echo Studio, along with the sentiment category for each review.")
        st.write("2. Displays the Sentiment Distribution of the reviews.")
        st.write("3. Generate a wordcloud for all the Reviews")
        st.write("4. Display the Most Frequent Words used in all the Reviews")
                
        Analyzer_choice1 = st.selectbox("Analysis Choice",  ["Display few Reviews for the product", "Display the Sentiment Distribution of the Reviews","Generate a wordcloud for all the Reviews",
                                                        "Display the Most Frequent Words used in all the Reviews"])
    
        if st.button("Analyze"):
        
            if Analyzer_choice1 == "Display few Reviews for the product":
                st.table(dfs.head(2))
                
            elif Analyzer_choice1 == "Display the Sentiment Distribution of the Reviews":
                st.image(image62, height = 1000, width = 1000)
            
            elif Analyzer_choice1 == "Generate a wordcloud for all the Reviews":
                st.image(image610,  height = 1000, width = 1000)
            
            else:
                st.image(image611, height = 1000, width = 1000)       
        
        
        st.write("5. Displays the the Positive Reviews")
        st.write("6. Displays the Most Positive Review")
        st.write("7. Generates a wordcloud for the Positive Reviews")            
        st.write("8. Displays the Most Frequent Words used in the Positive Reviews")
    
    
          
        Analyzer_choice2 = st.selectbox("Analysis Choice",  ["Display the Positive Reviews","Display the Most Positive Review",
                                                        "Generate a wordcloud for the Positive Reviews",
                                                        "Display the Most Frequent Words used in the Positive Reviews"])          
                
        if st.button("Analyze "):
        
            if Analyzer_choice2 == "Display the Positive Reviews":
                st.table(positive_reviews.head(2))
                
            elif Analyzer_choice2 == "Display the Most Positive Review":
                st.table(pos_max)
                
            elif Analyzer_choice2 == "Generate a wordcloud for the Positive Reviews":
                st.image(image66,  height = 1000, width = 1000)
                
            else:
                st.image(image68,  height = 1000, width = 1000)
                
            
        st.write("9. Displays the Negative Reviews")
        st.write("10. Displays the Most Negative Review")
        st.write("11. Generates a wordcloud for the Negative Reviews")            
        st.write("12. Displays the Most Frequent Words used in the Negative Reviews")
              
        Analyzer_choice3 = st.selectbox("Analysis Choice",  ["Displays the Negative Reviews","Display the Most Negative Review",
                                                        "Generate a wordcloud for the Negative Reviews",
                                                        "Display the Most Frequent Words used in the Negative Reviews"])          
                
        if st.button("Analyze  "):
        
            if Analyzer_choice3 == "Displays the Negative Reviews":
                st.table(negative_reviews.head(2))
                
            elif Analyzer_choice3 == "Display the Most Negative Review":
                st.table(neg_max[:1])
                
            elif Analyzer_choice3 == "Generate a wordcloud for the Negative Reviews":
                st.image(image67, height = 1000, width = 1000)
                
            else:
                st.image(image69, height = 1000, width = 1000)
   
        st.write("13. Displays the Neutral Reviews")
        st.write("14. Generate a wordcloud for the Neutral Reviews")
        st.write("15. Displays the Most Frequent Words used in the Neutral Reviews")

        Analyzer_choice4 = st.selectbox("Analysis Choice",  ["Display the Neutral Reviews","Generate a wordcloud for the Neutral Reviews",
                                                        "Display the Most Frequent Words used in the Neutral Reviews"])
        if st.button("Analyze   "):     
        
            if Analyzer_choice4 == "Display the Neutral Reviews":
                st.table(neutral_reviews.head(2))
            
            elif Analyzer_choice4 == "Generate a wordcloud for the Neutral Reviews":
                st.image(image612, height = 1000, width = 1000)
            
            else:
                st.image(image613, height = 1000, width = 1000)
        
    else:

        dfs = pd.read_csv("p77.csv") 
        dfs['reviews'].fillna("", inplace = True)
        dfs['stars'].fillna(dfs['stars'].mode(), inplace=True)
    
        pos_max = dfs.loc[dfs['Compound Score']==max(dfs['Compound Score'])]
        neg_max = dfs.loc[dfs['Compound Score']==min(dfs['Compound Score'])]
    
        gp = dfs.groupby(by=['Sentiment'])
        positive_reviews = gp.get_group('Positive')
        negative_reviews = gp.get_group('Negative')
        neutral_reviews = gp.get_group('Neutral')
    
        st.subheader("This is the Sentiment Analysis of all the Reviews for Amazon Alexa Voice Remote")
        image1 = cv2.imread('firestick.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for the Amazon Alexa Voice Remote are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Sentiment Analyzer are :")

        st.write("1. Displays the Reviews for the Amazon Alexa Voice Remote, along with the sentiment category for each review.")
        st.write("2. Displays the Sentiment Distribution of the reviews.")
        st.write("3. Generate a wordcloud for all the Reviews")
        st.write("4. Display the Most Frequent Words used in all the Reviews")
                
        Analyzer_choice1 = st.selectbox("Analysis Choice",  ["Display few Reviews for the product", "Display the Sentiment Distribution of the Reviews","Generate a wordcloud for all the Reviews",
                                                        "Display the Most Frequent Words used in all the Reviews"])
    
        if st.button("Analyze"):
        
            if Analyzer_choice1 == "Display few Reviews for the product":
                st.table(dfs.head(2))
                
            elif Analyzer_choice1 == "Display the Sentiment Distribution of the Reviews":
                st.image(image72, height = 1000, width = 1000)
            
            elif Analyzer_choice1 == "Generate a wordcloud for all the Reviews":
                st.image(image710,  height = 1000, width = 1000)
            
            else:
                st.image(image711, height = 1000, width = 1000)       
        
        
        st.write("5. Displays the the Positive Reviews")
        st.write("6. Displays the Most Positive Review")
        st.write("7. Generates a wordcloud for the Positive Reviews")            
        st.write("8. Displays the Most Frequent Words used in the Positive Reviews")
    
    
          
        Analyzer_choice2 = st.selectbox("Analysis Choice",  ["Display the Positive Reviews","Display the Most Positive Review",
                                                        "Generate a wordcloud for the Positive Reviews",
                                                        "Display the Most Frequent Words used in the Positive Reviews"])          
                
        if st.button("Analyze "):
        
            if Analyzer_choice2 == "Display the Positive Reviews":
                st.table(positive_reviews.head(2))
                
            elif Analyzer_choice2 == "Display the Most Positive Review":
                st.table(pos_max)
                
            elif Analyzer_choice2 == "Generate a wordcloud for the Positive Reviews":
                st.image(image76,  height = 1000, width = 1000)
                
            else:
                st.image(image78,  height = 1000, width = 1000)
                
            
        st.write("9. Displays the Negative Reviews")
        st.write("10. Displays the Most Negative Review")
        st.write("11. Generates a wordcloud for the Negative Reviews")            
        st.write("12. Displays the Most Frequent Words used in the Negative Reviews")
              
        Analyzer_choice3 = st.selectbox("Analysis Choice",  ["Displays the Negative Reviews","Display the Most Negative Review",
                                                        "Generate a wordcloud for the Negative Reviews",
                                                        "Display the Most Frequent Words used in the Negative Reviews"])          
                
        if st.button("Analyze  "):
        
            if Analyzer_choice3 == "Displays the Negative Reviews":
                st.table(negative_reviews.head(2))
                
            elif Analyzer_choice3 == "Display the Most Negative Review":
                st.table(neg_max[:1])
                
            elif Analyzer_choice3 == "Generate a wordcloud for the Negative Reviews":
                st.image(image77, height = 1000, width = 1000)
                
            else:
                st.image(image79, height = 1000, width = 1000)
   
        st.write("13. Displays the Neutral Reviews")
        st.write("14. Generate a wordcloud for the Neutral Reviews")
        st.write("15. Displays the Most Frequent Words used in the Neutral Reviews")

        Analyzer_choice4 = st.selectbox("Analysis Choice",  ["Display the Neutral Reviews","Generate a wordcloud for the Neutral Reviews",
                                                        "Display the Most Frequent Words used in the Neutral Reviews"])
        if st.button("Analyze   "):     
        
            if Analyzer_choice4 == "Display the Neutral Reviews":
                st.table(neutral_reviews.head(2))
            
            elif Analyzer_choice4 == "Generate a wordcloud for the Neutral Reviews":
                st.image(image712, height = 1000, width = 1000)
            
            else:
                st.image(image713, height = 1000, width = 1000)
        

elif choice == "Source Code":
    
    st.subheader("Code Images..........")
    st.graphviz_chart("""
        digraph{
        Product Review -> Sentiment
        Sentiment -> Positive
        Sentiment -> Neutral 
        Sentiment -> Negative
        Positive -> MostPositiveSentence
        Positive -> WordCloud
        Positive -> WordFrequency
        Negative -> MostNegativeSentence
        Negative -> WordCloud
        Negative -> WordFrequency
        Neutral -> WordCloud
        Neutral -> WordFrequency
        }
        """)

elif choice == "YouTube Project Walkthrough":
    
    st.write("Add YouTube Video ..... st.video(.mp4)...")
    
elif choice == "Data App Description":
    
    st.write("Data App Description Add the Medium Article GIF.....st.video(.mp4)...")
    
    
else:
    
    st.subheader("Add the LinkedIn GIF...st.video(.mp4)...Contact Info ??")
    st.subheader("Add Links for LinkedIn, GitHub, Portfolio Website")  













                                                          