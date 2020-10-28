# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:31:23 2020

@author:Ashutosh Shinde
"""
from selenium import webdriver
import time
import csv
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

"""
A function that uses selenium and chromedriver to get reviews for a amazon product.
url is the link the account
"""

def scrape(url):
    #open the browser and visit the url
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    time.sleep(4)
    driver.find_element_by_xpath("//a[@data-hook='see-all-reviews-link-foot']").click()
    time.sleep(3)

    fw=open('reviews_amz4.csv','w',encoding='utf8')
    writer=csv.writer(fw,lineterminator='\n') #create a csv writer for this file
    while(True):

        reviews=driver.find_elements_by_xpath("//div[@class='a-row a-spacing-small review-data']")
        stars=driver.find_elements_by_xpath(".//i[@data-hook='review-star-rating' or @data-hook='cmps-review-star-rating']")  
       
        for i in range(len(reviews)):
            textData, starData='NA' , 'NA'
            try:
                textData=reviews[i].text 
            except:
                print('No reviews')
                
            try:
                starData=stars[i].get_attribute("class")
                starData=re.sub('[a-zA-Z\-\s+]','',starData)              
            except:
                print('No ratings')
                  
            i+=1
                
            if textData!='NA' or starData!='NA':
                writer.writerow([textData, starData])
        
        try:
            nextPageBtn=driver.find_element_by_xpath("//li[@class='a-last']")
            
        except:
            break
                 
        nextPageBtn.click()
        time.sleep(4)

    fw.close()
    driver.close()
    
    return fw

#url = 'https://www.amazon.com/Gildan-Little-Hooded-Youth-Sweatshirt/dp/B076C8F7G1/ref=pd_rhf_ee_s_pd_crcd_0_6/138-3327149-6208232?_encoding=UTF8&pd_rd_i=B076C3LH9W&pd_rd_r=4fb30fb2-0cb3-43c6-8020-8cdc4de49884&pd_rd_w=34zgQ&pd_rd_wg=NDqj7&pf_rd_p=8019ba47-0a12-4976-b76b-5c932d60db6f&pf_rd_r=T1SAFXZAYEBT63ZRTG94&refRID=T1SAFXZAYEBT63ZRTG94&th=1&psc=1'
url='https://www.amazon.com/Sennheiser-Momentum-Cancelling-Headphones-Functionality/dp/B07VW98ZKG/ref=cm_cr_arp_d_product_top?ie=UTF8'
#scrape(url)

df = pd.read_csv("reviews_amz4.csv", names = ['reviews','stars'])
print("The dataset is: \n ", df.head())

print("The total no of reviews are :", df.shape[0])

