import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import os


def get_all_genres(soup):
    result_genres=[]
    all_genres=soup.find_all("p", {"class": 'text-muted'})
    # print(all_genres)

    for genre in all_genres:
        genre=str(genre.find_all("span",{"class":"genre"}))
        if genre=='[]':
            pass
        else:
            genre=genre.replace("<", "=")
            genre=genre.replace(">", "=")
            genre=genre.split('=')
            genre=genre[int((len(genre)/2))]
            result_genres.append(genre)
    # print(result_genres)       
    return result_genres

def get_all_titles(soup):
    result_topics=[]
    all_topics=soup.find_all('h3',{"class":"lister-item-header"})
    # print(all_topics)
    for topic in all_topics:
        topic=str(topic.find('a'))
        topic=topic.replace("<", "=")
        topic=topic.replace(">", "=")
        topic=topic.split('=')
        topic=topic[int(len(topic)/2)]
        result_topics.append(topic)
    # print(result_topics)
    return result_topics

def post_process(genres):
    post_process_genres=[]
    for i in genres:
        i=i.replace("\n","")
        i=i.replace(" ","")
        post_process_genres.append(i)
    return post_process_genres

def check_repeated_comma(x):
    list_x=x.split(',')
    if len(list_x)==3:
        return x
    else:
        return np.nan




def data_set(url):
    data_set=pd.DataFrame(columns=['movie','Primary Genre', 'Secondary Genre', 'Tertiary Genre'])
    page= requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    title=get_all_titles(soup)
    print('Titles Scraped')
    genres= get_all_genres(soup)
    print('Genres Scraped')
    genres=post_process(genres)
    print('Genres processed')
    data_set["movie"]=pd.Series(title)
    data_set["Primary Genre"]=pd.Series(genres)
    data_set["Primary Genre"]=data_set["Primary Genre"].apply(check_repeated_comma)
    data_set["Secondary Genre"]= data_set["Secondary Genre"].fillna("To Be Filled")
    data_set["Tertiary Genre"]= data_set["Tertiary Genre"].fillna("To Be Filled")
    data_set=data_set.loc[data_set["Primary Genre"]!=np.NaN]
    data_set=data_set.dropna(how="any")
    data_set[["Primary Genre","Secondary Genre","Tertiary Genre"]]=data_set["Primary Genre"].str.split(',', expand=True)
    print(data_set)
    data_set.to_csv("Dataset.csv", mode='a', header=False)


    # print(soup)



# os.system('cls')
# print('IMDB Scrapper')
# number_of_pages= int(input('Enter the number of various pages to scrap: '))
# for i in range(number_of_pages):
#     url = input('Enter the url: ')
#     data_set(url)

# main part
os.system('cls')
print('----------------------------------- IMDB Scraper -----------------------------------------------')
number_of_pages = int(input('Enter the number of various pages to scrape: '))
page_no = 1
for i in range(number_of_pages):
    # url = input('Enter the url: ')
    url = f'https://www.imdb.com/search/title/?genres=mystery&start={page_no}&explore=title_type,genres&ref_=adv_nxt'
    
    page_no = page_no + 50
    data_set(url)