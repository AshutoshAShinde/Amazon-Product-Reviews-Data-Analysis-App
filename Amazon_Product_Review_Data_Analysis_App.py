# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:51:08 2020

@author: Lenovo
"""

import streamlit as st
import pandas as pd
import matplotlib.image as mpimg
#
pd.set_option('display.max_colwidth', -1)
st.title('Amazon Product Reviews Data Analysis App')

image1 = mpimg.imread('snh2.jpg')
image2 = mpimg.imread('sentiment_distribution1.png')
image6 = mpimg.imread('positive_reviews_wc1.png')
image7 = mpimg.imread('negative_reviews_wc1.png')
image8 = mpimg.imread('positive_reviews_wf1.png')
image9 = mpimg.imread('negative_reviews_wf1.png')
image10 = mpimg.imread('total_reviews_wc1.png')
image11 = mpimg.imread('total_reviews_wf1.png')
image12 = mpimg.imread('neutral_reviews_wc1.png')
image13 = mpimg.imread('neutral_reviews_wf1.png')

image21 = mpimg.imread('ring.jpg') 
image22 = mpimg.imread('sentiment_distribution2.png')
image26 = mpimg.imread('positive_reviews_wc2.png')
image27 = mpimg.imread('negative_reviews_wc2.png')
image28 = mpimg.imread('positive_reviews_wf2.png')
image29 = mpimg.imread('negative_reviews_wf2.png')
image210 = mpimg.imread('total_reviews_wc2.png')
image211 = mpimg.imread('total_reviews_wf2.png')
image212 = mpimg.imread('neutral_reviews_wc2.png')
image213 = mpimg.imread('neutral_reviews_wf2.png')

image31 = mpimg.imread('hannah.png')
image32 = mpimg.imread('sentiment_distribution3.png')
image36 = mpimg.imread('positive_reviews_wc3.png')
image37 = mpimg.imread('negative_reviews_wc3.png')
image38 = mpimg.imread('positive_reviews_wf3.png')
image39 = mpimg.imread('negative_reviews_wf3.png')
image310 = mpimg.imread('total_reviews_wc3.png')
image311 = mpimg.imread('total_reviews_wf3.png')
image312 = mpimg.imread('neutral_reviews_wc3.png')
image313 = mpimg.imread('neutral_reviews_wf3.png')

image41 = mpimg.imread('kindle.jpg')
image42 = mpimg.imread('sentiment_distribution4.png')
image46 = mpimg.imread('positive_reviews_wc4.png')
image47 = mpimg.imread('negative_reviews_wc4.png')
image48 = mpimg.imread('positive_reviews_wf4.png')
image49 = mpimg.imread('negative_reviews_wf4.png')
image410 = mpimg.imread('total_reviews_wc4.png')
image411 = mpimg.imread('total_reviews_wf4.png')
image412 = mpimg.imread('neutral_reviews_wc4.png')
image413 = mpimg.imread('neutral_reviews_wf4.png')

image51 = mpimg.imread('k95.png')
image52 = mpimg.imread('sentiment_distribution5.png')
image56 = mpimg.imread('positive_reviews_wc5.png')
image57 = mpimg.imread('negative_reviews_wc5.png')
image58 = mpimg.imread('positive_reviews_wf5.png')
image59 = mpimg.imread('negative_reviews_wf5.png')
image510 = mpimg.imread('total_reviews_wc5.png')
image511 = mpimg.imread('total_reviews_wf5.png')
image512 = mpimg.imread('neutral_reviews_wc5.png')
image513 = mpimg.imread('neutral_reviews_wf5.png')

image61 = mpimg.imread('echo.jpg')
image62 = mpimg.imread('sentiment_distribution6.png')
image66 = mpimg.imread('positive_reviews_wc6.png')
image67 = mpimg.imread('negative_reviews_wc6.png')
image68 = mpimg.imread('positive_reviews_wf6.png')
image69 = mpimg.imread('negative_reviews_wf6.png')
image610 = mpimg.imread('total_reviews_wc6.png')
image611 = mpimg.imread('total_reviews_wf6.png')
image612 = mpimg.imread('neutral_reviews_wc6.png')
image613 = mpimg.imread('neutral_reviews_wf6.png')

image71 = mpimg.imread('firestick.jpg')
image72 = mpimg.imread('sentiment_distribution7.png')
image76 = mpimg.imread('positive_reviews_wc7.png')
image77 = mpimg.imread('negative_reviews_wc7.png')
image78 = mpimg.imread('positive_reviews_wf7.png')
image79 = mpimg.imread('negative_reviews_wf7.png')
image710 = mpimg.imread('total_reviews_wc7.png')
image711 = mpimg.imread('total_reviews_wf7.png')
image712 = mpimg.imread('neutral_reviews_wc7.png')
image713 = mpimg.imread('neutral_reviews_wf7.png')

st.subheader("This Data App performs the Analysis on the Reviews of Amazon Products")
        
st.sidebar.title("Navigation")
Others = ["Data Analysis App", "Source Code"]
choice = st.sidebar.radio("Select the Navigation", Others)

st.sidebar.title("Created By:")
st.sidebar.subheader("Ashutosh Shinde")
st.sidebar.subheader("[LinkedIn Profile](https://www.linkedin.com/in/ashutoshashinde/)")
st.sidebar.subheader("[GitHub Repository](https://github.com/AshutoshAShinde/Amazon-Product-Reviews-Data-Analysis-App)")

if choice == "Data Analysis App":
    
    st.graphviz_chart("""
        digraph{
        ProductReview -> Sentiment
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
        
    st.sidebar.title("Amazon Products")
    Products = [" Amazon Alexa Voice Remote"," Amazon Echo Studio","Ring Security Camera","Amazon Kindle","Sennheiser Wireless Headphones","The Four Winds: A Novel","K95 Face Mask"]     
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
    
        st.subheader("This is the Analysis of all the Reviews for Sennheiser Momentum 3 Wireless Headphones")
        image1 = mpimg.imread('snh2.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for Sennheiser Wireless Headphones are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Analyzer are :")

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
    
        st.subheader("This is the Analysis of all the Reviews for Ring Security Camera")
        image1 = mpimg.imread('ring.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for Ring Security Camera are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Analyzer are :")

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
    
        st.subheader("This is the Analysis of all the Reviews for The Four Winds: A Novel")
        image1 = mpimg.imread('hannah.png')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for The Four Winds: A Novel are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Analyzer are :")

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

        dfs = pd.read_csv("p44.csv") 
        dfs['reviews'].fillna("", inplace = True)
        dfs['stars'].fillna(dfs['stars'].mode(), inplace=True)
    
        pos_max = dfs.loc[dfs['Compound Score']==max(dfs['Compound Score'])]
        neg_max = dfs.loc[dfs['Compound Score']==min(dfs['Compound Score'])]
    
        gp = dfs.groupby(by=['Sentiment'])
        positive_reviews = gp.get_group('Positive')
        negative_reviews = gp.get_group('Negative')
        neutral_reviews = gp.get_group('Neutral')
    
        st.subheader("This is the Analysis of all the Reviews for Amazon Kindle")
        image1 = mpimg.imread('kindle.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for the Amazon Kindle are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Analyzer are :")

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
    
        st.subheader("This is the Analysis of all the Reviews for K95 Face Mask")
        image1 = mpimg.imread('k95.png')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for the K95 Face Mask are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Analyzer are :")

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
    
        st.subheader("This is the Analysis of all the Reviews for Amazon Echo Studio")
        image1 = mpimg.imread('echo.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for the Amazon Echo Studio are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Analyzer are :")

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
    
        st.subheader("This is the Analysis of all the Reviews for Amazon Alexa Voice Remote")
        image1 = mpimg.imread('firestick.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for the Amazon Alexa Voice Remote are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Analyzer are :")

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
        

else:
    
    st.subheader("Source Code")
    
    code = '''
 
import streamlit as st
import pandas as pd
import matplotlib.image as mpimg

pd.set_option('display.max_colwidth', -1)

st.title('Amazon Product Reviews Data Analysis App')

st.subheader("This App gives the Analysis of the reviews of various Products on Amazon.com")

st.sidebar.title("Navigation")
Others = ["Data Analysis App", "Source Code", "Contact"]
choice = st.sidebar.radio("Select the Navigation", Others)


if choice == "Data Analysis App":

    st.graphviz_chart("""
        digraph{
        ProductReview -> Sentiment
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
        
    st.sidebar.title("Amazon Products")
    Products = [" Amazon Echo Studio"," Amazon Alexa Voice Remote","Ring Security Camera","Amazon Kindle","Sennheiser Wireless Headphones","The Four Winds: A Novel","K95 Face Mask"]     
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
    
        st.subheader("This is the Analysis of all the Reviews for Sennheiser Momentum 3 Wireless Headphones")
        image1 = mpimg.imread('snh2.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for Sennheiser Wireless Headphones are: ', dfs.shape[0])
        st.subheader("The functions performed by the Analyzer are :")

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
    
        st.subheader("This is the Analysis of all the Reviews for Ring Security Camera")
        image1 = mpimg.imread('ring.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for Ring Security Camera are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Analyzer are :")

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
    
        st.subheader("This is the Analysis of all the Reviews for The Four Winds: A Novel")
        image1 = mpimg.imread('hannah.png')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for The Four Winds: A Novel are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Analyzer are :")

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
    
        st.subheader("This is the Analysis of all the Reviews for Amazon Kindle")
        image1 = mpimg.imread('kindle.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for the Amazon Kindle are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Analyzer are :")

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
    
        st.subheader("This is the Analysis of all the Reviews for K95 Face Mask")
        image1 = mpimg.imread('k95.png')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for the K95 Face Mask are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Analyzer are :")

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
    
        st.subheader("This is the Analysis of all the Reviews for Amazon Echo Studio")
        image1 = mpimg.imread('echo.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for the Amazon Echo Studio are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Analyzer are :")

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
    
        st.subheader("This is the Analysis of all the Reviews for Amazon Alexa Voice Remote")
        image1 = mpimg.imread('firestick.jpg')
    
        st.image(image1, width = 400)
        st.write('The total number of reviews for the Amazon Alexa Voice Remote are: ', dfs.shape[0])
    
        st.subheader("The functions performed by the Analyzer are :")

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
        

    '''
    

    st.code(code, language='python')
    


   








                                                          